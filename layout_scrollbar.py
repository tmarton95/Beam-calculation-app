from tkinter import*

"""
Force + Moment's list:
"""

class LayoutScrollbar:
    def __init__(self):
        self.last_selected_load = ""

    def draw_scroll_bar(self, window, HEIGHT_tab_5, HEIGHT_tab_6, WIDTH_tab_1):
        frame = Frame(window)
        frame.place(x = WIDTH_tab_1 + 6, y = HEIGHT_tab_5 + HEIGHT_tab_6 + 103, anchor ='w')

        list_box = Listbox(frame, font = ('Arial', 10), width = 25, height = 9, relief='ridge', borderwidth=0.5)
        list_box.pack(expand=True, fill=BOTH, side=LEFT)

        scroll_bar = Scrollbar(frame, orient=VERTICAL)
        scroll_bar.pack(fill=Y, side=RIGHT)

        list_box.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=list_box.yview)
        
        self.mylist = list_box


