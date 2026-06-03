# Smart Calculator Pro

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if b!=0:
        return a/b

    else:
        return "Cannot divide by zero"


print("\nSmart Calculator Pro ===")


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")    
print("5.Exit")

choice = int(input("Enter your choice (1-5): ")) 


print("you have selected option: ", choice)

if choice == 1:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result: ", add(a,b))

elif choice == 2:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result: ", subtract(a,b))

elif choice == 3:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result: ", multiply(a,b))

elif choice == 4:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result: ", division(a,b))

elif choice == 5:
    print("Thank you for using Smart Calculator Pro. Goodbye!")

else:
    print("Invalid choice. Please enter a number between 1 and 5.")