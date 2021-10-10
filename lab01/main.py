from utils.decision_system import DecisionSystem

def main():
    decision_system = DecisionSystem(name="iris_decision_system")
    decision_system.load_descriptors_from_file("lab01/data/iris-type.txt", "lab01/data/iris.txt")
    print(decision_system)

if __name__ == "__main__":
    main()