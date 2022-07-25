from tkinter import *

root = Tk()
root.title('checkboxes_learning')
root.geometry('500x300')

def parse():
    print(chkb1.get(),chkb2.get(),chkb3.get(),chkb4.get())

chkb1 = IntVar()
Checkbutton(text = 'Python', variable =chkb1).grid(row=0, sticky=W)
chkb2 = IntVar()
Checkbutton(text = 'PHP', variable =chkb2).grid(row=1, sticky=W)
chkb3 = IntVar()
Checkbutton(text = 'Ruby', variable =chkb3).grid(row=2, sticky=W)
chkb4 = IntVar()
Checkbutton(text = 'C+++', variable =chkb4).grid(row=3, sticky=W)

btn1 = Button(text='get the selection', command=parse).grid(row=4, sticky=W)
btn2 = Button(text='Close all', command = root.destroy).grid(row=5, sticky=E)

root.mainloop()