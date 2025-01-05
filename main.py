from bankAccount import BankAccount

def pinVerification(pin):
    if pin == '1234':
        return True
    else:
        return False
    #Pin verification would be handled better once connected to a database

def accountSelection():
    while True:
        print("Please select an account:")
        print("1 - Current Account")
        print("2 - Savings Account")
        try:
            account = int(input(">>> "))

            if account == 1:
                return 'CURRENT ACCOUNT'
            elif account == 2:
                return 'SAVINGS ACCOUNT'
            else:
                print("Account does not exist")

        except ValueError:
            print("Invalid input. Please enter a valid number")

def displayMenu():
    print("Please select an option:")
    print("1 - See balance")
    print("2 - Deposit")
    print("3 - Withdraw")

def displayBalance(id):
    balance = 0
    if id == 'BA123':
        balance = 50000
    return balance

def deposit(id):
    dep = True
    while dep:
        try:
            deposit_amount = int(input("Please input your deposit amount: "))
            print("Please insert notes into the bills slot")
            # This would be where we check if the notes inserted matches the amount inserted
            # Add deposit amount to account balance
            print("$",deposit_amount, "has been deposited")
            dep = False
        except ValueError:
            print("Invalid input. Please enter a number")

    return True

def withdraw(id):
    wd = True
    while wd:
        try:
            withdraw_amount = int(input("Please input the amount you want to withdraw: "))
            print("Please wait as we count your cash...")
            #This would be where we check if the ATM cash bin has enough cash
            #Check if amount is smaller than balance
            #If amount is smaller than balance then return true
            print("$",withdraw_amount, "has been withdrawn")
            print("Please take the bills from the cash slot")
            wd = False
        except ValueError:
            print("Invalid input. Please enter a number")
    return True


if __name__ == '__main__':

    testAccount = BankAccount(id='BA123', surname='Smith', first_name='Bob', pin='1234', balance=50000)

    atmOn = True
    card_inserted = True
    menu_selection = False
    while atmOn:
        print("Welcome, please insert your card")
        print("*Card inserted*")
        print("* Test pin is 1234 *")
        pin = input("Please input your pin: ")
        card_inserted = True

        while card_inserted:
            #Verify pin
            verify = pinVerification(pin)

            if verify:
                #Selecting account
                print(accountSelection())
                while menu_selection == False:
                    #Display menu
                    displayMenu()
                    try:
                        option = int(input(">>> "))

                        if option == 1:
                            print('Balance: ', displayBalance('BA123'))
                            menu_selection = True
                        elif option == 2:
                            deposit('BA123')
                            menu_selection = True
                        elif option == 3:
                            withdraw('BA123')
                            menu_selection = True
                        else:
                            print("Invalid option")
                    except ValueError:
                        print("Invalid input. Please enter a valid number")

                print("Thanks for using the ATM, please take your card")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                card_inserted = False
                menu_selection = False
            else:
                print("Incorrect pin, please try again")
                pin = input("Please input your pin: ")




