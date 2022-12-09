# mauseClickMakro and helps creating mauseClickMakro (source at the beginning

# mouse coordinates
from Xlib import X, display # import the necessary classes from the specified module
d = display.Display().screen().root.query_pointer() # get pointer location
x = str(d.root_x) # get x coord and convert to string
y = str(d.root_y) # get y coord and convert to string

x1 = d.root_x + 500
y1 = d.root_y + 500
mouse.click_absolute(x1 , y1, 1) 
c = "mouse.click_absolute(" + x + " ," + y + " , 1)\n"
clipboard.fill_clipboard(c)
# dialog.info_dialog(msg, x+", "+y) # create an info dialog to display the coordinates


# exit(1)

###############
# https://wildfiregames.com/forum/topic/101192-mouseclick-makro-to-set-game-defaults/
# try the recordet clicks in same script helps my very much testing it at same time:

mouse.click_absolute(2619 ,644 , 1) # click out somewhere

# set britains
mouse.click_absolute(2869 ,86 , 1)
keyboard.send_keys("b") # britains
# mouse.click_absolute(2843 ,162 , 1) # britains

# set map type random, mainland
mouse.click_absolute(3316 ,362 , 1) # map type
mouse.click_absolute(3370 ,413 , 1) # select random
time.sleep(.2)
mouse.click_absolute(2619 ,644 , 1) # click out somewhere

# exit(1) # work to hera in 1. local single game and in 2. lobby new game


# mouse.click_absolute(3361 ,415 , 1) # select map
mouse.click_absolute(3364 ,432 , 1) # select map
time.sleep(.1)
keyboard.send_keys("m") # next is maybe balanced
keyboard.send_keys("<enter>") 
mouse.click_absolute(2619 ,644 , 1) # click out somewhere

# exit(1) # work to hera in 1. local single game and in 2. lobby new game

# map size small
mouse.click_absolute(3352 ,509 , 1)
mouse.click_absolute(3382 ,558 , 1)

# disable treasures
time.sleep(.4)
mouse.click_absolute(3245 ,613 , 1) # sometimes maybe not work 
# mouse.click_absolute(3246 ,615 , 1)

mouse.click_absolute(3245 ,723 , 1) # enable allied view

# player max pop 250
mouse.click_absolute(3677 ,391 , 1)
time.sleep(.5)
mouse.click_absolute(3361 ,433 , 1)
mouse.click_absolute(3377 ,560 , 1)

# not rated
mouse.click_absolute(3652 ,428 , 1) # game type
mouse.click_absolute(3246 ,761 , 1) # not rated

mouse.click_absolute(3364 ,432 , 1) # map view (back to default start view)
mouse.click_absolute(3668 ,356 , 1)




