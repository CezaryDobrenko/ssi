from utils.algorithms.algorithm_firefly import AlgorithmFirefly

def main():
    gamma_0 = 0.1
    beta_0 = 0.3
    N = 20
    mu_0 = 0.05
    epochs = 20
    bounds = (0, 100)

    algorithm = AlgorithmFirefly(
        gamma_0, 
        beta_0, 
        mu_0, 
        N, 
        bounds, 
        save_each_epoch=True
    )
    algorithm.evolve_population(epochs)




if __name__ == "__main__":
    main()
