from utils.algorithms.algorithm_greedy_match import AlgorithmGreedyMatch
from utils.bitmap import Bitmap
import matplotlib.pyplot as plt
import numpy as np

def main():
    reference_matrix_1 = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
    ]
    reference_matrix_2 = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1],
    ]
    reference_matrix_3 = [
        [1, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 0],
    ]
    test_matrix = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
    ]

    reference_bitmaps = [
        Bitmap(reference_matrix_1, "ref_1"),
        Bitmap(reference_matrix_2, "ref_2"),
        Bitmap(reference_matrix_3, "ref_3"),
    ]
    test_bitmap = Bitmap(test_matrix, None)

    algorithm = AlgorithmGreedyMatch(reference_bitmaps)
    classified_bitmap = algorithm.classify_bitmap(test_bitmap, show_output=True)
    print(classified_bitmap)


if __name__ == "__main__":
    main()
