from load_classes import Force, Moment
from tkinter import messagebox
from tkinter import*
from sympy import*
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

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
    length_real = float(layout_properties.txt_beam.get())
    if length_real != 0:
        beam_properties.length_real = length_real
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
"""
Calculate reaction forces:
"""
def calc_reactions(const_fixed, const_roller, beam_properties, loads_properties, tab2_canvas):


    # Check that  odel is valid:
    const_fixed_out = const_fixed.x_real < 0 or const_fixed.x_real > beam_properties.length_real
    const_roll_out = const_roller.x_real < 0 or const_roller.x_real > beam_properties.length_real
    if const_roll_out or const_fixed_out:
        messagebox.showinfo(title="Warning", message = f"Constrains are not connected to the Beam!")
    else:
        Ax, Ay, By = symbols('Ax, Ay, By')
        equation_forces_x = Ax
        equation_forces_y = Ay + By
        equation_moments_A = By * (const_roller.x_real - const_fixed.x_real)

        for force in loads_properties.forces_dict:
            # Define forces + its locations:
            force_x = loads_properties.forces_dict[force].Fx
            force_y = loads_properties.forces_dict[force].Fy
            force_x_pos = loads_properties.forces_dict[force].x_real
            force_y_pos = loads_properties.forces_dict[force].y_real

            # Add to equations:
            equation_forces_x += force_x
            equation_moments_A += -force_x * force_y_pos
            equation_forces_y += force_y
            equation_moments_A += (force_x_pos - const_fixed.x_real) * force_y

        for moment in loads_properties.moments_dict:
            equation_moments_A += loads_properties.moments_dict[moment].My

        react_forces = solve([equation_forces_x, equation_forces_y, equation_moments_A])
        loads_properties.reactions['Ax'] = round(react_forces[Ax], 2)
        loads_properties.reactions['Ay'] = round(react_forces[Ay], 2)
        loads_properties.reactions['By'] = round(react_forces[By], 2)

        create_load_plot(
        fx_data = create_fx_data(const_fixed, beam_properties, loads_properties),
        fy_data = create_fy_data(const_fixed, const_roller, beam_properties, loads_properties),
        moment_z_data = create_moment_z_data(const_fixed, const_roller, beam_properties, loads_properties),
        tab2_canvas = tab2_canvas,
        beam_properties = beam_properties
        )
"""
Calculate reaction forces:
"""
def create_fx_data(const_fixed, beam_properties, loads_properties):
    fx_list = []
    for force in loads_properties.forces_dict:
        force_x = loads_properties.forces_dict[force].Fx
        force_x_pos = loads_properties.forces_dict[force].x_real

        if force_x != 0:
            fx_list.append([force_x_pos, force_x])

    fx_list.append([const_fixed.x_real, loads_properties.reactions['Ax']])
    fx_list.sort()
    print(fx_list)

    # Creating load-array for X:
    y = x = np.zeros(0)
    force_value = 0
    for k in range(len(fx_list)):
        x_start = fx_list[k][0]

        # At last load:
        if k == len(fx_list) - 1:
            x_end = fx_list[k][0]
        # At other loads:
        else:
            x_end = fx_list[k + 1][0]
        force_value += fx_list[k][1]

        x1 = np.linspace(x_start, x_end, 100)
        x = np.append(x, x1)
        y = np.append(y, -np.ones(x1.size) * force_value)

    # If beam left-end has no load:
    if fx_list[0][0] != 0:
        x_end = fx_list[0][0]
        load_start_x = np.linspace(0, x_end, 100)
        load_start_y = np.zeros(load_start_x.size)
        x = np.append(load_start_x, x)
        y = np.append(load_start_y, y)

    # If beam right end has no load:
    if fx_list[-1][0] != beam_properties.length_real:
        x_start = fx_list[-1][0]
        x_end = beam_properties.length_real
        load_end_x = np.linspace(x_start, x_end, 100)
        load_end_y = np.zeros(load_end_x.size)
        x = np.append(x, load_end_x)
        y = np.append(y, load_end_y)

    fx_data = [x, y]
    return fx_data
#=====================================================================================
def create_fy_data(const_fixed, const_roller, beam_properties, loads_properties):
    fy_list = []
    for force in loads_properties.forces_dict:
        force_y = loads_properties.forces_dict[force].Fy
        force_y_pos = loads_properties.forces_dict[force].x_real

        if force_y != 0:
            fy_list.append([force_y_pos, force_y])

    fy_list.append([const_fixed.x_real, loads_properties.reactions['Ay']])
    fy_list.append([const_roller.x_real, loads_properties.reactions['By']])

    fy_list.sort()
    print(fy_list)

    # Creating load-array for Y:
    y = x = np.zeros(0)
    force_value = 0
    for k in range(len(fy_list)):
        x_start = fy_list[k][0]

        # At last load:
        if k == len(fy_list) - 1:
            x_end = fy_list[k][0]
        # At other loads:
        else:
            x_end = fy_list[k + 1][0]
        force_value += fy_list[k][1]

        x1 = np.linspace(x_start, x_end, 100)
        x = np.append(x, x1)
        y = np.append(y, np.ones(x1.size) * force_value)

    # If beam left-end has no load:
    if fy_list[0][0] != 0:
        x_end = fy_list[0][0]
        load_start_x = np.linspace(0, x_end, 100)
        load_start_y = np.zeros(load_start_x.size)
        x = np.append(load_start_x, x)
        y = np.append(load_start_y, y)

    # If beam right end has no load:
    if fy_list[-1][0] != beam_properties.length_real:
        x_start = fy_list[-1][0]
        x_end = beam_properties.length_real
        load_end_x = np.linspace(x_start, x_end, 100)
        load_end_y = np.zeros(load_end_x.size)
        x = np.append(x, load_end_x)
        y = np.append(y, load_end_y)

    fy_data = [x, y]
    return fy_data
