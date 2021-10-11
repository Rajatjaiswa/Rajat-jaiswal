from tkinter import*
from tkinter import ttk

root=Tk()
root.title("chatbot")
root.geometry("700x650+300+10")

def clear():
    text.delete('1.0',END)
    entry.set('')

def send():
    send="\t\t\t"+"You  "+entry.get()
    text.insert(END,'\n'+send)
    if(entry.get()==''):
        msg='please enter some input'
        label_2.config(text=msg,fg='red')
    else:
        msg=''
        label_2.config(text=msg,fg='red')
    if(entry.get()=='hello'):
        text.insert(END,'\n\n'+'Bot:Hi')
    elif(entry.get()=='hi'):
        text.insert(END,'\n\n'+'Bot:Hello')
    elif(entry.get()=='how are you?'):
        text.insert(END,'\n\n'+'Bot:i m good  would you like to have tea or cofee')
    elif(entry.get()=='cofee'):
        text.insert(END,'\n\n'+'Bot: ok sir pls wait... ')
    elif(entry.get()=='tea'):
        text.insert(END,'\n\n'+'Bot: ok sir pls wait... ')
    elif(entry.get()=='who created you?'):
        text.insert(END,'\n\n'+'Bot:Rajat_j created me')
    elif(entry.get()=='who are you?'):
        text.insert(END,'\n\n'+'Bot:i am chat bot.')
    elif(entry.get()=='where can i use you?'):
        text.insert(END,'\n\n'+'Bot:in any vender or website or application')
    elif(entry.get()=='why do you do?'):
        text.insert(END,'\n\n'+'Bot:i can give you detail information')
    elif(entry.get()=='thank you'):
        text.insert(END,'\n\n'+'Bot:you most welcome')
    elif(entry.get()=='bye'):
        text.insert(END,'\n\n'+'Bot:bye')
    else:
        text.insert(END,'\n\n'+'Bot:sorry, i didnot  recognised you')      

main_frame=Frame(root,bd=4,bg="powder blue",width=430)
main_frame.pack()

label=Label(main_frame,bd=3,width=430,text="chat with me",bg='lightgreen',fg='red',font=('arial',30,'bold'))
label.pack()

scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=('arial',14),yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
text.pack()

btn_frame=Frame(root,bd=4,bg="white",width=430)
btn_frame.pack()
label_1=Label(btn_frame,text="Type something",bg='white',fg='green',font=('arial',15,'bold'))
label_1.grid(row=0,column=0,padx=5,sticky=W)

entry=StringVar()
entry1=Entry(btn_frame,width=80,font=('arial',15,'bold'),bd=5,textvariable=entry)
entry1.grid(row=0,column=1,ipady=6)

btn=Button(btn_frame,text='send>>',font=('arial',15,'bold'),width=8,bg='green',bd=6,command=send)
btn.grid(row=1,column=1)

btn_clear=Button(btn_frame,text='clear data',font=('arial',15,'bold'),width=8,bg='red',bd=6,fg='white',command=clear)
btn_clear.grid(row=1,column=0,sticky=W)

msg=''
label_2=Label(btn_frame,text=msg,bg='white',fg='green',font=('arial',15,'bold'))
label_2.grid(row=1,column=1,padx=5,sticky=W)




root.mainloop()

