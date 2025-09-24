import tkinter as t
import csv  as c

def expense():
    with open ("expenses.csv","a",newline='') as l:
        write=c.writer(l)
        write.writerow([e2.get(),int(e.get()),e1.get(),e3.get()])

m=t.Tk()
m.title("Expense Tracker")
w=t.Label(m,text='Amt spent').grid(row=0)
w=t.Label(m,text='spent where').grid(row=1)
w=t.Label(m,text='Date in DD-MM-YYYY').grid(row=2)
w=t.Label(m,text='UTR').grid(row=3)
e=t.Entry(m)
e1=t.Entry(m) 
e2=t.Entry(m)
e3=t.Entry(m)
e.grid(row=0,column=1)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
b=t.Button(m,text="submit",background='lightgray',activebackground='blue',command=expense).grid(row=4)
m.mainloop() 