import math

class Loads:
    def __init__(self):
        self.forces_dict = {}
        self.moments_dict = {}
        self.force_id = 0
        self.moment_id = 0

class Force:
    def __init__(self, modelspace_origin, name):
        self.name = name
        self.L = 50
        self.l = 20
        self.x_real = 0
        self.y_real = 0
        self.scale = 500
        self.Fx = 0
        self.Fy = 0
        self.origin_x, self.origin_y = modelspace_origin

    def draw_force(self, canvas_modelspace):
        self.x_end = self.origin_x + self.x_real * self.scale
        if self.Fy > 0:
            self.y_end = self.origin_y + 5 - self.y_real * self.scale
        elif self.Fy < 0:
            self.y_end = self.origin_y - 5 - self.y_real * self.scale
        elif self.Fy == 0:
            self.y_end = self.origin_y - 10 - self.y_real * self.scale

        alfa = math.asin(self.Fy / (self.Fy**2 + self.Fx**2)**0.5)
        beta = math.pi / 6
        self.y_start = self.y_end + self.L * math.sin(alfa)
        self.y_start_head1 = self.y_end + self.l * math.sin(alfa + beta)
        self.y_start_head2 = self.y_end + self.l * math.sin(alfa - beta)

        if self.Fx >= 0:
            self.x_start = self.x_end - self.L * math.cos(alfa)
            self.x_start_head1 = self.x_end - self.l * math.cos(alfa + beta)
            self.x_start_head2 = self.x_end - self.l * math.cos(alfa - beta)

        elif self.Fx < 0:
            self.x_start = self.x_end + self.L * math.cos(alfa)
            self.x_start_head1 = self.x_end + self.l * math.cos(alfa + beta)
            self.x_start_head2 = self.x_end + self.l * math.cos(alfa - beta)

        # Draw arrow main line:
        canvas_modelspace.create_line(self.x_start, self.y_start, self.x_end, self.y_end, width = 3, tag = self.name)

        # Draw arrow's head:
        canvas_modelspace.create_line(self.x_start_head1, self.y_start_head1, self.x_end, self.y_end, width = 3, tag = self.name)
        canvas_modelspace.create_line(self.x_start_head2, self.y_start_head2, self.x_end, self.y_end, width = 3, tag = self.name)


class Moment:
    def __init__(self, modelspace_origin, name):
        self.name = name
        self.L = 50
        self.l = 25
        self.x2_real = 0
        self.scale = 500
        self.My = 0
        self.Mz = 0
        self.origin_x, self.origin_y = modelspace_origin

    def draw_moment(self, canvas_modelspace):
        if self.My > 0:
            self.x2 = self.origin_x + self.x2_real * self.scale
            self.x1 = self.x2 - self.l
            self.x3 = self.x2 + self.l

            self.y1 = self.origin_y - 20
            self.y2 = self.y1 - 30
            self.y3 = self.y1

            # Draw curve:
            canvas_modelspace.create_line(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, smooth = 1, width = 2.5, tag = self.name)

            # Draw arrow's head:
            canvas_modelspace.create_line(self.x1, self.y1, self.x1 + 9, self.y1 - 18, width = 3, tag = self.name)
            canvas_modelspace.create_line(self.x1, self.y1, self.x1 + 17, self.y1 -5, width = 3, tag = self.name)

        elif self.My < 0:
            self.x2 = self.origin_x + self.x2_real * self.scale
            self.x1 = self.x2 - self.l
            self.x3 = self.x2 + self.l

            self.y1 = self.origin_y - 20
            self.y2 = self.y1 - 30
            self.y3 = self.y1

            # Draw curve:
            canvas_modelspace.create_line(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, smooth = 1, width = 2.5, tag = self.name)

            # Draw arrow's head:
            canvas_modelspace.create_line(self.x3, self.y3, self.x3 - 9, self.y3 - 18, width = 3, tag = self.name)
            canvas_modelspace.create_line(self.x3, self.y3, self.x3 - 17, self.y3 -5, width = 3, tag = self.name)
        
        if self.Mz > 0:
            self.x2 = self.origin_x + self.x2_real * self.scale
            self.x1 = self.x2 - self.l + 5
            self.x3 = self.x2 + self.l - 5

            self.y2 = self.origin_y - 15
            self.y1 = self.y3 = self.y2

            # Main lines:
            canvas_modelspace.create_line(self.x1, self.y1 + 3, self.x3, self.y3 + 3, width = 3.5, tag = self.name)
            canvas_modelspace.create_line(self.x1, self.y1 - 3, self.x3, self.y3 - 3, width = 3.5, tag = self.name)

            # Draw arrow's head:
            canvas_modelspace.create_line(self.x1 - 8, self.y1, self.x1 + 18, self.y1 + 10, width = 2.5, tag = self.name)
            canvas_modelspace.create_line(self.x1 - 8, self.y1, self.x1 + 18, self.y1 - 10, width = 2.5, tag = self.name)

        elif self.Mz < 0:
            self.x2 = self.origin_x + self.x2_real * self.scale
            self.x1 = self.x2 - self.l + 5
            self.x3 = self.x2 + self.l - 5

            self.y2 = self.origin_y - 15
            self.y1 = self.y3 = self.y2

            # Main lines:
            canvas_modelspace.create_line(self.x1, self.y1 + 3, self.x3, self.y3 + 3, width = 3.5, tag = self.name)
            canvas_modelspace.create_line(self.x1, self.y1 - 3, self.x3, self.y3 - 3, width = 3.5, tag = self.name)

            # Draw arrow's head:
            canvas_modelspace.create_line(self.x3 + 8, self.y1, self.x3 - 18, self.y1 + 10, width = 2.5, tag = self.name)
            canvas_modelspace.create_line(self.x3 + 8, self.y1, self.x3 - 18, self.y1 - 10, width = 2.5, tag = self.name)