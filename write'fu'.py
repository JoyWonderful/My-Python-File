from turtle import *
turtlesize(2.5)
bgcolor('seashell')
pencolor('red')
fillcolor('red')
penup()

goto(0,-150)
pendown()
begin_fill()
circle(150,steps=4)
end_fill()
penup()

pencolor('black')
fillcolor('black')
goto(0,-50)
write('福',align='center',font=('楷体',70))

hideturtle()

done()

#制作:权家乐  想法提供:权家乐
#版权所有 侵权必究
