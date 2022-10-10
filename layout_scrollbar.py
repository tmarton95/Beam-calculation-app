from tkinter import*
"""
Force + Moment's list:
"""
class LayoutScrollbar():
    def __init__(self, window):
        # FrameBIG = Frame(window)
        # Main = Canvas(FrameBIG, background="blue", height = 100,width =25)
        # Main.configure(scrollregion=Main.bbox("all"))

        # scroll = Scrollbar(FrameBIG ,orient="vertical", command=Main.yview)
        # Main.configure(yscrollcommand=scroll.set)

        # #scroll.pack(side="right", fill="y")
        # #Main.pack(side = BOTTOM, anchor = NW,fill="x")
        # Main.place(x = 260, y = 410, anchor='w')
        # FrameBIG.pack(anchor = W, fill = "x")
        # #FrameBIG.place(x = 260, y = 410, anchor='w')
        # #FrameBIG.pack()
        # #Main.configure(scrollregion=Main.bbox("all"))

        # Scrollbar: ===========================================================
        scroll_frame = Canvas(window, height = 100, width = 20,  background = "blue")
        scroll_frame.place(x = 400, y = 410, anchor ='w')

        objects_scroll = Scrollbar(scroll_frame)
        #objects_scroll.place(x = 0, y = 50, anchor='w')
        objects_scroll.pack()

        self.mylist = Listbox(window, width = 22, height = 8,  yscrollcommand = objects_scroll.set)
        self.mylist.place(x = 260, y = 410, anchor='w')
        self.last_selected_load = ""
        #objects_scroll.config(command = mylist.yview)
        #objects_scroll.set(50, 25)
