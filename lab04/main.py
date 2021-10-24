import numpy as np
import math
import random

def calculate_value_for_argument(argument):
    return math.sin(argument/10)*math.sin(argument/200)

def check_boundaries(value, left_bound, right_bound):
    if value < left_bound or value > right_bound:
        return (left_bound + right_bound)/2
    return value 

def main():
    iter = 100
    left_bound = 0
    right_bound = 100
    arguments = np.linspace(left_bound, right_bound, 100)

    wsp_przyrostu = 1.1
    variance = 10
    x = random.choice(arguments)
    y = calculate_value_for_argument(x)
    for _ in range(iter):
        variance_args = np.linspace(-variance, variance, 100)
        tmp_x = x + random.choice(variance_args)
        new_x = check_boundaries(tmp_x, left_bound, right_bound)
        new_y = calculate_value_for_argument(new_x)
        if(new_y >= y):
            x = new_x
            y = new_y
            variance *= wsp_przyrostu
        else:
            variance /= wsp_przyrostu
            
if __name__ == "__main__":
    main()
