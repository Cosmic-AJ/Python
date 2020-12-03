# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:31:27 2020

@author: Ayush Jain
"""

import turtle

turtle.setup(800,600)
turtle.Screen().bgcolor("orange")
board = turtle.Turtle()
board.shape("turtle")
 
circle_positions = [(-120,0,"blue"), (0,0,"black"), (120,0,"red"),
                    (-60,-60,"yellow"), (60,-60,"green")]
 
for pos in circle_positions:
  board.penup()
  board.setpos(pos[0],pos[1])
  board.pencolor(pos[2])
  board.pensize(5)
  board.pendown()
  board.circle(50)
 
turtle.done()