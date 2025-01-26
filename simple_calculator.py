import customtkinter
from tkinter import messagebox
from tkinter import END
root=customtkinter.CTk()
root.title("Simple Calculator")
root.geometry("300x340")
root.config(bg="black")
#functionality Part
def clear():
    entryField.delete(0,END)
def click(number):
    entryField.insert(END,number)
def answer():
    try:
        expression = entryField.get()
        if(len(expression)==0):
            #messagebox.showerror("Error","Please enter some number")
            pass
        elif(expression.isalpha()):
            messagebox.showerror("Error", "Please enter only digit values")
        else:
            res = eval(expression)
            entryField.delete(0, END)
            entryField.insert(0, res)
    except SyntaxError:
        messagebox.showerror("Error","Invalid Expression")
    except ZeroDivisionError:
        messagebox.showerror("Error","A number cannot be divided by zero")
def delete():
    expression = entryField.get()
    l=len(expression)
    expression=expression[0:l-1]
    entryField.delete(0, END)
    entryField.insert(0,expression)


entryField=customtkinter.CTkEntry(root,font=("arial",20,"bold"),text_color="white",fg_color="black",border_color="white",width=280,height=50,bg_color="black")
entryField.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
b7=customtkinter.CTkButton(root,text="7",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('7'))
b7.grid(row=1,column=0,pady=10)
b8=customtkinter.CTkButton(root,text="8",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('8'))
b8.grid(row=1,column=1)
b9=customtkinter.CTkButton(root,text="9",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('9'))
b9.grid(row=1,column=2)
bplus=customtkinter.CTkButton(root,text="+",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",fg_color="orange",hover_color="green",command=lambda :click('+'))
bplus.grid(row=1,column=3)

b4=customtkinter.CTkButton(root,text="4",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('4'))
b4.grid(row=2,column=0,pady=10)
b5=customtkinter.CTkButton(root,text="5",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('5'))
b5.grid(row=2,column=1)
b6=customtkinter.CTkButton(root,text="6",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('6') )
b6.grid(row=2,column=2)
bminus=customtkinter.CTkButton(root,text="-",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",fg_color="orange",hover_color="green",command=lambda :click('-'))
bminus.grid(row=2,column=3)

b1=customtkinter.CTkButton(root,text="1",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('1'))
b1.grid(row=3,column=0,pady=10)
b2=customtkinter.CTkButton(root,text="2",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('2'))
b2.grid(row=3,column=1)
b3=customtkinter.CTkButton(root,text="3",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('3'))
b3.grid(row=3,column=2)
bmultiply=customtkinter.CTkButton(root,text="*",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",fg_color="orange",hover_color="green",command=lambda :click('*'))
bmultiply.grid(row=3,column=3)

b0=customtkinter.CTkButton(root,text="0",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('0'))
b0.grid(row=4,column=0,pady=10)
bdot=customtkinter.CTkButton(root,text=".",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",command=lambda :click('.'))
bdot.grid(row=4,column=1)
bclear=customtkinter.CTkButton(root,text="C",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",fg_color="red",hover_color="red4",command=clear)
bclear.grid(row=4,column=2)

bdivision=customtkinter.CTkButton(root,text="/",font=("arial",20,"bold"),width=60,bg_color="black",cursor="hand2",fg_color="orange",hover_color="green",command=lambda :click('/'))
bdivision.grid(row=4,column=3)
bdelete=customtkinter.CTkButton(root,text="DEL",font=("arial",20,"bold"),width=140,bg_color="black",cursor="hand2",fg_color="red",hover_color="red3",command=delete)
bdelete.grid(row=5,column=0,columnspan=2,pady=10)
bequal=customtkinter.CTkButton(root,text="=",font=("arial",20,"bold"),width=140,bg_color="black",cursor="hand2",fg_color="green",hover_color="green3",command=answer)
bequal.grid(row=5,column=2,columnspan=2,pady=10)
root.mainloop()