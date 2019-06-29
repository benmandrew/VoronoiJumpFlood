import numpy as np



class Ball:
    def __init__(self, pos, vel, colour):
        self.pos = pos
        self.vel = vel
        self.colour = colour

    def move(self, bounds):
        self.pos = self.pos + self.vel
        if self.pos[0] < bounds.minBound[0]:
            self.pos[0] = bounds.minBound[0]
            self.vel[0] *= -1
        elif self.pos[0] > bounds.maxBound[0]:
            self.pos[0] = bounds.maxBound[0]
            self.vel[0] *= -1

        if self.pos[1] < bounds.minBound[1]:
            self.pos[1] = bounds.minBound[1]
            self.vel[1] *= -1
        elif self.pos[1] > bounds.maxBound[1]:
            self.pos[1] = bounds.maxBound[1]
            self.vel[1] *= -1

    def getIntPos(self):
        return self.pos.astype('int32')
