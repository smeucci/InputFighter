import sys, os, time
from utils import *
import pygame
import inspect

# Emulate keyboard inputs
def send():
    clock = pygame.time.Clock()
    inputs = setup("send")
    wait(2)
    for i in inputs:
        input(i)
        clock.tick(60)

# Read inputs from Hori fightstick
def read():
    clock = pygame.time.Clock()
    fightstick, outfile, i = setup("read")
    while True:
        inputs = fightstick.read()
        print inputs, i
        outfile.write(str(inputs) + "\n")
        clock.tick(60)
        i += 1

# Take screenshots at 60 fps
def screenshots(sec=1):
    clock = pygame.time.Clock()
    imgdir, start, i = setup("screenshots")
    while time.time() < start + sec:
        screenshot(imgdir, i, 641, 480, 1, 55)
        clock.tick(60)
        i += 1
    print "Screenshots: " + str(i - 1)

# Read inputs and take screenshots to build training set
def capture(sec=10):
    clock = pygame.time.Clock()
    fightstick, outfile, j = setup("read")
    imgdir, start, i = setup("screenshots")
    while time.time() < start + sec:
        inputs = fightstick.read()
        screenshot(imgdir, i, 641, 480, 1, 55)
        outfile.write(str(inputs) + "\n")
        print inputs, j
        clock.tick(60)
        i += 1; j += 1

# Take screenshots, for each frame predict the action and emulate the inputs
def cpu():
    clock = pygame.time.Clock()
    _, start, i = setup("screenshots")
    while time.time() < start + 10:
        # take frame
        frame = screenshot(None, i, 641, 480, 1, 55).getdata()
        # predict frame inputs
        inputs = predict_fake(frame)
        # input
        input(inputs)
        i += 1
        clock.tick(60)

# Main
def main():
    args = sys.argv
    if len(args) <= 1:
        print "No argument provided"
        sys.exit(0)

    if args[1] == "--read":
        read()
    elif args[1] == "--send":
        send()
    elif args[1] == "--screenshots":
        sec = int(args[2]) if len(args) > 2 else 1
        screenshots(sec)
    elif args[1] == "--capture":
        sec = int(args[2]) if len(args) > 2 else 10
        capture(sec)
    elif args[1] == "--cpu":
        cpu()
    else:
        print "Wrong argument provided.\n"
        sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
