class ATM(object):
    def __init__(self,AtmCardNumber,PinNumber,Balance):
        self.AtmCardNumber= AtmCardNumber
        self.PinNumber= PinNumber
        self.Balance = Balance

    def checkBalance(self):
        print("Check the amount of money left in your account",self.Balance)
    
    def cashWithdrawl(self):
        print("The amount of money you want to withdraw")

card1=ATM("0007","0101",17964)

card1.checkBalance()
card1.cashWithdrawl()

print(card1.AtmCardNumber)


