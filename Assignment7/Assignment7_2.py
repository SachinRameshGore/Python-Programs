class BankAccount:
	ROI=10.5
	def __init__(self,name,amount):
		self.Name = name
		self.Amount = amount
		
		
	
	def Diposit(self,value):
		self.Amount+=value
		print("Deposit:",self.Amount)
		
	def Withdraw(self,value):
		self.Amount-=value
		print("Withdreaw:",self.Amount)

	def CalculateInterest(self):
		
		Interest=BankAccount.ROI*self.Amount
		print("Interest:",Interest);
	
	def Display(self):
		print("Name:",self.Name)
		print("Amount:",self.Amount)
			
def main():
	
	obj1 = BankAccount("Jaydeep",10000)
	
	
	obj1.Diposit(100);
	
	obj1.Withdraw(100)
	
	obj1.CalculateInterest();
	
	obj1.Display()
if __name__=="__main__":
	main();