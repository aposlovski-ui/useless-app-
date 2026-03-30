from tkinter import *
import storage
import graphs
from graphs import Graph

#shows elements on the first screen
def data_on_screen():
    storage.get_data()
    c = list()
    b = list()
    for x in storage.on_file:
        for y in x:
            c.append(y)
    b = c[::4]
    for food in b:
        listbox.insert(END, food)

# submits an entry
def submit():
    entryname = entry.get().lower()
    storage.on_screen = entryname
    listbox.insert(END, entryname)
    entry.delete(0, END)
    entry.insert(END, 'продукт')
    storage.add_new_food()

# deletes the whole entry from the list and the foods.csv
def delete():
    if listbox.curselection():
        a = listbox.get(listbox.curselection())
        storage.on_screen = a
        listbox.delete(listbox.curselection())
        storage.remove_from_file()

# just closes the edit window
def close_window(new_window):
    a = list()
    new_window.destroy()
    # enables buttons
    submit_button.configure(state=ACTIVE)
    delete_button.configure(state=ACTIVE)
    edit_button.configure(state=ACTIVE)

    for i in range(3):
        a.append(Graph('aaa'))
    print(a)

# creates the edit window
def edit():
    if listbox.curselection():
        #gets selection and refreshes the list with foods info
        storage.on_screen = listbox.get(listbox.curselection())
        storage.get_data()

        new_window = Toplevel()
        new_window.geometry('500x500')
        new_window.configure(background='light yellow')
        new_window.protocol('WM_DELETE_WINDOW', lambda: close_window(new_window))
        label_t1 = Label(new_window, text=storage.new_data[0], background='light yellow')
        label_t2 = Label(new_window, text=storage.new_data[1], background='light yellow')
        label_t3 = Label(new_window, text=storage.new_data[2], background='light yellow')
        label_t4 = Label(new_window, text=storage.new_data[3], background='light yellow')
        entry_t1 = Entry(new_window, font='Arial 30')
        entry_t2 = Entry(new_window, font='Arial 30')
        entry_t3 = Entry(new_window, font='Arial 30')
        entry_t4 = Entry(new_window, font='Arial 30')
        
        #finds the foods entry and passes to enter_button()
        a = int()
        b = list
        for x in storage.on_file:
            for y in x:
                if y == storage.on_screen:
                    a = storage.on_file.index(x)
                    b = storage.on_file[a]
                    break
        # creates the enter_button
        new_button = Button(new_window, text='внести правки', command=lambda: enter_button(a, b, new_window,
                                                                                           entry_t1,
                                                                                           entry_t2,
                                                                                           entry_t3,
                                                                                           entry_t4))

        entry_t1.pack()
        entry_t2.pack()
        entry_t3.pack()
        entry_t4.pack()
        label_t1.pack()
        label_t2.pack()
        label_t3.pack()
        label_t4.pack()
        new_button.pack()
        entry_t1.place(relx=0.6, rely=0.2, anchor=CENTER)
        entry_t1.insert(0, b[0])
        entry_t2.place(relx=0.6, rely=0.4, anchor=CENTER)
        entry_t2.insert(0, b[1])
        entry_t3.place(relx=0.6, rely=0.6, anchor=CENTER)
        entry_t3.insert(0, b[2])
        entry_t4.place(relx=0.6, rely=0.8, anchor=CENTER)
        entry_t4.insert(0, b[3])
        label_t1.place(relx=0.1, rely=0.2, anchor=CENTER)
        label_t2.place(relx=0.1, rely=0.4, anchor=CENTER)
        label_t3.place(relx=0.1, rely=0.6, anchor=CENTER)
        label_t4.place(relx=0.1, rely=0.8, anchor=CENTER)
        new_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        #disables buttons
        submit_button.configure(state=DISABLED)
        delete_button.configure(state=DISABLED)
        edit_button.configure(state=DISABLED)


def enter_button(a, b, new_window, entry_t1, entry_t2, entry_t3, entry_t4):
    b[0] = entry_t1.get().lower()
    b[1] = entry_t2.get().lower()
    b[2] = entry_t3.get().lower()
    b[3] = entry_t4.get().lower()
    storage.on_file[a] = b
    storage.write_to_file()
    new_window.destroy()
    #enables buttons
    submit_button.configure(state=ACTIVE)
    delete_button.configure(state=ACTIVE)
    edit_button.configure(state=ACTIVE)


window = Tk()
window.title('Прикорм')
window.geometry('500x500')
window.configure(bg='light blue')


listbox = Listbox(window, bg='light yellow')#.pack(expand=1, fill='both')
listbox.pack(expand=1, fill='both')

#gets data on screen
data_on_screen()


entry = Entry(window, font='Arial 30') #show='*' for passwords
entry.insert(0,'продукт')
entry.pack()
#entry.update()


submit_button = Button(window, text='добавить',state=ACTIVE, command=submit,
                activebackground='yellow', activeforeground='green',
                fg='black', bg='white', compound='right')
submit_button.pack()
delete_button = Button(window, text='удалить',state=ACTIVE, command=delete,
                activebackground='yellow', activeforeground='green',
                fg='black', bg='white', compound='right')
delete_button.pack()
edit_button = Button(window, text='править',state=ACTIVE, command=edit,
                activebackground='yellow', activeforeground='green',
                fg='black', bg='white', compound='right')
edit_button.pack()



window.mainloop()




if __name__ == '__main__':
    pass


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
