from typing import List, Tuple

from utils.bitmap import Bitmap
from utils.plotter import Plotter


class HopfieldNetwork:
    __reference_bitmaps: List[Bitmap]
    __weight_matrix: List[List[int]]
    __bitmap_size: Tuple[int, int]
    __training_sets: List[List[int]]

    def __init__(self, reference_bitmaps: List[Bitmap], bitmap_size: Tuple[int, int]):
        self.__reference_bitmaps = reference_bitmaps
        self.__bitmap_size = bitmap_size
        self.__weight_matrix = self.__initialize_weight_matrix(bitmap_size)
        self.__training_sets = self.__initialize_training_sets(reference_bitmaps)

    def fix_bitmap(self, input_bitmap: Bitmap) -> Bitmap:
        test_set = self.__convert_bitmap_to_training_set(input_bitmap)
        for i in range(len(test_set)):
            tmp_sum = 0
            for j in range(len(test_set)):
                if i != j:
                    tmp_sum += test_set[j] * self.__weight_matrix[i][j]
            prediction_value = self.sigma_function(tmp_sum)
            if test_set[i] != prediction_value:
                test_set[i] *= -1

        output_bitmap = self.__convert_training_set_to_bitmap(test_set)
        reference_bitmap = self.__get_identified_bitmap(test_set)
        self.__draw_output(input_bitmap, output_bitmap, reference_bitmap)
        return output_bitmap

    def __initialize_weight_matrix(
        self, bitmap_size: Tuple[int, int]
    ) -> List[List[int]]:
        x_dimension, y_dimension = bitmap_size
        size = x_dimension * y_dimension
        return [[0 for _ in range(size)] for _ in range(size)]

    def __initialize_training_sets(
        self, reference_bitmaps: List[Bitmap]
    ) -> List[List[int]]:
        training_sets = []
        for reference_bitmap in reference_bitmaps:
            training_set = self.__convert_bitmap_to_training_set(reference_bitmap)
            training_sets.append(training_set)
        self.__train_network(training_sets)
        return training_sets

    def __train_network(self, training_sets: List[List[int]]) -> None:
        training_matrixes = []
        for training_set in training_sets:
            matrix = []
            for current_bit in training_set:
                matrix.append([bit * current_bit for bit in training_set])
            training_matrixes.append(matrix)

        for training_matrix in training_matrixes:
            for y in range(len(training_matrix)):
                for x in range(len(training_matrix[y])):
                    if x == y:
                        self.__weight_matrix[y][x] = 0
                    else:
                        self.__weight_matrix[y][x] += training_matrix[y][x]

    def add_bitmap_to_training_set(self, bitmap: Bitmap) -> None:
        test_set = self.__convert_bitmap_to_training_set(bitmap)
        self.__training_sets.append(test_set)
        self.__weight_matrix = self.__initialize_weight_matrix(self.__bitmap_size)
        self.__train_network(self.__training_sets)

    def sigma_function(self, value: int) -> int:
        if value >= 0:
            return 1
        return -1

    def __get_identified_bitmap(self, test_set: List[int]) -> Bitmap:
        for index in range(len(self.__training_sets)):
            if self.__training_sets[index] == test_set:
                return self.__reference_bitmaps[index]

    def __draw_output(
        self, input_bitmap: Bitmap, output_bitmap: Bitmap, reference_bitmap: Bitmap
    ) -> None:
        plotter = Plotter(subplots=(1, 3))
        plotter.add_title(f"input bitmap")
        plotter.draw_monochromatic_bitmap(input_bitmap)
        plotter.change_subplot(2)
        plotter.add_title(f"output bitmap")
        plotter.draw_monochromatic_bitmap(output_bitmap)
        plotter.change_subplot(3)
        plotter.add_title(f"reference bitmap")
        plotter.draw_monochromatic_bitmap(reference_bitmap)
        plotter.show()

    def __convert_bitmap_to_training_set(self, bitmap: Bitmap) -> List[int]:
        bitmap_matrix = bitmap.get_matrix()
        training_set = []
        for row in bitmap_matrix:
            for item in row:
                if item == 1:
                    training_set.append(1)
                else:
                    training_set.append(-1)
        return training_set

    def __convert_training_set_to_bitmap(self, training_set: List[int]) -> Bitmap:
        x_dimension, y_dimension = self.__bitmap_size
        converted_training_set = []
        for bit in training_set:
            if bit < 0:
                converted_training_set.append(0)
            else:
                converted_training_set.append(1)

        bitmap_matrix = []
        index = 0
        for _ in range(y_dimension):
            row = []
            for _ in range(x_dimension):
                row.append(converted_training_set[index])
                index += 1
            bitmap_matrix.append(row)

        return Bitmap(bitmap_matrix)
