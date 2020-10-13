#import turtle
import turtle

#define colors
colors=['red','yellow','green','blue','orange','indigo','purple']

#turtle pen
t=turtle.Pen()

#change speed of pen
t.speed(10)

#change the background color
turtle.bgcolor("black")

#make spiral
for i in range(250):
    t.pencolor(color[i%6])  #setting color
    t.width(i/100+1) #setting width
    t.forward(i) #moving forward
    t.left(59) #movingleft

turtle.done()    