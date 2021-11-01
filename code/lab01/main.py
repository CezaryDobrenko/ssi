from utils.decision_system import DecisionSystem

def main():
    decision_system = DecisionSystem(name="iris_decision_system")
    decision_system.load_descriptors_from_file(
        "data/iris-type.txt", "data/iris.txt"
    )

    print(decision_system.get_descriptor(1).get_value(2))
    print(decision_system.get_descriptor(1).get_value_type(2))
    print(decision_system.get_all_descriptors())
    print(decision_system.get_descriptors_by_class_name("Setosa"))


if __name__ == "__main__":
    main()
