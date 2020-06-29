import time
import random
import sys
import os
import json
import gc

sys.path.append(os.path.abspath('.'))

from . import _pygame_display
import pygame as _pygame
from pygame import locals as _locals

# import for tg_gui
import tg_gui_4 as _tg4
import tg_gui_4.backends.procedural as _tg4_std
from tg_gui_4 import hostviews as _hostviews
from tg_gui_4.control_interfaces import touchcontrol as _touchcontrol

# exports
from tg_gui_4 import *
from tg_gui_4.backends.procedural import *

_touchcontrol.init(_enable_edge_swipes=False)
_control_loop = _touchcontrol.loop

_debug = False

def _pickup_widget(inst, _debug=False):
    if isinstance(inst, (container)):
        print('picking up', inst)
        if _debug:
            _pygame_display .roundrect(inst, inst._phys_x ,inst._phys_y, inst._phys_width, inst._phys_height, color.purple, radius=0)
        else:
            _pygame_display .roundrect(inst, inst._phys_x ,inst._phys_y, inst._phys_width, inst._phys_height, color.black, radius=0)

_tg4.init(
            unit_base=150,
            unit_radius=0,
            port_pickup=_pickup_widget,
            font_size=1,
        )

_tg4_std.init(   rect=_pygame_display .roundrect,
                text=_pygame_display .placetext,
                centertext=_pygame_display .centertext,
                char_height=int(_pygame_display .char_height*1.25),
                char_width=int(_pygame_display .char_width*1.25),
            )


#pygame_display_update = _pygame_display .update
#pygame_event_get = _pygame.event.get
#pygame_mouse_get_pressed = _pygame.mouse.get_pressed
#pygame_mouse_get_pos = _pygame.mouse.get_pos



def by_id(item):
    return item._id

def _input_loop(root):
    should_loop = True

    while should_loop:

        for event in _pygame.event.get():
            if event.type == _pygame.KEYUP:
                if event.key == _locals.K_RIGHT:
                    nextables = action_types['nextview']
                    nextables.sort(key=by_id)
                    if len(nextables):
                        nextables[-1].nextview()
                elif event.key == K_LEFT:
                    prevables = action_types['priorview']
                    prevables.sort(key=by_id)
                    if len(prevables):
                        prevables[-1].priorview()

            elif event.type == _locals.QUIT:
                should_loop = False

        pointer_state = _pygame.mouse.get_pressed()[0]
        pointer_pos = _pygame.mouse.get_pos()

        if _debug:
            print(pointer_pos, pointer_state)
        _control_loop(pointer_pos, pointer_state, time.monotonic())

        _pygame_display.update()


def appwindow(width, height):
    assert isinstance(width, int), f"argument 'width' must be of type 'int', got type '{type(width).__name__}'"
    assert isinstance(height, int), f"argument 'height' must be of type 'int', got type '{type(height).__name__}'"
    _pygame_display.init(width, height)
    root_constructor= _hostviews.systemroot(width, height, x=0, y=0, place=True)
    def app_runner(cls):
        root = root_constructor(cls)
        _input_loop(root)
    return app_runner
