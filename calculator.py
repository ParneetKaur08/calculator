from tkinter import *
root=Tk()
root.title('CALCULATAR')
operator=""
#-----------------------------------------------------------------------functions-------------------------------------------------------------------------
def clickme (numbers):
    global operator
    operator=operator+str (numbers)
    text_input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_input.set("")

def equals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

#-------------------------------------------------------------------------frame-----------------------------------------------------------------------------

f1=Frame(root,width=900,height=700,relief=SUNKEN)
f1.pack()

#-------------------------------------------------------------------------heading------------------------------------------------------------------------------

labelinfo=Label(f1,text='calculator',font=('arial',30,'bold'),fg='blue',bd=10)
labelinfo.grid(columnspan=4)

#-------------------------------------------------------------------------textarea--------------------------------------------------------------------------------

text_input=StringVar()

txtdisplay=Entry(f1,font=('arial',20,'bold'),bd=7,textvariable=text_input,insertwidth=800,bg='white')
txtdisplay.grid(columnspan=4)

#-----------------------------------------------------------------------btn7,8,9,+,--------------------------------------------------------------------------


btn7=Button(f1,padx=16,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='7',bg='white',command=lambda:clickme(7))
btn7.grid(row=2,column=0)

btn8=Button(f1,padx=16,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='8',bg='white',command=lambda:clickme(8))
btn8.grid(row=2,column=1)

btn9=Button(f1,padx=18,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='9',bg='white',command=lambda:clickme(9))
btn9.grid(row=2,column=2)

btnadd=Button(f1,padx=17,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='+',bg='white',command=lambda:clickme('+'))
btnadd.grid(row=2,column=3)


#-----------------------------------------------------------------btn4,5,6,-,--------------------------------------------------------------------------------


btn4=Button(f1,padx=16,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='4',bg='white',command=lambda:clickme(4))
btn4.grid(row=3,column=0)

btn5=Button(f1,padx=16,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='5',bg='white',command=lambda:clickme(5))
btn5.grid(row=3,column=1)

btn6=Button(f1,padx=18,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='6',bg='white',command=lambda:clickme(6))
btn6.grid(row=3,column=2)

btnsub=Button(f1,padx=20,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='-',bg='white',command=lambda:clickme('-'))
btnsub.grid(row=3,column=3)

#---------------------------------------------------------------btn1,2,3,*,-------------------------------------------------------------------------

btn1=Button(f1,padx=16,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='1',bg='white',command=lambda:clickme(1))
btn1.grid(row=4,column=0)

btn2=Button(f1,padx=16,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='2',bg='white',command=lambda:clickme(2))
btn2.grid(row=4,column=1)

btn3=Button(f1,padx=18,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='3',bg='white',command=lambda:clickme(3))
btn3.grid(row=4,column=2)

btnmul=Button(f1,padx=20,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='*',bg='white',command=lambda:clickme('*'))
btnmul.grid(row=4,column=3)


#---------------------------------------------------------------btn0,c,/,.,=,-----------------------------------------------------------------------------------

btn0=Button(f1,padx=16,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='0',bg='white',command=lambda:clickme(0))
btn0.grid(row=5,column=0)

btnclear=Button(f1,padx=16,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='c',bg='orange',command=clrdisplay)
btnclear.grid(row=5,column=1)

btndiv=Button(f1,padx=22,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='/',bg='white',command=lambda:clickme('/'))
btndiv.grid(row=5,column=2)

btndot=Button(f1,padx=20,pady=16,fg='black',bd=7,font=('ariel',20,'bold'),text='.',bg='white',command=lambda:clickme('.'))
btndot.grid(row=5,column=3)

btnequal=Button(f1,padx=16,pady=16,fg='black',bd=7,width=17,font=('ariel',20,'bold'),text='=',bg='orange',command=equals)
btnequal.grid(columnspan=4)

root.mainloop()
