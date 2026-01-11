#Assignment 2 Question 3
#import required modules from library
import turtle as t
import math

#Draw one edge using recursion
def draw_edge(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        segment = length / 3 # Divide the length into three segments
        draw_edge(segment, depth - 1)
        t.left(60)
        draw_edge(segment, depth - 1)
        t.right(120)
        draw_edge(segment, depth - 1)
        t.left(60)
        draw_edge(segment, depth - 1)
