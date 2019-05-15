import random

class Item(object):
    def __init__(self, v, w):
        self.value = v # Item's value. You want to maximize that!
        self.weight = w # Item's weight. The sum of all items should be <= CAPACITY

class Genetic:
	def __init__(self):
		self.ITEMS = [Item(50, 30), Item(30, 50), Item(20, 40), Item(30, 20), Item(50, 60)]
        # Capacity of the knapsack
		self.CAPACITY = 110
        # Size of initial population filled with some permutation of 0s and 1s
		self.POP_SIZE = 4
        # Maximum number of generations the algorithm will run
		self.GEN_MAX = 50
		
	def fitness(self,target):
		total_value = 0
		total_weight = 0
		
		for i in range(len(target)):
			if (target[i] == 1):
				total_value += self.ITEMS[i].value * self.ITEMS[i].weight
				total_weight += self.ITEMS[i].weight

		if total_weight > self.CAPACITY:
			return 0
		else:
			return total_value
	
	def initial_population(self,amount):
		pop=[]
		for i in range(amount):
			individual=[]
			for j in range(len(self.ITEMS)):
				individual.append(random.randint(0, 1))
			pop.append(individual)
		return pop
	
	
	
	def mutate_individual(self,target):
		r = random.randint(0, len(target) - 1)
		if target[r] == 1:
			target[r] = 0
		else:
			target[r] = 1
			
		return target
			
		

	def crossover_mutation(self,parents):
		father=parents[0]
		mother=parents[1]
		index1 = random.randint(0, len(father) - 1)
        ############# crossover #############
		child1 = father[:index1] + mother[index1:]
		child2 = mother[:index1] + father[index1:]

        ############# mutation #############
		child1=self.mutate_individual(child1)
		child2=self.mutate_individual(child2)
        #self.mutate_individual(child1)
        #self.mutate_individual(child2)
		
		parents.append(child1)
		parents.append(child2)
		return parents
	
	def eval_population(self,pop, fit):
		new_pop = []
		parent_len = 2
		count = 0
        # for selection
		for i in range(len(fit)):
			if (fit[i] > 0):
				if (count == parent_len):
					break
				new_pop.append(pop[i])
				count += 1
		new_pop = self.crossover_mutation(new_pop)
		return new_pop
	
	def create_generations(self):
		generation = 1
		population = self.initial_population(self.POP_SIZE)
		print("old ", population)
		for g in range(0, self.GEN_MAX):
			fitness_list = []
			print("Generation",generation, "with", len(population))
			population = sorted(population, key=self.fitness, reverse=True)
			for i in population:
				print(str(i),", fit:", self.fitness(i))
				fitness_list.append(self.fitness(i))  # we add this to hold the fitness values
			population = self.eval_population(population, fitness_list)
			print("new ", population)
			generation += 1
		population = sorted(population, key=self.fitness, reverse=True)
		print("best items: ", population[0], "with fitness: ", self.fitness(population[0]))


g=Genetic()
g.create_generations()
