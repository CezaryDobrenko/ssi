from utils.algorithms.algorithm_hopfield_network import HopfieldNetwork
from utils.bitmap import Bitmap
from utils.drawer import Drawer


def main():
    reference_matrix_1 = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
    ]
    reference_matrix_2 = [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],
    ]
    reference_matrix_3 = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ]

    reference_bitmaps = [
        Bitmap(reference_matrix_1),
        Bitmap(reference_matrix_2),
        Bitmap(reference_matrix_3),
    ]

    drawer = Drawer((0, 5), (0, 5))
    test_matrix = drawer.draw_matrix()
    test_bitmap = Bitmap(test_matrix)

    algorithm = HopfieldNetwork(reference_bitmaps, (5, 5))
    algorithm.fix_bitmap(test_bitmap)


if __name__ == "__main__":
    main()
