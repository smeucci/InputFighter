import subprocess
import time
import keycodes
import pygame

def wait(sec):
    time.sleep(sec)

def command(flags):
    cmd = ""
    keys = keycodes.KEYS
    for k, f in zip(keys, flags):
        cmd += "xsendkeycode " + str(k) + " " + str(f) + "; "
    return cmd

def input(flags, time=0.05):
    cmd = command(flags)
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    wait(time)

class Hori:
    def __init__(self):
        try:
            pygame.init()
            self.fightstick = pygame.joystick.Joystick(0)
            self.fightstick.init()
        except:
            print "unable to connect to Hori"

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

        return [up, down, left, right, lp, mp, hp, lk, mk, hk]
