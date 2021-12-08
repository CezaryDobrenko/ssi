import math
from typing import List, Optional, Tuple

from utils.bitmap import Bitmap
from utils.plotter import Plotter


class AlgorithmGreedyMatch:
    __reference_bitmaps: List[Bitmap]

    def __init__(self, reference_bitmaps: List[Bitmap]):
        self.__reference_bitmaps = reference_bitmaps

    def classify_bitmap(
        self, test_bitmap: Bitmap, show_output: Optional[bool] = False
    ) -> Bitmap:
        bitmaps_distance = {}
        for reference_bitmap in self.__reference_bitmaps:
            reference_class = reference_bitmap.get_class_name()
            measure_1 = self.calculate_measure_of_dissimilarity(
                reference_bitmap, test_bitmap
            )
            measure_2 = self.calculate_measure_of_dissimilarity(
                test_bitmap, reference_bitmap
            )
            distance = -measure_1 - measure_2
            bitmaps_distance[reference_class] = distance
        most_similar_class = max(bitmaps_distance, key=bitmaps_distance.get)
        test_bitmap.set_class_name(most_similar_class)
        if show_output:
            ref_bitmap = self.get_reference_bitmap_by_class_name(most_similar_class)
            self.__draw_output(test_bitmap, ref_bitmap)
        return test_bitmap

    def calculate_measure_of_dissimilarity(
        self, reference_bitmap: Bitmap, test_bitmap: Bitmap
    ):
        measure = 0
        test_matrix = test_bitmap.get_matrix()
        reference_matrix = reference_bitmap.get_matrix()
        for test_x in range(len(test_matrix)):
            test_row = test_matrix[test_x]
            for test_y in range(len(test_row)):
                start_point = (test_x, test_y)
                min_distance = float("inf")
                if test_matrix[test_x][test_y] == 1:
                    for ref_x in range(len(reference_matrix)):
                        ref_row = reference_matrix[ref_x]
                        for ref_y in range(len(ref_row)):
                            if reference_matrix[ref_x][ref_y] == 1:
                                end_point = (ref_x, ref_y)
                                cur_distance = self.__calculate_euclidean_distance(
                                    start_point, end_point
                                )
                                min_distance = min(min_distance, cur_distance)
                    measure = measure + min_distance
        return measure

    def __calculate_euclidean_distance(
        self, start_point: Tuple[int, int], end_point: Tuple[int, int]
    ) -> float:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return math.sqrt(
            math.pow((start_x - end_x), 2) + math.pow((start_y - end_y), 2)
        )

    def __draw_output(self, test_bitmap: Bitmap, ref_bitmap: Bitmap) -> None:
        plotter = Plotter(subplots=(1, 2))
        plotter.add_title(f"reference bitmap class: {ref_bitmap.get_class_name()}")
        plotter.draw_monochromatic_bitmap(ref_bitmap)
        plotter.change_subplot(2)
        plotter.add_title(f"test bitmap classified as: {test_bitmap.get_class_name()}")
        plotter.draw_monochromatic_bitmap(test_bitmap)
        plotter.show()

    def __calculate_manhattan_distance(
        self, start_point: Tuple[int, int], end_point: Tuple[int, int]
    ) -> int:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return abs(start_x - end_x) + abs(start_y - end_y)

    def add_reference_bitmap(self, reference_bitmap: Bitmap) -> None:
        if not reference_bitmap.get_class_name():
            raise Exception("Reference bitmap must have a class defined!")
        self.__reference_bitmaps.append(reference_bitmap)

    def remove_reference_bitmap(self, index: int) -> None:
        if index > len(self.__reference_bitmaps):
            raise Exception("Bitmap with given index does not exist!")
        self.__reference_bitmaps.remove(index)

    def get_reference_bitmap(self, index: int) -> Bitmap:
        if index > len(self.__reference_bitmaps):
            raise Exception("Bitmap with given index does not exist!")
        return self.__reference_bitmaps[index]

    def get_reference_bitmap_by_class_name(self, class_name: str) -> Bitmap:
        ref_bitmap_output = None
        for ref_bitmap in self.__reference_bitmaps:
            if ref_bitmap.get_class_name() == class_name:
                ref_bitmap_output = ref_bitmap
        if not ref_bitmap_output:
            raise Exception("Bitmap with given class name does not exist!")
        return ref_bitmap_output

    def __str__(self):
        return f"AlgorithmGreedyMatch: reference_bitmaps: {self.__reference_bitmaps}"
