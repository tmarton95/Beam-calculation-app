from tkinter import*
from load_classes import Force

"""
Create force object:
"""
def create_force(layout_properties, loads_properties, modelspace_origin, canvas_modelspace, scrollbar_properties):
    # Get forces from text field:
    Fx = float(layout_properties.txt_force_x.get())
    Fy = float(layout_properties.txt_force_y.get())
    if Fx != 0 or Fy != 0:
        loads_properties.force_id += 1
        force_name = f"Force_{loads_properties.force_id}"

        # Create instance for new force object + add to the dictionary:
        loads_properties.forces_dict[force_name] = loads_properties.forces_dict.get(force_name, Force(modelspace_origin, name = force_name))

        # Set up attributes for the force object:
        loads_properties.forces_dict[force_name].x_real = float(layout_properties.txt_force_x_pos.get())
        loads_properties.forces_dict[force_name].y_real = float(layout_properties.txt_force_y_pos.get())
        loads_properties.forces_dict[force_name].Fx = Fx
        loads_properties.forces_dict[force_name].Fy = Fy
        loads_properties.forces_dict[force_name].draw_force(canvas_modelspace)
        scrollbar_properties.mylist.insert(END, force_name)

"""
Remove forces from list:
"""
def remove_obj(loads_properties, scrollbar_properties, canvas_modelspace):
    selected_name = scrollbar_properties.mylist.get(scrollbar_properties.mylist.curselection())
    canvas_modelspace.delete(selected_name)
    del loads_properties.forces_dict[selected_name]
    scrollbar_properties.mylist.delete(ACTIVE)

"""
Updating properties:
"""
def edit_geometry(layout_properties, canvas_modelspace, const_fixed, const_roller, beam_properties):
    # Get x-distance of constrain from text:
    const_fixed.x_real = float(layout_properties.txt_const1_x.get())
    const_roller.x_real = float(layout_properties.txt_const2_x.get())

    # Delete figure of previous constrain:
    canvas_modelspace.delete('constfix_1', 'constfix_2', 'constfix_3')
    canvas_modelspace.delete('constroll_1', 'constroll_2', 'constroll_3', 'constroll_4')

    # Draw new figure:
    const_fixed.draw_const(canvas_modelspace)
    const_roller.draw_const(canvas_modelspace)

    # Update beam properties + draw it:
    beam_length = float(layout_properties.txt_beam.get())
    if beam_length != 0:
        beam_properties.length_real = beam_length
        canvas_modelspace.delete('beam')
        beam_properties.draw_beam(canvas_modelspace)
    
    beam_properties.d = float(layout_properties.txt_d.get())
    beam_properties.a = float(layout_properties.txt_a.get())
    beam_properties.b = float(layout_properties.txt_b.get())

"""
Edit loads:
"""
def edit_loads(scrollbar_properties, loads_properties, layout_properties):
    try:
        selected_name = scrollbar_properties.mylist.get(scrollbar_properties.mylist.curselection())
        scrollbar_properties.last_selected_load = selected_name

        # Write out selected force's forces + position:
        layout_properties.txt_force_x_pos.delete (0, 10)
        layout_properties.txt_force_y_pos.delete (0, 10)
        layout_properties.txt_force_x.delete (0, 10)
        layout_properties.txt_force_y.delete (0, 10)

        # Insert load values to the entry boxes:
        layout_properties.txt_force_x_pos.insert(END, loads_properties.forces_dict[selected_name].x_real)
        layout_properties.txt_force_y_pos.insert(END, loads_properties.forces_dict[selected_name].y_real)
        layout_properties.txt_force_x.insert(END, loads_properties.forces_dict[selected_name].Fx)
        layout_properties.txt_force_y.insert(END, loads_properties.forces_dict[selected_name].Fy)
    except:
        pass


"""
Apply loads:
"""
def apply_loads(scrollbar_properties, loads_properties, canvas_modelspace, layout_properties):
    selected_name = scrollbar_properties.last_selected_load

    # Get force data from text:
    loads_properties.forces_dict[selected_name].Fx = float(layout_properties.txt_force_x.get())
    loads_properties.forces_dict[selected_name].Fy = float(layout_properties.txt_force_y.get())
    loads_properties.forces_dict[selected_name].x_real = float(layout_properties.txt_force_x_pos.get())
    loads_properties.forces_dict[selected_name].y_real = float(layout_properties.txt_force_y_pos.get())

    # Update position of load / load's figure:
    canvas_modelspace.delete(selected_name)
    loads_properties.forces_dict[selected_name].draw_force(canvas_modelspace)
    