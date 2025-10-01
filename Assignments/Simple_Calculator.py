
def addition(x, y):
    return (x + y)
def subtraction(x, y):
    return (x - y)
def multiplication(x, y):
    return (x * y)
def division(x, y):
    return (x / y)
def modulus(x, y):
    return (x % y)


while(True):    #Since question is not clear about whether we should exit the program after invalid inputs, I've put both types
    try:
        user_input = int(input("Select operations: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Modulus \nEnter choice (1/2/3/4/5): "))
        if(user_input < 1 or user_input > 5):
            print("\nInvalid choice. Please choose a number from 1 to 5.")
            continue
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
    except ValueError:
        print("\nInvalid input. Please enter numeric values only.")
        continue        #We can put Break to exit the loop & end the program and continue if we want our user to keep giving input. 

    if(user_input == 1):
        ans = addition(first_number, second_number)
        print(f"{first_number} + {second_number} = {ans:.2f}")
        break
    elif(user_input == 2):
        ans = subtraction(first_number, second_number)
        print(f"{first_number} - {second_number} = {ans:.2f}")
        break
    elif(user_input == 3):
        ans = multiplication(first_number, second_number)
        print(f"{first_number} * {second_number} = {ans:.2f}")
        break
    else:
        try:
            if(user_input == 4):
                ans = division(first_number, second_number)
                print(f"{first_number} / {second_number} = {ans:.2f}")
                break
            elif(user_input == 5):
                ans = modulus(first_number, second_number)
                print(f"{first_number} % {second_number} = {ans:.2f}")
                break
        except ZeroDivisionError:
            print("\nDenominator can not be Zero(0).")
            break          #We can put continue if we want our user to keep giving input. Break to exit the loop & end the program
