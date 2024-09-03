from numpy import arange, array, pi, cos
import matplotlib.pyplot as plt
from Differential_class_Lande_g_Factor import Equations
from Constants import hbar, e, m
import sys

def graph():
    w_x = 1/hbar
    w_y, w_c, B, V_sd, theta, n = 2*w_x, 2*w_x, 1, 1, pi/2, 5

    Traces = 30 #Increments to increase the g-factor and number of energy level
    g, g_inc = 0, 0.20

    x_initial = arange(0, 20, 0.1)

    dG_values = []

    for i in range(0, Traces):
        equation = Equations(w_x, w_y, w_c, g, V_sd, B, theta)
        dG = 0.5*equation.T(n, x_initial) + 2*i
        dG_values.append(dG)
        g = g + g_inc

    dG_values = array(dG_values)

    x_min, x_max = x_initial.min(), x_initial.max()
    dG_min, dG_max = dG_values.min(), dG_values.max()

    # View all Conductance on one graph
    fig, ax = plt.subplots()
    ax.set_title(r'Material Conductance Values', fontsize=20)
    ax.set_xlabel(r'Landé g-factor', fontsize=20)
    ax.set_ylabel(r'Differential of the Conductance $\frac{dG}{dg}$', fontsize=20)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(dG_min, dG_max + 1)

    plt.grid(True)

    for i in range(0, Traces):
        ax.plot(x_initial, dG_values[i])

    plt.show()

if __name__ == "__main__":
    graph()
