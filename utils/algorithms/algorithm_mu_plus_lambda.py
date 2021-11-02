import copy
import random
from typing import List, Optional, Tuple

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

from utils.probe import Probe


class AlgorithmMuPlusLambda:
    __specimens: List[Probe]
    __bounds: Tuple[int, int]
    __mi_value: int
    __lambda_value: int
    __mutation_level: int
    __tournament_size: int
    __show_each_epoch: bool
    __save_each_epoch: bool

    def __init__(
        self,
        mi_value: int,
        lambda_value: int,
        bounds: Tuple[int, int],
        mutation_level: int,
        tournament_size: Optional[int] = 2,
        show_each_epoch: Optional[bool] = False,
        save_each_epoch: Optional[bool] = False,
    ):
        self.__mi_value = mi_value
        self.__lambda_value = lambda_value
        self.__bounds = bounds
        self.__tournament_size = tournament_size
        self.__mutation_level = mutation_level
        self.__show_each_epoch = show_each_epoch
        self.__save_each_epoch = save_each_epoch
        self.__specimens = self.__generate_mu_population(mi_value, bounds)

    def evolve_population(self, epochs: int) -> None:
        for index in range(epochs):
            self.__specimens = self.__generate_next_population(
                self.__lambda_value, index
            )

    def get_best_specimen(self, specimens: Optional[List[Probe]] = None) -> Probe:
        population = specimens if specimens else self.__specimens
        best_specimen = population[0]
        for specimen in population:
            if best_specimen.get_value() < specimen.get_value():
                best_specimen = specimen
        return best_specimen

    def get_specimen(self, index: int) -> Probe:
        return self.__specimens[index]

    def add_specimen(self, specimen: Probe) -> None:
        self.__specimens.append(specimen)

    def __generate_mu_population(self, quantity: int, bounds) -> List[Probe]:
        population = []
        left_bound, right_bound = bounds
        for _ in range(quantity):
            x1 = random.uniform(left_bound, right_bound)
            x2 = random.uniform(left_bound, right_bound)
            population.append(Probe(x1, x2))
        return population

    def __generate_lambda_population(self, quantity: int) -> List[Probe]:
        next_population = []
        for _ in range(quantity):
            tournament_winner = self.__execute_tournament(self.__specimens)
            mutated_winner = self.__mutate_probe(tournament_winner)
            next_population.append(mutated_winner)
        return next_population

    def __generate_next_population(self, quantity: int, index: int) -> List[Probe]:
        next_population = self.__generate_lambda_population(quantity)
        population = [*self.__specimens, *next_population]
        best_specimen = self.get_best_specimen(self.__specimens)

        if self.__save_each_epoch or self.__show_each_epoch:
            self.draw_plot(self.__specimens, next_population, index)

        new_population = []
        for _ in range(self.__mi_value - 1):
            tournament_winner = self.__execute_tournament(population)
            new_population.append(tournament_winner)
        new_population.append(best_specimen)
        return new_population

    def __mutate_probe(self, specimen: Probe) -> List[Probe]:
        x1, x2 = specimen.get_coordinates()
        new_x1 = self.__check_boundaries(
            x1 + random.uniform(-self.__mutation_level, self.__mutation_level)
        )
        new_x2 = self.__check_boundaries(
            x2 + random.uniform(-self.__mutation_level, self.__mutation_level)
        )
        specimen.set_coordinates(new_x1, new_x2)
        return specimen

    def __check_boundaries(self, value: float) -> float:
        left_bound, right_bound = self.__bounds
        value = left_bound if value < left_bound else value
        value = right_bound if value > right_bound else value
        return value

    def __copy_specimen(self, specimen: Probe) -> Probe:
        return copy.deepcopy(specimen)

    def __execute_tournament(self, population: List[Probe]) -> Probe:
        tournament_pool = random.sample(population, self.__tournament_size)
        tournament_winner = self.get_best_specimen(tournament_pool)
        return self.__copy_specimen(tournament_winner)

    def draw_plot(
        self,
        parent_population: List[Probe],
        children_population: List[Probe],
        index: int,
    ):
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

        for parent_probe in parent_population:
            x1, x2 = parent_probe.get_coordinates()
            plt.scatter(x1, x2, c="blue")

        for children_probe in children_population:
            x1, x2 = children_probe.get_coordinates()
            plt.scatter(x1, x2, c="red")

        if self.__show_each_epoch:
            plt.show()
        if self.__save_each_epoch:
            plt.savefig(f"plots/{index}.jpg", dpi=100)
        plt.close()
