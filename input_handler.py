def get_numbers(num_1, num_2):
    num_1 = None
    num_2 = None

    while True:
        num_1 = input("Please input the first number: ")
        if num_1.isdigit() == False:
            print("Please make sure to input a number")
        else:
            num_1 = int(num_1)
            break
    while True:
        num_2 = input("Please input the second number: ")
        if num_2.isdigit() == False:
            print("Please make sure to input a number")
        else:
            num_2 = int(num_2)
            break

    return num_1, num_2

def operation_function():
    while True:
        operation = input("Please choose an operation to perform (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'): # iterate to find any of the 4 symbols
            return operation
        else:
            print("Please make sure to input a valid operation")
