def char_to_digit(c):
    # convert a character to its corresponding digit value
    if c.isdigit():
        return int(c)
    else:
        return ord(c.upper()) - ord('A') + 10

def base_p_to_decimal(number_str, base_p):
    # convert a number from base `p` to decimal
    decimal = 0
    length = len(number_str)
    for i, char in enumerate(number_str):
        decimal += char_to_digit(char) * (base_p ** (length - i - 1))
    return decimal

def run():
    while True:
        # main function to run the program
        print("=" * 50)
        print(" " * 10 + "Program 2: Base p to Decimal Conversion")
        print("=" * 50)
        number_str = input("Enter the number in base p: ")
        base_p = int(input("Enter the base p: "))

        decimal = base_p_to_decimal(number_str, base_p)
        print("-" * 50)
        print(f"Decimal equivalent: {decimal}")
        print("=" * 50)

        # ask the user if they want to rerun or return to the menu
        choice = input("Do you want to (1) rerun this program or (2) return to the main menu? (1/2): ")
        if choice == '2':
            break  # return to the main menu

if __name__ == "__main__":
    run()