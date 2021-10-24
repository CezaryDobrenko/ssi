from typing import List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, subplots: Optional[Tuple[int, int]] = None):
        if subplots:
            self.subplot_x_count, self.subplot_y_count = subplots
            self.fig, self.ax = plt.subplots(self.subplot_x_count, self.subplot_y_count)
            self.total_subplots = self.subplot_x_count * self.subplot_y_count
            self.change_subplot(1)
        else:
            self.fig, self.ax = plt.subplots()

        self.serie_number = 0
        self.series = ["r-", "bo", "g--", "c-", "mo", "y--", "k-", "ro", "b--", "g-"]

    def clear(self):
        self.serie_number = 0
        self.ax.cla()

    def show(self):
        plt.show()

    def add_grid(self):
        plt.grid()

    def add_title(self, title: str):
        plt.title(title)

    def add_labels(self, label_x: str, label_y: str):
        plt.xlabel(label_x)
        plt.ylabel(label_y)

    def get_serie_style(self):
        return self.series[self.serie_number % 10]

    def change_subplot(self, index: int):
        if index < 1 or index > self.total_subplots:
            raise Exception("Subplot with that index does not exist!")

        plt.subplot(self.subplot_x_count, self.subplot_y_count, index)

    def draw_point(self, x: float, y: float, size: int = 10, color: str = "black"):
        plt.scatter(x, y, s=size, c=[color])
        plt.draw()

    def draw_points(
        self,
        arguments: List[float],
        values: List[float],
        size: int = 10,
        color: str = "black",
    ):
        if len(arguments) != len(values):
            raise Exception("Arguments length do not match length of values!")

        plt.scatter(arguments, values, s=size, c=[color])
        plt.draw()

    def draw_line(
        self, point1: Tuple[float, float], point2: Tuple[float, float], style: str = ""
    ):
        if not style:
            style = self.get_serie_style()
            self.serie_number += 1

        x_start, y_start = point1
        x_end, y_end = point2
        plt.plot([x_start, x_end], [y_start, y_end], style)
        plt.draw()

    def draw_poly_line(
        self, arguments: List[float], values: List[float], style: str = ""
    ):
        if not style:
            style = self.get_serie_style()
            self.serie_number += 1

        plt.plot(arguments, values, style)
        plt.draw()

    def draw_curve(
        self,
        point1: Tuple[float, float],
        point2: Tuple[float, float],
        style: str = "",
        smoothnes: int = 100,
    ):
        if not style:
            style = self.get_serie_style()
            self.serie_number += 1

        x_start, y_start = point1
        x_end, y_end = point2
        a = (y_end - y_start) / (np.cosh(x_end) - np.cosh(x_start))
        b = y_start - a * np.cosh(x_start)
        arguments = np.linspace(x_start, x_end, smoothnes)
        values = a * np.cosh(arguments) + b
        plt.plot(arguments, values, style)
