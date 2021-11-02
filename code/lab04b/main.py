from utils.algorithms.algorithm_mu_plus_lambda import AlgorithmMuPlusLambda


def main():
    epochs = 20
    mi_value = 4
    lambda_value = 10
    tournament_size = 2
    bounds = (0, 100)
    mutation_level = 10

    algorithm = AlgorithmMuPlusLambda(
        mi_value,
        lambda_value,
        bounds,
        mutation_level,
        tournament_size,
        save_each_epoch=True,
    )
    algorithm.evolve_population(epochs)
    print(algorithm.get_best_specimen())


if __name__ == "__main__":
    main()
