import math

class ConstrainFix:
    def __init__(self, modelspace_origin):
        self.x_origin, self.y_origin = modelspace_origin
        self.x_real = 0
        self.scale = 500
        self.l = 35
    def draw_const(self, canvas_modelspace):
        x = self.x_real * self.scale + self.x_origin
        y = self.y_origin + 4

        start_1 = end_3 = [x, y]
        start_2 = end_1 = [x + self.l*math.sin(math.pi/6), y + self.l*math.cos(math.pi/6)]
        start_3 = end_2 = [x - self.l*math.sin(math.pi/6),y + self.l*math.cos(math.pi/6)]

        # Right line:
        canvas_modelspace.create_line(start_1[0], start_1[1], end_1[0], end_1[1], width=3, tag = 'constfix')
        # Bottom line:
        canvas_modelspace.create_line(start_2[0], start_2[1], end_2[0], end_2[1], width=3, tag = 'constfix')
        # Left line:
        canvas_modelspace.create_line(start_3[0], start_3[1], end_3[0], end_3[1], width=3, tag = 'constfix')

        # Ground-lines:
        end_4 = [start_3[0] - 7, start_3[1] + 15]
        for i in range(4):
            canvas_modelspace.create_line(start_3[0] + i*11, start_3[1], end_4[0] + i*11, end_4[1], width=2.5, tag = 'constfix')


class ConstrainRolling:
    def __init__(self, modelspace_origin):
        self.x_origin, self.y_origin = modelspace_origin
        self.x_real = 1
        self.scale = 500
        self.l = 35
    def draw_const(self, canvas_modelspace):
        x = self.x_real * self.scale + self.x_origin
        y = self.y_origin + 4

        start_1 = end_3 = [x, y]
        start_2 = end_1 = [x + self.l*math.sin(math.pi/6), y + self.l*math.cos(math.pi/6)]
        start_3 = end_2 = [x - self.l*math.sin(math.pi/6), y + self.l*math.cos(math.pi/6)]

        # right line:
        canvas_modelspace.create_line(start_1[0], start_1[1], end_1[0], end_1[1], width=3, tag = 'constroll')
        # Bottom line:
        canvas_modelspace.create_line(start_2[0], start_2[1], end_2[0], end_2[1], width=3, tag = 'constroll')
        # Left line:
        canvas_modelspace.create_line(start_3[0], start_3[1], end_3[0], end_3[1], width=3, tag = 'constroll')

        r = 9
        canvas_modelspace.create_oval(x - r, start_2[1] + 2*r, x + r, start_2[1], width=3, tag = 'constroll')
        
        # Ground-lines:
        canvas_modelspace.create_line(start_2[0], start_2[1] + 18, end_2[0], end_2[1] + 18, width=3, tag = 'constroll')

        end_4 = [start_3[0] - 7, end_2[1] + 15 + 18]
        for i in range(4):
            canvas_modelspace.create_line(start_3[0] + i*11, start_3[1] + 18, end_4[0] + i*11, end_4[1], width=2.5, tag = 'constroll')