from operations import add, subtract, multiply, divide, power, modulus
from utils import get_number

while True:
    print("\n--- CLI Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Power\n7. Exit")

    choice = input("Enter choice: ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in {"1", "2", "3", "4", "5", "6"}:
        print("Invalid choice!")
        continue

    x = get_number("Enter first number: ")
    y = get_number("Enter second number: ")

    try:
        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", subtract(x, y))
        elif choice == "3":
            print("Result:", multiply(x, y))
        elif choice == "4":
            print("Result:", divide(x, y))
        elif choice == "5":
            print("Result:", modulus(x, y))
        elif choice == "6":
            print("Result:", power(x, y))
    except ValueError as e:
        print("Error:", e)
