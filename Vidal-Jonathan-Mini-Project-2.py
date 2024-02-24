# Vidal-Jonathan-Mini-Project-2.py

"""Generate single-digit multiplication problems for elementary school students."""

import random #gives the ability to generate random numbers

correct_feedback = ['Very good!', 'Nice work!', 'Keep up the good work!']
negative_feedback = ['Incorrect.', 'Please try again.', 'Wrong.', 'Try once more.', 'Incorrect.', 'Keep trying.']

def generate_question():
    """Generates 2 random numbers for a multiplication problem"""
    num1 = random.randint(1, 9) #range of 1-9 so that only single digit numbers are given
    num2 = random.randint(1, 9) 
    return (num1, num2) #the tuple that temporarily holds the problem's numbers 

def check_answer(num1, num2, correct_answer):
    """Checks the for the product of two randomly generated numbers"""
    if correct_answer == num1 * num2: #answer key for question
        correct_index = random.randint(0,2)
        print(correct_feedback[correct_index])
        return True #returns true so that the while loop continues to prompt questions 
    
print("Welcome to Jonathan Vidal's multiplication game!")

while True: #while loop to continuously generate and ask questions unless prompted a "-1"
    num1, num2 = generate_question() #uses function to create question with two random numbers
    question = f"How much is {num1} * {num2}? (Enter -1 to exit the game.): "
    answer = int(input(question))

    while answer != -1: 
        if check_answer(num1, num2, answer): #uses function to check answer to question given
            break #gives a new question once the correct answer to the old question is given
        else: # loop to repeat question if answer is incorrect
            incorrect_index = random.randint(0,5)
            print(negative_feedback[incorrect_index])
            answer = int(input(question))
    
    if answer == -1:
        print('\n Thanks for playing!')
        break #ends the entire while loop if a -1 is given

