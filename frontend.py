from tkinter import *
import backend
window=Tk()
def end():
    exit()

def activate():
    if link_1.get()!="" and times_1.get()!="" and timee_1!=""  :
        backend.join(gcp.get(),str(link_1.get()),str(times_1.get()),str(timee_1.get()))
    else:
        inst.config(text="Give  a valid link and starting and ending time atleast in Link 1")
    if link_2.get()!="" and times_2.get()!="" and timee_2!=""  :
        backend.join(gcp.get(),str(link_2.get()),str(times_2.get()),str(timee_2.get()))
    else:
        inst.config(text="FINISHED")
    if link_3.get()!="" and times_3.get()!="" and timee_3!=""  :
        backend.join(gcp.get(),str(link_3.get()),str(times_3.get()),str(timee_3.get()))
    else:
        inst.config(text="FINISHED")        
    if link_4.get()!="" and times_4.get()!="" and timee_4!=""  :
        backend.join(gcp.get(),str(link_4.get()),str(times_4.get()),str(timee_4.get()))
    else:
        inst.config(text="FINISHED")
    if link_5.get()!="" and times_5.get()!="" and timee_5!=""  :
        backend.join(gcp.get(),str(link_5.get()),str(times_5.get()),str(timee_5.get()))
    else:
        inst.config(text="FINISHED")
    if link_6.get()!="" and times_6.get()!="" and timee_6!=""  :
        backend.join(gcp.get(),str(link_6.get()),str(times_6.get()),str(timee_6.get()))
    else:
        inst.config(text="FINISHED")
    inst.config(text="FINISHED")
    


l1=Label(window,text="Link1")
l1.grid(row=0,column=0)
l2=Label(window,text="Link2")
l2.grid(row=1,column=0)
l3=Label(window,text="Link3")
l3.grid(row=2,column=0)
l4=Label(window,text="Link4")
l4.grid(row=3,column=0)
l5=Label(window,text="Link5")
l5.grid(row=4,column=0)
l6=Label(window,text="Link6")
l6.grid(row=5,column=0)

link_1=StringVar()
e1=Entry(window,textvariable=link_1,width=50)
e1.grid(row=0,column=1)
t1l1=Label(window,text="Start Time:")
t1l1.grid(row=0,column=2)
times_1=StringVar()
st1=Entry(window,textvariable=times_1)
st1.grid(row=0,column=3)
t1l2=Label(window,text="End Time:")
t1l2.grid(row=0,column=4)
timee_1=StringVar()
et1=Entry(window,textvariable=timee_1)
et1.grid(row=0,column=5)

link_2=StringVar()
e2=Entry(window,textvariable=link_2,width=50)
e2.grid(row=1,column=1)
t2l1=Label(window,text="Start Time:")
t2l1.grid(row=1,column=2)
times_2=StringVar()
st2=Entry(window,textvariable=times_2)
st2.grid(row=1,column=3)
t2l2=Label(window,text="End Time:")
t2l2.grid(row=1,column=4)
timee_2=StringVar()
et2=Entry(window,textvariable=timee_2)
et2.grid(row=1,column=5)

link_3=StringVar()
e3=Entry(window,textvariable=link_3,width=50)
e3.grid(row=2,column=1)
t3l1=Label(window,text="Start Time:")
t3l1.grid(row=2,column=2)
times_3=StringVar()
st3=Entry(window,textvariable=times_3)
st3.grid(row=2,column=3)
t3l2=Label(window,text="End Time:")
t3l2.grid(row=2,column=4)
timee_3=StringVar()
et3=Entry(window,textvariable=timee_3)
et3.grid(row=2,column=5)

link_4=StringVar()
e4=Entry(window,textvariable=link_4,width=50)
e4.grid(row=3,column=1)
t4l1=Label(window,text="Start Time:")
t4l1.grid(row=3,column=2)
times_4=StringVar()
st4=Entry(window,textvariable=times_4)
st4.grid(row=3,column=3)
t4l2=Label(window,text="End Time:")
t4l2.grid(row=3,column=4)
timee_4=StringVar()
et4=Entry(window,textvariable=timee_4)
et4.grid(row=3,column=5)

link_5=StringVar()
e5=Entry(window,textvariable=link_5,width=50)
e5.grid(row=4,column=1)
t5l1=Label(window,text="Start Time:")
t5l1.grid(row=4,column=2)
times_5=StringVar()
st5=Entry(window,textvariable=times_5)
st5.grid(row=4,column=3)
t5l2=Label(window,text="End Time:")
t5l2.grid(row=4,column=4)
timee_5=StringVar()
et5=Entry(window,textvariable=timee_5)
et5.grid(row=4,column=5)

link_6=StringVar()
e6=Entry(window,textvariable=link_6,width=50)
e6.grid(row=5,column=1)
t6l1=Label(window,text="Start Time:")
t6l1.grid(row=5,column=2)
times_6=StringVar()
st6=Entry(window,textvariable=times_6)
st6.grid(row=5,column=3)
t6l2=Label(window,text="End Time:")
t6l2.grid(row=5,column=4)
timee_6=StringVar()
et6=Entry(window,textvariable=timee_6)
et6.grid(row=5,column=5)

cl=Label(window,text="chrome.exe path:")
cl.grid(row=6,column=0)
cp=StringVar()
gcp=Entry(window,textvariable=cp,width=50)
gcp.grid(row=6,column=1)


start=Button(window,text="START!",width=20,pady=10,command=activate)
start.grid(row=7,column=1)
start=Button(window,text="END",width=20,pady=10,command=end)
start.grid(row=7,column=3)

inst=Label(window,text="INSTRUCTION:- \n1-Specify your chrome.exe path\n2-Keep atleast 10 second break in each link\n3-Press END to end the script in between\n4-Teams application should be running in background\n4-Time should be strictly in HH:MM:SS format")
inst.place(relx = 0.5,
                   rely = 0.8,
                   anchor = 'center')
inst.grid(row=8,column=2)
window.mainloop()