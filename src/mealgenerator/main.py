
###main.py##
#
import sys
import os 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#from mealgenerator.crew import MealgeneratorCrew
from .crew import MealgeneratorCrew

# This main file is intended to be a way for you to run your
# crew locally. Replace 'inputs' with values you want to test.
# It will automatically interpolate any tasks and agents information.

def run():
    """
    Run the crew.
    """
    inputs = {
        'cuisine': 'BBQ',
        'meal_type': 'dinner',
        'meal_number': 1,  # Example value for meal number
        'cooking_time': 30,
        'difficulty': 'easy'
    }
    MealgeneratorCrew().crew().kickoff(inputs=inputs)



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        
        'cuisine': 'BBQ',
        'meal_type': 'dinner'
    }
    try:
        MealgeneratorCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MealgeneratorCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        
        'cuisine': 'BBQ',
        'meal_type': 'dinner'
    }
    try:
        MealgeneratorCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    # Ensure the script can handle running, training, replaying, and testing based on arguments.
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == 'run':
            run()
        elif command == 'train':
            train()
        elif command == 'replay':
            replay()
        elif command == 'test':
            test()
        else:
            print(f"Unknown command: {command}")
    else:
        run()  # Default to run if no command is provided
