#function
def add(a,b):
    return a + b

def subtract (a,b):
    return a - b 

def multiply (a,b):
    return a * b

def divide (a,b):
    return 

def exponentiation (a,b):
    a ** b

def floordivision (a,b):
    a//b

#note
o = "Operations: \n - add = ' + ' \n - substract = ' - ' \n - multiply = ' x ' \n - divide = ' : ' \n - exponentiation = ' ^ ' \n - floor division = ' // '"
print(o)

#input and calculating

while True:
    # take input from the user
    num1 = float(input("First number: "))
    choice = input("Enter choice= ")
    num2 = float(input("Second number: "))
    if choice in ('+', '-', 'x', ':', '^', '//'):
        
        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'x':
            print(num1, "x", num2, "=", multiply(num1, num2))

        elif choice == ':':
            print(num1, ":", num2, "=", divide(num1, num2))

        elif choice == '^':
            print(num1, "^", num2, "=", exponentiation(num1, num2))

        elif choice == '//':
            print(num1, "//", num2, "=", floordivision(num1, num2))
        
        # loop or not
        next_calculation = input("Wanna do next calculation? (y/n)= ")
        if next_calculation == "no":
          break

    else:
        print("something wrong. I can't calculate this.")
    


