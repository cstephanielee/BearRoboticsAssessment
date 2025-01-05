from bankAccount import BankAccount

def pinVerification(pin):
    if pin == '1234':
        return True
    else:
        return False

def displayBalance(id):
    balance = 0
    if id == 'BA123':
        balance = 50000
    return balance

def deposit(id, amount):
    #Add deposit amount to account balance
    return True

def withdraw(id, amount):
    #Check if amount is smaller than balance
    #If amount is smaller than balance then return true
    return True


if __name__ == '__main__':

    testAccount = BankAccount(id='BA123', surname='Smith', first_name='Bob', pin='1234', balance=50000)

    atmOn = True
    card_inserted = True
    while atmOn:
        print("Welcome, please insert your card")
        print("*Card inserted*")
        print("* Test pin is 1234 *")
        pin = input("Please input your pin: ")
        card_inserted = True

        while card_inserted:
            verify = pinVerification(pin)

            #Selecting account
            if verify:
                print("Please select an account:")
                print("1 - Current Account")
                print("2 - Savings Account")
                account = int(input(">>> "))
                if account == 1:
                    print("CURRENT ACCOUNT")
                else:
                    print("Savings ACCOUNT")
                #Display menu
                print("Please select an option:")
                print("1 - See balance")
                print("2 - Deposit")
                print("3 - Withdraw")
                option = int(input(">>> "))
                if option == 1:
                    print('Balance: ', displayBalance('BA123'))
                elif option == 2:
                    deposit_amount = int(input("Please input your deposit amount: "))
                    print("Please insert notes into the bills slot")
                    #This would be where we check if the notes inserted matches the amount inserted
                    deposit('BA123', deposit_amount)
                    print(deposit_amount, "has been deposited")
                elif option == 3:
                    withdraw_amount = int(input("Please input the amount you want to withdraw: "))
                    print("Please wait as we count your cash")
                    #This would be where we check if the ATM cash bin has enough cash
                    withdraw('BA123', withdraw_amount)
                    print("Please take the bills from the cash slot")
                print("Thanks for using the ATM, please take your card")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                card_inserted = False
            else:
                print("Incorrect pin, please try again")
                pin = input("Please input your pin: ")




