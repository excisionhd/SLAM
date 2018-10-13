#!/usr/bin/env python

import cv2
import pygame

width = 1920//2
height = 1080//2

screen = pygame.display.set_mode((width, height))

def process_frame(img):
    img = cv2.resize(img, (1920//2, 1080//2))
    cv2.imshow('image', img)
    cv2.waitKey(0)
    print(img.shape)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break