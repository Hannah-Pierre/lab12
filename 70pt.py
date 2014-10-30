####################################################
#
#              70pt - Add a new Button 
#                  called "Goodbye"
#
####################################################

from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1["text"]= "Hello"
		self.button1["background"] = "red"
		self.button1.grid(row=0,column=0)	### (1)


		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="World!")  
		self.button2.configure(background="green")               
		self.button2.grid(row=0,column=1)	 ### (2)
		

		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Test?", background="cyan")  
		self.button3.grid(row=0,column=2)	  ### (3)
		
		
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="goodbye", background="yellow")  
		self.button3.grid(row=0,column=3)	  ### (4)	
	
		
root = Tk()
myapp = MyApp(root)
root.mainloop()