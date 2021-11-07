import re
from typing import List, Optional, Tuple

from distinctipy import distinctipy
from PIL import Image

from utils.descriptor import Descriptor
from utils.plotter import Plotter


class DecisionSystem:
    __name: str
    __default_class_name: str
    __class_names: List[str]
    __descriptors: List[Descriptor]
    __plots: List[str]

    def __init__(self, name):
        self.__name = name
        self.__class_names = []
        self.__descriptors = []
        self.__plots = []
        self.__default_class_name = "set"

    def load_descriptors_from_file(self, attrib_path: str, data_path: str) -> None:
        attrib_types = self.__load_descriptors_types(attrib_path)
        last_attrib = attrib_types[-1]
        with open(data_path) as values_from_file:
            for values in values_from_file.readlines():
                attrib_values = self.__parse_descriptors_values(
                    values.split(), attrib_types
                )
                class_name = (
                    self.__class_names[int(attrib_values.pop())-1]
                    if last_attrib is True
                    else self.__default_class_name
                )
                if class_name not in self.__class_names:
                    self.__class_names.append(class_name)
                descriptor = Descriptor(
                    class_name=class_name,
                    values=attrib_values,
                    values_types=attrib_types,
                )
                self.__descriptors.append(descriptor)

    def __load_descriptors_types(self, attrib_path: str) -> List[bool]:
        descriptor_types = []
        with open(attrib_path) as atribs:
            for atrib in atribs.readlines():
                atrib_data = atrib.split()
                if atrib_data[1] == "n":
                    descriptor_types.append(False)
                else:
                    descriptor_types.append(True)
            self.__class_names = self.__parse_class_names(atrib_data)
        return descriptor_types

    def __parse_class_names(self, atrib_data: str) -> List[str]:
        raw_type_data = atrib_data[0]
        type_data = re.split(r"[\()=\,\)]", raw_type_data)[1:-1]
        type_names = type_data[1::2]
        return type_names

    def __parse_descriptors_values(
        self, raw_atribs_values: List[str], atribs_type: List[bool]
    ) -> List:
        if len(raw_atribs_values) != len(atribs_type):
            raise Exception("data definition do not match given data!")

        descriptor_values = []
        for i in range(len(raw_atribs_values)):
            if not atribs_type[i]:
                parsed_value = float(raw_atribs_values[i].replace(",", "."))
            else:
                parsed_value = raw_atribs_values[i]
            descriptor_values.append(parsed_value)
        return descriptor_values

    def add_descriptor(self, descriptor: Descriptor) -> None:
        self.__descriptors.append(descriptor)

    def get_descriptor(self, index: int) -> Descriptor:
        return self.__descriptors[index]

    def get_all_descriptors(self) -> List[Descriptor]:
        return self.__descriptors

    def get_descriptors_by_class_name(self, class_name: str) -> List[Descriptor]:
        list_of_descriptors = []
        for descriptor in self.__descriptors:
            if descriptor.get_class_name() == class_name:
                list_of_descriptors.append(descriptor)
        return list_of_descriptors

    def get_values_from_descriptors(
        self, index: int, class_name: Optional[str] = None
    ) -> List:
        if class_name:
            descriptors = self.get_descriptors_by_class_name(class_name=class_name)
        else:
            descriptors = self.get_all_descriptors()

        values = []
        for descriptor in descriptors:
            values.append(descriptor.get_value(index))
        return values

    def remove_descriptor(self, index: int) -> None:
        self.__descriptors.remove(index)

    def add_plot(
        self,
        subplots_info: Tuple[int, int],
        subplots_data: List[Tuple[int, int]],
        selected_classes: Optional[List[str]] = None,
        show_plot: Optional[bool] = False,
        save_plot: Optional[bool] = False,
    ) -> None:
        if selected_classes:
            classes = selected_classes
        else:
            classes = self.__class_names

        plotter = Plotter(subplots=subplots_info)
        count_classes = len(classes)
        current_plot = len(self.__plots)
        current_subplot = 1
        for subplot_data in subplots_data:
            index_x, index_y = subplot_data
            plotter.change_subplot(current_subplot)
            plotter.add_title(f"Plot {current_subplot}")
            plotter.add_labels(
                f"data from index: {index_x}", f"data from index: {index_y}"
            )
            colors = distinctipy.get_colors(count_classes)
            for i in range(count_classes):
                values_x = self.get_values_from_descriptors(index_x, classes[i])
                values_y = self.get_values_from_descriptors(index_y, classes[i])
                plotter.draw_points(
                    values_x,
                    values_y,
                    color=colors[i],
                    label=f"class= {classes[i]}",
                )
            current_subplot += 1
        if save_plot:
            plotter.save(f"plot_{current_plot}")
            self.__plots.append(f"plot_{current_plot}")
        plotter.show() if show_plot else None
        plotter.close()

    def show_plot(self, file_name: str) -> None:
        if file_name in self.__plots:
            img = Image.open(f"plots/{file_name}.png")
            img.show()
        else:
            raise Exception(
                f"Plot with that name does not exist! Choices are: {self.__plots}"
            )

    def __str__(self):
        return f"DecisionSystem: name= {self.__name}, descriptors= {self.__descriptors}"
