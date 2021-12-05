from typing import List, Tuple
import matplotlib.pyplot as plt

class Drawer:
    fig: object
    ax: List[object]
    output_matrix: List[List[float]]
    __xticks = List[int]
    __yticks = List[int]

    def __init__(self, drawer_x_range: Tuple[float, float], drawer_y_range: Tuple[float, float]):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        start_x, end_x = drawer_x_range
        start_y, end_y = drawer_y_range
        self.ax.set_xlim([start_x, end_x])
        self.ax.set_ylim([start_y, end_y])
        self.__xticks = [i for i in range(start_x, end_x+1)]
        self.__yticks = [i for i in range(start_y, end_y+1)]
        self.output_matrix = [[0 for _ in range(end_x)]for _ in range(end_y)]

    def __onclick(self, event):
        self.output_matrix[int(event.ydata)][int(event.xdata)] = 1
        plt.scatter(int(event.xdata)+0.5, int(event.ydata)+0.5, color='black', marker="s", s=1000)
        self.fig.canvas.draw()

    def draw_matrix(self) -> List[List[float]]:
        _ = self.fig.canvas.mpl_connect('button_press_event', self.__onclick)
        plt.grid()
        plt.xticks(self.__xticks)
        plt.yticks(self.__yticks)
        plt.show()
        return self.output_matrix[::-1]

    def get_matrix(self) -> List[List[float]]:
        return self.output_matrix