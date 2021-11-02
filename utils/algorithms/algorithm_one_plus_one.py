import math
import random
from typing import List, Tuple

import numpy as np

from utils.plotter import Plotter


class AlgorithmOnePlusOne:
    __current_x: float
    __current_y: float
    __increment_factor: float
    __scatter_factor: float
    __bounds: Tuple[float, float]
    __plot: Plotter

    def __init__(
        self,
        bounds: Tuple[float, float],
        increment_factor: float = 1.1,
        scatter_factor: float = 10,
    ):
        left_bound, right_bound = bounds
        arguments = np.linspace(left_bound, right_bound, 100)
        start_x = random.choice(arguments)
        start_y = self.__calculate_value(start_x)
        self.__current_x = start_x
        self.__current_y = start_y
        self.__increment_factor = increment_factor
        self.__scatter_factor = scatter_factor
        self.__bounds = bounds
        self.__plot = self.__create_base_plot(arguments, start_x, start_y)

    def evolve(self, epochs: int, show_plot: bool = False):
        left_bound, right_bound = self.__bounds
        points_x = []
        points_y = []
        for _ in range(epochs):
            arguments = np.linspace(-self.__scatter_factor, self.__scatter_factor, 100)
            tmp_x = self.__current_x + random.choice(arguments)
            new_x = self.__check_boundaries(tmp_x, left_bound, right_bound)
            new_y = self.__calculate_value(new_x)
            if new_y >= self.__current_y:
                self.__current_x = new_x
                self.__current_y = new_y
                self.__scatter_factor *= self.__increment_factor
                points_x.append(new_x)
                points_y.append(new_y)
            else:
                self.__scatter_factor /= self.__increment_factor
        self.__plot.draw_point(
            points_x.pop(), points_y.pop(), size=50, label="final point"
        )
        self.__plot.draw_points(points_x, points_y, color="green", label="steps")
        if show_plot:
            self.__plot.show()

    def get_coordinates(self) -> Tuple[float, float]:
        return (self.__current_x, self.__current_y)

    def __calculate_value(self, x):
        return math.sin(x / 10) * math.sin(x / 200)

    def __check_boundaries(self, value, left_bound, right_bound):
        if value < left_bound or value > right_bound:
            return (left_bound + right_bound) / 2
        return value

    def __create_base_plot(
        self, arguments: List[float], start_x: float, start_y: float
    ):
        values = [self.__calculate_value(x) for x in arguments]
        plot = Plotter()
        plot.draw_poly_line(arguments, values, label="function")
        plot.draw_point(start_x, start_y, size=30, color="blue", label="start point")
        return plot
