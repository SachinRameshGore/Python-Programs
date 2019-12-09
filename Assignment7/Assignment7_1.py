class BookStore:
	NoOfBooks=0;
	def __init__(self,name,auther):
		self.Name = name
		self.Auther = auther
		BookStore.NoOfBooks+=1;
		
		
	def Display(self):
		print(self.Name)
		print(self.Auther)
		print(BookStore.NoOfBooks)
	


def main():
	
	obj1 = BookStore("Linux System Programming","Robert love")
	
	obj1.Display();
	
	obj2 = BookStore("C Programming","Dennis Ritche")
	
	obj2.Display();
	
if __name__=="__main__":
	main();