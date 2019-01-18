"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Liam Groom.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
import math as m
window = rg.TurtleWindow()
wasd=rg.SimpleTurtle('circle')
dwas=rg.SimpleTurtle('triangle')


window.tracer(2000)
zelda=rg.SimpleTurtle('turtle')
zelda.speed=10000000000
for k in range(500):
    zelda.pen=rg.Pen('purple',1)
    zelda.draw_square(1+k/2)
    zelda.left(10)
    zelda.pen=rg.Pen('blue',2)
    zelda.forward(10+k)
    zelda.pen=rg.Pen('yellow',1)
    zelda.draw_circle(2+(k/250))
    zelda.pen = rg.Pen('blue',1)
    zelda.backward(10+k)
    zelda.right(10)
    zelda.right(2+(24/(k+1)))
    wasd.go_to(rg.Point(k,k))
    wasd.right(2)
    wasd.forward((10000-m.sin(k))/(k+1))
    wasd.go_to(rg.Point(0,0))