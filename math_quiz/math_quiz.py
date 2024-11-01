import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    
    Parameters:
    min_value (int): The minimum integer value.
    max_value (int): The maximum integer value.
    
    Returns:
    int: A random integer within the specified range.
    """
    return random.randint(min_value, max_value)


def choose_operator():
    """
    Randomly choose a math operator from addition, subtraction, and multiplication.
    
    Returns:
    str: The chosen operator.
    """
    return random.choice(['+', '-', '*'])


def calculate_expression(n1, n2, operator):
    """
    Calculate the expression based on the two numbers and the chosen operator.
    
    Parameters:
    n1 (int): The first number.
    n2 (int): The second number.
    operator (str): The operator to use ('+', '-', '*').
    
    Returns:
    tuple: A tuple containing the string representation of the problem and the result.
    """
    expression = f"{n1} {operator} {n2}"
    # Perform the calculation based on the operator
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    else:  # operator is '*'
        result = n1 * n2
    
    return expression, result

def math_quiz():
    """
    Run the math quiz game where users answer math problems and score points.
    """
    score = 0
    total_questions = 3  

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = generate_random_integer(1, 10)
        n2 = generate_random_integer(1, 5)  
        operator = choose_operator()

        problem, answer = calculate_expression(n1, n2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling for user input
        try:
            user_answer = float(input("Your answer: "))  # Accepting float to allow for division results
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue  # Skip this iteration and ask the next question

        # Check if the user answer matches the calculated answer
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1  # Increment score by 1 for a correct answer
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
