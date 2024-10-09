class BankAccount:
    def __init__(self):
        self.account_balance=0
    def deposit(self,amount):
        self.account_balance+= amount

    def withdraw(self,amount):
        
        if  self.account_balance< amount:
            return False
        
        else:
            self.account_balance >= amount
            return True
    
    def display_balance(self):
        print (f"the current balance is:{self.account_balance}")


#  Le paramètre self est nécessaire pour accéder aux attributs et méthodes de l'instance de la classe.