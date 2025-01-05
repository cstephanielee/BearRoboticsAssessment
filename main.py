from bankAccount import BankAccount

if __name__ == '__main__':

    testAccount = BankAccount(id='BA123', surname='Smith', first_name='Bob', pin='1234', balance=50000)

    atmOn = True
    if atmOn:
        print("Welcome, please insert your card")
