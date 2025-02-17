def decimal_to_base(n, base):
    # convert a decimal number `n` to a given `base`
    digits = []
    while n > 0:
        digits.append(n % base)
        n = n // base
    digits.reverse()
    return digits

def digits_to_string(digits, base):
    # convert a list of digits to a string representation
    if base > 10:
        # for bases > 10, use letters for digits > 9
        return ''.join([chr(ord('A') + d - 10) if d >= 10 else str(d) for d in digits])
    else:
        return ''.join(map(str, digits))

def run():
    # main function to run the program
    print("=" * 50)
    print(" " * 10 + "Program 1: Number Conversion")
    print("=" * 50)
    n = int(input("Enter a natural number: "))

    # binary conversion
    binary = decimal_to_base(n, 2)
    print("-" * 50)
    print(f"Binary: {digits_to_string(binary, 2)}")

    # octal conversion
    octal = decimal_to_base(n, 8)
    print(f"Octal: {digits_to_string(octal, 8)}")

    # hexadecimal conversion
    hexa = decimal_to_base(n, 16)
    print(f"Hexadecimal: {digits_to_string(hexa, 16)}")
    print("=" * 50)

if __name__ == "__main__":
    run()