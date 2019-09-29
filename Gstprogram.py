class product:
	def __init__(self):
		self.product_id=input("Enter the product id =")
		self.product_name=input("Enter the product name =")
		self.product_price=float(input("Enter the product price ="))
	def product_info(self):
		print("Product Id :",self.product_id)
		print("Product name :",self.product_name)
		print("Product price :",self.product_price)
		
class gst(product):
	def __init__(self):
		super().__init__()
	def gst(self):
		gst=self.product_price*0.02
		self.product_price=self.product_price+gst
		print("After Applying Gst Product Price is :",self.product_price)
		
g1=gst()
g1.product_info()
g1.gst()