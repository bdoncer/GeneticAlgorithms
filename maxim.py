from bees_algorithm import BeesAlgorithm
import matplotlib.pyplot as plt
import numpy as np


def function(x_tab):
    return [np.cos(xi) for xi in x_tab]

def function_to_plot(x):
    return  np.cos(x)





class MaxCtr:
    def __init__(self):
        self.left_boundary = []
        self.right_boundary = []
        self.function = None


    def result_clicked(self):
        alg = BeesAlgorithm(function, self.left_boundary, self.right_boundary, ns=0, nb=14, ne=1, nrb=5, nre=30,
                            stlim=10)
        alg.performFullOptimisation(max_iteration=5000)
        best = alg.best_solution
        return best.values,best.score

    def plot_function(self):
        x_range = self.right_boundary[0] - self.left_boundary[0]
        x_plot = [i for i in
                  np.arange(self.left_boundary[0], self.right_boundary[0],
                            x_range / 1000)]
        x_plot.append(self.right_boundary[0])
        y_plot = []
        for x in x_plot:
            y_plot.append(function_to_plot(x))

        plt.plot(x_plot, y_plot, color="pink")
        plt.show()
