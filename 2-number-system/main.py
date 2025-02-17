def display_menu():
    # display the main menu with borders for better visual appeal
    print("=" * 50)
    print(" " * 18 + "Main Menu")
    print("=" * 50)
    print("1. Convert a natural number to binary, octal, and hexadecimal")
    print("2. Convert a number from base p to decimal")
    print("3. Convert a number from base p to base q")
    print("4. Convert ASCII characters to decimal and calculate the sum")
    print("5. Exit")
    print("=" * 50)

def main():
    # main loop to keep the program running until the user chooses to exit
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # run program 1: number conversion
            import program1
            program1.run()
        elif choice == '2':
            # run program 2: base p to decimal conversion
            import program2
            program2.run()
        elif choice == '3':
            # run program 3: base p to base q conversion
            import program3
            program3.run()
        elif choice == '4':
            # run program 4: ASCII to decimal conversion
            import program4
            program4.run()
        elif choice == '5':
            # exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            # handle invalid input
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()