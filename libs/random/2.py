"""
Generate a random no. with weights

Here, chances of occuring '3' is most relatively
"""
import random


l = [1, 3, 6, 8, 9, 10]             # list
w = [10, 25, 15, 15, 15, 20]        # weights

print(random.choices(l, w))