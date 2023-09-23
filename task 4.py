
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1  Sum")
        print("2  Subtract")
        print("3  Multiply")
        print("4  Division")
        print("5  Calculate triangle area")
        print("6  Calculate circle area")
        print("7  Calculate rectangle area")
        print("8  Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = add(num1, num2)
            print("   =   ", result)
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = subtract(num1, num2)
            print("   =   ", result)
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = multiply(num1, num2)
            print("   =   ", result)
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = divide(num1, num2)
            print("   =   ", result)
        elif choice == '5':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            result = triangle_area(base, height)
            print("   =   ", result)
        elif choice == '6':
            radius = float(input("Enter the radius of the circle: "))
            result = circle_area(radius)
            print("   =   ", result)
        elif choice == '7':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            result = rectangle_area(length, width)
            print("   =   ", result)
        elif choice == '8':
            print("Exiting")
            break
        else:
            print(" Please select a valid option.")

if __name__ == "__main__":
    main_menu()
