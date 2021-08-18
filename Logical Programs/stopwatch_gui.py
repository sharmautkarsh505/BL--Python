"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 18:30:00
Last Modified by:---
Last Modified time:----
Title : Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
"""
#learn how to implement with tklinter,as it is an inbuilt fucntion

import pygame
import pygame.freetype

def main():
    pygame.init()
    screen=pygame.display.set_mode((300, 300))
    clock=pygame.time.Clock()
    font=pygame.freetype.SysFont(None, 34)
    font.origin=True
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return
        screen.fill(pygame.Color('grey'))
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        font.render_to(screen, (100, 100), out, pygame.Color('black'))
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__': main()