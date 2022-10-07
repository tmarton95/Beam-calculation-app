from tkinter import*

from functions import edit_loads

class Layout():
    def __init__(self, window, create_force, remove_obj, loads_properties, modelspace_origin, canvas_modelspace, scrollbar_properties, edit_loads):
        self.Const1_pic = PhotoImage(file = "pics\\const1.png").subsample(5, 5)
        self.Const2_pic = PhotoImage(file = "pics\\Const2_2.png").subsample(5, 5)
        self.Beam1_pic = PhotoImage(file = "pics\\Beam1_2.png").subsample(5, 5)
        self.Force1_pic = PhotoImage(file = "pics\\Force_1.png").subsample(5, 5)
        self.Moment1_pic = PhotoImage(file = "pics\\Moment_1.png").subsample(5, 5)
        """
        For constrain-1 properties:
        """
        Label(window, image = self.Const1_pic).place(x = 30, y= 35, anchor = 'center')
        label_const1_x = Label(window, text = "X  [m]:", font = ('Verdana', 9), borderwidth = 0.75,
                                                    relief = 'ridge', bg = 'white', width = 10, height = 1)
        label_const1_x.place(x = 70, y = 35, anchor = 'w')

        self.txt_const1_x = Entry(window, width = 8)
        self.txt_const1_x.place(x = 170, y = 35, anchor = 'w')
        self.txt_const1_x.insert(END, '0')

        """
        For constrain-2 properties:
        """
        Label(window, image = self.Const2_pic).place(x = 30, y= 120, anchor = 'center')
        label_const2_x = Label(window, text = "X  [m]:", font = ('Verdana', 9), borderwidth = 0.75,
                                                    relief = 'ridge', bg = 'white', width = 10, height = 1)
        label_const2_x.place(x = 70, y = 120, anchor = 'w')

        self.txt_const2_x = Entry(window, width = 8)
        self.txt_const2_x.place(x = 170, y = 120, anchor = 'w')
        self.txt_const2_x.insert(END, '1')

        """
        For Beam properties:
        """
        Label(window, image = self.Beam1_pic).place(x = 30, y= 205, anchor = 'center')
        label_beam_x = Label(window, text = "Length [m]:", font = ('Verdana', 9), borderwidth = 0.75,
                                                    relief = 'ridge', bg = 'white', width = 10, height = 1)
        label_beam_x.place(x = 70, y = 205, anchor = 'w')

        self.txt_beam = Entry(window, width = 8)
        self.txt_beam.place(x = 170, y = 205, anchor = 'w')
        self.txt_beam.insert(END, '1')

        """
        For cross-section properties:
        """
        label_cross = Label(window, text = "Cross-section", font = ('Verdana', 10), borderwidth = 1,
                                                    relief = 'ridge', bg = 'white', width = 25, height = 1)
        label_cross.place(x = 30, y = 250, anchor = 'w')

        label_d = Label(window, text = "Ød [mm]:", font = ('Verdana', 9), borderwidth = 0.75,
                                                    relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_d.place(x = 25, y = 300, anchor = 'w')

        self.txt_d = Entry(window, width = 9)
        self.txt_d.place(x = 110, y = 300, anchor = 'w')
        self.txt_d.insert(END, '0')

        label_a = Label(window, text = "a [mm]:", font = ('Verdana', 9), borderwidth = 0.75,
                                                    relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_a.place(x = 25, y = 340, anchor = 'w')

        self.txt_a = Entry(window, width = 9)
        self.txt_a.place(x = 110, y = 340, anchor = 'w')
        self.txt_a.insert(END, '0')

        label_b = Label(window, text = "b [mm]:", font = ('Verdana', 9), borderwidth = 0.75,
                                                    relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_b.place(x = 25, y = 380, anchor = 'w')

        self.txt_b = Entry(window, width = 9)
        self.txt_b.place(x = 110, y = 380, anchor = 'w')
        self.txt_b.insert(END, '0')

        """
        For Force properties:
        """
        # Icon:
        Label(window, image = self.Force1_pic).place(x = 280, y= 35, anchor = 'center')

        # 'Add' button:
        btn_add_force = Button(window, text = "+", height = 2, font = ('Arial', 16), 
                                command = lambda: create_force(self, loads_properties, modelspace_origin, canvas_modelspace, scrollbar_properties))
        btn_add_force.place(x = 280, y = 110, anchor = 'center')

        # X-position:
        label_force_x = Label(window, text = "X [m]:", font = ('Verdana', 9), borderwidth = 0.75,
                                                    relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_force_x.place(x = 320, y = 35, anchor = 'w')

        self.txt_force_x = Entry(window, width = 9)
        self.txt_force_x.place(x = 400, y = 35, anchor = 'w')
        self.txt_force_x.insert(END, '0')

        # Y-position:
        label_force_y = Label(window, text = "Y [m]:", font = ('Verdana', 9), borderwidth = 0.75,
                                            relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_force_y.place(x = 320, y = 70, anchor = 'w')

        self.txt_force_y = Entry(window, width = 9)
        self.txt_force_y.place(x = 400, y = 70, anchor = 'w')
        self.txt_force_y.insert(END, '0')

        # X-component:
        label_fx = Label(window, text = "Fx [N]:", font = ('Verdana', 9), borderwidth = 0.75,
                                    relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_fx.place(x = 320, y = 105, anchor = 'w')

        self.txt_fx = Entry(window, width = 9)
        self.txt_fx.place(x = 400, y = 105, anchor = 'w')
        self.txt_fx.insert(END, '0')

        # Y-component:
        label_fy = Label(window, text = "Fy [N]:", font = ('Verdana', 9), borderwidth = 0.75,
                                    relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_fy.place(x = 320, y = 140, anchor = 'w')

        self.txt_fy = Entry(window, width = 9)
        self.txt_fy.place(x = 400, y = 140, anchor = 'w')
        self.txt_fy.insert(END, '0')

        """
        For Moment properties:
        """
        # Icon:
        Label(window, image = self.Moment1_pic).place(x = 280, y= 200, anchor = 'center')

        # 'Add' button:
        btn_add_moment = Button(window, text = "+", height = 2, font = ('Arial', 16))
        btn_add_moment.place(x = 280, y = 270, anchor = 'center')

        # X-position:
        label_moment_x = Label(window, text = "X [m]:", font = ('Verdana', 9), borderwidth = 0.75,
                                                    relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_moment_x.place(x = 320, y = 210, anchor = 'w')

        self.txt_moment_x = Entry(window, width = 9)
        self.txt_moment_x.place(x = 400, y = 210, anchor = 'w')
        self.txt_moment_x.insert(END, '0')

        # Y-component:
        label_my = Label(window, text = "My [Nm]:", font = ('Verdana', 9), borderwidth = 0.75,
                                            relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_my.place(x = 320, y = 245, anchor = 'w')

        self.txt_my = Entry(window, width = 9)
        self.txt_my.place(x = 400, y = 245, anchor = 'w')
        self.txt_my.insert(END, '0')

        # Z-component:
        label_mz = Label(window, text = "Mz [Nm]:", font = ('Verdana', 9), borderwidth = 0.75,
                                    relief = 'ridge', bg = 'white', width = 8, height = 1)
        label_mz.place(x = 320, y = 280, anchor = 'w')

        self.txt_mz = Entry(window, width = 9)
        self.txt_mz.place(x = 400, y = 280, anchor = 'w')
        self.txt_mz.insert(END, '0')


        # Remove + Edit button from load-list:
        btn_remove = Button(window, text = "Remove", height = 1, width = 8, font = ('Arial', 10), 
                                background = 'grey', command= lambda: remove_obj(loads_properties, scrollbar_properties, canvas_modelspace))
        btn_remove.place(x = 460, y = 415, anchor = 'center')

        btn_edit = Button(window, text = "Edit", height = 1, width = 8, font = ('Arial', 10), 
                                background = 'grey', command= lambda: edit_loads(scrollbar_properties, loads_properties, canvas_modelspace, layout_properties = self))
        btn_edit.place(x = 460, y = 360, anchor = 'center')