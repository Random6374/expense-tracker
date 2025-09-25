import tkinter as t
import csv  as c

def expense():
    with open ("expenses.csv","a",newline='') as l:
        write=c.writer(l)
        write.writerow([e2.get(),int(e.get()),e1.get(),e3.get()])
    
def add_screen():
    menu.pack_forget()
    review.pack_forget()
    add_expense.pack(fill="both",expand=True)

def menu_screen():
    add_expense.pack_forget()
    review.pack_forget()
    menu.pack(fill="both",expand=True)

def review_screen():
    menu.pack_forget()
    add_expense.pack_forget()
    review.pack(fill="both",expand=True)
    

m=t.Tk()
m.title("Expense Tracker")

#############################################################################
#THE FRAMES
menu=t.Frame(m,bg='lightblue')
add_expense=t.Frame(m,bg='lightblue')
review=t.Frame(m,background="lightblue")
#############################################################################
menu.pack(fill='both',expand=True)
button=t.Button(menu,text='Add expense',background='lightgray',activebackground='red',command=add_screen).pack()
button=t.Button(menu,text="Review",background='lightgray',activebackground='blue',command=review_screen).pack()


#############################################################################
#The Add Expense Screen
w=t.Label(add_expense,text='Amt spent').grid(row=0)
w=t.Label(add_expense,text='spent where').grid(row=1)
w=t.Label(add_expense,text='Date in DD-MM-YYYY').grid(row=2)
w=t.Label(add_expense,text='UTR').grid(row=3)
e=t.Entry(add_expense)
e1=t.Entry(add_expense) 
e2=t.Entry(add_expense)
e3=t.Entry(add_expense)
e.grid(row=0,column=1)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
b=t.Button(add_expense,text="submit",background='lightgray',activebackground='blue',command=expense).grid(row=4)
button=t.Button(add_expense,text="back",background='lightgray',activebackground='red',command=menu_screen).grid()
###############################################################################
# for loop to read the expenses 
count=0
with open ("expenses.csv",'r') as f:
    for line in f:
        count+=1

for _ in range(0,count):
    pass
# The Review screen
button=t.Button(review,text="Back",background='lightgray',activebackground="Red",command=menu_screen).pack()

m.mainloop() 