import sys, os
import utils
import pygame
import inspect


def read():
    fightstick = utils.Hori()
    clock = pygame.time.Clock()
    dir = os.path.dirname(os.path.abspath(__file__))
    outfile = open(dir + "/../data/inputs.txt", "w")
    while(1):
        try:
            inputs = fightstick.read()
            print inputs
            outfile.write(str(inputs) + "\n")
            clock.tick(120)
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

def main():
    args = sys.argv
    if len(args) <= 1:
        print "No argument provided"
        sys.exit(0)

    if args[1] == "--read":
        read()
    elif args[1] == "--send":
        send()
    else:
        print "Wrong argument provided.\n"
        sys.exit(0)

if __name__ == "__main__":
    main()
