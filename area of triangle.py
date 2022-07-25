from tkinter import *

root = Tk()
root.geometry('800x500')
root.title('area of triangle')

var1=IntVar()
var2=IntVar()
var3=IntVar()

def calculus():
    var4 = var1.get() 
    var5 = var2.get()
    var6 = var3.get()
    var7 = var4+var5+var6
    en4.insert(0, var7)
    var9 = var7/2
    var8 = (var9*(var9-var4)*(var9-var5)*(var9-var6))**(0.5)
    en5.insert(0, var8)
def dele():
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)

Label(text = 'Area of triangle knowing 3 sides', font = ('arial', 20, 'bold')).grid(row = 0, column=1, sticky=W)

Label(text = 'side 1', font = ('arial', 20, 'bold'), padx=10).grid(row = 1, column=0, sticky=W)
en1 = Entry(font = ('arial', 20, 'bold'), textvariable = var1, width = 30)
en1.grid(row = 1, column = 1)
Label(text = 'side 2', font = ('arial', 20, 'bold'),padx=10).grid(row = 2, column=0, sticky=W)
en2 = Entry(font = ('arial', 20, 'bold'), textvariable = var2, width = 30)
en2.grid(row = 2, column = 1)
Label(text = 'side 3', font = ('arial', 20, 'bold'),padx=10).grid(row = 3, column=0, sticky=W)
en3 = Entry(font = ('arial', 20, 'bold'), textvariable = var3, width = 30)
en3.grid(row = 3, column = 1)
Label(text = 'Perimetr', font = ('arial', 20, 'bold'),padx=10).grid(row = 4, column=0, sticky=W)
en4 = Entry(font = ('arial', 20, 'bold'), width = 30)
en4.grid(row = 4, column = 1)
Label(text = 'Area is', font = ('arial', 20, 'bold'),padx=10).grid(row = 5, column=0, sticky=W)
en5 = Entry(font = ('arial', 20, 'bold'), width = 30)
en5.grid(row = 5, column = 1)

btn1 = Button(text = 'Calculate', font = ('arial', 20, 'bold'), width = 20, command=calculus).grid(row=6, column=1, sticky=W)
btn2 = Button(text = 'Clear', font = ('arial', 20, 'bold'), width = 10, command=dele).grid(row=6, column=1, sticky=E)
root.mainloop()