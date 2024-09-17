import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MealgeneratorCrew:
    """Mealgenerator crew"""
    agents_config_path = 'src/mealgenerator/config/agents.yaml'
    tasks_config_path = 'src/mealgenerator/config/tasks.yaml'

    def __init__(self):
        with open(self.agents_config_path, 'r') as agents_file:
            self.agents_config = yaml.safe_load(agents_file)
        
        with open(self.tasks_config_path, 'r') as tasks_file:
            self.tasks_config = yaml.safe_load(tasks_file)
        
        self.user_preferences = {}

    @agent
    def user_input_agent(self) -> Agent:
        return Agent(config=self.agents_config['user_input_agent'], verbose=True)

    @agent
    def ingredient_agent(self) -> Agent:
        return Agent(config=self.agents_config['ingredient_agent'], verbose=True)

    @agent
    def recipe_agent(self) -> Agent:
        return Agent(config=self.agents_config['recipe_agent'], verbose=True)

    @task
    def collect_preferences_task(self) -> Task:
        def collect_user_preferences(inputs):
            # Update user preferences with collected inputs
            self.user_preferences.update(inputs)

            # Ask user about specific ingredient preferences or allergies
            ingredient_preferences = input("Please provide details about what ingredients you prefer or wish to avoid (e.g., 'no nuts', 'prefer vegetables'): ")
            self.user_preferences['ingredient_preferences'] = ingredient_preferences
            
            # Limit the number of meals to 5
            meal_count = int(self.user_preferences.get('meal_count', 1))
            self.user_preferences['meal_count'] = min(meal_count, 5)
            
            return self.user_preferences

        return Task(
            config=self.tasks_config['collect_preferences_task'],
            agent=self.user_input_agent(),
            custom_task_function=collect_user_preferences
        )

    @task
    def suggest_ingredients_task(self) -> Task:
        def suggest_ingredients(inputs):
            preferences = self.user_preferences or inputs
            ingredient_preferences = preferences.get('ingredient_preferences', 'No specific preferences provided')

            return f"Suggested ingredients based on your preferences: {ingredient_preferences}"

        return Task(
            config=self.tasks_config['suggest_ingredients_task'],
            agent=self.ingredient_agent(),
            custom_task_function=suggest_ingredients
        )

    @task
    def generate_recipe_task(self, inputs=None) -> Task:
        def generate_recipe(inputs):
            preferences = self.user_preferences or inputs
            cooking_time = preferences.get('cooking_time', '45 minutes')
            difficulty = preferences.get('difficulty', 'medium')
            meal_number = inputs.get('meal_number', 1)
            ingredient_preferences = preferences.get('ingredient_preferences', 'No specific preferences')

            recipe = f"Recipe {meal_number} generated based on {preferences}\n\n"
            recipe += f"### Cooking Time: {cooking_time}\n"
            recipe += f"### Difficulty Level: {difficulty}\n"
            recipe += f"### Ingredient Preferences: {ingredient_preferences}\n\n"
            
            if difficulty == 'easy':
                recipe += "This is an easy recipe with simplified steps."
            elif difficulty == 'hard':
                recipe += "This recipe has more complex steps for experienced cooks."
            
            return recipe

        return Task(
            config=self.tasks_config['generate_recipe_task'],
            agent=self.recipe_agent(),
            custom_task_function=generate_recipe,
            output_file=f'meal_recipe_{(inputs or {}).get("meal_number", 1)}.md'
        )

    @crew
    def crew(self) -> Crew:
        def run_meals(inputs):
            meal_count = self.user_preferences.get('meal_count', 1)

            # Generate multiple meals in sequence without any delay or feedback collection
            for meal_number in range(1, meal_count + 1):
                inputs['meal_number'] = meal_number
                print(self.tasks['generate_recipe_task'].run(inputs=inputs))

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            custom_process=run_meals,
            verbose=True
        )
