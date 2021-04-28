"""
Sungmin Kim
ball_puzzle.py
"""

from ball_puzzle_animate import *
from stack import *


def first_balls(ball_colors):
    """
    takes a string of R G B characters and adds them to the red can stack
    """
    red_can = make_empty_stack()
    for color in ball_colors:
        push(red_can, color)
    return red_can


def solve(red_can, blue_can, green_can):
    """
    solves the ball puzzle, each parameter is an empty stack except
    for red can which is filled.
    takes balls from a can and puts a ball of a target color
    into the right can. The other colors go into the other can as a throwaway.
    This is repeated until cans are sorted.
    """
    
    
    counter = 0
    can_list = [red_can, green_can, blue_can]
    while not is_empty(red_can):
        top_ball = pop(red_can)
        if top_ball == "B":
            push(blue_can, top_ball)
            animate_move(can_list, 0, 2)
        else:
            push(green_can, top_ball)
            animate_move(can_list, 0, 1)
        counter += 1
        
    while not is_empty(green_can):
        top_ball = pop(green_can)
        if top_ball == "R":
            push(red_can, top_ball)
            animate_move(can_list, 1, 0)
        else:
            push(blue_can, top_ball)
            animate_move(can_list, 1, 2)
        counter += 1
        
    while not is_empty(blue_can):
        top_ball = pop(blue_can)
        if top_ball == "G":
            push(green_can, top_ball)
            animate_move(can_list, 2, 1)
            counter += 1
        
    return counter

    
def main():
    """
    calls functions to animate the solving of the puzzle
    """
    balls = input("Enter the color of the balls starting in the red can:")
    animate_init(balls)
    print(solve(first_balls(balls), make_empty_stack(), make_empty_stack()))
    print("Close the window to quit")
    animate_finish()
main()

    
