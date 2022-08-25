# Code by AmirMotefaker

# Create Address Book 

from tkinter import *

root = Tk()
root.geometry('400x400')
root.config(bg = 'SlateGray3')
root.resizable(0,0)
root.title('AmirMotefaker - Address Book')
contactlist = [
    ['Elon Musk',  '0123456789'],
    ['Jeff Bezos',  '0987654321'],
    ['Bill Gates',   '4325164587'],
    ['Larry Page', '1254785412'],
    ['Sergey Brin',   '2541549805'],
    ['Steve Ballmer' , '3251807141'],
    ]
Name = StringVar()
Number = StringVar()
frame = Frame(root)
frame.pack(side = RIGHT)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

def Selected():
    return int(select.curselection()[0])
def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()
def DELETE():
    del contactlist[Selected()]
    Select_set()
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
def EXIT():
    root.destroy()
def RESET():
    Name.set('')
    Number.set('')
def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()

Label(root, text = 'NAME', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 100, y=20)
Label(root, text = 'PHONE NO.', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Number).place(x= 130, y=70)
Button(root,text=" ADD", font='arial 12 bold',bg='SlateGray4', command = AddContact).place(x= 50, y=110)
Button(root,text="EDIT", font='arial 12 bold',bg='SlateGray4',command = EDIT).place(x= 50, y=260)
Button(root,text="DELETE", font='arial 12 bold',bg='SlateGray4',command = DELETE).place(x= 50, y=210)
Button(root,text="VIEW", font='arial 12 bold',bg='SlateGray4', command = VIEW).place(x= 50, y=160)
Button(root,text="EXIT", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 300, y=320)
Button(root,text="RESET", font='arial 12 bold',bg='SlateGray4', command = RESET).place(x= 50, y=310)
root.mainloop()
