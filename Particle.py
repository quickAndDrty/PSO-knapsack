import numpy as np
import random
import math

class Particle():

    def __init__(self, position, velocity, fitness):
        self.position = position
        self.velocity = velocity
        self.fitness = fitness
        self.pBest = [0]*len(position)

    def sigmoid(self, value):
        return 1.0/(1.0 + math.exp((-1.0) * value))

    def updatePosition(self):

        for i in range(len(self.position)):
            rnd = random.random()
            if (rnd < self.sigmoid(self.velocity[i])):
                self.position[i] = 1
            else:
                self.position[i] = 0

    def updateVelocity(self, w, c1, c2, gBest):
        #print("gbest: ", gBest)
        cognitive = c1 * random.random() * (np.asarray(self.pBest) - np.asarray(self.position))
        social = c2 * random.random() * (np.asarray(gBest) - np.asarray(self.position))
        #print("pbest: ", self.pBest)
        #print("cognitive: ", cognitive)
        #print("social: ", social)
        self.velocity = w * np.asarray(self.velocity) + cognitive + social


    def updateFitness(self, f):
        self.fitness = f

    def updatePBest(self, p):
        self.pBest = p

    def getPosition(self):
        return self.position[:]

    def getPBest(self):
        return self.pBest[:]

    def getVelocity(self):
        return self.velocity[:]

    def getParticle(self):

        #print(string, "afiseaza ma")
        strPos = (', '.join(str(x) for x in self.position))
        strVelocity = (', '.join(str(x) for x in self.velocity))
        return ("position: " + strPos + " velocity: " + strVelocity + " fitness: "+ str(self.fitness))
