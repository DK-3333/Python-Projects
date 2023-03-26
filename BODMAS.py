# Number game

import random

def operationComputation(a, o, b):
    if o == 0:
        return a + b
    elif o == 1:
        return a - b
    else:
        return a * b


def operationCompleteComputation(roundNo, operators, inputs):
    if roundNo == 1:
        return operationComputation(inputs[0], operators[0], inputs[1])
    elif roundNo == 2:
        return operationComputation(operationComputation(inputs[0], operators[0], inputs[1]), operators[1], inputs[2])
    elif roundNo == 3:
        return operationComputation(
            operationComputation(operationComputation(inputs[0], operators[0], inputs[1]), operators[1], inputs[2]),
            operators[2], inputs[3])
    elif roundNo == 4:
        return operationComputation(operationComputation(
            operationComputation(operationComputation(inputs[0], operators[0], inputs[1]), operators[1], inputs[2]),
            operators[2], inputs[3]), operators[3], inputs[4])
    else:
        return operationComputation(operationComputation(operationComputation(
            operationComputation(operationComputation(inputs[0], operators[0], inputs[1]), operators[1], inputs[2]),
            operators[2], inputs[3]), operators[3], inputs[4]), operators[4], inputs[5])


def operationIndicator(num):
    if num == 0:
        op = '+'
        return op
    elif num == 1:
        op = '-'
        return op
    else:
        op = '*'
        return op


def roundUserOutput(roundNo, inputs, operatorsCharacter):
    if roundNo == 1:
        print("\nCompute (" + str(inputs[0]) + str(operatorsCharacter[0]) + str(inputs[1]) + ")\n")
    elif roundNo == 2:
        print("\nCompute ((" + str(inputs[0]) + str(operatorsCharacter[0]) + str(inputs[1]) + ")" + str(
            operatorsCharacter[1]) + str(inputs[2]) + ")\n")
    elif roundNo == 3:
        print("\nCompute (((" + str(inputs[0]) + str(operatorsCharacter[0]) + str(inputs[1]) + ")" + str(
            operatorsCharacter[1]) + str(inputs[2]) + ")" + str(operatorsCharacter[2]) + str(inputs[3]) + ")\n")
    elif roundNo == 4:
        print("\nCompute ((((" + str(inputs[0]) + str(operatorsCharacter[0]) + str(inputs[1]) + ")" + str(
            operatorsCharacter[1]) + str(inputs[2]) + ")" + str(operatorsCharacter[2]) + str(inputs[3]) + ")" + str(
            operatorsCharacter[3]) + str(inputs[4]) + ")\n")
    elif roundNo == 5:
        print("\nCompute (((((" + str(inputs[0]) + str(operatorsCharacter[0]) + str(inputs[1]) + ")" + str(
            operatorsCharacter[1]) + str(inputs[2]) + ")" + str(operatorsCharacter[2]) + str(inputs[3]) + ")" + str(
            operatorsCharacter[3]) + str(inputs[4]) + ")" + str(operatorsCharacter[4]) + str(inputs[5]) + ")\n")


def answerCheck(ansUser, ansCorrect):
    if ansUser == ansCorrect:
        print("Congratulations, Your answer is Correct!\n")
        return 1
    else:
        print("Your answer is Wrong!\n\n")
        return 0


def roundCheck(roundNo):
    if roundNo != 5:
        print("\n")
    else:
        print("Thank you for playing the game.")
        exit()


def inputChecker(inputs):
    j = 0
    k = 1

    for x in range(6):
        if inputs[j] == inputs[k]:
            print("Please enter different values")
            exit()
        elif inputs == 0:
            print("0 is not accepted. Please enter different values")
            exit()
        else:
            print("\n")


# Main game

print("Enter different numbers and the program will assign a random operator between them.")
print("You will have to calculate the result of the operation.")
print( "If you answer correctly, you will gain a point and move on to the next question where the number of operators will increase by 1.")
print("\n")

roundNo = 1
score = 0

while True:

    i = 0

    inputs = []
    operators = []
    operatorsCharacter = []

    # Round begins
    print("--------------------------------------------------------------")
    print("Round ", roundNo)
    print("Please enter", roundNo + 1, "different numbers (integers only): \n")
    print("Enter your answer\n")
    
    for num in range(0, roundNo + 1):
        ele = int(input())
        inputs.append(ele)

    inputChecker(inputs)

    for i in range(0, roundNo):
        num = random.randint(0, 3)
        operators.append(num)

        op = operationIndicator(num)
        operatorsCharacter.append(op)

    # Printing operations to perform to the user

    roundUserOutput(roundNo, inputs, operatorsCharacter)

    print("Enter your answer: ")
    ansUser = int(input())

    ansCorrect = operationCompleteComputation(roundNo, operators, inputs)

    print("The correct answer is ", ansCorrect)

    score = score + answerCheck(ansUser, ansCorrect)

    print("Your score is ", score)

    roundNo = roundNo + 1
    roundCheck(roundNo)