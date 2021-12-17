from utils.algorithms.algorithm_fuzzy_controller import AlgorithmFuzzyController


def main():
    for _ in range(1):
        algorithm = AlgorithmFuzzyController()
        algorithm.play(save_frames=False, freeze_on_end=False, save_logs=True)
        game_result = algorithm.get_game_result()
        print(game_result)


if __name__ == "__main__":
    main()
