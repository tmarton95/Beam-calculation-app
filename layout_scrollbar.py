from tkinter import*
"""
Force + Moment's list:
"""
class LayoutScrollbar():
    def __init__(self, window):
        frame = Frame(window)
        frame.place(x = 265, y = 420, anchor ='w')

        list_box = Listbox(frame, font = ('Arial', 10), width = 15, height = 8)
        list_box.pack(expand=True, fill=BOTH, side=LEFT)

        scroll_bar = Scrollbar(frame, orient=VERTICAL)
        scroll_bar.pack(fill=Y, side=RIGHT)

        list_box.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=list_box.yview)
        
        self.mylist = list_box
        self.last_selected_load = ""

