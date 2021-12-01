import random
import math
from typing import List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np

from utils.probe import Probe


class AlgorithmFirefly:
    __specimens: List[Probe]
    __bounds: Tuple[int, int]
    __gamma_0: float
    __beta_0: float
    __mu_0: float
    __show_each_epoch: bool
    __save_each_epoch: bool

    def __init__(
        self,
        gamma_0: float,
        beta_0: float,
        mu_0: float,
        N: int,
        bounds: Tuple[int, int],
        show_each_epoch: Optional[bool] = False,
        save_each_epoch: Optional[bool] = False,
    ):
        self.__gamma_0 = gamma_0
        self.__beta_0 = beta_0
        self.__mu_0 = mu_0
        self.__bounds = bounds
        self.__show_each_epoch = show_each_epoch
        self.__save_each_epoch = save_each_epoch
        self.__specimens = self.__generate_population(N, bounds)


    def evolve_population(self, epochs: int) -> None:
        for index in range(epochs):
            self.__specimens = self.__evolve_next_population(index)

    def __evolve_next_population(self, index: int) -> List[Probe]:
        for probe_a in sorted(self.__specimens, key=lambda _: random.random()):
            for probe_b in sorted(self.__specimens, key=lambda _: random.random()):
                if probe_b.get_value() > probe_a.get_value():
                    dist = self.__calculate_distance(probe_a, probe_b)
                    gamma = self.__gamma_0 / dist
                    beta = self.__beta_0 * math.pow(math.e, -gamma * math.pow(dist,2))
                    xa1, xa2 = probe_a.get_coordinates()
                    xb1, xb2 = probe_b.get_coordinates()
                    new_xa1 = self.__check_boundaries(xa1 + beta * (xb1 - xa1))
                    new_xa2 = self.__check_boundaries(xa2 + beta * (xb2 - xa2))
                    probe_a.set_coordinates(new_xa1, new_xa2)
            xa1, xa2 = probe_a.get_coordinates()
            new_xa1 = self.__check_boundaries(xa1 + random.uniform(-3, 3))
            new_xa2 = self.__check_boundaries(xa2 + random.uniform(-3, 3))
            probe_a.set_coordinates(new_xa1, new_xa2)
        self.draw_plot(self.__specimens, index)
        return self.__specimens

    def __check_boundaries(self, value: float) -> float:
        left_bound, right_bound = self.__bounds
        value = left_bound if value < left_bound else value
        value = right_bound if value > right_bound else value
        return value

    def __calculate_distance(self, probe_a: Probe, probe_b: Probe) -> float:
        x1, y1 = probe_a.get_coordinates()
        x2, y2 = probe_b.get_coordinates()
        return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

    def __generate_population(self, quantity: int, bounds) -> List[Probe]:
        population = []
        left_bound, right_bound = bounds
        for _ in range(quantity):
            x1 = random.uniform(left_bound, right_bound)
            x2 = random.uniform(left_bound, right_bound)
            population.append(Probe(x1, x2))
        return population
    
    def draw_plot(self, population: List[Probe], index: int):
        x1 = np.linspace(0, 100)
        x2 = np.linspace(0, 100)
        X1, X2 = np.meshgrid(x1, x2)

        Value = (
            np.sin(X1 * 0.05)
            + np.sin(X2 * 0.05)
            + 0.4 * np.sin(X1 * 0.15) * np.sin(X2 * 0.15)
        )
        fig, ax = plt.subplots()
        CS = ax.contour(X1, X2, Value)
        ax.clabel(CS, inline=True, fontsize=10)
        ax.set_title("sin(x1*0.05)+sin(x2*0.05)+0.4*sin(x1*0.15)*sin(x2*0.15)")

        for probe in population:
            x1, x2 = probe.get_coordinates()
            plt.scatter(x1, x2, c="blue")

        if self.__show_each_epoch:
            plt.show()
        if self.__save_each_epoch:
            plt.savefig(f"plots/{index}.jpg", dpi=100)
        plt.close()
