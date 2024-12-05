class Operations:
    @staticmethod # without @staticmethod, we would be required to access the instance (self)
    def __init__():
        pass
    
    @staticmethod
    def addition(num_1, num_2):
        result = num_1 + num_2
        return result
    
    @staticmethod
    def subtraction(num_1, num_2):
        result = num_1 - num_2
        return result

    @staticmethod
    def multiplication(num_1, num_2):
        result = num_1 * num_2
        return result

    @staticmethod
    def division(num_1, num_2):
        if num_2 != 0:
            result = num_1 / num_2
            return result
        else:
            return "Error, you cannot divide by 0"
