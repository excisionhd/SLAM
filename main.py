#!/usr/bin/env python

import cv2
import pygame
import sdl2

width = 1920//2
height = 1080//2


def process_frame(img):
    img = cv2.resize(img, (width, height))

    cv2.imshow('image',img)
    #window.refresh()

    #print(img.shape)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break