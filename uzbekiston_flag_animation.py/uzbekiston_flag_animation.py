#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:37:30 2023

@author: umidjon
"""

import pygame
import sys

# Pygame o'yinini boshlash
pygame.init()

# O'yin oynasining hajmi
WIDTH, HEIGHT = 1000, 800

# Qora rang
BLACK = (4, 4, 8)

# O'yin oynasini yaratish
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("O'yin")

# Yer rasmi
floor_img = pygame.image.load("Twiter.png")
floor_img = pygame.transform.scale(floor_img, (WIDTH, HEIGHT))

# Qo'lda yerga tushgan nuktani ko'rsatadigan rasmi
dot_img = pygame.Surface((40, 40))
pygame.draw.circle(dot_img, (255, 0, 0), (30, 30), 30)

# Nuktaning x va y koordinatalari
dot_x, dot_y = WIDTH // 2, HEIGHT // 2

# Pygame taymeri
clock = pygame.time.Clock()

# O'yin asosiy tsikli
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Nuktani yangi koordinataga o'zgartirish
    dot_x += 1
    dot_y += 1

    # Ekranni tozalash
    screen.fill(BLACK)

    # Yer rasmini ekranga chizish
    screen.blit(floor_img, (0, 0))

    # Nuktani ekranga chizish
    screen.blit(dot_img, (dot_x, dot_y))

    # Ekran yangilanishini ko'rsatish
    pygame.display.update()

    # FPS (keyingi kadrlar soni) ni sozlash
    clock.tick(60)
