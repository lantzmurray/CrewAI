Mealgenerator Crew
Welcome to the Mealgenerator Crew project, powered by crewAI. This project is designed to help you set up a multi-agent AI system for meal planning, leveraging the flexible framework provided by crewAI. The goal of this project is to generate customized meal plans based on user preferences, dietary restrictions, and ingredient specifications.

Features
Collect user preferences for meal planning, including dietary restrictions and cooking difficulty.
Generate personalized meal plans with ingredients based on user input.
Supports customization of meal types, cuisines, and cooking time.
Installation
Ensure you have Python version between 3.10 and 3.13 installed on your system. This project uses Poetry for dependency management and package handling, offering a seamless setup and execution experience.

Steps to Set Up
Install Poetry by typing the following command: pip install poetry

Navigate to your project directory: cd mealgenerator

Lock and install dependencies: First, type: poetry lock Then, type: poetry install

Activate the virtual environment if it is not automatically activated: poetry shell

Running the Mealgenerator
After installation, you can run the meal generator by typing: python -m src.mealgenerator.main run

Customization
This project allows users to customize the meal generation process through simple inputs, such as:

Dietary restrictions
Preferred cuisines
Meal types (e.g., breakfast, lunch, dinner)
Cooking time
Difficulty level
Ingredients to avoid (e.g., allergens like nuts or specific dislikes)
By inputting your preferences, the system will generate tailored meal plans suited to your needs.
