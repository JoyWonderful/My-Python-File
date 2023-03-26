import turtle
s = turtle.Screen()
def pos(x, y) :
    turtle.speed('fast')
    turtle.goto(x, y)
    turtle.write('x: ' + str(x) + ' y: ' + str(y))

s.onclick(pos,btn=1)
s.mainloop()

#制作:权家乐  想法提供:权家乐
#版权所有 侵权必究
