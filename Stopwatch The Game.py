# from __future__ import division
try:
    import simplegui
except ImportError:
    import simpleguics2pygame as simplegui

    
# ================================ my code ================================

# "Stopwatch: The Game"

# define global variables
total_ticks = 0
successful_stops = 0
total_stops = 0
interval_ticks = 10 # manage to stop the watch on 5s
#stop_ticks = None # record the time that user have stopped the watch
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    seconds = t / 10 % 60
    minutes = t / 10 / 60
    
    if(seconds < 10):   seconds_text = '0' + str(seconds)
    else:               seconds_text = str(seconds)
    
    return str(minutes) + ':' + seconds_text + '.' + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_btn_handler():
    global is_running
    is_running = True
    timer.start()

def stop_btn_handler():
    global total_ticks, interval_ticks, total_stops, successful_stops, is_running
    timer.stop()
    #print 'total_ticks =', total_ticks
    if(is_running):
        total_stops = total_stops + 1
        if(total_ticks % interval_ticks == 0):
            successful_stops = successful_stops + 1
    is_running = False
    
def reset_btn_handler():
    global total_ticks, successful_stops, total_stops, is_running
    timer.stop()
    total_ticks = 0
    successful_stops = 0
    total_stops = 0
    is_running = False

# define event handler for timer with 0.1 sec interval
def tick():
    global total_ticks
    total_ticks = total_ticks + 1

# define draw handler
def draw_handler(canvas):
    global total_ticks, total_stops, successful_stops
    canvas.draw_text(format(total_ticks), (45, 90), 40, 'White')
    canvas.draw_text(str(successful_stops)+'/'+str(total_stops), (150, 30), 25, 'Red')
    
# create frame
timer = simplegui.create_timer(100, tick)
frame = simplegui.create_frame("Stopwatch", 200, 150)
frame.set_draw_handler(draw_handler)

# register event handlers
frame.add_button('Start', start_btn_handler, 100)
frame.add_button('Stop', stop_btn_handler, 100)
frame.add_button('Reset', reset_btn_handler, 100)

# start frame
frame.start()
