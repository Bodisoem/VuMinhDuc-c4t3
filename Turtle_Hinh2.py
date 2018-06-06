from turtle import *

speed(10)
pencolor("red")
color = ["blue","red","blue","red","blue","red"]
for i in range(5):
   for x in range(i+2):
       pencolor(color[i])
       forward(100)
       left( 360/(i + 2) )


mainloop()
