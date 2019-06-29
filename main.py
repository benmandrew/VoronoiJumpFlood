import numpy as np
from random import randint, uniform
from ball import Ball
from jump import JFA
import time
import datetime

import subprocess as sp
import os
import shlex

frameRate = 24
nFrames = frameRate * 10
nBalls = 50
size = 640
balls = list()

root = "C:\\Users\\Mirrorworld\\Desktop\\VJF\\"

class Bounds:
    minBound = np.array([0, 0], np.float32)
    maxBound = np.array([size - 1, size - 1], np.float32)

def spawnBalls():
    for i in range(nBalls):
        pos = np.array(
            [uniform(0, size - 1),
             uniform(0, size - 1)],
            np.float32)
        vel = np.array(
            [uniform(-0.7, 0.7),
             uniform(-0.7, 0.7)],
            np.float32)
        colour = np.array(
           [randint(0, 255),
            randint(0, 255),
            randint(0, 255)],
            np.uint8)
        balls.append(Ball(pos, vel, colour))

def predictTime(elapsed, index):
    timePerBall = elapsed / index
    return round(timePerBall * (nFrames - index), 1)

def getIdxStr(index):
    idxStr = str(index)
    while len(idxStr) < 3:
        idxStr = "0" + idxStr
    return "img{}.png".format(idxStr)

def deleteImages():
    for i in range(nFrames):
        os.remove(getIdxStr(i + 1))

def getOutFileName():
    return datetime.date.today().strftime("%Y-%m-%d %H-%M-%S") + ".mp4"

def main():

    spawnBalls()

    start = time.time()

    for i in range(nFrames):
        print("Frame {}/{}".format(i + 1, nFrames))
        jfa = JFA(size)

        frameStart = time.time()
        jfa.render(balls, i)
        print("Frame time    : {}".format(round(time.time() - frameStart, 1)))
        print("Predicted time: {}".format(predictTime(time.time() - start, i + 1)))
        print()

        for ball in balls:
            ball.move(Bounds)

    print("TOTAL TIME: {}".format(time.time() - start))

    saveCommand  = "ffmpeg -framerate {} -i img%03d.png \"{}\"".format(frameRate, getOutFileName())
    sp.check_call(shlex.split(saveCommand))

    #deleteImages()




if __name__ == "__main__":
    main()
















