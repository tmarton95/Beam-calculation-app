from tkinter import*
from beam_class import Beam
from force_moment_classes import Force
from constrain_classes import ConstrainFix, ConstrainRolling
import layout

window = Tk()
window.title("Beam tool")
window.geometry('1200x600')

"""
Initial properties:
"""
WIDTH_modelspace = 700
HEIGHT_modelspace = 600
X_modelspace = 500
Y_modelspace = 0

canvas_modelspace = Canvas(window, width = WIDTH_modelspace, height = HEIGHT_modelspace, bg = "lightblue")
canvas_modelspace.place(x = X_modelspace, y = Y_modelspace)

modelspace_origin = [100, 250]

forces_dict = {}
moments_dict = {}

"""
Create force object:
"""
force_id = 1
def create_force():
    global force_id
    Fx = float(LayoutProperties.txt_fx.get())
    Fy = float(LayoutProperties.txt_fy.get())
    if Fx != 0 or Fy != 0:
        force_name = f"force_{force_id}"
        forces_dict[force_name] = forces_dict.get(force_name, Force(modelspace_origin, name = force_name))
        forces_dict[force_name].x_real = float(LayoutProperties.txt_force_x.get())
        forces_dict[force_name].Fx = Fx
        forces_dict[force_name].Fy = Fy
        forces_dict[force_name].draw_force(canvas_modelspace)
        LayoutProperties.mylist.insert(END, force_name)
        force_id += 1

"""
Remove forces from list:
"""
def remove_obj():
    selected_name = LayoutProperties.mylist.get(LayoutProperties.mylist.curselection())
    canvas_modelspace.delete(selected_name)
    del forces_dict[selected_name]
    LayoutProperties.mylist.delete(ACTIVE)

"""
Updating properties:
"""
def get_properties():
    const_fixed.x_real = float(LayoutProperties.txt_const1_x.get())
    canvas_modelspace.delete('constfix_1'); canvas_modelspace.delete('constfix_2'); canvas_modelspace.delete('constfix_3')
    const_fixed.draw_const(canvas_modelspace)

    const_roller.x_real = float(LayoutProperties.txt_const2_x.get())
    canvas_modelspace.delete('constroll_1'); canvas_modelspace.delete('constroll_2')
    canvas_modelspace.delete('constroll_3'); canvas_modelspace.delete('constroll_4')
    const_roller.draw_const(canvas_modelspace)

    beam_length = float(LayoutProperties.txt_beam.get())
    if beam_length != 0:
        beam1.length_real = beam_length
        canvas_modelspace.delete('beam')
        beam1.draw_beam(canvas_modelspace)
    
    beam1.d = float(LayoutProperties.txt_d.get())
    beam1.a = float(LayoutProperties.txt_a.get())
    beam1.b = float(LayoutProperties.txt_b.get())

"""
Define initial instances from classes:
"""
LayoutProperties = layout.Layout(window, create_force, remove_obj)

beam1 = Beam(modelspace_origin); beam1.draw_beam(canvas_modelspace)

const_fixed = ConstrainFix(modelspace_origin); const_fixed.draw_const(canvas_modelspace)

const_roller = ConstrainRolling(modelspace_origin); const_roller.draw_const(canvas_modelspace)



# 'Update' button:
btn_add_moment = Button(window, text = "Update", width = 11, height = 1, font = ('Arial', 14), background='orange', command = get_properties)
btn_add_moment.place(x = 100, y = 450, anchor = 'center')

window.mainloop()