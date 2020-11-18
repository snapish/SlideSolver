from os import path
import pynput
import os
import re
import pygetwindow as gw
import time
import random
import numpy
import ctypes  # An included library with Python install.
import clipboard
from pynput.keyboard import Key, Controller


def waitUntil():
    mustend = time.time() + 5
    while time.time() < mustend:
        if gw.getActiveWindow().title in "RuneScape":
            return True
        time.sleep(1)
    return False


def remover(oldList):
    newList = ''.join([i for i in oldList if not i.isdigit() and i != "." and i != "\n" and i !="\r"])  # remove dots, newlines, and digits
    return newList

def findSteps(oldList):
    # the possible directions of arrow keys to press
    steps = ["up", "right", "left", "down"]
    for step in steps:
        # get the starting indicies of each steps substring found in the step list
        inds = [i for i in range(len(oldList)) if oldList.startswith(step, i)]
        loopCount = 0  # for offsetting when adding a space
        for x in inds:  # for every step found
            # add a space before the steps starting index
            oldList = oldList[:x + loopCount] + " " + oldList[x + loopCount:]
            loopCount += 1
    newList = oldList
    return newList


def main():
    numerator = range(301, 489)
    denominator = range(501, 999)
    movesText = clipboard.paste()
    moveList = findSteps(remover(movesText))# send the text files contents to the functions that make it nice and neat
    keyboard = Controller()
    # divide up moves from string into array
    moveList = moveList.strip().split(' ')
    print(moveList)
    for index, move in enumerate(moveList):  # start doing the steps
        numerator = range(301, 489)
        denominator = range(501, 999)
        try:
            while gw.getActiveWindow().title != "RuneScape":  # wiat until we're focused on correct app
                time.sleep(1)
        except Exception:  # passes for when there isnt a focused window, happens when switching between windows
            pass

        time.sleep(random.choice(numerator)/random.choice(denominator)/13)
        if move.strip() in "up" and move.strip() != "":
            keyboard.press(Key.up)    # hold down for random amount of time
            time.sleep(random.choice(numerator) /random.choice(denominator) /2)
            keyboard.release(Key.up)
        if move.strip() in "down" and move.strip() != "":
            keyboard.press(Key.down)
            time.sleep(random.choice(numerator) /random.choice(denominator) /2)
            keyboard.release(Key.down)
        if move.strip() in "right" and move.strip() != "":
            keyboard.press(Key.right)
            time.sleep(random.choice(numerator) /random.choice(denominator) /2)
            keyboard.release(Key.right)
        if move.strip() in "left" and move.strip() != "":
            keyboard.press(Key.left)
            time.sleep(random.choice(numerator) /random.choice(denominator) /2)
            keyboard.release(Key.left)
        time.sleep(random.random() / 13)  # time between inputs

if __name__ == "__main__":
    main()
