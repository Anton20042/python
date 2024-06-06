import time
import random
import math

results = []


def start_timer():
    global start_time, running
    start_time = time.time()
    running = True


def stop_timer():
    global elapsed_time, running
    if running:
        elapsed_time += time.time() - start_time
        running = False
        return elapsed_time


def reset_timer():
    global elapsed_time, running
    elapsed_time = 0
    running = False


def display_timer():
    global elapsed_time
    seconds = elapsed_time % 60
    minutes = elapsed_time // 60
    print("Time: {:02}:{:05.2f}".format(int(minutes), seconds))


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/', '**', 'sqrt', 'missing', 'time', 'distance', 'probability'])

    if operator == '+':
        result = num1 + num2
        question = f"{len(results) + 1}. What is {num1} + {num2}?"
    elif operator == '-':
        result = num1 - num2
        question = f"{len(results) + 1}. What is {num1} - {num2}?"
    elif operator == '*':
        result = num1*num2
        question = f"{len(results) + 1}. What is {num1}  {num2}?"
    elif operator == '/':
        result = num1 / num2
        question = f"{len(results) + 1}. What is {num1} / {num2}?"
    elif operator == '**':
        result = num1**2
        question = f"{len(results) + 1}. What is {num1} squared?"
    elif operator == 'sqrt':
        result = math.sqrt(num1)
        question = f"{len(results) + 1}. What is the square root of {num1}?"
    elif operator == 'missing':
        result = num2
        question = f"{len(results) + 1}. {num1} + ? = {num2}"
    elif operator == 'time':
        distance = random.randint(50, 100)
        speed = random.randint(5, 15)
        result = distance / speed
        question = f"{len(results) + 1}. What time does it take to travel {distance} km at a speed of {speed} km/h?"
    elif operator == 'distance':
        time = random.randint(2, 5)
        speed = random.randint(10, 20)
        result = time*speed
        question = f"{len(results) + 1}. What distance will be covered in {time} hours at a speed of {speed} km/h?"
    elif operator == 'probability':
        favorable_outcomes = random.randint(1, 6)
        total_outcomes = 6
        result = favorable_outcomes / total_outcomes
        question = f"{len(results) + 1}. What is the probability of rolling a {favorable_outcomes} on a fair 6-sided dice?"

    return question, result


def check_answer(question, user_answer):
    return question == user_answer


def show_results():
    sorted_results = sorted(results, key=lambda x: (x[0], x[1]), reverse=True)
    print("RESULTS:")
    for score, num_questions in sorted_results:
        print(f"Score: {score}, Number of questions: {num_questions}")


def run_quiz(time_limit=60):
    start_timer()
    current_score = 0
    current_num_questions = 0

    while True:
        question, correct_answer = generate_question()
        print(question)

        user_answer = input("Your answer: ")

        if user_answer.lower() == 'exit':
            break

        if check_answer(float(user_answer), correct_answer):
            current_score += 1
            print("Correct!")
        else:
            print("Incorrect!")

        current_num_questions += 1

        elapsed_time = stop_timer()

        if elapsed_time > time_limit:
            display_timer()
            results.append((current_score, current_num_questions))
            show_results()
            break

        start_timer()


while True:
    time_limit = int(input("Enter the time limit for each round in seconds: "))
    print("Starting a new quiz session...")
    run_quiz(time_limit)

    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != 'yes':
        break
