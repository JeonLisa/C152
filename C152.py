from tkinter import *
root=Tk()
root.title("Multidimensional Arrays")
root.geometry("500x500")
label_1=Label(root)
label_1.place(relx=0.5,rely=0.3,anchor=CENTER)
Array_3d=[[["Lim Ju Kyung","A","Good"],["Lee Sooho","A+","Exelent"],["Han Seo Jun","B","Good"],["Kang Sujin","A-","Good Job"]]]
def Check():
    label_1["text"]=Array_3d[0][1][0]+" Got Grade "+Array_3d[0][1][1]+" And He Is Doing "+Array_3d[0][1][2]
button_1=Button(root,text="Check Your Report Card",command=Check)
button_1.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()