# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:17:44 2020

@author: sis
"""


from turtle import*
def snowflake(lengthside,levels):
    if levels==0:
        forward(lengthside)
        return
    lengthside /=3.0
    snowflake(lengthside,levels-1)
    left(60)
    snowflake(lengthside,levels-1)
    right(120)
    snowflake(lengthside,levels-1)
    left(60)
    snowflake(lengthside,levels-1)
if __name__=="__main__":
    speed(9999)
    length=300.0
    penup()
    backward(length/2.0)
    pendown()
    for i in range(3):
        snowflake(length,4)
        right(120)
    mainloop()
    