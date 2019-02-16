import math
import numpy
import pandas as pd
import csv

numpy.seterr(all='ignore')

class OptimizableFunction:
    def __init__(self):
        pass
    def get_value(self,  points):
        pass
    def get_gradient(self,  points):
        pass
    def load_data(self, i):
        pass
    def get_initial_point(self, i):
        pass

class FunctionG(OptimizableFunction):
    def __init__(self):
        # self.a = 1   #input("Enter value of a for g(z)")
        # self.b = 100 #input("Enter value of a for g(z)")
        pass

    def load_data(self, i):
        self.x = 0
        self.y = 0
        if(i == 1):
            self.x = input("Enter value of a for g(z): ")
            self.y = input("Enter value of b for g(z): ")
        data_dist = [[1, 100], [self.x, self.y]]
        self.a = float(data_dist[i][0])
        self.b = float(data_dist[i][1])

    def get_value(self,  points):
        return (((self.a -  points[0]) ** 2) + (self.b * (( points[1] -  points[0]) ** 2) ** 2))
        
    def get_gradient(self,  points):
        return numpy.array([
            -2 * (self.a -  points[0]) - (4 * self.b *  points[0] * ( points[1] - ( points[0] ** 2))),
            2 * self.b * ( points[1] - ( points[0] ** 2))
            ], dtype = 'd')

    def get_initial_point(self, i):
        return numpy.array([[0.2, 0.2],[0.5,0.5]], dtype = 'd')[i]
    
class FunctionF(OptimizableFunction):
    def __init__(self):
        pass

    def load_data(self, i):
        data_dist = [pd.Series.tolist((pd.read_csv("a1_q4_f_data1.csv")['data1'])), pd.Series.tolist((pd.read_csv("a1_q4_f_data2.csv")['data1'])) ]
        self.data = data_dist[i]

    def get_initial_point(self, i):
        return numpy.array([[0.0, 0.0],[0.5,0.5]], dtype = 'd')[i]

    def get_value(self,  points):
        return (-1 * sum(list(map(lambda x: points[x], self.data))) + math.log(math.exp(points[0]) + numpy.exp(points[1])))
        
    def get_gradient(self,  points):
        return numpy.array([
            -1 * sum(list(map(lambda x: 1 if (x == 0) else 0, self.data))) + numpy.exp(points[0])/(numpy.exp(points[0]) + numpy.exp(points[1])),
            -1 * sum(list(map(lambda x: 0 if (x == 0) else 1, self.data))) + numpy.exp(points[1])/(numpy.exp(points[0]) + numpy.exp(points[1]))
        ], dtype = 'd')

class GradientDescent:
    def __init__(self):
        pass

    def get_learning_rate(self, t):
        return []

    def optimize(self, y):
        for i in range(2):
            init_points = y.get_initial_point(i)
            print("Initial:", init_points)
            for t in range(10000):
                yval = y.get_value(init_points)
                ydash = y.get_gradient(init_points)
                alpha = self.get_learning_rate([t, ydash])
                # print(ydash, init_points)
                init_points = init_points - alpha*(ydash)
            # print("Results for y: ",type(y))
            print("points: ",init_points)
            print("y value: ",yval)

    
class RobbinsMonro(GradientDescent):
    def __init__(self):
        self.T = 100
        self.k = 1

    def get_learning_rate(self, param):
        return ((param[0] + self.T) ** -self.k)

class AdaGrad(GradientDescent):
    def __init__(self):
        self.n = 0.1
        self.e = 10 ** (-8)
        self.ydashSum = numpy.array([0.0, 0.0], dtype = 'd')

    def get_learning_rate(self, param):
        self.ydashSum += param[1] ** 2
        denominator0 = math.sqrt(self.e + self.ydashSum[0])
        denominator1 = math.sqrt(self.e + self.ydashSum[1])
        return numpy.array([self.n/denominator0, self.n/denominator1], dtype = 'd')

def main():
    obj1 = FunctionG()
    for i in range(2):
        obj1.load_data(i)
        robbinG = RobbinsMonro()
        print("Results of g(z) with Robbins Monro Learning Rate")
        robbinG.optimize(obj1)
        adaG = AdaGrad()
        print("Results of g(z) with AdaGrad Learning Rate")
        adaG.optimize(obj1)

    obj2 = FunctionF()
    for i in range(2):
        obj2.load_data(1)
        robbingF = RobbinsMonro()
        print("Results of f(w) with Robbins Monro Learning Rate")
        robbingF.optimize(obj2)
        adaF = AdaGrad()
        print("Results of f(w) with AdaGrad Learning Rate")
        adaF.optimize(obj2)

main()