from utils.decision_system import DecisionSystem
import matplotlib.pyplot as plt
import numpy as np

def main():
    decision_system = DecisionSystem(name="spirala_decision_system")
    decision_system.load_descriptors_from_file(
        "data/spirala-type.txt", "data/spirala.txt"
    )
    print(decision_system)



if __name__ == "__main__":
    main()