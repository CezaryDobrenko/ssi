from typing import List


class Descriptor:
    __values: List[float]
    __values_types: List[bool]

    def __init__(self, class_name: str, values_types: List[bool], values: List[float]):
        self.__class_name = class_name
        self.__values = values
        self.__values_types = values_types

    def set_value_type(self, value_type: float) -> None:
        self.__values_types.append(value_type)

    def get_value_type(self, index: int) -> bool:
        return self.__values_types[index]

    def set_value(self, value: float) -> None:
        self.__values.append(value)

    def get_value(self, index: int) -> float:
        return self.__values[index]

    def set_class_name(self, class_name: str) -> None:
        self.__class_name = class_name

    def get_class_name(self) -> str:
        return self.__class_name

    def __str__(self):
        return f"Descriptor: class= {self.__class_name}, values={str(self.__values)}, types={str(self.__values_types)}"

    def __repr__(self):
        return f"\nDescriptor: class= {self.__class_name}, values={str(self.__values)}, types={str(self.__values_types)}"
