from tkinter import*
from tkinter import ttk
from beam_class import Beam
from load_classes import Loads
from layout_main_class import Layout
from layout_scrollbar import LayoutScrollbar
from constrain_classes import ConstrainFix, ConstrainRolling
from functions import calc_reactions

window = Tk()
window.title("Beam tool")
window.geometry('1098x478')

""" Initial properties: """
# Size of 'modelspace' canvas:
WIDTH_modelspace = 700
HEIGHT_modelspace = 472
# Position of 'modelspace' canvas:
X_modelspace = 392
Y_modelspace = 0
modelspace_origin = [100, 220]

canvas_modelspace = Canvas(window, width = WIDTH_modelspace, height = HEIGHT_modelspace)
canvas_modelspace.place(x = X_modelspace, y = Y_modelspace)

tabControl = ttk.Notebook(canvas_modelspace, width = WIDTH_modelspace, height = HEIGHT_modelspace - 20)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Analysis Model')
tabControl.add(tab2, text ='Results - Load charts')
tabControl.add(tab3, text ='Results - Stress charts')
tabControl.pack(fill = "both", expand = 1)

tab1_canvas = Canvas(tab1, bg = "lightblue", relief='ridge', borderwidth=1)
tab1_canvas.pack(expand = 1, fill ="both")

tab2_canvas = Canvas(tab2, bg = "#eddb90", relief='ridge', borderwidth=1)
tab2_canvas.pack(expand = 1, fill ="both")

"""
Define initial instances from classes + draw figures:
"""
loads_properties = Loads()

scrollbar_properties = LayoutScrollbar()

const_fixed = ConstrainFix(modelspace_origin)
const_fixed.draw_const(tab1_canvas)

const_roller = ConstrainRolling(modelspace_origin)
const_roller.draw_const(tab1_canvas)

beam_properties = Beam(modelspace_origin)
beam_properties.draw_beam(tab1_canvas)

layout_properties = Layout(window, tab1_canvas, tab2_canvas, modelspace_origin, loads_properties, scrollbar_properties, const_fixed, const_roller, beam_properties)

btn_calc = Button(tab2_canvas, text = "Calculate!", command = lambda: calc_reactions(const_fixed, const_roller, beam_properties, loads_properties, tab2_canvas))
btn_calc.place(x=10, y=10)

window.mainloop()