import math
from typing import Tuple


class Probe:
    __x1: float
    __x2: float
    __value: float

    def __init__(self, x1: float, x2: float):
        self.__x1 = x1
        self.__x2 = x2
        self.__value = self.__calculate_value(x1, x2)

    def set_coordinates(self, x1: float, x2: float) -> None:
        self.__x1 = x1
        self.__x2 = x2
        self.__value = self.__calculate_value(x1, x2)

    def get_coordinates(self) -> Tuple[float, float]:
        return (self.__x1, self.__x2)

    def get_value(self) -> float:
        return self.__value

    def __calculate_value(self, x1, x2) -> float:
        return (
            math.sin(x1 * 0.05)
            + math.sin(x2 * 0.05)
            + 0.4 * math.sin(x1 * 0.15) * math.sin(x2 * 0.15)
        )

    def __str__(self):
        return (
            f"Probe: coordinates(x1={self.__x1}, x2={self.__x2}, value={self.__value})"
        )

    def __repr__(self):
        return (
            f"Probe: coordinates(x1={self.__x1}, x2={self.__x2}, value={self.__value})"
        )