#=====================================================================================
def create_moment_z_data(const_fixed, const_roller, beam_properties, loads_properties):
    # PLACEHOLDERS...:
    x = np.linspace(0, beam_properties.length_real, 100)
    y = x * 0
    moment_z_data = [x, y]

    #===========================================================================================
    # moment_z_list = []
    # for force in loads_properties.forces_dict:
    #     force_y = loads_properties.forces_dict[force].Fy
    #     force_y_pos = loads_properties.forces_dict[force].x_real

    #     if force_y != 0:
    #         moment_z_list.append([force_y_pos, force_y, 'Fy'])

    # moment_z_list.append([const_fixed.x_real, loads_properties.reactions['Ay'], 'Fy'])
    # moment_z_list.append([const_roller.x_real, loads_properties.reactions['By'], 'Fy'])

    # #=======================
    # moment_z_list = []
    # for moment in loads_properties.moments_dict:
    #     moment_z = loads_properties.moments_dict[moment].My
    #     moment_z_pos = loads_properties.moments_dict[moment].x2_real

    #     if moment_z != 0:
    #         moment_z_list.append([moment_z_pos, moment_z, 'Mz'])

    # moment_z_list.sort()
    # #=======================
    # # Creating load-array for Y:
    # y = x = np.zeros(0)
    # moment_value = 0
    # eq_moment_z = []
    # fy_last_loads = []
    # x_coord = symbols('x_coord')
    # for k in range(len(moment_z_list)):
    #     x_start = moment_z_list[k][0]

    #     # At last load:
    #     if k == len(moment_z_list) - 1:
    #         x_end = moment_z_list[k][0]
    #     # At other loads:
    #     else:
    #         x_end = moment_z_list[k + 1][0]

    #     x1 = np.linspace(x_start, x_end, 100)
    #     x = np.append(x, x1)
    #     if moment_z_list[k][2] == 'Mz':
    #         moment_value += moment_z_list[k][1]
    #         y = np.append(y, np.ones(x1.size) * moment_value)

    #     elif moment_z_list[k][2] == 'Fy' and fy_last_loads == []:
    #         eq_moment_z.append(x_coord * moment_z_list[1])



    # # If beam left-end has no load:
    # if moment_z_list[0][0] != 0:
    #     x_end = moment_z_list[0][0]
    #     load_start_x = np.linspace(0, x_end, 100)
    #     load_start_y = np.zeros(load_start_x.size)
    #     x = np.append(load_start_x, x)
    #     y = np.append(load_start_y, y)

    # # If beam right end has no load:
    # if moment_z_list[-1][0] != beam_properties.length_real:
    #     x_start = moment_z_list[-1][0]
    #     x_end = beam_properties.length_real
    #     load_end_x = np.linspace(x_start, x_end, 100)
    #     load_end_y = np.zeros(load_end_x.size)
    #     x = np.append(x, load_end_x)
    #     y = np.append(y, load_end_y)

    # moment_z_data = [x, y]
    #===========================================================================================
    return moment_z_data
"""
Plot load charts
"""
def create_load_plot(fx_data, fy_data, moment_z_data, tab2_canvas, beam_properties):

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    ax1.plot(fx_data[0], fx_data[1])
    ax2.plot(fy_data[0], fy_data[1])
    ax3.plot(moment_z_data[0], moment_z_data[1])

    L = beam_properties.length_real
    ax1.set_xticks([0, L / 5, 2*L / 5, 3*L / 5, 4*L / 5, L ])
    ax2.set_xticks([0, L / 5, 2*L / 5, 3*L / 5, 4*L / 5, L ])
    ax3.set_xticks([0, L / 5, 2*L / 5, 3*L / 5, 4*L / 5, L ])

    ax1.set_ylabel('Nx [N]', labelpad=8)
    ax2.set_ylabel('Vy [N]', labelpad=8)
    ax3.set_ylabel('Mz [Nm]', labelpad=8)

    ax3.set_xlabel('x [m]')

    # ax1.spines['right'].set_color('none')
    # ax1.spines['top'].set_color('none')

    fig.set_figwidth(5)
    fig.set_figheight(4)
    fig.tight_layout(pad = 1, w_pad = 0.2, h_pad = 0.6)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas_plot = FigureCanvasTkAgg(fig, master = tab2_canvas)  
    canvas_plot.draw()
  
    # placing the canvas on the Tkinter window
    canvas_plot.get_tk_widget().place(x = 195, y = 50)

    plt.show()



