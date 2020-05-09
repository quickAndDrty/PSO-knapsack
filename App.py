from Knapsack import *

k = Knapsack()
#k.readFromFile()
k.readFromFile2()


bestSolution = []
bestFitness = 0
avg = 0
f = open ("PSO.txt", "w")


for i in range(10):
    fitness, solution = k.run(10, 1, 2, 2, 20)
    print(fitness, " ", solution)
    avg += fitness
    if (fitness > bestFitness):
        bestFitness = fitness
        bestSolution = solution[:]

'

