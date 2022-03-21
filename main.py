import pygame as pg
from pygame_menu import Theme, Menu, events, sound

from functions import run
from classes import *
from constants import *

pg.init()

win = pg.display.set_mode(WIN_SIZE)
pg.display.set_caption('Pong')


theme = Theme(
    # general
    selection_color = OBJ_COLOR,
    # title
    title = True,
    title_font = STANDARD_FONT,
    title_font_color = BACKGROUND_COLOR,
    title_background_color = OBJ_COLOR,
    # background
    background_color = BACKGROUND_COLOR,
    # widget
    widget_font = STANDARD_FONT,
    widget_font_color = OBJ_COLOR
)

engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION, '.\sounds\defend.wav')

menu = Menu('Pong', WIN_SIZE[0], WIN_SIZE[1], theme=theme)
menu.set_sound(engine)

# menu.add.image('.\images\snake.gif')
menu.add.vertical_margin(100)
menu.add.button('Play', run, win)
menu.add.button('Quit', events.EXIT)
menu.add.vertical_margin(20)
menu.add.label('Arrow Keys to move:\n◄▲▼►')
menu.add.vertical_margin(200)
menu.add.label('by: LucasGoncSilva')

menu.mainloop(win)