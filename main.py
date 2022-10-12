from tkinter import*
from beam_class import Beam
from load_classes import Loads
from layout_main_class import Layout
from layout_scrollbar import LayoutScrollbar
from constrain_classes import ConstrainFix, ConstrainRolling

window = Tk()
window.title("Beam tool")
window.geometry('1200x600')
window.config(bg = '#9bf280')

"""
Initial properties:
"""
WIDTH_modelspace = 700
HEIGHT_modelspace = 600
X_modelspace = 500
Y_modelspace = 0
modelspace_origin = [100, 250]

canvas_modelspace = Canvas(window, width = WIDTH_modelspace, height = HEIGHT_modelspace, bg = "lightblue", relief='ridge', borderwidth=1)
canvas_modelspace.place(x = X_modelspace, y = Y_modelspace)

"""
Define initial instances from classes + draw figures:
"""
loads_properties = Loads()

scrollbar_properties = LayoutScrollbar(window)

const_fixed = ConstrainFix(modelspace_origin)
const_fixed.draw_const(canvas_modelspace)

const_roller = ConstrainRolling(modelspace_origin)
const_roller.draw_const(canvas_modelspace)

beam_properties = Beam(modelspace_origin)
beam_properties.draw_beam(canvas_modelspace)

layout_properties = Layout(window, canvas_modelspace, modelspace_origin, loads_properties, scrollbar_properties, const_fixed, const_roller, beam_properties)

window.mainloop()