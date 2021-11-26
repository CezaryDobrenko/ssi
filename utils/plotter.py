from typing import List, Optional, Tuple
from utils.bitmap import Bitmap

import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    fig: object
    ax: List[object]
    __total_subplots: int
    __current_subplot: Optional[int]
    __subplot_y_count: int
    __subplot_x_count: int

    def __init__(self, subplots: Optional[Tuple[int, int]] = None):
        if subplots:
            self.__subplot_x_count, self.__subplot_y_count = subplots
            self.fig, self.ax = plt.subplots(
                self.__subplot_x_count, self.__subplot_y_count
            )
            self.__total_subplots = self.__subplot_x_count * self.__subplot_y_count
            self.__current_subplot = 1
            self.change_subplot(1)
        else:
            self.fig, self.ax = plt.subplots()
            self.__current_subplot = None

        self.serie_number = 0
        self.series = ["r-", "bo", "g--", "c-", "mo", "y--", "k-", "ro", "b--", "g-"]

    def clear(self) -> None:
        self.serie_number = 0
        if self.__current_subplot:
            for x_axis in self.ax:
                for subplot in x_axis:
                    subplot.cla()
        else:
            self.ax.cla()

    def show(self) -> None:
        plt.show()
    
    def close(self) -> None:
        plt.close()

    def save(self, file_name: str) -> None:
        plt.tight_layout()
        plt.savefig(f"plots/{file_name}.png", dpi=300)

    def add_grid(self) -> None:
        plt.grid()

    def add_title(self, title: str) -> None:
        plt.title(title)

    def add_labels(self, label_x: str, label_y: str) -> None:
        plt.xlabel(label_x)
        plt.ylabel(label_y)

    def get_serie_style(self) -> None:
        return self.series[self.serie_number % 10]

    def change_subplot(self, index: int) -> None:
        if index < 1 or index > self.__total_subplots:
            raise Exception("Subplot with that index does not exist!")

        plt.subplot(self.__subplot_x_count, self.__subplot_y_count, index)
        self.__current_subplot = index

    def draw_point(
        self, x: float, y: float, label: str, size: int = 10, color: str = "black"
    ) -> None:
        plt.scatter(x, y, s=size, c=[color], label=label)
        plt.legend(loc="upper left", prop={"size": 6})
        plt.draw()

    def draw_points(
        self,
        arguments: List[float],
        values: List[float],
        label: str,
        size: int = 10,
        color: str = "black",
    ) -> None:
        if len(arguments) != len(values):
            raise Exception("Arguments length do not match length of values!")

        plt.scatter(arguments, values, s=size, c=[color], label=label)
        plt.legend(loc="upper left", prop={"size": 6})
        plt.draw()

    def draw_line(
        self,
        point1: Tuple[float, float],
        point2: Tuple[float, float],
        label: str,
        style: str = "",
    ) -> None:
        if not style:
            style = self.get_serie_style()
            self.serie_number += 1

        x_start, y_start = point1
        x_end, y_end = point2
        plt.plot([x_start, x_end], [y_start, y_end], style)
        plt.legend(loc="upper left", prop={"size": 6})
        plt.draw()

    def draw_poly_line(
        self, arguments: List[float], values: List[float], label: str, style: str = ""
    ) -> None:
        if not style:
            style = self.get_serie_style()
            self.serie_number += 1

        plt.plot(arguments, values, style, label=label)
        plt.legend(loc="upper left", prop={"size": 6})
        plt.draw()

    def draw_curve(
        self,
        point1: Tuple[float, float],
        point2: Tuple[float, float],
        label: str,
        style: str = "",
        smoothnes: int = 100,
    ) -> None:
        if not style:
            style = self.get_serie_style()
            self.serie_number += 1

        x_start, y_start = point1
        x_end, y_end = point2
        a = (y_end - y_start) / (np.cosh(x_end) - np.cosh(x_start))
        b = y_start - a * np.cosh(x_start)
        arguments = np.linspace(x_start, x_end, smoothnes)
        values = a * np.cosh(arguments) + b
        plt.plot(arguments, values, style, label=label)
        plt.legend(loc="upper left", prop={"size": 6})
        plt.draw()

    def draw_monochromatic_bitmap(self, bitmap: Bitmap) -> None:
        Z = np.array(bitmap.get_matrix())
        x,y = Z.shape
        G = np.zeros((x,y,3))
        G[Z==1] = [0,0,0]
        G[Z==0] = [1,1,1]
        plt.imshow(G,interpolation='nearest')
