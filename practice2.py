MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("enter the amount you want to deposit :$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a number which is greater than 0")
        else:
            print("Error: Please enter a number only here")
    return amount


def get_number_of_lines():
    while True:
        lines = input("enter the lines to bet on (1 - " + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number")
        else:
            print("Error: Please enter a number only here")
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
