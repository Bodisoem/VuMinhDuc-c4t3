from turtle import *

shape('turtle')
speed(0)
color = ["red","blue","pink","yellow","gray"]
for i in range(5):

    for x in range( i + 2):
        pencolor(color[i])
        left(360/(i + 2))
        forward(100)

mainloop()