# write functions here, don't add input('') statements here!
# to create the program classes and functions

def test_config():
    return True

import os

class Stock:                                                # Create class Stock

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol (self):
        return self.__symbol

    def get_company_name (self):
        return self.__company_name

def get_stock_list ():

    stock_list = []                                         # create empty stock list

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "stock_file.dat")
#    print (file_path)

    try:
        with open(file_path, "r") as file:            # open the stock_file.dat as read only
            
            for line in file:
                parts = line.strip().split (" ", 1)         # split on first space
                
                if len(parts) == 2:                         # create 5 Stock instances
                    symbol, company_name = parts
                    stock = Stock(symbol, company_name)
                    stock_list.append(stock)                # append stocks to a list
    
    except FileNotFoundError:
        print("stock_file.dat not found. Please make sure the file exists.")
    
    return stock_list
