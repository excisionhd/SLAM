#!/usr/bin/env python3

import cv2
import sdl2
import sdl2.ext

class Display(object, self):
    def __init__():
        self.W, self.H = W, H
        self.window = sdl2.ext.Window("SLAM", size=(W,H), position=(100,100))
        self.window.show()

    def draw(img):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)

        surf = sdl2.ext.pixels3d(window.get_surface())
        surf[:] = img[:,:]
        window.refresh()