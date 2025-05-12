# add import

# define the main function to call the multiplication table functions

import question_b

def main():                                                         # defines and runs the main menu and prompt for inputs

    while True:
        print("User Menu:")
        print("1 - Display Multiplication Table")
        print("2 - Exit")

        choice = input("Enter your choice (1 or 2): ")              # prompts user to choose between two options

        if choice == '1':                               
            table = question_b.create_multiplication_table ()
            print ("\n Multiplication Table:")
            question_b.display_multiplication_table (table)

        elif choice == '2':                                         # confirms user input to exit the program

            confirm_exit = input ('Are you sure you want to exit? (y/n)')

            if confirm_exit == 'y':                                 # exits program
                print ('Exiting program... ')
                break
            else:                                                   # continues program
                print ('Continuing program... \n')

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()