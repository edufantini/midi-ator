import matplotlib.pyplot as plt
import numpy as np

def print_graph(time, seq, events):

    fig, ax = plt.subplots()
    scatter = ax.scatter(time, seq, c=events)

    # produce a legend with the unique colors from the scatter
    legend1 = ax.legend(*scatter.legend_elements(),
                        loc="best", title="Evento")

    plt.show()
