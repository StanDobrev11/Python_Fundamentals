class Circle:
    __pi = 3.14

    def __init__(self, diam):
        self.diam = diam

    def calculate_circumference(self):  # 2 * pi * r
        return 2 * Circle.__pi * self.diam / 2

    def calculate_area(self):  # pi . r ** 2
        return (self.diam / 2) ** 2 * Circle.__pi

    def calculate_area_of_sector(self, deg_angle):
        return (deg_angle / 360) * Circle.__pi * (self.diam / 2) ** 2
