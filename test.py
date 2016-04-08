from raspirobotboard import *

import sys
import pygame

rr = RaspiRobot()

pygame.init()
screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('RaspiRobot')
pygame.mouse.set_visible(0)

state = None

blink_state = 1

timer = 0


def reverse():
    global state
    state = "reverse"
    rr.set_led1(1)
    rr.set_led2(1)
    rr.forward()


def forward():
    global state
    state = "forward"
    rr.set_led1(0)
    rr.set_led2(0)
    rr.reverse()


def right():
    global state
    state = "right"
    rr.set_led1(0)
    rr.set_led2(1)
    rr.left()


def left():
    global state
    state = "left"
    rr.set_led1(1)
    rr.set_led2(0)
    rr.right()


def stop():
    global state
    state = "stopped"
    rr.stop()
    rr.set_led1(0)
    rr.set_led2(0)


def blinkleds():
    global blink_state
    blink_state = not blink_state
    rr.set_led1(blink_state)
    rr.set_led2(blink_state)


def execute_state():
    global timer
    timer += 1

    if state == "reverse":
        if timer % 5000 == 0:
            blinkleds()

        if timer > 10000:
            timer = 0

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    forward()
                elif event.key == pygame.K_DOWN:
                    reverse()
                elif event.key == pygame.K_RIGHT:
                    right()
                elif event.key == pygame.K_LEFT:
                    left()
                elif event.key == pygame.K_SPACE:
                    stop()

        execute_state()

    except KeyboardInterrupt:
        print("Control C Received!")
        rr.stop()
        sys.exit(1)
