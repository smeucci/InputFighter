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
            clock.tick(20)
        except KeyboardInterrupt:
            sys.exit(0)

def send():
    utils.wait(2)
    utils.input([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
    utils.input([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    utils.input([0, 1, 1, 0, 0, 0, 0, 0, 0, 0])
    utils.input([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    utils.input([0, 1, 0, 1, 0, 0, 0, 0, 0, 0])
    utils.input([0, 0, 0, 1, 0, 0, 0, 1, 1, 0])
    utils.input([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1)
    utils.input([0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    utils.input([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    utils.input([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    utils.input([0, 1, 0, 1, 0, 0, 1, 0, 0, 0])
    utils.input([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

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
