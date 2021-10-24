from typing import List, Tuple
import numpy as np
import math
import random

class Probe:
    __x1: float
    __x2: float
    __value: float

    def __init__(self, x1: float, x2: float):
        self.__x1 = x1
        self.__x2 = x2
        self.__value = self.__calculate_value(x1, x2)

    def __calculate_value(x1, x2):
        return math.sin(x1*0.05)+math.sin(x2*0.05)+0.4*math.sin(x1*0.15)*math.sin(x2*0.15)

    def get_value(self) -> float:
        return self.__value

    def get_coordinates(self) -> Tuple[float, float]:
        return (self.x, self.y)

class AlgorithmMuPlusLambda:
    __specimens: List[Probe]
    __bounds: Tuple[int, int]
    __mi_value: int
    __lambda_value: int

    def __init__(self, mi_value: int, lambda_value: int, bounds: Tuple[int, int]):
        self.__mi_value = mi_value
        self.__lambda_value = lambda_value
        self.__bounds = bounds
        self.__specimens = self.__generate_random_population(mi_value, bounds)

    def get_specimen(self, index: int) -> Probe:
        return self.__specimens[index]

    def get_best_specimen(self) -> Probe:
        best_specimen = self.__specimens[0]
        for specimen in self.__specimens:
            if best_specimen.get_value() < specimen.get_value():
                best_specimen = specimen
        return best_specimen

    def add_specimen(self, specimen: Probe) -> None:
        self.__specimens.append(specimen)

    def __generate_random_population(self, quantity: int, bounds) -> List[Probe]:
        base_population = []
        left_bound, right_bound = bounds
        x1 = random.uniform(left_bound, right_bound)
        x2 = random.uniform(left_bound, right_bound)
        for _ in range(quantity):
            base_population.append(Probe(x1, x2))
        return base_population

    def __generate_next_population(self, quantity: int, bounds)  -> List[Probe]:
        next_population = self.__generate_random_population(quantity, bounds)
        population = [*self.__specimens, *next_population]
        best_base_specimen = self.get_best_specimen(self.__specimens)

        new_population = []
        for _ in range(self.__mi_value-1):
            new_population.append()
        new_population.append(best_base_specimen)
        return next_population

    def evolve_population(self, epochs) -> None:
        for _ in range(epochs):
            self.__specimens = self.__generate_next_population(self.__lambda_value, self.__bounds)


def check_boundaries(value, left_bound, right_bound):
    if value < left_bound or value > right_bound:
        return (left_bound + right_bound)/2
    return value 

def main():
    iter = 100
    left_bound = 0
    right_bound = 100
    mi = 4
    lambda_ = 10
    turniej_rozmiar = 2
    arguments_x1 = np.linspace(left_bound, right_bound, 100)
    arguments_x2 = np.linspace(left_bound, right_bound, 100)
            
if __name__ == "__main__":
    main()
