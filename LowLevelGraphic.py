#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 12:20:28 2025

@author: colecurtis.22
"""
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))

blue = (28, 30, 133)
gold = (255, 232, 20)
white = (255, 255, 255)
black = (0, 0, 0)

surface = pygame.Surface((600, 400))
surface.fill(white)

#P shape
pygame.draw.rect(surface, blue, (120, 100, 180, 400))
pygame.draw.circle(surface, blue, (300, 200), 100)

#gold ball
pygame.draw.circle(surface, gold, (320, 200), 60)

#lines around ball
pygame.draw.circle(surface, black, (320, 200), 60, 3)
pygame.draw.line(surface, black, (260, 200), (380, 200), 3)
pygame.draw.line(surface, black, (320, 140), (320, 260), 3)

#lines coming off of ball
pygame.draw.line(surface, gold, (140, 180), (260, 160), 6)
pygame.draw.line(surface, gold, (140, 210), (260, 190), 6)
pygame.draw.line(surface, gold, (140, 240), (260, 220), 6)

screen.blit(surface, (0, 0))
pygame.display.flip()

