import random

# Number of individuals in each generation
POPULATION_SIZE = 100000

# Valid genes
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Target string to be generated
TARGET = "DUKHAAN KAMIMPANGAN"

class Individual:
    '''
    Class representing individual in population
    '''
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(cls):
        '''
        create random genes for mutation
        '''
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(cls):
        '''
        create chromosome or string of genes
        '''
        global TARGET
        gnome_len = len(TARGET)
        return [cls.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''
        # chromosome for offspring
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            # random probability
            prob = random.random()

            # if prob is less than 0.30, insert gene
            # from parent 1
            if prob < 0.30:
                child_chromosome.append(gp1)

            # if prob is between 0.30 and 0.80, insert
            # gene from parent 2
            elif prob < 0.80:
                child_chromosome.append(gp2)

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())

        # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(child_chromosome)

    def cal_fitness(self):
        '''
        Calculate fitness score, it is the number of
        characters in string which differ from target
        string
        '''
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt: fitness += 1
        return fitness


# Driver code
def main():
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population (populasi awal)
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    while not found:

        # sort the population in increasing order of fitness score
        # (Evaluasi Nilai Fitness)
        population = sorted(population, key=lambda x: x.fitness)

        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break

        # otherwise generate new offsprings for new generation
        new_generation = []

        # perform elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # from 50% of fittest population (Seleksi), Individuals
        # will mate (Reproduksi) to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tString: {}\tFitness: {}".\
            format(generation,
                   "".join(population[0].chromosome),
                   population[0].fitness))
        generation += 1

    print("Generation: {}\tString: {}\tFitness: {}".\
            format(generation,
                   "".join(population[0].chromosome),
                   population[0].fitness))


if __name__ == '__main__':
    main()
