from turtle import *

speed(0)

color = ["red","blue","brown","yellow","gray"]


for x in range(5):
    pencolor(color[x])
    fillcolor(color[x])
    begin_fill()
    for i in range(2):
        forward(50)
        right(90)
        forward(100)
        right(90)
    forward(50)
    end_fill()

mainloop()