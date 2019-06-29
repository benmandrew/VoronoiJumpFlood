import numpy as np
from PIL import Image
from random import randint, uniform
import math
import time

from ball import Ball

class JFA:

    def __init__(self, size):
        self.size = size
        self.maxSteps = math.floor(math.log(size, 2) + 1)
        self.texture = np.array(
            [[[-1, -1]] * size] * size,
            np.int32)
        self.outTexture = np.array(
            [[[0, 0, 0]] * size] * size,
            np.uint8)
        self.colourDict = dict()

    def seed(self, balls):
        for ball in balls:
            pos = ball.getIntPos()
            self.texture[pos[0], pos[1]] = pos
            self.colourDict[tuple(pos)] = ball.colour

    def stepJFA(self, coord, stepWidth):
        bestDist = 9999.0
        bestCoord = np.array([-1, -1], np.int32)
        bestColour = np.array([0, 0, 0], np.int8)

        for y in range(-1, 2):
            for x in range(-1, 2):
                sampleCoord = coord + np.array([x, y]) * stepWidth
                if not (0 <= sampleCoord[0] < self.size and 0 <= sampleCoord[1] < self.size):
                    continue
                seedCoord = self.texture[sampleCoord[0], sampleCoord[1]]

                if tuple(seedCoord) in self.colourDict:

                    dist = np.linalg.norm(seedCoord - coord)

                    if (seedCoord[0] != -1 or seedCoord[1] != -1) and dist < bestDist:
                        bestDist = dist
                        bestCoord = seedCoord
                        bestColour = self.colourDict[tuple(seedCoord)]

        return bestCoord, bestColour

    def levelJFA(self, level):
        stepWidth = math.floor(pow(2, self.maxSteps - level - 1) + 0.5)
        for y in range(self.size):
            for x in range(self.size):
                self.texture[x, y], self.outTexture[x, y] = self.stepJFA(np.array([x, y]), stepWidth)

    def JFA(self):
        for level in range(self.maxSteps):
            self.levelJFA(level)

    def render(self, balls, index):
        self.seed(balls)
        self.JFA()
        im = Image.fromarray(self.outTexture)
        im.save(getFilename(index))

def getFilename(index):
    idxStr = str(index + 1)
    while len(idxStr) < 3:
        idxStr = "0" + idxStr
    return "img{}.png".format(idxStr)


















