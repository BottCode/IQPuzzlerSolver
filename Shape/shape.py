class Shape:
    # shape_code is a list of numbers in {0,1,2,3} which represents the shape of each variable.
    def __init__(self, shape_code, color, name, domain):
        self.shape_code = shape_code
        self.color = color
        self.name = name
        self.domain = domain
