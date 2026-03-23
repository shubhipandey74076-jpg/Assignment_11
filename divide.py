# function to divide two numbers
def divide(a, b):
    # check if denominator is zero
    if b == 0:
        return "Cannot divide by zero"
    return a / b   # returns division result

# take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# call function and print result
print("Division =", divide(num1, num2))