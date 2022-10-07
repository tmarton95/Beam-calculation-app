import math

class ConstrainFix:
    def __init__(self, modelspace_origin):
        self.x_origin = modelspace_origin[0]
        self.y_origin = modelspace_origin[1]

        self.x_real = 0
        self.scale = 500
    def draw_const(self, canvas_modelspace):
        x = self.x_real * self.scale + self.x_origin
        canvas_modelspace.create_line(x, self.y_origin, x + 35*math.sin(math.pi/6), self.y_origin + 35*math.cos(math.pi/6), width=3, tag = 'constfix_1')
        canvas_modelspace.create_line(x + 35*math.sin(math.pi/6), self.y_origin + 35*math.cos(math.pi/6), 
                                        x - 35*math.sin(math.pi/6), self.y_origin + 35*math.cos(math.pi/6), width=3, tag = 'constfix_2')
        canvas_modelspace.create_line(x - 35*math.sin(math.pi/6), self.y_origin + 35*math.cos(math.pi/6), x, self.y_origin, width=3, tag = 'constfix_3')


class ConstrainRolling:
    def __init__(self, modelspace_origin):
        self.x_origin = modelspace_origin[0]
        self.y_origin = modelspace_origin[1]

        self.x_real = 1
        self.scale = 500
    def draw_const(self, canvas_modelspace):
        x = self.x_real * self.scale + self.x_origin
        canvas_modelspace.create_line(x, self.y_origin, x + 35*math.sin(math.pi/6), self.y_origin + 35*math.cos(math.pi/6), width=3, tag = 'constroll_1')
        canvas_modelspace.create_line(x + 35*math.sin(math.pi/6), self.y_origin + 35*math.cos(math.pi/6), 
                                        x - 35*math.sin(math.pi/6), self.y_origin + 35*math.cos(math.pi/6), width=3, tag = 'constroll_2')
        canvas_modelspace.create_line(x - 35*math.sin(math.pi/6), self.y_origin + 35*math.cos(math.pi/6), x, self.y_origin, width=3, tag = 'constroll_3')
        r = 9
        canvas_modelspace.create_oval(x - r, self.y_origin + 35*math.cos(math.pi/6) + 2*r,
                                        x + r, self.y_origin + 35*math.cos(math.pi/6), width=3, tag = 'constroll_4')