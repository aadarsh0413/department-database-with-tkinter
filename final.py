import customtkinter as ctk
 
from tkinter import * 
from tkinter import ttk
import mysql.connector


import mysql.connector
con = mysql.connector.connect(host="localhost",password='root',user='root')

global let
let = con.cursor ()



#GUI

root = ctk.CTk()
root.title("first project")

frame = ctk.CTkFrame(root,200,200)
frame.pack()

label1 = ctk.CTkLabel(frame,text="DEPARTMENT ID ")
label1.grid(row=0,column=0)

t1 = ctk.CTkEntry(frame)
t1.grid(row=0,column=1)

label2 = ctk.CTkLabel(frame,text="DEPARTMENT NAME ")
label2.grid(row=1,column=0)

t2 = ctk.CTkEntry(frame)
t2.grid(row=1,column=1)

def insert():
    let.execute("USE depT")
    id = '"' +t1.get()+'"'
    name= '"' +t2.get()+'"'
    let.execute("INSERT INTO dep VALUES ({},{})".format(id,name))
    t1.delete(0,END)
    t2.delete(0,END)
    con.commit()



button = ctk.CTkButton(frame,100,10,5,text="INSERT",command=insert)
button.grid(row=2,column=0)

def show_table():
   let.execute("USE depT")
   let.execute("SELECT * FROM dep")
   
   flag = 0
  
   table.heading("dep_id",text='dept_id')
   table.heading("dep_name",text='dep_name')
  
   table.pack(fill="both",expand=True)

   if flag ==0:
         d = let.fetchall()
         for i in d : 
          table.insert(parent="",index=0,values= i)
          flag=1
   else :
       k = let.fetchall()
       for i in k :
           if i not in d:
              table.insert(parent="",index=0,values= i)
               
   
#    if flag !=1 :
# # insert the values 
#     for i in d : 
#       table.insert(parent="",index=0,values= i)
#     flag=1
   
#    else:
#     table.delete(0,END)

  

button = ctk.CTkButton(frame,100,10,5,text="DISPLAY",command=show_table)
button.grid(row=2,column=1)

table = ttk.Treeview(root,columns= ("dep_id","dep_name"),show="headings")
table.delete()


root.mainloop()