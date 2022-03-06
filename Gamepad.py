##!/usr/bin/env python

# pip install pygame

import pygame
from pygame.locals import *
import sys

# size of window
SCREEN_WIDTH = 350
SCREEN_HEIGHT = 250
SPEED = 1.0

class JoyStatus:
    def __init__(self):
        self.axLx = 0
        self.axLy = 0
        self.axRx = 0
        self.axRy = 0
        self.hatL = 0
        self.hatR = 0
        self.hatU = 0
        self.hatD = 0
        self.btn = [0,0,0,0,0,0,0,0,0,0,0,0]

class Position:
    def __init__(self):
        self.clear()
    def clear(self):
        self.lx = 0.0
        self.ly = 0.0
        self.lz = 0.0
        self.rx = 0.0
        self.ry = 0.0
        self.rz = 0.0

JStat = JoyStatus()
Pos = Position()

#Initialize JOYSTICK
pygame.joystick.init()
try:
    joy = pygame.joystick.Joystick(0)
    #joy.init()
    print("Number of Button : " + str(joy.get_numbuttons()))
    print("Number of Axis : " + str(joy.get_numaxes()))
    print("Number of Hats : " + str(joy.get_numhats()))
except pygame.error:
    print("Joystick is not found")
    sys.exit()

#
# main
#
def main():
    # create window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('JOYSTICK')
    pygame.display.flip()

    while True:
        #event
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        
        JStat.axLx = joy.get_axis(0)
        JStat.axLy = joy.get_axis(1)
        JStat.axRx = joy.get_axis(2)
        JStat.axRy = joy.get_axis(3)
        
        ShowPad(screen)

        if joy.get_button(8) == 1:
            print("BACK button")

        if joy.get_button(9) == 1:
            print("START button")

        pygame.time.wait(10)

    return

def ShowPad(screen):
    font = pygame.font.Font(None, 18)

    # Value of Joystick
    Pos.lx = int((JStat.axLx+1) * 20 + 100)     #LeftStickX -1...+1
    Pos.ly = int((JStat.axLy+1) * 20 + 150)     #LeftStickY
    Pos.rx = int((JStat.axRx+1) * 20 + 200)     #RightStickX
    Pos.ry = int((JStat.axRy+1) * 20 + 150)     #RightStickY

    # HatSwitch (cross-key)
    hat_input = joy.get_hat(0)

    if hat_input[0] < 0:
        JStat.hatL = 0
        JStat.hatR = 1
    elif hat_input[0] > 0:
        JStat.hatL = 1
        JStat.hatR = 0
    else:
        JStat.hatL = 1
        JStat.hatR = 1

    if hat_input[1] < 0:
        JStat.hatD = 0
        JStat.hatU = 1
    elif hat_input[1] > 0:
        JStat.hatD = 1
        JStat.hatU = 0
    else:
        JStat.hatD = 1
        JStat.hatU = 1

    for i in range(12):
        if joy.get_button(i) == 1:
            JStat.btn[i] = 0
        else:
            JStat.btn[i] = 1


    # refresh window
    screen.fill((0,40,0))

    pygame.draw.circle(screen, (255,255,255), (120,170), 40, JStat.btn[10])
    pygame.draw.circle(screen, (255,255,255), (220,170), 40, JStat.btn[11])
    pygame.draw.circle(screen, (0,255,0), (Pos.lx, Pos.ly), 5)
    pygame.draw.circle(screen, (0,255,0), (Pos.rx, Pos.ry), 5)

    pygame.draw.rect(screen, (255,255,255), Rect(30,100,15,15), JStat.hatL)
    pygame.draw.rect(screen, (255,255,255), Rect(70,100,15,15), JStat.hatR)
    pygame.draw.rect(screen, (255,255,255), Rect(50,80,15,15), JStat.hatU)
    pygame.draw.rect(screen, (255,255,255), Rect(50,120,15,15), JStat.hatD)

    pygame.draw.rect(screen, (255,255,255), Rect(250,100,15,15), JStat.btn[0])    #X
    pygame.draw.rect(screen, (255,255,255), Rect(270,120,15,15), JStat.btn[1])    #A
    pygame.draw.rect(screen, (255,255,255), Rect(290,100,15,15), JStat.btn[2])    #B
    pygame.draw.rect(screen, (255,255,255), Rect(270,80,15,15), JStat.btn[3])    #Y

    pygame.draw.rect(screen, (255,255,255), Rect(30,50,50,15), JStat.btn[4])    #L1
    pygame.draw.rect(screen, (255,255,255), Rect(250,50,50,15), JStat.btn[5])   #L2
    pygame.draw.rect(screen, (255,255,255), Rect(30,30,50,15), JStat.btn[6])    #R1
    pygame.draw.rect(screen, (255,255,255), Rect(250,30,50,15), JStat.btn[7])   #R2

    pygame.draw.rect(screen, (255,255,255), Rect(120,80,20,15), JStat.btn[8])    #Back
    pygame.draw.rect(screen, (255,255,255), Rect(200,80,20,15), JStat.btn[9])    #Start

    #Show value
    text = font.render("X: {:.3f}".format(JStat.axLx), True, (255,255,255))
    screen.blit(text, [10,180])
    text = font.render("Y: {:.3f}".format(JStat.axLy), True, (255,255,255))
    screen.blit(text, [10,200])
    text = font.render("Rx: {:.3f}".format(JStat.axRx), True, (255,255,255))
    screen.blit(text, [270,180])
    text = font.render("Ry: {:.3f}".format(JStat.axRy), True, (255,255,255))
    screen.blit(text, [270,200])

    pygame.display.update()


if __name__ == '__main__':
    main()
