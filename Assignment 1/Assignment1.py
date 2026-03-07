# Program Name: Assignment1.py
# Course: IT3883 / Section W01
# Student Name: Jaxon Evans
# Assignment Number: Assignment 1
# Due Date: 01/24/2026
# Purpose: Give the user a menu of four options to choose.
# Each selection ranges from storing information, clearing data, display what is stored, and exiting the program
# Resources Used: Python review modules and previous python assignments

# Empty string to start, but it will store all the users inputs
data = ""

# Extra variable to control the loop.
loop = True

# Create while loop to run while true, but breaks if it becomes false
while loop:

    # Creates the menu and gives the user different options
    print("\nMenu:")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Get the users input
    opt = input("Enter your number: ")

    # Checks the users input to identify if it is valid or invalid
    valid = False

    # Allows the user to enter any text and stores it in the buffer
    if opt == "1":
        text = input("Add text: ")
        data = data + text
        valid = True

    # Clears anything that the user previously put inside the buffer
    if opt == "2":
        data = ""
        print("Buffer cleared.")
        valid = True

    # Displays the text in the current buffer
    if opt == "3":
        print("\nCurrent Buffer:")
        print(data)
        valid = True

    # Exits the program
    if opt == "4":
        print("Exiting program.")
        loop = False
        valid = True

    # If user enters a number that is not 1-4 then it displays a message
    if not valid:
        print("Enter a number from 1 to 4.")
