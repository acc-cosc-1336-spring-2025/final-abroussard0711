#write functions here, don't add input('') statements here!

# to create the program classes and functions

def test_config():
    return True

def create_multiplication_table ():                 # create the multiplication table function

    table = []                                      # create the empty table list

    for i in range (1, 6):                          # create rows 1 - 6
        row = []

        for j in range (1, 11):                     # create columns 1 - 10
            row.append (i * j)
        
        table.append (row)                          # create multiplication table
    
    return table


def display_multiplication_table (table):           # create display function

    for row in table:

        for num in row:
            print(f"{num:3}", end=" ")              # Format spacing

        print()