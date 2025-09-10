"""Python calc"""
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
operations = {"+" : add ,
              "-" : subtract,
              "*" : multiply,
              "/" : divide}
print("Welcome to the python calculator .")
a = float(input("Insert the first number : "))
operation = input("Enter the operation : '+','-','*','/'.")
b = float(input("Insert the second number : "))
result = operations[operation](a,b)
print(f"The result is {result} ")
retry = False
while not retry:
    check = input("Do you want to continue on the last result or try again from the begining.'y','n'")
    if check == 'y':
        a = result
    else:
        a = float(input("Enter the first number : "))
    operation = input("Enter the operation.'+','-','*','/'")
    b = float(input("Enter the second number : "))
    result = operations[operation](a,b)
    print(f"The result is {result}")