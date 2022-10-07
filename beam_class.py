class Beam:
    def __init__(self, modelspace_origin):
        self.x_start = modelspace_origin[0]
        self.y_start = modelspace_origin[1]
        self.length_real = 1    # real beam length in meter
        self.scale = 500

        self.d = 0
        self.a = 0
        self.b = 0
        
    def draw_beam(self, canvas_modelspace):
        self.length = self.length_real * self.scale
        self.x_end = self.x_start + self.length
        canvas_modelspace.create_line(self.x_start, self.y_start, self.x_end, self.y_start, width=8, tag = 'beam')