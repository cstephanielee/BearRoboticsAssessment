class BankAccount:
    def __init__(self, id, surname, first_name, pin, balance):
        self.id = id
        self.surname = surname
        self.first_name = first_name
        self.pin = pin
        self.balance = balance

    def getId(self):
        return self.id

    def getSurname(self):
        return self.surname

    def getFirstName(self):
        return self.first_name

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
