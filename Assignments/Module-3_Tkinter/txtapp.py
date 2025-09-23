import tkinter

app=tkinter.Tk()
app.title("TOPS")
app.geometry("300x300")
app.config(bg="light blue")

tkinter.Label(text="Firstname:",bg="light blue",fg="red",font='Constantia 15 bold').grid(row=0,column=0)

tkinter.Label(text="Lastname:",bg="light blue",fg="red",font='Constantia 15 bold').grid(row=1,column=0)

fnm=tkinter.Entry()
fnm.grid(row=0,column=1)
lnm=tkinter.Entry()
lnm.grid(row=1,column=1)

def getval():
    print("Firstname:",fnm.get())
    print("Lastname:",lnm.get())
    

tkinter.Button(text="Submit",fg="red",font='Constantia 15 bold',command=getval).place(x=100,y=100)
app.mainloop()
