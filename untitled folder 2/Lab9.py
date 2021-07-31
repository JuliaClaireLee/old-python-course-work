##import turtle
##fred = turtle.Turtle()
##window = turtle.Screen()
##fred.backward(150)
##for i in range(360):
##    fred.forward(1)  # Take 1 step forward
##    fred.right(1)
import turtle
def koch(t, order, size):
    if order == 0:                  # The base case is just a straight line
        t.forward(size)
        
    else:
        koch(t, order-1, size/3)    # koch-ify the 1st line
        t.left(60)                  # rotate 60deg to the left
        koch(t, order-1, size/3)    # koch-ify the 2nd line
        t.right(120)                # rotate 120deg to the right
        koch(t, order-1, size/3)    # koch-ify the 3rd line
        t.left(60)                  # rotate 60deg to the left
        koch(t, order-1, size/3)    # koch-ify the 4th line
        
def main():
    fred = turtle.Turtle()
    window = turtle.Screen()
    fred.color("green")
    # We'll need to move Fred over to the left to start
    fred.penup()
    fred.backward(150)
    fred.pendown()
    # Call the koch procedure to start drawing
    koch(fred, 4, 300)
main()
