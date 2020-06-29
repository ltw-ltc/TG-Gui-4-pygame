from tg_gui_4 import *
import pygame
from pygame.locals import *
from math import pi
import os

char_height = 28 + 1
char_width = 12

def init(width, height, x=500, y=50):
    global screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'
    pygame.init()
    # options # fonts = pygame.font.get_fonts()
    screen = pygame.display.set_mode((width, height))
    pygame.font.init()

update = pygame.display.update

def rgb_to_pygame(clr):
    #print('rgb_to_pygame clr type:', clr, type(clr))
    return ((clr >> 16) & 0xff), ((clr >> 8) & 0xff), ((clr >> 0) & 0xff)

_debug_clrs = [color_.orange, color_.yellow, color_.green, color_.white, color_.blue, color_.purple]

def roundrect(self, x, y, width, height, color, radius = 0, debug=False):
    #time.sleep(.25)
    if debug:
        inst = self
        pygame.draw.rect(screen, rgb_to_pygame(_debug_clrs[0]), (inst._phys_x - self.margin,
                            inst._phys_y - self.margin, inst._phys_width + self.margin*2,
                            inst._phys_height + self.margin*2), 0)
        _debug_clrs.append(_debug_clrs.pop(0))

    if radius >= 1:
        color = rgb_to_pygame(color)
        pygame.draw.rect(screen, color, (x+radius ,y,width-radius*2,height), 0)
        pygame.draw.rect(screen, color, (x ,y+radius,width,height-radius*2), 0)
        pygame.draw.circle(screen, color, (x+radius,y+radius), radius, 0)
        pygame.draw.circle(screen, color, (x+width-radius,y+radius), radius, 0)
        pygame.draw.circle(screen, color, (x+radius,y+height-radius), radius, 0)
        pygame.draw.circle(screen, color, (x+width-radius,y+height-radius), radius, 0)
    else:
        pygame.draw.rect(screen, rgb_to_pygame(color), (x, y, width, height), 0)
    #pygame.display.update()

def placetext(self, x, y, text, color = color_.white, background = color_.black,size = 1):
    color = rgb_to_pygame(color)
    background = rgb_to_pygame(background)
    for line in text.split('\n'):
        myfont = pygame.font.SysFont('couriernewttf', int(20*size))
        textsurface = myfont.render(line, False, color)
        screen.blit(textsurface,(x,y))
        y+= size*char_height
    #pygame.display.update()
    #pygame.event.get()

def centertext(self, x, y, text, color = color_.white, background = color_.black,size = 1):
    color = rgb_to_pygame(color)
    background = rgb_to_pygame(background)
    lines = text.split('\n')
    for line in lines:
        myfont = pygame.font.SysFont('couriernewttf', int(20*size))
        textsurface = myfont.render(line, False, color)
        #print(dir(textsurface))
        screen.blit(textsurface,(x - int(char_width*(len(line))/2)*size, y -  int(char_height*(len(lines)/4))*size ))
        y+= size*char_height
    #pygame.display.update()
    #pygame.event.get()
