from math import pow

class OptimizableFunction:
    def __init__(self):
        pass
    def get_value(self, knob1, knob2):
        pass
    def get_gradient(self):
        pass
    def load_data(self, i):
        pass
    def get_initial_point(self, i):
        pass

class FunctionG(OptimizableFunction):
    def __init__(self):
        self.a = 1   #input("Enter value of a for g(z)")
        self.b = 100 #input("Enter value of a for g(z)")

    def get_value(self, z1, z2):
        return (pow((self.a - z1), 2) + self.b * pow((z2 - pow(z1, 2)), 2))
        
    def get_gradient(self, z1, z2):
        return ([
            -2 * (self.a - z1) - (-4 * self.b * z1 * (z2 - pow(z1, 2))),
            2 * self.b * z2 - (z2 - pow(z1, 2))
            ])

    def get_initial_point(self, z1, z2):
        return {z1: 0, z2: 0}

class GradientDescent:
    def __init__(self):
        pass

