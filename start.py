from os import path
import pynput
import os
import re
import pygetwindow as gw
import time
import random
import numpy
import ctypes  # An included library with Python install.   
from pynput.keyboard import Key, Controller

def waitUntil():
    mustend = time.time() + 5 
    while time.time() < mustend:
        if gw.getActiveWindow().title in "RuneScape":
            return True
        time.sleep(1)
    return False

def remover(oldList):
    newList = ''.join([i for i in oldList if not i.isdigit() and i != "." and i != "\n"]) #remove dots, newlines, and digits
    return newList

def findSteps(oldList):
    steps = ["up", "right","left","down"] #the possible directions of arrow keys to press
    for step in steps: 
        inds = [i for i in range(len(oldList)) if oldList.startswith(step, i)] #get the starting indicies of each steps substring found in the step list
        loopCount = 0 #for offsetting when adding a space
        for x in inds: #for every step found
            oldList = oldList[:x + loopCount] + " " + oldList[x + loopCount:] #add a space before the steps starting index
            loopCount += 1 
    newList = oldList
    return newList

def main() :
    numerator = range(301, 489)
    denominator = range(501, 999)
    if path.exists('steps.txt'):
        movesText = open('steps.txt', 'r')
        moveList = findSteps(remover(movesText.read())) #send the text files contents to the functions that make it nice and neat
        movesText.close() 
        keyboard = Controller() 
        moveList = moveList.split(' ') #divide up moves from string into array
        print(moveList)
        count = 0
        for move in moveList: #start doing the steps
            numerator = range(301, 489)
            denominator = range(501, 999)
            try:
                while gw.getActiveWindow().title != "RuneScape": # wiat until we're focused on correct app
                    time.sleep(1)
            except Exception: #passes for when there isnt a focused window, happens when switching between windows
                pass
            time.sleep(random.choice(numerator)/random.choice(denominator)/10)
            if move.strip() in "up" and move.strip() != "":
                keyboard.press(Key.up)
                time.sleep(random.choice(numerator)/random.choice(denominator) / 2) #hold down for random amount of time
                keyboard.release(Key.up)

            if move.strip() in "down"  and move.strip() != "":
                keyboard.press(Key.down)
                time.sleep(random.choice(numerator)/random.choice(denominator) / 2)
                keyboard.release(Key.down)

            if move.strip() in "right" and move.strip() != "":
                keyboard.press(Key.right)
                time.sleep(random.choice(numerator)/random.choice(denominator) / 2)
                keyboard.release(Key.right)
                
            if move.strip() in "left" and move.strip() != "":
                keyboard.press(Key.left)
                time.sleep(random.choice(numerator)/random.choice(denominator) / 2)
                keyboard.release(Key.left)

            time.sleep(random.random() /10) #time between inputs
    else:
        ctypes.windll.user32.MessageBoxW(0, "File steps.txt doesn't exist!\nCreate a file named steps.txt in the /GitHub/SlideSolver/ directory", "Error!", 0)

if __name__ == "__main__":
    main()

