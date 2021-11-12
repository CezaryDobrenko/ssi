from utils.algorithms.algorithm_k_means import AlgorithmKMeans
from utils.decision_system import DecisionSystem


def main():
    k = 4
    iterations = 100
    decision_system = DecisionSystem(name="spirala_decision_system")
    decision_system.load_descriptors_from_file(
        "data/spirala-type.txt", "data/spirala.txt"
    )

    algorithm = AlgorithmKMeans(decision_system, k)
    algorithm.execute(iterations, save_each_iteration_plot=False, show_final_plot=True)


if __name__ == "__main__":
    main()
