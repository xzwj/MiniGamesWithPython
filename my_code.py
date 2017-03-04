# from __future__ import division
try:
    import simplegui
except ImportError:
    import simpleguics2pygame as simplegui

    
# ================================ my code ================================

import math

polyline = []


# define mouseclick handler
def click(pos):
    global polyline
    print pos
    polyline.append(pos)
          
# button to clear canvas
def clear():
    global polyline
    polyline = []

# define draw
def draw(canvas):
    global polyline
    i = 0
    while i < len(polyline) - 1:
        canvas.draw_line(polyline[i], polyline[i+1], 1, 'White')
                   
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()

