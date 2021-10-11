from typing import List
from utils.descriptor import Descriptor


class DecisionSystem:
    __descriptors = []

    def __init__(self, name):
        self.__name = name

    def load_descriptors_from_file(self, attrib_path: str, data_path: str) -> None:
        attrib_types = self.__load_descriptors_types(attrib_path)
        with open(data_path) as values_from_file:
            for values in values_from_file.readlines():
                attrib_values = self.__parse_descriptors_values(
                    values.split(), attrib_types
                )
                class_name = attrib_values.pop()
                descriptor = Descriptor(
                    class_name=class_name,
                    values_types=attrib_types,
                    values=attrib_values,
                )
                self.__descriptors.append(descriptor)

    def __load_descriptors_types(self, attrib_path: str) -> List[bool]:
        descriptor_types = []
        with open(attrib_path) as atribs:
            for atrib in atribs.readlines():
                atrib_data = atrib.split()
                if atrib_data[1] == "n":
                    descriptor_types.append(True)
                else:
                    descriptor_types.append(False)
        return descriptor_types

    def __parse_descriptors_values(
        self, raw_atribs_values: List[str], atribs_type: List[bool]
    ) -> List:
        if len(raw_atribs_values) != len(atribs_type):
            raise Exception("data definition do not match given data!")

        descriptor_values = []
        for i in range(len(raw_atribs_values)):
            if atribs_type[i]:
                parsed_value = float(raw_atribs_values[i].replace(",", "."))
            else:
                parsed_value = raw_atribs_values[i]
            descriptor_values.append(parsed_value)
        return descriptor_values

    def add_descriptor(self, descriptor: Descriptor) -> None:
        self.__descriptors.append(descriptor)

    def get_descriptor(self, index: int) -> Descriptor:
        return self.__descriptors[index]

    def get_descriptors(self) -> List[Descriptor]:
        return self.__descriptors

    def get_descriptors_by_class_name(self, class_name: str) -> List[Descriptor]:
        list_of_descriptors = []
        for descriptor in self.__descriptors:
            if descriptor.get_class_name() == class_name:
                list_of_descriptors.append(descriptor)
        return list_of_descriptors

    def remove_descriptor(self, index: int) -> None:
        self.__descriptors.remove(index)

    def __str__(self):
        return f"DecisionSystem: name= {self.__name}, descriptors= {self.__descriptors}"