#add import

# define the main function to call the stock_purchase_history function

import question_a

def main():

    while True:
        print("Stock Menu:")
        print("1 - Display Stock Purchase History")
        print("2 - Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            question_a.stock_purchase_history()

        elif choice == '2':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()