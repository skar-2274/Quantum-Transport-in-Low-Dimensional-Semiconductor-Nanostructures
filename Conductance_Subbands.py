from numpy import arange, array, pi, cos
import matplotlib.pyplot as plt
from Conductance_class import Equations
from Constants import hbar, e, m
import sys

def graph():
    w_x = 1/hbar
    w_y, w_c, V_sd, B, theta, g = 2*w_x, 2*w_x, 0, 0, pi/2, 1

    Traces = 50 #Increments to increase the source drain voltage and number of energy level
    n, n_inc = 0, 1

    x_initial = arange(0, 16, 0.1)

    G_values = []

    for i in range(0, Traces):
        equation = Equations(w_x, w_y, w_c, g, V_sd, B, theta)
        G = 0.5 * equation.T(n, x_initial - i)
        G_values.append(G)
        n = n + n_inc

    G_values = array(G_values)

    x_min, x_max = x_initial.min(), x_initial.max()
    G_min, G_max = G_values.min(), G_values.max()

    # View all Conductance on one graph
    fig, ax = plt.subplots()
    ax.set_title(r'Material Conductance Values', fontsize=20)
    ax.set_xlabel(r'Fermi Energy $(E_{F}-U_{0})/(\hbar \omega_{x})$', fontsize=20)
    ax.set_ylabel(r'Conductance G ($\frac{2e^2}{h}$)', fontsize=20)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(G_min, G_max + 0.25)

    plt.grid(True)

    for i in range(0, Traces):
        ax.plot(x_initial, G_values[i])

    plt.show()

if __name__ == "__main__":
    graph()
