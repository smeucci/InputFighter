import sys, os, time
from utils import *
import pygame
import inspect


def send():
    clock = pygame.time.Clock()
    inputs = setup("send")
    wait(2)
    for i in inputs:
        input(i)
        clock.tick(60)

def read():
    clock = pygame.time.Clock()
    fightstick, outfile, i = setup("read")
    while True:
        inputs = fightstick.read()
        print inputs, i
        outfile.write(str(inputs) + "\n")
        clock.tick(60)
        i += 1

def screenshots(sec=1):
    clock = pygame.time.Clock()
    imgdir, start, i = setup("screenshots")
    while time.time() < start + sec:
        screenshot(imgdir, i, 641, 480, 1, 55)
        clock.tick(60)
        i += 1
    print "Screenshots: " + str(i)

def capture(sec=10):
    clock = pygame.time.Clock()
    imgdir, start, i = setup("screenshots")
    fightstick, outfile, j = setup("read")
    while time.time() < start + sec:
        inputs = fightstick.read()
        screenshot(imgdir, i, 641, 480, 1, 55)
        outfile.write(str(inputs) + "\n")
        print inputs, j
        clock.tick(60)
        i += 1; j += 1

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
    else:
        print "Wrong argument provided.\n"
        sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
