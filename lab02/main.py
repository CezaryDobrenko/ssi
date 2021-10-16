from utils.decision_system import DecisionSystem
from utils.plotter import Plotter


def draw_face():
    plotter = Plotter()
    plotter.add_grid()
    plotter.draw_point(-1, 1, size=30, color="blue")
    plotter.draw_point(0, 0, size=30, color="blue")
    plotter.draw_point(1, 1, size=30, color="blue")
    plotter.draw_curve((-2, 0), (0, -2), style="r-")
    plotter.draw_curve((-2, 0), (0, 2), style="r-")
    plotter.draw_curve((2, 0), (0, -2), style="r-")
    plotter.draw_curve((2, 0), (0, 2), style="r-")
    plotter.draw_curve((-1, 0), (0, -1), style="y-")
    plotter.draw_curve((0, -1), (1, 0), style="y-")
    plotter.show()


def subplot_example():
    plotter = Plotter(subplots=(2, 3))

    x = [1, 2, 3]
    y = [1, -1, 3]
    plotter.draw_poly_line(x, y)

    plotter.change_subplot(2)
    plotter.draw_point(1, 2)

    plotter.change_subplot(3)
    plotter.draw_line((1, 2), (2, 3), "r-")

    plotter.change_subplot(5)
    plotter.draw_curve((1, 2), (2, 3), "r-")
    plotter.draw_point(2, 2, size=20, color="blue")

    plotter.show()


def main():
    # draw_face()
    # subplot_example()

    decision_system = DecisionSystem(name="iris_decision_system")
    decision_system.load_descriptors_from_file(
        "lab01/data/iris-type.txt", "lab01/data/iris.txt"
    )
    decision_system.add_plot(
        subplots_info=(2, 2),
        subplots_data=[(2, 3), (1, 3), (0, 3), (1, 2)],
        show_plot=True,
    )


if __name__ == "__main__":
    main()
