import math

class Force:
    def __init__(self, modelspace_origin, name):
        self.name = name
        self.L = 50
        self.l = 20
        self.x_real = 0.5
        self.scale = 500
        self.Fx = 0
        self.Fy = -1
        self.origin_x = modelspace_origin[0]
        self.y_end = modelspace_origin[1]

    def draw_force(self, canvas_modelspace):
        self.x_end = self.origin_x + self.x_real * self.scale

        alfa = math.asin(self.Fy / (self.Fy**2 + self.Fx**2)**0.5)
        beta = math.pi / 6
        self.y_start = self.y_end + self.L * math.sin(alfa)
        self.y_start_minor1 = self.y_end + self.l * math.sin(alfa + beta)
        self.y_start_minor2 = self.y_end + self.l * math.sin(alfa - beta)

        if self.Fx >= 0:
            self.x_start = self.x_end - self.L * math.cos(alfa)
            self.x_start_minor1 = self.x_end - self.l * math.cos(alfa + beta)
            self.x_start_minor2 = self.x_end - self.l * math.cos(alfa - beta)

        elif self.Fx < 0:
            self.x_start = self.x_end + self.L * math.cos(alfa)
            self.x_start_minor1 = self.x_end + self.l * math.cos(alfa + beta)
            self.x_start_minor2 = self.x_end + self.l * math.cos(alfa - beta)

        # Draw arrow main line:
        canvas_modelspace.create_line(self.x_start, self.y_start, self.x_end, self.y_end, width = 3, tag = self.name)

        # Draw arrow's head:
        canvas_modelspace.create_line(self.x_start_minor1, self.y_start_minor1, self.x_end, self.y_end, width = 3, tag = self.name)
        canvas_modelspace.create_line(self.x_start_minor2, self.y_start_minor2, self.x_end, self.y_end, width = 3, tag = self.name)