import copy
import math
import random
from typing import Dict, List, Optional, Tuple

from utils.decision_system import DecisionSystem
from utils.descriptor import Descriptor


class AlgorithmKMeans:
    __decision_system: DecisionSystem
    __middle_points: List[Descriptor]

    def __init__(self, decision_system: DecisionSystem, k: int):
        probes = decision_system.get_all_descriptors()
        self.__decision_system = decision_system
        self.__middle_points = self.__get_random_middle_points(probes, k)

    def execute(
        self,
        iterations: int,
        save_each_iteration_plot: Optional[bool] = False,
        show_final_plot: Optional[bool] = False,
    ) -> None:
        probes = self.__decision_system.get_all_descriptors()
        for _ in range(iterations):
            groups_classificators = self.__group_probes(probes)
            for group_index, group_descriptors in groups_classificators.items():
                if group_descriptors:
                    middle_point = self.__middle_points[int(group_index)]
                    self.__adjust_coorinates(middle_point, group_descriptors)
            self.__create_plot(self.__middle_points, save=save_each_iteration_plot)
        self.__create_plot(
            self.__middle_points, show=show_final_plot, save=save_each_iteration_plot
        )

    def __adjust_coorinates(
        self, middle_point: Descriptor, group_descriptors: List[Descriptor]
    ) -> None:
        for attrib_index in range(len(middle_point.get_values())):
            sum_of_group = 0
            count_of_group = len(group_descriptors)
            for group_descriptor in group_descriptors:
                sum_of_group += group_descriptor.get_value(attrib_index)
            middle_point.update_value(attrib_index, sum_of_group / count_of_group)

    def __group_probes(self, probes: List[Descriptor]) -> Dict[str, List[Descriptor]]:
        groups_classificators: Dict[str, List[Descriptor]] = {}
        class_names = []
        for probe_s in probes:
            distances = self.__calculate_probe_distance(probe_s)
            class_name = str(self.__get_minimum_index_from_list(distances))
            probe_s.set_class_name(class_name)
            if class_name in groups_classificators.keys():
                groups_classificators.get(class_name).append(probe_s)
            else:
                groups_classificators[class_name] = []
                class_names.append(class_name)
        self.__decision_system.set_class_names(class_names)
        return groups_classificators

    def __calculate_probe_distance(self, probe_s: Descriptor) -> List[float]:
        distances = []
        for middle_point_v in self.__middle_points:
            distances.append(self.__get_euclidean_distance(probe_s, middle_point_v))
        return distances

    def __get_euclidean_distance(
        self, descriptor_1: Descriptor, descriptor_2: Descriptor
    ) -> float:
        x1, y1 = descriptor_1.get_values()
        x2, y2 = descriptor_2.get_values()
        return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

    def __get_minimum_index_from_list(self, input_list: List[float]) -> int:
        min_value = input_list[0]
        min_index = 0
        for index in range(1, len(input_list)):
            if input_list[index] < min_value:
                min_value = input_list[index]
                min_index = index
        return min_index

    def __get_random_middle_points(self, probes: List[Descriptor], k: int):
        middle_points = []
        for _ in range(k):
            middle_points.append(copy.deepcopy(random.choice(probes)))
        return middle_points

    def __convert_middle_points(
        self, middle_points: List[Descriptor]
    ) -> List[Tuple[float, float]]:
        middle_points_x = []
        middle_points_y = []
        for middle_point in middle_points:
            x, y = middle_point.get_values()
            middle_points_x.append(x)
            middle_points_y.append(y)
        return (middle_points_x, middle_points_y)

    def __create_plot(
        self,
        middle_points: List[Descriptor],
        show: Optional[bool] = False,
        save: Optional[bool] = False,
    ):
        if show or save:
            middle_points_coords = self.__convert_middle_points(middle_points)
            self.__decision_system.add_plot(
                (1, 1),
                [(0, 1)],
                special_points=middle_points_coords,
                show_plot=show,
                save_plot=save,
            )
