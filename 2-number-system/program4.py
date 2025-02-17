def run():
    # main function to run the program
    print("=" * 50)
    print(" " * 10 + "Program 4: ASCII to Decimal Conversion")
    print("=" * 50)
    input_str = input("Enter a string: ")

    print("-" * 50)
    print("Character | Decimal Value")
    print("-" * 50)
    total_sum = 0
    for char in input_str:
        decimal_value = ord(char)
        print(f"{char:^9} | {decimal_value:^13}")
        total_sum += decimal_value

    print("-" * 50)
    print(f"Total Sum: {total_sum}")
    print("=" * 50)

if __name__ == "__main__":
    run()