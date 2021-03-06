#!/usr/bin/env python3

import cv2
import sdl2
import sdl2.ext
sdl2.ext.init()

W = 1920//2
H = 1080//2


window.show()

class Display(object):
    def __init__():
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


def process_frame(img):
    img = cv2.resize(img, (W, H))

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break