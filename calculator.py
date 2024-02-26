import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_logarithm(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    print("Scientific Calculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Logarithm")
    print("4. Power")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = float(input("Enter a number: "))
        print("Square root:", square_root(x))
    elif choice == 2:
        x = int(input("Enter a number: "))
        print("Factorial:", factorial(x))
    elif choice == 3:
        x = float(input("Enter a number: "))
        print("Natural logarithm:", natural_logarithm(x))
    elif choice == 4:
        x = float(input("Enter the base: "))
        b = float(input("Enter the exponent: "))
        print("Power:", power(x, b))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
