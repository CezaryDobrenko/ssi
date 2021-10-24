from utils.evolution_one_plus_one import AlgorithmOnePlusOne

def main():
    bounds = (0,100)
    epochs = 100

    algorithm = AlgorithmOnePlusOne(bounds)
    algorithm.evolve(epochs, show_plot=True)

            
if __name__ == "__main__":
    main()
