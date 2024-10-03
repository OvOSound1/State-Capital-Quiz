# Importing the random module to use its functions
import random

# Function to read the file containing state-capital pairs and return a list of states with their capitals
def read_file(file_name):
    states = []
    with open(file_name) as file:
        for line in file:
            state, capital = line.strip().split(',')
            states.append([state, capital])
    return states

# Function to get a random state from the list
def get_random_state(states):
    return random.choice(states)

# Function to get random choices for the quiz, including the correct capital
def get_random_choices(states, correct_capital):
    choices = [correct_capital]
    while len(choices) < 4:
        capital = random.choice(states)[1]
        if capital != correct_capital and capital not in choices:
            choices.append(capital)
    random.shuffle(choices)
    return choices

# Function to ask a multiple-choice question
def ask_question(correct_state, possible_answers):
    while True:
        print(f"The capital of {correct_state} is:")
        for i, option in enumerate(possible_answers):
            print(f"{chr(65 + i)}. {option}")
        selection = input("Enter selection: ").upper()
        if selection in ['A', 'B', 'C', 'D']:
            return ord(selection) - 65
        else:
            print("Invalid input. Input choice A-D.")

# Main function to execute the quiz
def main():
    # Reading the file and obtaining the list of states with their capitals
    states = read_file('statecapitals.txt')

    # Initializing points for the quiz
    points = 0
    print("- State Capitals Quiz -")

    # Loop for 10 quiz questions
    for i in range(1, 11):
        print(f"{i}. ", end="")

        # Getting a random state and its correct capital
        correct_state, correct_capital = get_random_state(states)

        # Getting random choices for the quiz, including the correct capital
        possible_answers = get_random_choices(states, correct_capital)

        # Asking the question and getting the user's selection
        selection = ask_question(correct_state, possible_answers)

        # Checking if the selected answer is correct and updating points
        if possible_answers[selection] == correct_capital:
            print("Correct!")
            points += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_capital}.")

    # Displaying the final score at the end of the quiz
    print(f"End of test. You got {points} correct.")

# Calling the main function to run the quiz
main()

