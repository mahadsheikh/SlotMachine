import random


MAX_LINES = 3  # global constant for the lines they can bet on
MAX_BET = 100
MIN_BET = 1
# defining the number of cols and rows in our slot machine 
ROW = 3
COL = 3
# using a dictionary to have set the symbols in the reels, using alphabets instead of images to make it easy
symbol_count = { # this is defined for each of the cols or reels in the slot machine
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}


def get_slot_spin(rows,cols,symbols): # this is to make the slot machine stucture decided by the no of rows and cols
    all_symbols = [] # need to populate this list by iteratin thru the dictionary
    for symbol, sym_count in symbols.items(): # iterates thru the dict and store the frequency of symbols that we have for each reel
        for _ in range(sym_count):
            all_symbols.append(symbol)

    # need to set how many values in every col

    columns = [] # 3 cols total hence the 3 nested lists would be made

    #for each col we need the number of values decided by how many rows we have 

    for _ in range(cols):
        column = []
        current_sym = all_symbols[:] # this is the copy list and we need to make a copy by using the colon other wise it acts as a reference
        for row in range(rows):
            value = random.choice(current_sym) # we need to use a copy of the all symbols list beacue once we select one element we cant use it again so we will just remove it entirely causing it to be removed
            current_sym.remove(value) # removing the selected to remove using it again
            column.append(value)

        columns.append(column)

    return columns



def print_slot(columns):
    # since we created nested list so they are basically rows and we need to transpose them to cols so we can use them
    #transposing the nested col list

    for row in range(len(columns[0])):  # determine the number of rows and that we get from the number of elements in each col hence this logic
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end = " | ") # end by default is new line but we can change it so that we can make it do what we want, we still want a new line after evey row
            else:
                print(column[row], end = "")
        print() # this is so that after every row we can get a new line in the print and have it sorted or just print a new line after the for loop ends



def deposit(): #responsible to collect user input for the money they deposit
    while True: #run until valid amount
        amount = input("What amount would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount) # string to int for the amount after check
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number")

    return amount

def get_no_lines():
    # pick number between 1 and 3 since max lines is 3
    while True: #run until valid lines
        lines = input("Enter the number of lines ou would like to bet on (1-"+str(MAX_LINES)+")? => ")
        if lines.isdigit():
            lines = int(lines) # string to int for the lines after check
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be valid in range.")
        else:
            print("Please enter a valid number")

    return lines


def get_bet():
    # this functions will get all the bet that the user places
    while True: #run until valid amount
        b_amount = input("What amount would you like to bet? $")
        if b_amount.isdigit():
            b_amount = int(b_amount) # string to int for the b_amount after check
            if MIN_BET <= b_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number")

    return b_amount




def main(): # this is done to call it when we need to re run the program
    balance = deposit()
    lines = get_no_lines()

    # got to check if the bet is in the balance range so using while loop
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if total_bet > balance:
            print(f"Insufficient Balance to place bet. Current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${lines*bet}.")

    slots = get_slot_spin(ROW,COL,symbol_count)
    print_slot(slots)

main()