from numpy import arange, array, pi, cos
import matplotlib.pyplot as plt
from w_c_class import Equations
from Constants import hbar, e, m
import sys

def graph():
    w_x = 1/hbar
    w_y, B, V_sd, theta, n = 2*w_x, 2, 0*hbar*w_x/e, pi, 4

    Traces = 20 #Increments to increase the g-factor and number of energy level
    g, g_inc = 0, 0.5

    x_initial = arange(0, 65, 0.1)

    G_values = []

    for i in range(0, Traces):
        equation = Equations(w_x, w_y, g, V_sd, B, theta)
        G = 0.5 * equation.T(n, x_initial - 2 * i)
        G_values.append(G)
        g = g + g_inc

    G_values = array(G_values)

    x_min, x_max = x_initial.min(), x_initial.max()
    G_min, G_max = G_values.min(), G_values.max()

    # View all Conductance on one graph
    fig, ax = plt.subplots()
    ax.set_title(r'Material Conductance Values', fontsize=20)
    ax.set_xlabel(r'Landé g-factor', fontsize=20)
    ax.set_ylabel(r'Conductance G ($\frac{2e^2}{h}$)', fontsize=20)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(G_min, G_max + 0.25)

    plt.grid(True)

    for i in range(0, Traces):
        ax.plot(x_initial, G_values[i])

    plt.show()

if __name__ == "__main__":
    graph()
