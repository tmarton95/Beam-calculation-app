from tkinter import*
from functions import create_force, create_moment, update_geometry, remove_obj, edit_loads, apply_loads

class Layout:
    def __init__(self, window, canvas_modelspace, modelspace_origin, loads_properties, scrollbar_properties, const_fixed, const_roller, beam_properties):
        self.Const1_pic = PhotoImage(file = "pics\\const1.png")
        self.Const2_pic = PhotoImage(file = "pics\\Const2_2.png")
        self.Beam1_pic = PhotoImage(file = "pics\\Beam1_2.png")
        self.Force1_pic = PhotoImage(file = "pics\\Force_1.png")
        self.Moment1_pic = PhotoImage(file = "pics\\Moment_1.png")
        self.cross_section_pic_1 = PhotoImage(file = "pics\\circle1.png")
        self.cross_section_pic_2 = PhotoImage(file = "pics\\rec1.png")
        """
        Define model spaces:
        """
        op_tabs_color = '#9bf280'

        WIDTH_tab_1 = 190
        HEIGHT_tab_1 = 60

        WIDTH_tab_2 = WIDTH_tab_1
        HEIGHT_tab_2 = HEIGHT_tab_1

        WIDTH_tab_3 = WIDTH_tab_1
        HEIGHT_tab_3 = HEIGHT_tab_1

        WIDTH_tab_4 = WIDTH_tab_1
        HEIGHT_tab_4 = 145

        WIDTH_tab_5 = 190
        HEIGHT_tab_5 = 140

        WIDTH_tab_6= WIDTH_tab_5
        HEIGHT_tab_6 = 130

        WIDTH_tab_7= WIDTH_tab_6
        HEIGHT_tab_7 = 145

        padx_img = 6
        padx_text = 60
        padx_entry = 130
        pady_tab4 = 35
        pady_tab1 = 0
        pady_tab5 = 0
        padx_tab5 = WIDTH_tab_1 + 7
        pady_tab5_text = 32
        pady_tab5_shift = -5

        canvas_tab_1 = Canvas(window, width = WIDTH_tab_1, height = HEIGHT_tab_1, bg = op_tabs_color, relief='ridge', borderwidth=1)
        canvas_tab_1.place(x = 0, y = pady_tab1)

        canvas_tab_2 = Canvas(window, width = WIDTH_tab_2, height = HEIGHT_tab_2, bg = op_tabs_color, relief='ridge', borderwidth=1)
        canvas_tab_2.place(x = 0, y = pady_tab1 + HEIGHT_tab_1)

        canvas_tab_3 = Canvas(window, width = WIDTH_tab_3, height = HEIGHT_tab_3, bg = op_tabs_color, relief='ridge', borderwidth=1)
        canvas_tab_3.place(x = 0, y = pady_tab1 + HEIGHT_tab_1 + HEIGHT_tab_2)

        canvas_tab_4 = Canvas(window, width = WIDTH_tab_4, height = HEIGHT_tab_4, bg = op_tabs_color, relief='ridge', borderwidth=1)
        canvas_tab_4.place(x = 0, y = pady_tab1 + HEIGHT_tab_1 + HEIGHT_tab_2 + HEIGHT_tab_3)

        canvas_tab_5 = Canvas(window, width = WIDTH_tab_5, height = HEIGHT_tab_5, bg = op_tabs_color, relief='ridge', borderwidth=1)
        canvas_tab_5.place(x = padx_tab5, y = pady_tab5)

        canvas_tab_6 = Canvas(window, width = WIDTH_tab_6, height = HEIGHT_tab_6, bg = op_tabs_color, relief='ridge', borderwidth=1)
        canvas_tab_6.place(x = padx_tab5, y = pady_tab5 + HEIGHT_tab_5)

        canvas_tab_7 = Canvas(window, width = WIDTH_tab_7, height = HEIGHT_tab_7, bg = op_tabs_color, relief='ridge', borderwidth=1)
        canvas_tab_7.place(x = 0, y = pady_tab1 + HEIGHT_tab_1 + HEIGHT_tab_2 + HEIGHT_tab_3 + HEIGHT_tab_4)


        """
        Constrain-1 properties: ON TAB 1
        """
        Label(canvas_tab_1, image = self.Const1_pic, relief='solid', borderwidth=0.5).place(x = padx_img, y = HEIGHT_tab_1 / 2, anchor = 'w')
        label_const1_x = Label(canvas_tab_1, text = "X  [m]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_const1_x.place(x = padx_text, y = HEIGHT_tab_1 / 2, anchor = 'w')

        self.txt_const1_x = Entry(canvas_tab_1, width = 8)
        self.txt_const1_x.place(x = padx_entry, y = HEIGHT_tab_1 / 2, anchor = 'w')
        self.txt_const1_x.insert(END, '0')

        """
        Constrain-2 properties: ON TAB 2
        """
        Label(canvas_tab_2, image = self.Const2_pic, relief='solid', borderwidth=0.5).place(x = padx_img, y = HEIGHT_tab_2 / 2, anchor = 'w')
        label_const2_x = Label(canvas_tab_2, text = "X  [m]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_const2_x.place(x = padx_text, y = HEIGHT_tab_2 / 2, anchor = 'w')

        self.txt_const2_x = Entry(canvas_tab_2, width = 8)
        self.txt_const2_x.place(x = padx_entry, y = HEIGHT_tab_2 / 2, anchor = 'w')
        self.txt_const2_x.insert(END, '1')

        """
        Beam properties:  ON TAB 3
        """
        Label(canvas_tab_3, image = self.Beam1_pic, relief='solid', borderwidth=0.5).place(x = padx_img, y = HEIGHT_tab_3 / 2, anchor = 'w')
        label_beam_x = Label(canvas_tab_3, text = "L  [m]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_beam_x.place(x = padx_text, y = HEIGHT_tab_3 / 2, anchor = 'w')

        self.txt_beam = Entry(canvas_tab_3, width = 8)
        self.txt_beam.place(x = padx_entry, y = HEIGHT_tab_3 / 2, anchor = 'w')
        self.txt_beam.insert(END, '1')

        """
        Cross-section properties: ON TAB 4
        """
        # Diameter: -----------------------
        Label(canvas_tab_4, image = self.cross_section_pic_1, relief='solid', borderwidth=0.5).place(x = padx_img, y = pady_tab4, anchor = 'w')
        label_d = Label(canvas_tab_4, text = "Ød [mm]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_d.place(x = padx_text, y = pady_tab4, anchor = 'w')

        self.txt_d = Entry(canvas_tab_4, width = 8)
        self.txt_d.place(x = padx_entry, y = pady_tab4, anchor = 'w')
        self.txt_d.insert(END, '0')

        # Rectangle: -----------------------
        Label(canvas_tab_4, image = self.cross_section_pic_2, relief='solid', borderwidth=0.5).place(x = padx_img, y = pady_tab4 + 65, anchor = 'w')

        label_a = Label(canvas_tab_4, text = "a [mm]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_a.place(x = padx_text, y = pady_tab4 + 50, anchor = 'w')

        self.txt_a = Entry(canvas_tab_4, width = 8)
        self.txt_a.place(x = padx_entry, y = pady_tab4 + 50, anchor = 'w')
        self.txt_a.insert(END, '0')

        label_b = Label(canvas_tab_4, text = "b [mm]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_b.place(x = padx_text, y = pady_tab4 + 85, anchor = 'w')

        self.txt_b = Entry(canvas_tab_4, width = 8)
        self.txt_b.place(x = padx_entry, y = pady_tab4 + 85, anchor = 'w')
        self.txt_b.insert(END, '0')

        """
        Force properties: ON TAB 5
        """
        # Icon:
        Label(canvas_tab_5, image = self.Force1_pic, relief='solid', borderwidth=0.5).place(x = padx_img, y= 30, anchor = 'w')

        # 'Add' button:
        btn_add_force = Button(canvas_tab_5, text = "+", height = 2, font = ('Arial', 16), 
                                command = lambda: create_force(self, loads_properties, modelspace_origin, canvas_modelspace, scrollbar_properties))
        btn_add_force.place(x = padx_img + 6, y = 95, anchor = 'w')

        # X-position:
        label_force_x_pos = Label(canvas_tab_5, text = "X  [m]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_force_x_pos.place(x = padx_text, y = pady_tab5_shift + pady_tab5_text, anchor = 'w')

        self.txt_force_x_pos = Entry(canvas_tab_5, width = 8)
        self.txt_force_x_pos.place(x = padx_entry, y = pady_tab5_shift + pady_tab5_text, anchor = 'w')
        self.txt_force_x_pos.insert(END, '0.0')

        # Y-position:
        label_force_y_pos = Label(canvas_tab_5, text = "Y  [m]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_force_y_pos.place(x = padx_text, y = pady_tab5_shift+ pady_tab5_text * 2, anchor = 'w')

        self.txt_force_y_pos = Entry(canvas_tab_5, width = 8)
        self.txt_force_y_pos.place(x = padx_entry, y = pady_tab5_shift + pady_tab5_text * 2, anchor = 'w')
        self.txt_force_y_pos.insert(END, '0.0')

        # X-component:
        label_force_x = Label(canvas_tab_5, text = "Fx [N]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_force_x.place(x = padx_text, y = pady_tab5_shift + pady_tab5_text * 3, anchor = 'w')

        self.txt_force_x = Entry(canvas_tab_5, width = 8)
        self.txt_force_x.place(x = padx_entry, y = pady_tab5_shift + pady_tab5_text * 3, anchor = 'w')
        self.txt_force_x.insert(END, '0.0')

        # Y-component:
        label_force_y = Label(canvas_tab_5, text = "Fy [N]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_force_y.place(x = padx_text, y = pady_tab5_shift + pady_tab5_text * 4, anchor = 'w')

        self.txt_force_y = Entry(canvas_tab_5, width = 8)
        self.txt_force_y.place(x = padx_entry, y = pady_tab5_shift + pady_tab5_text * 4, anchor = 'w')
        self.txt_force_y.insert(END, '0.0')

        """
        Moment properties:  ON TAB 6
        """
        # Icon:
        Label(canvas_tab_6, image = self.Moment1_pic, relief='solid', borderwidth=0.5).place(x = padx_img, y= 30, anchor = 'w')

        # 'Add' button:
        btn_add_moment = Button(canvas_tab_6, text = "+", height = 2, font = ('Arial', 16),
        command = lambda: create_moment(self, loads_properties, modelspace_origin, canvas_modelspace, scrollbar_properties))
        btn_add_moment.place(x = padx_img + 6, y = 95, anchor = 'w')

        # X-position:
        label_moment_x_pos = Label(canvas_tab_6, text = "X [m]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_moment_x_pos.place(x = padx_text, y = pady_tab5_shift + pady_tab5_text, anchor = 'w')

        self.txt_moment_x_pos = Entry(canvas_tab_6, width = 8)
        self.txt_moment_x_pos.place(x = padx_entry, y = pady_tab5_shift + pady_tab5_text, anchor = 'w')
        self.txt_moment_x_pos.insert(END, '0')

        # Y-component:
        label_moment_y = Label(canvas_tab_6, text = "My [Nm]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_moment_y.place(x = padx_text, y = pady_tab5_shift + pady_tab5_text * 2, anchor = 'w')

        self.txt_moment_y = Entry(canvas_tab_6, width = 8)
        self.txt_moment_y.place(x = padx_entry, y = pady_tab5_shift + pady_tab5_text * 2, anchor = 'w')
        self.txt_moment_y.insert(END, '0')

        # Z-component:
        label_moment_z = Label(canvas_tab_6, text = "Mz [Nm]:", font = ('Verdana', 9), bg = op_tabs_color)
        label_moment_z.place(x = padx_text, y = pady_tab5_shift + pady_tab5_text * 3, anchor = 'w')

        self.txt_moment_z = Entry(canvas_tab_6, width = 8)
        self.txt_moment_z.place(x = padx_entry, y = pady_tab5_shift + pady_tab5_text * 3, anchor = 'w')
        self.txt_moment_z.insert(END, '0')

        """
        Other operating buttons + labels:
        """
        label_selections = Label(window, text = "Load selections:", font = ('Verdana', 9, 'italic'), borderwidth = 0.75,
                                    relief = 'ridge', bg = 'white', width = 27, height = 1)
        label_selections.place(x = WIDTH_tab_1 + 8, y = HEIGHT_tab_5 + HEIGHT_tab_6 + 16, anchor = 'w')

        label_load_modification = Label(canvas_tab_7, text = "Load modifications:", font = ('Verdana', 9, 'italic'), borderwidth = 0.75,
                                    relief = 'ridge', bg = 'white', width = 26, height = 1)
        label_load_modification.place(x = 5, y = 70, anchor = 'w')

        # Update geometry:
        btn_update_geometry = Button(canvas_tab_7, text = "Update Geometry", width = 20, height = 1, font = ('Arial', 11), background='orange', 
                            command = lambda: update_geometry(beam_properties, canvas_modelspace, const_fixed, const_roller, layout_properties = self))
        btn_update_geometry.place(x = 3, y = 18, anchor = 'w')

        # Edit loads:
        btn_edit_loads = Button(canvas_tab_7, text = "Edit", height = 1, width = 8, font = ('Arial', 10), background = 'grey', 
                            command= lambda: edit_loads(loads_properties, scrollbar_properties, layout_properties = self))
        btn_edit_loads.place(x = 45, y = 95, anchor = 'center')

        # Apply loads:
        btn_apply = Button(canvas_tab_7, text = "Apply", height = 1, width = 8, font = ('Arial', 10,), background = 'grey', 
                            command= lambda: apply_loads(canvas_modelspace, loads_properties, scrollbar_properties, layout_properties = self))
        btn_apply.place(x = WIDTH_tab_7 - 45, y = 95, anchor = 'center')

        # Remove
        btn_remove = Button(canvas_tab_7, text = "Remove", height = 1, width = 8, font = ('Arial', 10), background = 'grey', 
                            command= lambda: remove_obj(canvas_modelspace, loads_properties, scrollbar_properties, layout_properties = self))
        btn_remove.place(x = WIDTH_tab_7 / 2, y = 130, anchor = 'center')

        self.txt_load_name = Entry(window, width = 21, font = (10), relief='solid', borderwidth=0.5)
        self.txt_load_name.place(x = WIDTH_tab_1 + 8, y = HEIGHT_tab_5 + HEIGHT_tab_6 + 195, anchor = 'w')
        self.txt_load_name.insert(END, 'Load-name...')
        self.txt_load_name.config(state = 'disabled')

        scrollbar_properties.draw_scroll_bar(window, HEIGHT_tab_5, HEIGHT_tab_6, WIDTH_tab_1)

