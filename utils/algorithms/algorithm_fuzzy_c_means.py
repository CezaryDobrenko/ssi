import math
import random
from typing import List, Optional, Tuple

from utils.decision_system import DecisionSystem
from utils.descriptor import Descriptor


class AlgorithmFuzzyCMeans:
    __decision_system: DecisionSystem
    __D: List[List[float]]
    __U: List[List[float]]
    __V: List[List[float]]
    __M: int
    __n: int
    __m: int
    __fcm_m: int
    __smallest_possible_value: float
    __momentum: int

    def __init__(
        self, decision_system: DecisionSystem, fcm_m: int, c: int, momentum: int = 2
    ):
        class_names = self.__generate_class_names(c)
        decision_system.set_class_names(class_names)
        self.__decision_system = decision_system
        M = len(decision_system.get_all_descriptors())
        n = len(decision_system.get_descriptor(0).get_values())
        m = c
        self.__D = [[random.uniform(0, 1) for _ in range(M)] for _ in range(m)]
        self.__M = M
        self.__n = n
        self.__m = m
        self.__fcm_m = fcm_m
        self.__momentum = -momentum
        self.__smallest_possible_value = 0.0000001

    def execute(
        self,
        iters: int,
        save_each_iter_plot: Optional[bool] = False,
        show_final_plot: Optional[bool] = False,
    ) -> None:
        self.__U = self.__calculate_U()
        self.__V = self.__calculate_V()
        for _ in range(iters):
            self.__D = self.__calculate_D()
            self.__U = self.__calculate_U()
            self.__V = self.__calculate_V()
            self.__assign_probes_to_class()
            middle_points = self.__convert_middle_points()
            if save_each_iter_plot:
                self.__create_plot(middle_points, save=True)
        if show_final_plot:
            self.__create_plot(middle_points, show=True)

    def __calculate_D(self):
        D = [[0 for _ in range(self.__M)] for _ in range(self.__m)]
        for j in range(self.__m):
            for s in range(self.__M):
                x1, y1 = self.__decision_system.get_descriptor(s).get_values()
                x2, y2 = self.__V[j]
                new_distance = math.sqrt(
                    math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)
                )
                if new_distance > self.__smallest_possible_value:
                    D[j][s] = new_distance
                else:
                    D[j][s] = self.__smallest_possible_value
        return D

    def __calculate_U(self):
        U = [[0 for _ in range(self.__M)] for _ in range(self.__m)]
        for j in range(self.__m):
            for s in range(self.__M):
                first = math.pow(self.__D[j][s], 1 / (1 - self.__fcm_m))
                secound = 0
                for j_prim in range(self.__m):
                    secound += math.pow(self.__D[j_prim][s], 1 / (1 - self.__fcm_m))
                U[j][s] = first / secound
        return U

    def __calculate_V(self):
        V = [[0 for _ in range(self.__n)] for _ in range(self.__m)]
        for j in range(self.__m):
            for i in range(self.__n):
                first = self.__momentum
                secound = self.__momentum
                for s in range(self.__M):
                    first += math.pow(
                        self.__U[j][s], self.__fcm_m
                    ) * self.__decision_system.get_descriptor(s).get_value(i)
                    secound += math.pow(self.__U[j][s], self.__fcm_m)
                V[j][i] = first / secound
        return V

    def __assign_probes_to_class(self) -> None:
        for index in range(len(self.__decision_system.get_all_descriptors())):
            class_aligment = []
            for j in range(self.__m):
                class_aligment.append(self.__U[j][index])

            current_class_value = class_aligment[0]
            current_class_name = "0"
            for class_index in range(len(class_aligment)):
                if current_class_value < class_aligment[class_index]:
                    current_class_value = class_aligment[class_index]
                    current_class_name = str(class_index)
            self.__decision_system.get_descriptor(index).set_class_name(
                current_class_name
            )

    def __convert_middle_points(self) -> Tuple[List[float]]:
        middle_points_x = []
        middle_points_y = []
        for v_item in self.__V:
            x, y = v_item
            middle_points_x.append(x)
            middle_points_y.append(y)
        return (middle_points_x, middle_points_y)

    def __generate_class_names(self, c: int) -> List[str]:
        class_names = []
        for class_name in range(c):
            class_names.append(str(class_name))
        return class_names

    def __create_plot(
        self,
        middle_points: List[Descriptor],
        show: Optional[bool] = False,
        save: Optional[bool] = False,
    ) -> None:
        if show or save:
            self.__decision_system.add_plot(
                (1, 1),
                [(0, 1)],
                special_points=middle_points,
                show_plot=show,
                save_plot=save,
            )
