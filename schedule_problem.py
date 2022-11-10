import random

import numpy as np
from collections import Counter

from deap import base
from deap import creator
from deap import tools

professors = ['Caetano', 'Fabrício', 'Tadeu', 'Ermerson',
              'Cesar', 'Jhonatta', 'Bruno', 'Priscilla']



ind = np.array([[1, 2, 3, 4, 5],
                [1, 2, 6, 7, 1],
                [2, 1, 8, 9, 2],
                [4, 1, 3, 2, 0]
                ])

individual = [
    [1, 2, 3, 4, 5],
    [1, 2, 6, 7, 1],
    [2, 1, 8, 9, 2],
    [4, 1, 3, 2, 0]
]


def evaluate(individual):
    result = 0
    for i in range(5):
        counter = Counter(individual[:, i])
        amount = sum([v for (k, v) in dict(counter).items() if v > 1])
        result += round(amount / 2)
    return [result]


def chromosome():
    ind = []
    for i in range(4):
        ind.append(random.sample(individual[i], 5))
    return ind


def create_individuo():
    ind = []
    for i in range(4):
        ind.append(random.sample(individual[i], 5))
    return np.array(ind)


creator.create('FitnessMax', base.Fitness, weights=(1.0,))
creator.create('Individual', np.ndarray, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register('individual', tools.initRepeat,
                 creator.Individual, chromosome, 1)
#toolbox.register('individual', tools.initRepeat, creator.Individual, chromosome, 1)

toolbox.register('population', tools.initRepeat, list, toolbox.individual)

toolbox.register('evaluate', evaluate)

toolbox.register('mate', tools.cxTwoPoint)

toolbox.register('mutate', tools.mutFlipBit, indpb=0.05)

toolbox.register('select', tools.selTournament, tournsize=3)


def main():
    random.seed(64)

    pop = toolbox.population(n=2)
    print(pop)
    # print(evaluate(pop[0]))


if __name__ == "__main__":
    main()
