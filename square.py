from turtle import *

length = input("skriv lengden eller bredden av kvadratet i cm: ")
color('red', 'yellow')
begin_fill()
speed(1)
for i in range(4):
    forward(int(length))
    left(90)