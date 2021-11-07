from utils.decision_system import DecisionSystem
from utils.descriptor import Descriptor
import random
import math
import copy

def calculate_distance(descriptor_1: Descriptor, descriptor_2: Descriptor) -> float:
    x1, y1 = descriptor_1.get_values()
    x2, y2 = descriptor_2.get_values()
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def get_minimum_index_from_list(input_list) -> int:
    min_value = input_list[0]
    min_index = 0
    for index in range(1, len(input_list)):
        if input_list[index] < min_value:
            min_value = input_list[index]
            min_index = index
    return min_index

def main():
    decision_system = DecisionSystem(name="spirala_decision_system")
    decision_system.load_descriptors_from_file(
        "data/spirala-type.txt", "data/spirala.txt"
    )

    k = 4
    epochs = 100

    middle_points = []
    probes = decision_system.get_all_descriptors()

    for _ in range(k):
        middle_points.append(copy.deepcopy(random.choice(probes)))
    
    for _ in range(epochs):
        groups_classificators = {}
        for probe_s in probes:
            distances = []
            for middle_point_v in middle_points:
                distances.append(calculate_distance(probe_s, middle_point_v))
            u_index = str(get_minimum_index_from_list(distances))
            probe_s.set_class_name(u_index)
            if u_index in groups_classificators.keys():
                groups_classificators.get(u_index).append(probe_s)
            else:
                groups_classificators[u_index] = []
                
        for group_index, group_descriptors in groups_classificators.items():
            if group_descriptors:
                middle_point = middle_points[int(group_index)]
                for attrib_index in range(len(middle_point.get_values())):
                    sum_of_group = 0;
                    count_of_group = len(group_descriptors);
                    for group_descriptor in group_descriptors:
                        sum_of_group += group_descriptor.get_value(attrib_index)
                    middle_point.update_value(attrib_index, sum_of_group/count_of_group)

    decision_system.add_plot((1,1), [(0,1)], selected_classes=["0","1","2","3"], show_plot=True)

    #TO DO
    # Refactor to OOP
    # Delete from commit history this junk

if __name__ == "__main__":
    main()
