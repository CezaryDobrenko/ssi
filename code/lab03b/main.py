import math
import random

from utils.algorithms.algorithm_fuzzy_c_means import AlgorithmFuzzyCMeans
from utils.decision_system import DecisionSystem


def main():
    iters = 20
    fcm_m = 2
    c = 3
    decision_system = DecisionSystem(name="spirala_decision_system")
    decision_system.load_descriptors_from_file(
        "data/spirala-type.txt", "data/spirala.txt"
    )

    algorithm = AlgorithmFuzzyCMeans(decision_system, fcm_m, c)
    algorithm.execute(iters, save_each_iter_plot=True, show_final_plot=True)


if __name__ == "__main__":
    main()
