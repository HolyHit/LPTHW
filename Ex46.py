import sys
def isprime(num):
    if num < 2:
        error ("Numbers less than 2 cannot be tested for primeness")
        return False
    elif num == 2:
        return True
    else:
        d = 2
        while d < (num/2):
            if num % d == 0:
                return False
            d = d + 1
        return True

def fibonacci(num):
    if num < 1:
        error("Cannot get a Fibonacci sequence number less than 1")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        last = 0
        current = 1
        for i in range (num - 2 ):
            temp = current
            current = last + current
            last = temp
        return current

def factorial(num):
    if num < 1:
        error ("Cannot get factorial of a number less than 1")
        return 0
    elif num == 1:
        return 1
    else:
        result = 1
        while num > 1:
            result = result * num
            num = num -1
        return result

def error(why):
    print "ERROR: ", why


def parse(userinput):
    inputs = userinput.split()
    try:
        val1 = int(inputs[0])
        operation = inputs[1]
        if operation == 'prime':
            return isprime(val1)
        elif operation == 'fib':
            return fibonacci(val1)
        elif operation == 'fact':
            return factorial(val1)
        else:
            val2 = int(inputs[2])
            if operation == '+':
                return val1 + val2
            elif operation == '-':
                return val1 - val2
            elif operation == '*':
                return val1 * val2
            elif operation == '/':
                return val1/val2
            else:
                raise SyntaxError()
    except ValueError:
        error("Invalid number, first and third values must be an integer")
    except SyntaxError:
        error("Invalid operation, the options are: + - * / prime fib fact")

def startcalc():
    print "Welcome to CALC, type quit to exit."
    print "Enter your calculations in the format: X + Y"
    print "For single value calculations use: X fib"
    print "Avaiable operations: + - * / primte fib fact"
    userinput = raw_input("CALC> ")
    while userinput.lower() != "quit":
        print userinput, " = ", parse(userinput)
        userinput = raw_input("CALC> ")
    print "Goodbye!"

if __name__ == "__main__":
    startcalc()
