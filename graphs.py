from tkinter import *

class Graph:
    data_to_process = list()
    def __init__(self, name):
        self.name = name
        self.open_graph()
    #def __repr__(self):
    #    return self.name
    #def __del__(self):
    #    print("Deleting graph")
    def open_graph(self):
        #print(self)
        new_window = Toplevel()
        new_window.title(self.name)
        new_window.geometry('500x500')
        new_window.configure(bg='light blue')
        new_window.protocol('WM_DELETE_WINDOW', lambda: self.close_graph(new_window))
        label = Label(new_window, text="one day here will be a fancy table", background='light yellow', font=('Arial', 30, 'bold'))
        label.pack()
        #self.fancy_graphs.append(self.name)
        #print(self.fancy_graphs)
    def close_graph(self, new_window):
        new_window.destroy()
        del self
        #print(self)

