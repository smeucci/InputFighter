import sys, os, time
import utils
import pygame
import inspect


def read():
    fightstick = utils.Hori()
    clock = pygame.time.Clock()
    dir = os.path.dirname(os.path.abspath(__file__))
    outfile = open(dir + "/../data/inputs.txt", "w")
    while True:
        try:
            inputs = fightstick.read()
            print inputs
            outfile.write(str(inputs) + "\n")
            clock.tick(60)
        except KeyboardInterrupt:
            sys.exit(0)

def send():
    clock = pygame.time.Clock()
    dir = os.path.dirname(os.path.abspath(__file__))
    inputs = utils.parse(dir + "/../data/inputs.txt")
    utils.wait(2)
    for i in inputs:
        utils.input(i)
        clock.tick(60)

def capture():
    clock = pygame.time.Clock()
    dir = os.path.dirname(os.path.abspath(__file__))
    imgdir = dir + "/../data/img/"
    if not os.path.exists(imgdir): os.makedirs(imgdir)
    timeout_start, timeout, i = time.time(), 1, 1
    while time.time() < timeout_start + timeout:
        try:
            utils.screenshot(imgdir, i, 641, 480, 1, 55)
            clock.tick(60)
            i += 1
        except KeyboardInterrupt:
            break
    print "Screenshots: " + str(i)

def main():
    args = sys.argv
    if len(args) <= 1:
        print "No argument provided"
        sys.exit(0)

    if args[1] == "--read":
        read()
    elif args[1] == "--send":
        send()
    elif args[1] == "--capture":
        capture()
    else:
        print "Wrong argument provided.\n"
        sys.exit(0)

if __name__ == "__main__":
    main()
