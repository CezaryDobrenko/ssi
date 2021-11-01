from matplotlib.pyplot import show
from utils.decision_system import DecisionSystem
from utils.plotter import Plotter


def draw_face():
    plotter = Plotter()
    plotter.add_grid()
    plotter.draw_point(-1, 1, size=30, color="blue", label="upper face")
    plotter.draw_point(0, 0, size=30, color="blue", label="upper face")
    plotter.draw_point(1, 1, size=30, color="blue", label="upper face")
    plotter.draw_curve((-2, 0), (0, -2), style="r-", label="outer face")
    plotter.draw_curve((-2, 0), (0, 2), style="r-", label="outer face")
    plotter.draw_curve((2, 0), (0, -2), style="r-", label="outer face")
    plotter.draw_curve((2, 0), (0, 2), style="r-", label="outer face")
    plotter.draw_curve((-1, 0), (0, -1), style="y-", label="smile")
    plotter.draw_curve((0, -1), (1, 0), style="y-", label="smile")
    plotter.show()


def subplot_example():
    plotter = Plotter(subplots=(2, 3))

    x = [1, 2, 3]
    y = [1, -1, 3]
    plotter.draw_poly_line(x, y, label="ployline example")

    plotter.change_subplot(2)
    plotter.draw_point(1, 2, label="point example")

    plotter.change_subplot(3)
    plotter.draw_line((1, 2), (2, 3), style="r-", label="line example")

    plotter.change_subplot(5)
    plotter.draw_curve((1, 2), (2, 3), style="r-", label="curve example")
    plotter.draw_point(2, 2, size=20, color="blue", label="point example")
    plotter.show()


def main():
    # draw_face()
    # subplot_example()

    decision_system = DecisionSystem(name="iris_decision_system")
    decision_system.load_descriptors_from_file(
        "data/iris-type.txt", "data/iris.txt"
    )
    decision_system.add_plot(
        subplots_info=(2, 2),
        subplots_data=[(2, 3), (1, 3), (0, 3), (1, 2)],
        show_plot=False
    )
    decision_system.add_plot(
        subplots_info=(2, 2),
        subplots_data=[(1, 2), (2, 3), (1, 3), (3, 2)],
        show_plot=False
    )
    #decision_system.show_plot("plot_1")
    decision_system.show_plots()


if __name__ == "__main__":
    main()
