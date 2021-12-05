from utils.algorithms.algorithm_greedy_match import AlgorithmGreedyMatch
from utils.drawer import Drawer
from utils.bitmap import Bitmap

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

    reference_bitmaps = [
        Bitmap(reference_matrix_1, "ref_1"),
        Bitmap(reference_matrix_2, "ref_2"),
        Bitmap(reference_matrix_3, "ref_3"),
    ]

    drawer = Drawer((0,4), (0,5))
    test_matrix = drawer.draw_matrix()
    test_bitmap = Bitmap(test_matrix, None)

    algorithm = AlgorithmGreedyMatch(reference_bitmaps)
    algorithm.classify_bitmap(test_bitmap, show_output=True)


if __name__ == "__main__":
    main()