class BankAccount:
    def __init__(self, account_number, holder_name, initail_balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = initail_balance



    def deposit(self, amount):
        if amount >0: 
            self.__balance += amount
            print(f"Deposit of {amount} Seccuss....")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0< amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} Success....")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance
    

acc = BankAccount("PKR123", "Hamza", 80000)
acc.deposit(5000)
acc.withdraw(2000)
print("Your Balance is:", acc.get_balance())