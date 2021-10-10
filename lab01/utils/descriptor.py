class Descriptor():
    """
    Descriptor
    """

    __values_types = []
    __values = []

    def __init__(self, class_name: str):
        self.__class_name = class_name

    def set_value_type(self, value_type: float) -> None:
        self.__values_types.append(value_type)
    
    def set_values_types(self, values_types: list) -> None:
        self.__values_types = values_types

    def get_value_type(self, index: int):
        return self.__values_types[index]

    def set_value(self, value: float) -> None:
        self.__values.append(value)

    def set_values(self, values: list) -> None:
        self.__values = values
    
    def get_value(self, index: int):
        return self.__values[index]

    def __str__(self):
        return f"Descriptor: class= {self.__class_name}, values={str(self.__values)}, types={str(self.__values_types)}"

    def __repr__(self):
        return f"\nDescriptor: class= {self.__class_name}, values={str(self.__values)}, types={str(self.__values_types)}"