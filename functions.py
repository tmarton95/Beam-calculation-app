from tkinter import*
from load_classes import Force, Moment

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
Create moment object:
""" 
def create_moment(layout_properties, loads_properties, modelspace_origin, canvas_modelspace, scrollbar_properties):
    # Get forces from text field:
    My = float(layout_properties.txt_moment_y.get())
    Mz = float(layout_properties.txt_moment_z.get())
    if My != 0 or Mz != 0:
        loads_properties.moment_id += 1
        moment_name = f"Moment_{loads_properties.moment_id}"

        loads_properties.moments_dict[moment_name] = loads_properties.moments_dict.get(moment_name, Moment(modelspace_origin, name = moment_name))

        # Set up attributes for the force object:
        loads_properties.moments_dict[moment_name].x2_real = float(layout_properties.txt_moment_x_pos.get())
        loads_properties.moments_dict[moment_name].My = My
        loads_properties.moments_dict[moment_name].Mz = Mz
        loads_properties.moments_dict[moment_name].draw_moment(canvas_modelspace)
        scrollbar_properties.mylist.insert(END, moment_name)

"""
Updating properties:
"""
def update_geometry(beam_properties, canvas_modelspace, const_fixed, const_roller, layout_properties):
    # Get x-distance of constrain from text:
    const_fixed.x_real = float(layout_properties.txt_const1_x.get())
    const_roller.x_real = float(layout_properties.txt_const2_x.get())

    # Delete figure of previous constrain:
    canvas_modelspace.delete('constfix', 'constroll')

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
def edit_loads(loads_properties, scrollbar_properties, layout_properties):
    try:
        selected_name = scrollbar_properties.mylist.get(scrollbar_properties.mylist.curselection())
        scrollbar_properties.last_selected_load = selected_name

        if selected_name in loads_properties.forces_dict:
            # Write out selected force's forces + position:
            layout_properties.txt_force_x_pos.delete(0, 10)
            layout_properties.txt_force_y_pos.delete(0, 10)
            layout_properties.txt_force_x.delete(0, 10)
            layout_properties.txt_force_y.delete(0, 10)

            # Insert load values to the entry boxes:
            layout_properties.txt_force_x_pos.insert(END, loads_properties.forces_dict[selected_name].x_real)
            layout_properties.txt_force_y_pos.insert(END, loads_properties.forces_dict[selected_name].y_real)
            layout_properties.txt_force_x.insert(END, loads_properties.forces_dict[selected_name].Fx)
            layout_properties.txt_force_y.insert(END, loads_properties.forces_dict[selected_name].Fy)

        elif selected_name in loads_properties.moments_dict:
            # Write out selected force's forces + position:
            layout_properties.txt_moment_x_pos.delete(0, 10)
            layout_properties.txt_moment_y.delete(0, 10)
            layout_properties.txt_moment_z.delete(0, 10)

            # Insert load values to the entry boxes:
            layout_properties.txt_moment_x_pos.insert(END, loads_properties.moments_dict[selected_name].x2_real)
            layout_properties.txt_moment_y.insert(END, loads_properties.moments_dict[selected_name].My)
            layout_properties.txt_moment_z.insert(END, loads_properties.moments_dict[selected_name].Mz)

        layout_properties.txt_load_name.config(state = 'normal')
        layout_properties.txt_load_name.delete(0, END)
        layout_properties.txt_load_name.insert(END, selected_name)

    except:
        print("Select a Load!")

"""
Apply loads:
"""
def apply_loads(canvas_modelspace, loads_properties, scrollbar_properties, layout_properties):
    if scrollbar_properties.last_selected_load != "":
        selected_name = scrollbar_properties.last_selected_load

        if selected_name in loads_properties.forces_dict:
            # Get force data from text:
            loads_properties.forces_dict[selected_name].Fx = float(layout_properties.txt_force_x.get())
            loads_properties.forces_dict[selected_name].Fy = float(layout_properties.txt_force_y.get())
            loads_properties.forces_dict[selected_name].x_real = float(layout_properties.txt_force_x_pos.get())
            loads_properties.forces_dict[selected_name].y_real = float(layout_properties.txt_force_y_pos.get())

            # Delete old load figure:
            canvas_modelspace.delete(selected_name)

            # Update load obj:
            new_name = layout_properties.txt_load_name.get()
            loads_properties.forces_dict[new_name] = loads_properties.forces_dict.pop(selected_name)
            loads_properties.forces_dict[new_name].name = new_name

            # Draw load figure with new tag-name:
            loads_properties.forces_dict[new_name].draw_force(canvas_modelspace)

        elif selected_name in loads_properties.moments_dict:
            # Get force data from text:
            loads_properties.moments_dict[selected_name].My = float(layout_properties.txt_moment_y.get())
            loads_properties.moments_dict[selected_name].Mz = float(layout_properties.txt_moment_z.get())
            loads_properties.moments_dict[selected_name].x2_real = float(layout_properties.txt_moment_x_pos.get())

            # Delete old load figure:
            canvas_modelspace.delete(selected_name)

            # Update load obj:
            new_name = layout_properties.txt_load_name.get()
            loads_properties.moments_dict[new_name] = loads_properties.moments_dict.pop(selected_name)
            loads_properties.moments_dict[new_name].name = new_name

            # Draw load figure with new tag-name:
            loads_properties.moments_dict[new_name].draw_moment(canvas_modelspace)

        # Update name on scrollbar-list:
        scrollbar_properties.mylist.delete(ACTIVE)
        scrollbar_properties.mylist.insert(END, new_name)

        # Update nem entry-box:
        layout_properties.txt_load_name.delete(0, END)
        layout_properties.txt_load_name.insert(END, 'Load-name')
        layout_properties.txt_load_name.config(state = 'disabled')

        scrollbar_properties.last_selected_load = ""
    
"""
Remove forces from list:
"""
def remove_obj(canvas_modelspace, loads_properties, scrollbar_properties, layout_properties):
    try:
        selected_name = scrollbar_properties.mylist.get(scrollbar_properties.mylist.curselection())
        canvas_modelspace.delete(selected_name)
        if selected_name in loads_properties.forces_dict:
            del loads_properties.forces_dict[selected_name]
        elif selected_name in loads_properties.moments_dict:
            del loads_properties.moments_dict[selected_name]

        scrollbar_properties.mylist.delete(ACTIVE)

        end_index = scrollbar_properties.mylist.index("end")
        if end_index == 0:
            layout_properties.txt_load_name.delete(0, END)
            layout_properties.txt_load_name.insert(END, 'Load-name')
            layout_properties.txt_load_name.config(state = 'disabled')
    except:
        print("Select a Load!")