##!/usr/bin/env python

# pip install pygame

from turtle import pos
import pygame
from pygame.locals import *
import time
import sys
import struct
import socket

#import ModbusTCP
#import TcpClient

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
BasePos = Position()
RelativePos = Position()

#Initialize JOYSTICK
pygame.joystick.init()
try:
    joy = pygame.joystick.Joystick(0)
    joy.init()
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

        Pos.lx = joy.get_axis(0)
        Pos.ly = joy.get_axis(1)
        Pos.rx = joy.get_axis(2)
        Pos.ry = joy.get_axis(3)

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
    JStat.axLx = int((joy.get_axis(0)+1) * 20 + 100)     #LeftStickX -1...+1
    JStat.axLy = int((joy.get_axis(1)+1) * 20 + 150)     #LeftStickY
    JStat.axRx = int((joy.get_axis(2)+1) * 20 + 200)     #RightStickX
    JStat.axRy = int((joy.get_axis(3)+1) * 20 + 150)     #RightStickY

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
    pygame.draw.circle(screen, (0,255,0), (JStat.axLx, JStat.axLy), 5)
    pygame.draw.circle(screen, (0,255,0), (JStat.axRx, JStat.axRy), 5)

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
    text = font.render("X: {:.3f}".format(Pos.lx), True, (255,255,255))
    screen.blit(text, [10,180])
    text = font.render("Y: {:.3f}".format(Pos.ly), True, (255,255,255))
    screen.blit(text, [10,200])
    text = font.render("Rx: {:.3f}".format(Pos.rx), True, (255,255,255))
    screen.blit(text, [270,180])
    text = font.render("Ry: {:.3f}".format(Pos.ry), True, (255,255,255))
    screen.blit(text, [270,200])

    pygame.display.update()


if __name__ == '__main__':
    main()
