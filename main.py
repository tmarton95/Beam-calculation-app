from tkinter import*
from beam_class import Beam
from load_classes import Loads
from layout_main_class import Layout
from constrain_classes import ConstrainFix, ConstrainRolling
from functions import create_force, remove_obj, get_properties


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

"""
Define initial instances from classes:
"""
loads_properties = Loads()

layout_properties = Layout(window, create_force, loads_properties, modelspace_origin, canvas_modelspace)

beam_properties = Beam(modelspace_origin)
beam_properties.draw_beam(canvas_modelspace)

const_fixed = ConstrainFix(modelspace_origin)
const_fixed.draw_const(canvas_modelspace)

const_roller = ConstrainRolling(modelspace_origin)
const_roller.draw_const(canvas_modelspace)


# 'Update' button:
btn_add_moment = Button(window, text = "Update", width = 11, height = 1, font = ('Arial', 14), background='orange', 
                        command = lambda: get_properties(layout_properties, canvas_modelspace, const_fixed, const_roller, beam_properties))
btn_add_moment.place(x = 100, y = 450, anchor = 'center')

window.mainloop()