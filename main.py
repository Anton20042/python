import time
import random
import math
import numpy


global elapsed_time,running
elapsed_time=0
running=False
results = []
points = 0
timer_speed = 1.0
score_multiplier = 1
max_level = 20
timer_speed_cost = 10
score_multiplier_cost = 20

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
    question = ""
    result = None
    dificult=0
    operators = ['+', '-', '*', '/', '**', 'sqrt', 'missing', 'time', 'distance', 'probability', 'arithmetic mean',
                 'percentage', 'probability2', 'probability3', 'simple interest', 'combinations', 'area', 'volume',
                 'ratio', 'circumference', 'surface area', 'slope', 'compound interest', 'discount', 'commission',
                 'profit and loss', 'time and work', 'speed and time', 'speed and distance', 'probability4',
                 'probability5', 'permutations', 'geometric mean', 'harmonic mean', 'quadratic equation',
                 'percentage_increase','fraction_addition','system_of_equations', 'trigonometric_ratios',
                 'linear_equation', 'system_of_linear_equations','matrix_multiplication','determinant_of_matrix',
                 'interest_problem']
    operator = random.choice(operators)
    if operator == '+':
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        result = num1 + num2
        dificult=1
        question = f"{len(results) + 1}. What is {num1} + {num2}?"
    elif operator == '-':
        num1 = random.randint(50, 100)
        num2 = random.randint(1, 49)
        result = num1 - num2
        dificult=1
        question = f"{len(results) + 1}. What is {num1} - {num2}?"
    elif operator == '*':
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        result = num1 * num2
        dificult=1
        question = f"{len(results) + 1}. What is {num1} * {num2}?"
    elif operator == '/':
        num1 = random.randint(10, 100)
        num2 = random.randint(1, 10)
        result = num1 / num2
        dificult=1
        question = f"{len(results) + 1}. What is {num1} / {num2}?"
    elif operator == '**':
        num1 = random.randint(2, 10)
        result = num1 ** 2
        dificult =2
        question = f"{len(results) + 1}. What is {num1} squared?"
    elif operator == 'sqrt':
        square_root = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        num5 = random.choice(square_root)
        result = math.sqrt(num5)
        dificult =2
        question = f"{len(results) + 1}. What is the square root of {num5}?"
    elif operator == 'missing':
        num1 = random.randint(1, 50)
        num2 = random.randint(num1 + 1, 100)
        result = num2 - num1
        dificult =2
        question = f"{len(results) + 1}. {num1} + ? = {num2}"
    elif operator == 'time':
        distance = random.randint(50, 500)
        speed = random.randint(10, 100)
        result = distance / speed
        dificult =2
        question = f"{len(results) + 1}. What time does it take to travel {distance} km at a speed of {speed} km/h?"
    elif operator == 'distance':
        time = random.randint(1, 10)
        speed = random.randint(20, 100)
        result = time * speed
        dificult =2
        question = f"{len(results) + 1}. What distance will be covered in {time} hours at a speed of {speed} km/h?"
    elif operator == 'probability':
        favorable_outcomes = random.randint(1, 20)
        total_outcomes = random.randint(favorable_outcomes + 1, 100)
        result = favorable_outcomes / total_outcomes
        dificult =2
        question = f"{len(results) + 1}. What is the probability of selecting a favorable outcome from {total_outcomes} total outcomes, if there are {favorable_outcomes} favorable outcomes?"
    elif operator == 'arithmetic mean':
        num3 = random.randint(1, 50)
        num4 = random.randint(1, 50)
        num5 = random.randint(1, 50)
        num6 = random.randint(1, 50)
        result = (num3 + num4 + num5 + num6) / 4
        dificult =3
        question = f"{len(results) + 1}. Find the arithmetic mean of the numbers {num3}, {num4}, {num5}, and {num6}."
    elif operator == 'percentage':
        possible_values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        percent = random.choice(possible_values)
        number = random.randint(1, 99)
        result = (number * 100) / percent
        dificult =3
        question = f"{len(results) + 1}. How many objects are there in total if it is known that {percent}% of these are {number} objects?"
    elif operator == 'probability2':
        angle = [60, 70, 80, 90, 100, 120, 130, 140, 150, 160, 170]
        favorable_outcomes = random.choice(angle)
        result = (180 - favorable_outcomes) / 2
        dificult =3
        question = f"{len(results) + 1}. Find the unknown angle of an isosceles triangle if the larger angle is {favorable_outcomes} degrees."
    elif operator == 'probability3':
        favorable_outcomes = random.randint(1, 20)
        result = math.sqrt(2 * (favorable_outcomes ** 2))
        dificult =3
        question = f"{len(results) + 1}. Find the hypotenuse in an isosceles right triangle if it is known that the leg is equal to {favorable_outcomes}."
    elif operator == 'simple interest':
        principal = random.randint(1000, 10000)
        rate = random.randint(5, 15)
        time = random.randint(1, 5)
        result = (principal * rate * time) / 100
        dificult =3
        question = f"{len(results) + 1}. Calculate the simple interest if the principal is {principal}, the rate is {rate}%, and the time is {time} years."
    elif operator == 'combinations':
        n = random.randint(5, 10)
        r = random.randint(2, n - 1)
        result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        dificult =3
        question = f"{len(results) + 1}. How many combinations of {n} distinct objects can be formed, taking {r} at a time?"
    elif operator == 'area':
        length = random.randint(5, 20)
        width = random.randint(5, 20)
        result = length * width
        dificult =3
        question = f"{len(results) + 1}. What is the area of a rectangle with length {length} and width {width}?"
    elif operator == 'volume':
        length = random.randint(3, 10)
        width = random.randint(3, 10)
        height = random.randint(3, 10)
        result = length * width * height
        dificult =3
        question = f"{len(results) + 1}. What is the volume of a rectangular prism with length {length}, width {width}, and height {height}?"
    elif operator == 'ratio':
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        result = num1 / num2
        dificult =3
        question = f"{len(results) + 1}. What is the ratio of {num1} to {num2}?"
    elif operator == 'circumference':
        radius = random.randint(5, 20)
        result = 2 * math.pi * radius
        dificult =3
        question = f"{len(results) + 1}. What is the circumference of a circle with radius {radius}?"
    elif operator == 'surface area':
        length = random.randint(5, 10)
        width = random.randint(5, 10)
        height = random.randint(5, 10)
        result = 2 * (length * width + length * height + width * height)
        dificult =3
        question = f"{len(results) + 1}. What is the surface area of a rectangular prism with length {length}, width {width}, and height {height}?"
    elif operator == 'slope':
        x1 = random.randint(1, 10)
        y1 = random.randint(1, 10)
        x2 = random.randint(x1 + 1, 20)
        y2 = random.randint(y1 + 1, 20)
        result = (y2 - y1) / (x2 - x1)
        dificult =3
        question = f"{len(results) + 1}. What is the slope of the line that passes through the points ({x1}, {y1}) and ({x2}, {y2})?"
    elif operator == 'trigonometric_ratios':
       angle = random.randint(30, 60)
       side_a = random.randint(5, 10)
       side_b = random.randint(5, 10)
       if angle == 30:
          result = side_a / (2 * side_b)
       elif angle == 45:
         result = side_a / (math.sqrt(2) * side_b)
       elif angle == 60:
         result = side_a / side_b
         dificult = 4
         question = f"{len(results) + 1}. If the angle is {angle} degrees and the lengths of the sides are {side_a} and {side_b}, what is the value of the trigonometric ratio?"

    elif operator == 'fraction_addition':
        num1 = random.randint(1, 10)
        den1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        den2 = random.randint(1, 10)
        common_den = math.lcm(den1, den2)
        new_num1 = num1 * (common_den // den1)
        new_num2 = num2 * (common_den // den2)
        result = (new_num1 + new_num2) / common_den
        dificult = 3
        question = f"{len(results) + 1}. Add the fractions {num1}/{den1} and {num2}/{den2}."
    elif operator == 'discount':
        original_price = random.randint(100, 1000)
        discount_percent = random.randint(10, 50)
        result = original_price - (original_price * discount_percent / 100)
        dificult =3
        question = f"{len(results) + 1}. If an item's original price is {original_price} and the discount is {discount_percent}%, what is the discounted price?"
    elif operator == 'commission':
        sales_amount = random.randint(1000, 10000)
        commission_rate = random.randint(5, 15)
        result = sales_amount * commission_rate / 100
        dificult =3
        question = f"{len(results) + 1}. Calculate the commission if the sales amount is {sales_amount} and the commission rate is {commission_rate}%."
    elif operator == 'percentage_increase':
        original_value = random.randint(100, 1000)
        percent_increase = random.randint(10, 50)
        result = original_value + (original_value * percent_increase / 100)
        dificult = 3
        question = f"{len(results) + 1}. If the original value is {original_value} and the percentage increase is {percent_increase}%, what is the new value?"
    elif operator == 'profit and loss':
        cost_price = random.randint(100, 1000)
        selling_price = random.randint(cost_price + 1, 2 * cost_price)
        result = (selling_price - cost_price) / cost_price * 100
        dificult =3
        question = f"{len(results) + 1}. If the cost price of an item is {cost_price} and the selling price is {selling_price}, what is the percentage of profit or loss?"
    elif operator == 'time and work':
        work = random.randint(10, 50)
        time1 = random.randint(1, 5)
        time2 = random.randint(time1 + 1, 10)
        result = work / (time1 + time2)
        dificult =3
        question = f"{len(results) + 1}. If a person can complete a work in {time1} days, and another person can complete the same work in {time2} days, what is the rate at which the work is completed?"
    elif operator == 'speed and time':
        distance = random.randint(50, 500)
        time = random.randint(1, 10)
        result = distance / time
        dificult =3
        question = f"{len(results) + 1}. If a person travels a distance of {distance} km in {time} hours, what is their speed?"
    elif operator == 'speed and distance':
        speed = random.randint(20, 100)
        time = random.randint(1, 10)
        result = speed * time
        dificult =3
        question = f"{len(results) + 1}. If a person travels at a speed of {speed} km/h for {time} hours, what distance did they cover?"
    elif operator == 'probability4':
        event_outcomes = random.randint(1, 20)
        total_outcomes = random.randint(event_outcomes + 1, 50)
        result = event_outcomes / total_outcomes
        dificult =3
        question = f"{len(results) + 1}. What is the probability of an event occurring if there are {event_outcomes} favorable outcomes out of {total_outcomes} total outcomes?"
    elif operator == 'probability5':
        event_outcomes = random.randint(1, 10)
        total_outcomes = random.randint(event_outcomes + 1, 20)
        result = (total_outcomes - event_outcomes) / total_outcomes
        dificult =3
        question = f"{len(results) + 1}. What is the probability of an event not occurring if there are {event_outcomes} favorable outcomes out of {total_outcomes} total outcomes?"
    elif operator == 'permutations':
        n = random.randint(5, 10)
        r = random.randint(2, n - 1)
        result = math.factorial(n) // math.factorial(n - r)
        dificult=3
        question = f"{len(results) + 1}. How many permutations of {n} distinct objects can be formed, taking {r} at a time?"
    elif operator == 'geometric mean':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        result = (num1 * num2 * num3) ** (1 / 3)
        dificult=3
        question = f"{len(results) + 1}. Find the geometric mean of the numbers {num1}, {num2}, and {num3}."
    elif operator == 'system_of_equations':
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)
        e = random.randint(1, 5)
        f = random.randint(1, 5)
        x = (c*d - b*f) / (a*d - b*c)
        y = (a*f - c*e) / (a*d - b*c)
        result = (x, y)
        dificult = 4
        question = f"{len(results) + 1}. Solve the system of linear equations: {a}x + {b}y = {c}, {d}x + {e}y = {f}."
    elif operator == 'harmonic mean':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        result = 3 / ((1 / num1) + (1 / num2) + (1 / num3))
        dificult=3
        question = f"{len(results) + 1}. Find the harmonic mean of the numbers {num1}, {num2}, and {num3}."
    elif operator == 'quadratic equation':
        a = random.randint(1, 5)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            result = (x1, x2)
            dificult =3
            question = f"{len(results) + 1}. Solve the quadratic equation {a}x^2 + {b}x + {c} = 0."
        else:
            result = "No real solutions"
            dificult=3
            question = f"{len(results) + 1}. Solve the quadratic equation {a}x^2 + {b}x + {c} = 0."


    elif operator == 'midpoint':
        x1 = random.randint(1, 10)
        y1 = random.randint(1, 10)
        x2 = random.randint(11, 20)
        y2 = random.randint(11, 20)
        result_x = (x1 + x2) / 2
        result_y = (y1 + y2) / 2
        dificult=3
        question = f"{len(results) + 1}. What is the midpoint of the line segment connecting the points ({x1}, {y1}) and ({x2}, {y2})?"
    elif operator == 'distance_between_points':
        x1 = random.randint(1, 10)
        y1 = random.randint(1, 10)
        x2 = random.randint(11, 20)
        y2 = random.randint(11, 20)
        result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        dificult=3
        question = f"{len(results) + 1}. What is the distance between the points ({x1}, {y1}) and ({x2}, {y2})?"
    elif operator == 'compound_interest':
        principal = random.randint(1000, 10000)
        rate = random.randint(5, 15)
        time = random.randint(1, 5)
        result = principal * (1 + rate / 100) ** time
        dificult=3
        question = f"{len(results) + 1}. Calculate the compound interest for a principal of {principal}, rate of {rate}%, and time of {time} years."
    elif operator == 'simple_interest':
        principal = random.randint(1000, 10000)
        rate = random.randint(5, 15)
        time = random.randint(1, 5)
        result = (principal * rate * time) / 100
        dificult=3
        question = f"{len(results) + 1}. Calculate the simple interest for a principal of {principal}, rate of {rate}%, and time of {time} years."
    elif operator == 'percent_change':
        initial_value = random.randint(100, 1000)
        final_value = random.randint(initial_value + 1, initial_value * 2)
        result = (final_value - initial_value) / initial_value * 100
        dificult=3
        question = f"{len(results) + 1}. What is the percent change from {initial_value} to {final_value}?"
    elif operator == 'profit_loss':
        cost_price = random.randint(100, 1000)
        selling_price = random.randint(cost_price + 1, cost_price * 2)
        if selling_price > cost_price:
            result = (selling_price - cost_price) / cost_price * 100
            dificult=4
            question = f"{len(results) + 1}. What is the profit percentage if the cost price is {cost_price} and the selling price is {selling_price}?"
        else:
            result = (cost_price - selling_price) / cost_price * 100
            dificult=4
            question = f"{len(results) + 1}. What is the loss percentage if the cost price is {cost_price} and the selling price is {selling_price}?"
    elif operator == 'tax_tip':
        original_amount = random.randint(100, 1000)
        tax_rate = random.randint(5, 15)
        tip_rate = random.randint(10, 20)
        tax_amount = original_amount * tax_rate / 100
        tip_amount = original_amount * tip_rate / 100
        result = original_amount + tax_amount + tip_amount
        dificult=4
        question = f"{len(results) + 1}. What is the total amount to be paid if the original amount is {original_amount}, the tax rate is {tax_rate}%, and the tip rate is {tip_rate}%?"
    elif operator == 'linear_equation':
        a = random.randint(1, 5)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        x = random.randint(-10, 10)
        result = a * x + b
        dificult = 4
        question = f"{len(results) + 1}. Solve the linear equation {a}x + {b} = {c}."
    elif operator == 'average_speed':
        distance = random.randint(50, 100)
        time1 = random.randint(1, 3)
        time2 = random.randint(4, 6)
        result = (distance / time1 + distance / time2) / 2
        dificult=4
        question = f"{len(results) + 1}. What is the average speed if the distance is {distance} km and the times are {time1} hours and {time2} hours?"
    elif operator == 'work_time':
        work_done_by_A = random.randint(1, 5)
        work_done_by_B = random.randint(1, 5)
        total_work = random.randint(10, 20)
        result = total_work / (work_done_by_A + work_done_by_B)
        dificult=5
        question = f"{len(results) + 1}. If person A can do {work_done_by_A} units of work and person B can do {work_done_by_B} units of work, how long will it take them to complete {total_work} units of work?"
        if operator == 'determinant':
            size = random.randint(2, 4)
            matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
            det = numpy.linalg.det(matrix)
            while det == 0:
                matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
                det = numpy.linalg.det(matrix)
            result = round(det, 2)
            dificult = 5
            question = f"{len(results) + 1}. Find the determinant of the matrix {matrix}."
    elif operator == 'work_rate':
            work_done_by_A = random.randint(1, 5)
            work_done_by_B = random.randint(1, 5)
            total_work = random.randint(10, 20)
            if total_work == 0:
                return generate_question()  # Рекурсивный вызов, если total_work равен 0
            result = (work_done_by_A + work_done_by_B) / total_work
            dificult = 5
            question = f"{len(results) + 1}. If person A can do {work_done_by_A} units of work and person B can do {work_done_by_B} units of work, what is their combined work rate to complete {total_work} units of work?"
    elif operator == 'matrix_multiplication':
        rows1 = random.randint(2, 4)
        cols1 = random.randint(2, 4)
        rows2 = cols1
        cols2 = random.randint(2, 4)
        matrix1 = [[random.randint(1, 10) for _ in range(cols1)] for _ in range(rows1)]
        matrix2 = [[random.randint(1, 10) for _ in range(cols2)] for _ in range(rows2)]
        result_matrix = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
        dificult = 5
        question = f"{len(results) + 1}. Multiply the matrices {matrix1} and {matrix2}."
    elif operator == 'interest_problem':
        principal = random.randint(1000, 10000)
        rate = random.randint(5, 15)
        time = random.randint(1, 5)
        result = principal * (1 + rate / 100 * time)
        dificult = 5
        question = f"{len(results) + 1}. A person invests {principal} dollars at an annual interest rate of {rate}% for {time} years. What is the final amount, including the principal and interest?"
    elif operator == 'mixture_problem':
        concentration_A = random.randint(10, 50)
        volume_A = random.randint(1, 5)
        concentration_B = random.randint(60, 90)
        volume_B = random.randint(1, 5)
        result = (concentration_A * volume_A + concentration_B * volume_B) / (volume_A + volume_B)
        dificult=5
        question = f"{len(results) + 1}. A mixture is made by combining {volume_A} liters of a solution with {concentration_A}% concentration and {volume_B} liters of a solution with {concentration_B}% concentration. What is the concentration of the final mixture?"
    return question, result, dificult


def check_answer(question, user_answer):
    return question == user_answer


def show_results():
    sorted_results = sorted(results, key=lambda x: (x[0], x[1]), reverse=True)
    print("RESULTS:")
    for score, num_questions in sorted_results:
        print(f"Player: {name}, Score: {score}, Number of questions: {num_questions}")


def run_quiz(time_limit=60):
    start_timer()
    current_score = 0
    current_num_questions = 0
    dificult=1

    while True:
        try:
            question, correct_answer, dificult = generate_question()
            print(question)

            user_answer = input("Your answer: ")
            if user_answer == "":
                print("ERROR")
            elif user_answer.lower() == 'exit':
                break
            elif check_answer(float(user_answer), correct_answer):
                current_score += dificult * score_multiplier
                print("Correct!")
            else:
                print("Incorrect!")

            current_num_questions += 1

            elapsed_time = stop_timer()
            elapsed_time /= timer_speed

            if elapsed_time > time_limit:
                display_timer()
                results.append((current_score, current_num_questions))
                show_results()
                break

            start_timer()
        except ZeroDivisionError:
            print("Error: Division by zero. Skipping this question.")
            continue

def display_store():
    print("Store:")
    print("1. Upgrade Timer Speed (Cost: {})".format(timer_speed_cost))
    print("2. Upgrade Score Multiplier (Cost: {})".format(score_multiplier_cost))
def upgrade_store(choice):
    global points, timer_speed, score_multiplier

    if choice =='1':
        if timer_speed < max_level:
            if points >= timer_speed_cost:
                points -= timer_speed_cost
                timer_speed += 0.1
                print("Timer speed upgraded!")
            else:
                print("Not enough points to upgrade timer speed!")
        else:
            print("Timer speed is already at maximum level!")
    elif choice == '2':
        if score_multiplier < max_level:
            if points >= score_multiplier_cost:
                points -= score_multiplier_cost
                score_multiplier += 1
                print("Score multiplier upgraded!")
            else:
                print("Not enough points to upgrade score multiplier!")
        else:
            print("Score multiplier is already at maximum level!")
    else:
        print("Invalid choice. Please try again.")
while True:
    name=input("Player:")
    time_limit = int(input("Enter the time limit for each round in seconds: "))
    print("Starting a new quiz session...")
    run_quiz(time_limit)
    display_store()
    choice = input("Buy something? (1/2): ")
    if choice=='1' or '2':
        upgrade_store(choice)



    again = input("Do you want to play again? (yes/no): ")

    if again.lower() != 'yes':
        break

