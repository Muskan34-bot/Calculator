print("---Simple Calculator---\n")

print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")

option = int(input("Choose an Operation: "))
result = 0

if(option in [1,2,3,4]):
    num1 = float(input("\nEnter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    if(option == 1):
        result = num1 + num2
    
    elif(option == 2):
        result = num1 - num2

    elif(option == 3):
        result = num1 * num2

    elif(option == 4):
        if(num2 != 0):
          result = num1 / num2
        else:
            print("\nError! Division by zero is not allowed...")

else:
    print("\nInvalid Operation entered...")

print("\nThe result of the operation is {}".format(result))