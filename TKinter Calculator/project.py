from tkinter import Tk, Entry, Button, StringVar
class Calculator:
    def __init__(self, master):
        master.title('Simple Calculator')
        master.geometry('360x260+0+0')
        master.config(bg='#438')
        master.resizable(False, False)
               
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width = 28,bg='lightblue', font = ('Times', 16), textvariable = self.equation).place(x=0,y=0)
        Button(width=8, text = '(', relief ='flat', command=lambda:self.show('(')).place(x=0,y=50)
        Button(width=8, text = ')', relief ='flat', command=lambda:self.show(')')).place(x=90, y=50)
        Button(width=8, text = '%', relief ='flat', command=lambda:self.show('%')).place(x=180, y=50)
        Button(width=8, text = '1', relief ='flat', command=lambda:self.show(1)).place(x=0,y=90)
        Button(width=8, text = '2', relief ='flat', command=lambda:self.show(2)).place(x=90,y=90)
        Button(width=8, text = '3', relief ='flat', command=lambda:self.show(3)).place(x=180,y=90)
        Button(width=8, text = '4', relief ='flat', command=lambda:self.show(4)).place(x=0,y=130)
        Button(width=8, text = '5', relief ='flat', command=lambda:self.show(5)).place(x=90,y=130)
        Button(width=8, text = '6', relief ='flat', command=lambda:self.show(6)).place(x=180,y=130)
        Button(width=8, text = '7', relief ='flat', command=lambda:self.show(7)).place(x=0,y=170)
        Button(width=8, text = '8', relief ='flat', command=lambda:self.show(8)).place(x=180,y=170)
        Button(width=8, text = '9', relief ='flat', command=lambda:self.show(9)).place(x=90,y=170)
        Button(width=8, text = '0', relief ='flat', command=lambda:self.show(0)).place(x=0,y=210)
        Button(width=8, text = '.', relief ='flat', command=lambda:self.show('.')).place(x=90,y=210)
        Button(width=8, text = '+', relief ='flat', command=lambda:self.show('+')).place(x=270,y=90)
        Button(width=8, text = '-', relief ='flat', command=lambda:self.show('-')).place(x=270,y=130)
        Button(width=8, text = '/', relief ='flat', command=lambda:self.show('/')).place(x=270,y=170)
        Button(width=8, text = 'x', relief ='flat', command=lambda:self.show('*')).place(x=270,y=210)
        Button(width=8, text = '=', bg='green', relief ='flat', command=self.solve).place(x=180, y=210)
        Button(width=8, text = 'AC', relief ='flat', command=self.clear).place(x=270,y=50)
    def show(self, value):
        self.entry_value +=str(value)
        self.equation.set(self.entry_value)
      
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
    
    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)
    
root = Tk()
calculator = Calculator(root)
root.mainloop()