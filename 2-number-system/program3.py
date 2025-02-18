from program2 import base_p_to_decimal
from program1 import decimal_to_base, digits_to_string

def run():
    while True:
        # main function to run the program
        print("=" * 50)
        print(" " * 10 + "Program 3: Base p to Base q Conversion")
        print("=" * 50)
        number_str = input("Enter the number in base p: ")
        base_p = int(input("Enter the base p: "))
        base_q = int(input("Enter the base q: "))

        # convert from base p to decimal
        decimal = base_p_to_decimal(number_str, base_p)

        # convert from decimal to base q
        digits = decimal_to_base(decimal, base_q)
        result = digits_to_string(digits, base_q)

        print("-" * 50)
        print(f"Number in base {base_q}: {result}")
        print("=" * 50)

        # ask the user if they want to rerun or return to the menu
        choice = input("Do you want to (1) rerun this program or (2) return to the main menu? (1/2): ")
        if choice == '2':
            break  # return to the main menu

if __name__ == "__main__":
    run()