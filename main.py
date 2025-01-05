from bankAccount import BankAccount

def pinVerification(pin):
    if pin == '1234':
        return True
    else:
        return False

if __name__ == '__main__':

    testAccount = BankAccount(id='BA123', surname='Smith', first_name='Bob', pin='1234', balance=50000)

    atmOn = True
    while atmOn:
        print("Welcome, please insert your card")
        print("*Card inserted*")
        print("* Test pin is 1234 *")
        pin = input("Please input your pin: ")
        verify = pinVerification(pin)
        print(verify)


