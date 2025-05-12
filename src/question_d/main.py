#add import

# define the main function to call the stock_purchase_history function

import question_d


def main():

    stock_list = question_d.get_stock_list ()

    if not stock_list:
        return

    while True:
        print("Stock Menu:")
        print("1 - Display Stock Purchase History")
        print("2 - Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            print(f"{'Symbol':<10} {'Company Name'}")               # Display the stock list
            print('-' * 30)

            for stock in stock_list:
                print(f"{stock.get_symbol():<10} {stock.get_company_name()}")

        elif choice == '2':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()