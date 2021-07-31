# -------------------------------------------------
#        Name: Julia Lee AND SOMTO OKONKWO
#    Filename: fractal.py
#        Date: 10/24/2018
#
# Description: This lab is a  recursion to make
#                     A fractal
#  
#                          
# ---------------------------------------------------

import turtle
def tri(t, order, size):
    if order == 0:                  # The base case is just a triangle
       t.left(60)
       t.forward(size)
       t.backward(size)
       t.right(60)
       t.forward(size)
       t.left(60)
       t.left(60)
       t.forward(size)
    else:
        tri(t, order-1, size/3)
        tri(t, order-1, size/3)
        tri(t, order-1, size/3)
        t.penup()
        t.left(240)
        t.pendown()
        
def main():
    fred = turtle.Turtle()
    window = turtle.Screen()
    fred.color("green")
    # We'll need to move Fred over to the left to start
    fred.penup()
    fred.backward(150)
    fred.pendown()
    tri(fred, 2, 300)
main()
