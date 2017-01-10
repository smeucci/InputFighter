import subprocess
import time, os, sys
import keycodes
import pygame
import autopy.key as auto
import Image
import gtk.gdk


# Toggle keyDown property for selected keys
def input(flags):
    keys = keycodes.AUTOPYKEYS
    for k, f in zip(keys, flags):
        if f == 1: auto.toggle(k, True)
        else: auto.toggle(k, False)

# Parse txt file containing list of 0-1 values as inputs
def parse(fid):
    with open(fid, "r") as f:
        lines = f.read().splitlines()
    inputs = []
    for line in lines:
        line = line.replace("[", "").replace("]", "")
        input = [int(x.strip()) for x in line.split(",")] # TODO convert int to bool
        inputs.append(input)
    return inputs

# Take a screenshot, if dir is not None save on disk, otherwise return the image
def screenshot(dir, index, width, height, offset_x=0, offset_y=0):
    try:
        im = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, width, height)
        im.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(),
                             offset_x, offset_y, 0, 0, width, height)
    except:
        sys.exit(0)
    final_im = Image.frombuffer("RGB", (width, height), im.get_pixels(),
                                "raw", "RGB", im.get_rowstride(), 1)
    if dir != None: final_im.save(dir + "frame-" + str(index) + ".jpg")
    else: return final_im


###################
# Setup functions #
###################

def setup_send():
    dir = os.path.dirname(os.path.abspath(__file__))
    return parse(dir + "/../data/cpu.txt")

def setup_read():
    fightstick = Hori()
    dir = os.path.dirname(os.path.abspath(__file__))
    outfile = open(dir + "/../data/inputs.txt", "w")
    return fightstick, outfile, 1

def setup_screenshots():
    dir = os.path.dirname(os.path.abspath(__file__))
    imgdir = dir + "/../data/img/"
    if not os.path.exists(imgdir): os.makedirs(imgdir)
    start = time.time()
    return imgdir, start, 1

def setup(name):
    switch = {
        'send': setup_send,
        'read': setup_read,
        'screenshots': setup_screenshots
    }
    return switch.get(name)()


##############
# Classifier #
##############

def predict_fake(frame):
    return [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


###########
# Objects #
###########

class Hori:
    def __init__(self):
        try:
            pygame.init()
            self.fightstick = pygame.joystick.Joystick(0)
            self.fightstick.init()
        except:
            print "unable to connect to Hori"
            sys.exit(0)

    def read(self):
        pygame.event.pump()
        # Directions
        up, down, left, right = [0, 0, 0, 0]
        hat = self.fightstick.get_hat(0)
        if hat[0] == 1: right = 1
        elif hat[0] == -1: left = 1
        if hat[1] == 1: up = 1
        elif hat[1] == -1: down = 1
        # Punches
        lp = self.fightstick.get_button(keycodes.LP)
        mp = self.fightstick.get_button(keycodes.MP)
        hp = self.fightstick.get_button(keycodes.HP)
        # Kicks
        lk = self.fightstick.get_button(keycodes.LK)
        mk = self.fightstick.get_button(keycodes.MK)
        hk = self.fightstick.get_button(keycodes.HK)
        # Return
        return [up, down, left, right, lp, mp, hp, lk, mk, hk]
