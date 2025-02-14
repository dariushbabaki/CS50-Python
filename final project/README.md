## Goal or nonsense game

## video Demo: <https://youtu.be/vedvNu3MwMk?si=cJvQoswq5S_DMoLI>

## programming by:

- Dariush Babaki 

## Description:

Goal or nonsense, or "Guess tvi Hand," is a simple yet engaging Python game in which the player tries to guess which hand a ball is hidden in. The game randomly selects either the left or right hand to hide the ball, and the player’s goal is to guess the correct hand. This project is implemented in two Python files, each serving a distinct purpose: `project.py` for the main game functionality and `test_project.py` for testing the code.


- project.py

The `project.py` file contains the core logic of the game. It includes functions for hiding the ball, receiving the player's guess, and checking if the guess matches the hidden hand. Here’s a breakdown of each main function:

main(): This is the entry point of the game, presenting a welcome message and guiding the player through making a guess. After a guess is made, the function calls other components to validate and display the result.

  hide_ball(): A utility function that randomly picks either "left" or "right" to determine where the ball is hidden. This function leverages Python's `random.choice()` to introduce randomness.

  guess_hand(choice): This function validates the player’s input to ensure they have guessed either "left" or "right". If the input is invalid, it raises a `ValueError` with an appropriate message.

  check_guess(choice): It calls `hide_ball()` to determine the actual hidden hand and compares it with the player's choice, returning a tuple with the result of the guess (True/False) and the actual hidden hand for reference.


- test_project.py

  The `test_project.py` file contains test cases using the `pytest` framework to ensure the reliability of the main game components in `project.py`. These tests are designed to validate various aspects of the game:

  test_hide_ball(): Confirms that the `hide_ball` function always returns either "left" or "right" as expected.

    test_guess_hand(): Verifies that `guess_hand` correctly returns the input for valid guesses ("left" or "right") and raises a `ValueError` for any invalid guesses.

    test_check_guess(): Ensures that `check_guess` returns a boolean result and that the hidden hand is always one of the two options.


    Design Considerations:

    This project follows a modular structure, making it easy to test and maintain. By separating the main gameplay logic from the test cases, we ensure that each part of the project can be independently assessed. Additionally, using `pytest` as the testing framework allows for efficient test execution and improved reliability.

    This README provides an overview of how the game works, the functions involved, and the design decisions behind each choice, making it straightforward for future developers or users to understand and extend the project. This simple yet fun project serves as an introduction to Python, randomization, and testing practices.
