class product:
	def __init__(self):
		self.product_id=input("Enter the product id =")
		self.product_name=input("Enter the product name =")
		self.product_price=float(input("Enter the product price ="))
	def product_info(self):
		print("Product Id :",self.product_id)
		print("Product name :",self.product_name)
		print("Product price :",self.product_price)
		
class discount(product):
	def __init__(self):
		super().__init__()
	def discount(self):
		discount=int(input("Enter your Discount ="))
		self.product_price=self.product_price-(self.product_price/100)*discount
		print("After Adding Discount Product price is :",self.product_price)
		
d1=discount()
d1.product_info()
d1.discount()
		