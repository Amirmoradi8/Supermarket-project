#Model
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datain import Database

db = Database('f:/market.db')
#Gui
amir = Tk()
amir.geometry('570x400+520+80')
amir.resizable(0,0)
amir.title('سوپرمارکت مسعود')
amir.config(bg ='#3842d7')

#Functions

def populate_list():
    
    list_box.delete(0,END)
    rec = db.select_record()
    # print(rec)
    for row in rec :
        list_box.insert(END, row)
        
def save ():
    db.insert_table(name_entry.get() , price_entry.get() , price2_entry.get() , number_entry.get())
    clear()
    populate_list()
    
def clear ():
    name_entry.delete(0,END)
    price_entry.delete(0,END)
    price2_entry.delete(0,END)
    number_entry.delete(0,END)
    
    name_entry.focus_set()

def select_item(event):
    global selected_item
    index = list_box.curselection()
    selected_item = list_box.get(index)
    name_entry.delete(0,END)
    name_entry.insert(0 , selected_item[1])
        
    price_entry.delete(0,END)
    price_entry.insert(0, selected_item[2])
        
    price2_entry.delete(0,END)
    price2_entry.insert(0 , selected_item[3])
        
    number_entry.delete(0,END)
    number_entry.insert(0 , selected_item[4])

def remove():
    
    global selected_item
    index = list_box.curselection()
    selected_item = list_box.get(index)
    x = messagebox.askquestion('.!.!Warning!.!.' , 'گزینه انتخابی حذف شود؟')
    if x == 'yes':
        db.delete_record(int(selected_item[0]))
        clear()
        populate_list()

def update():
    global selected_item
    db.update_records(selected_item[0], name_entry.get() , price_entry.get() , price2_entry.get() , number_entry.get())
    
    populate_list()
    
    
def search():
    
    row = db.search_records(name_entry.get())
    price_entry.insert(0 ,row[2])
    price2_entry.insert(0 ,row[3])
    number_entry.insert(0 ,row[4])

def Exit():
    c = messagebox.askquestion('.!.!Warning!.!.' , 'آیا برای خروج مطمین هستید ؟')
    if c == 'yes':
        amir.destroy()


#Widget

#name_label
        
name_label = Label(amir , text = 'نام کالا : ' , font= 'arial 15' , bg ='#df8618' , fg='black')
name_label.place(x=45 , y=10)

#name_entry

name_entry = Entry(amir , width=20 )
name_entry.place(x=150 , y=15)

#price_label

price_label = Label(amir , text='قیمت خرید : ' , font='arial 15' , bg ='#df8618' , fg='black')
price_label.place(x=320, y=10)

#price_entry

price_entry = Entry(amir , width=20 ) 
price_entry.place(x=430 , y=15)

#price2_label

price2_label = Label(amir , text='قیمت فروش : ' , font='arial 15' , bg ='#df8618' , fg='black')
price2_label.place(x=12, y=60)

#price2_entry

price2_entry = Entry(amir , width=20 ) 
price2_entry.place(x=150 , y=65)

#number_label

number_label = Label(amir , text= 'تعداد : ' , font='arial 15' , bg ='#df8618' , fg='black')
number_label.place(x=330 , y=60)

#number_entry

number_entry = Entry(amir , width=20 ) 
number_entry.place(x=430 , y=65)

#Button

add_btn = ttk.Button(amir , width=20 , text='اضافه کردن' , command=save )
add_btn.place(x=320, y=150) 

search_btn = ttk.Button(amir , width=20 , text='جستجوی کالا' , command=search)
search_btn.place(x=384, y=190)

delete_btn = ttk.Button(amir , width=20 , text= 'حذف کالا' , command=remove)
delete_btn.place(x=320, y=230)

edit_btn = ttk.Button(amir , width=20 , text= 'ویرایش' , command=update)
edit_btn.place(x=385, y=270)

close_btn = ttk.Button(amir , width=20 , text= 'خروج' , command=Exit)
close_btn.place(x=320, y=310)

#ListBox

list_box = Listbox(amir , width=38 , height=14)
list_box.place(x=30 , y=130)


list_box.bind('<<ListboxSelect>>' , select_item)
amir.mainloop()