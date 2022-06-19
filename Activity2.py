# Bruno, Jared Ivan D.
# Hilario, Cyrille Jaye N.

import random

def add(x, y):
    return x + y

def subtrct(x, y):
    return x - y

def multiply(x, y):
    return x * y

def dividiby(x, y):
    return x / y

while True:

    score = 0
    choice = input("Enter your choice from 1 to 4: ")
    reps = int(input("How many problems?: "))

    for i in range(reps):
        if choice in ('1', '2', '3', '4'):

            if choice == '1':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = add(num1, num2)
                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score+=1
                else:
                    print("Wrong! the correct answer is ", num3)
            
            elif choice == '2':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtrct(num1, num2)
                print("What is the difference of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score+=1
                else:
                    print("Wrong! the correct answer is ", num3)
            
            elif choice == '3':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)
                print("What is the product of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score+=1
                else:
                    print("Wrong! the correct answer is ", num3)
            
            elif choice == '4':
                num1 = round(float(random.randint(0, 9)), 2)
                num2 = round(float(random.randrange(2, 10, 2)), 2)
                num3 = dividiby(num1, num2)
                print("What is the quotient of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score+=1
                else:
                    print("Wrong! the correct answer is ", num3)
        else:
            print("Invalid Input 1 to 4 only.")
            break
    
    print("Score: " + str(score) + "/" + str(reps))
    
    try_again = input("Want to try again? (yes/no): ")
    if try_again == "no":
        break