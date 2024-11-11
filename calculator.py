class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        if b == 0:
            return "Cannot divide by Zero."
            # raise ZeroDivisionError("Cannot divide by Zero.")
        elif ( a < 0 ) or ( b < 0 ):
            a, b = abs(a), abs(b)
            while a >= b:
                a = self.subtract(abs(a), abs(b))
                result += 1
            return -(result)

        else:
            while a >= b:
                a = self.subtract(abs(a), abs(b))
                result += 1
            return result
    
    def modulo(self, a, b):
        b_original = b
        neg = a < 0 and b < 0
        result = 0
        if b == 0:
            return "Cannot mod by Zero."
        a, b = abs(a), abs(b)
        while a >= b:
            a = a - b
        result = a 
        return -result if neg or b_original < 0 else result


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
