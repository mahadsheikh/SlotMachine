MAX_LINES = 3  # global constant for the lines they can bet on
MAX_BET = 100
MIN_BET = 1



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
    bet = get_bet()
    print(balance,lines,bet)


main()