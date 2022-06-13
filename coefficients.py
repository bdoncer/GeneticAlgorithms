import numpy
import pygad

function_inputs = None
desired_output = None

def fitness_func(solution, solution_index):
    if function_inputs == None or desired_output == None:
        return 0
    output = numpy.sum(solution * function_inputs)
    return 1.0 / numpy.abs(output - desired_output)

class Coefficients:
    def __init__(self):
        self.function_inputs = None
        self.desired_output = None
        self.num_genes = None
        self.sol_per_pop = 50
        self.init_range_low = -2
        self.init_range_high = 5
        self.mutation_percent_genes = 50
        self.num_generations = 100
        self.num_parents_mating = 10


    def result_clicked(self):
        global function_inputs, desired_output
        function_inputs = self.function_inputs
        desired_output = self.desired_output
        ga_instance = pygad.GA(num_generations=self.num_generations,
                               num_parents_mating=self.num_parents_mating,
                               fitness_func=fitness_func,
                               sol_per_pop=self.sol_per_pop,
                               num_genes=self.num_genes,
                               init_range_low=self.init_range_low,
                               init_range_high=self.init_range_high,
                               mutation_percent_genes=self.mutation_percent_genes)



        ga_instance.run()
        solution, _, _ = ga_instance.best_solution()
        return solution