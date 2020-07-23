# Initialise variables
options = [0, 1, 2, 3, 4]

# Start loop so that it runs until the user exit
while True:
    # Print options and get selection from user
    print("Please select an option: "
          "\n1: Addition "
          "\n2: Subtraction "
          "\n3: Multiplication "
          "\n4: Division"
          "\n0: Exit")
    selection = int(input())

    # If statement to check to see if the selection is valid
    if selection in options:
        # If statement to run the calculator unless the user selects 0
        if selection in (1, 2, 3, 4):
            # Get user to input two numbers and save them as x and y
            print("Please enter two numbers:")
            x = int(input())
            y = int(input())
            if selection == 1:
                result = x + y
                print("The result is: {}".format(result))
            elif selection == 2:
                result = x - y
                print("The result is: {}".format(result))
            elif selection == 3:
                result = x * y
                print("The result is: {}".format(result))
            elif selection == 4:
                result = x // y
                print("The result is: {}".format(result))
        # Exit the program if user selects 0
        elif selection == 0:
            print("Goodbye!")
            break
    # Ensure the user selects one of the options available
    else:
        print("Please choose a valid option")
