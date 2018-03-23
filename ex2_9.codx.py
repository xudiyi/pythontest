# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:21:38 2018

@author: asus1
"""
#.e2.2Drowpython.py
from turtle import *
setup(650, 350, 200, 200)
penup()
fd(-250)
pendown()
pensize(15)
pencolor("pink")
seth(-20)
for i in range(4):
    circle(25, 85)
    pencolor("yellow")
    circle(-25, 85)
circle(20, 60/1.5)
pencolor("pink")
fd(35)
circle(20, 60 /1.5)
pencolor("purple")
fd(35)
    

