from operations import Operations
from input_handler import operation_function, get_numbers

def main():
    num_1 = None
    num_2 = None

    while True:
        num_1, num_2 = get_numbers(num_1, num_2)
        operation = operation_function()
        if operation == "+": 
            result = Operations.addition(num_1, num_2)
            print(f"{num_1} {operation} {num_2} is equal to {result}")
        elif operation == "-":
            result = Operations.subtraction(num_1, num_2)
            print(f"{num_1} {operation} {num_2} is equal to {result}")
        elif operation == "*":
            result = Operations.multiplication(num_1, num_2)
            print(f"{num_1} {operation} {num_2} is equal to {result}")
        elif operation == "/":
            result = Operations.division(num_1, num_2)
            print(f"{num_1} {operation} {num_2} is equal to {result}")

if __name__ == "__main__":
    main()
