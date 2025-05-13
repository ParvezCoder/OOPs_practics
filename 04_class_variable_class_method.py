# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows 
# changing the bank name. Show that it affects all instances.
class Bank():
    bank_name = "Defaul_bank"

    def __init__(self,customer_name):
        self.customer_name = customer_name
    
    @classmethod
    def bank_name_change(cls,name):
        Bank.bank_name = name

    def show_detail(self):
        print(f"Custome: {self.customer_name}, Bank: {Bank.bank_name}")

see = Bank("Ali")
see.show_detail()
see.bank_name_change("New Bank name")
see.show_detail()
