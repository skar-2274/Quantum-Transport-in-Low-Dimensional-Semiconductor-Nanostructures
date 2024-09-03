from numpy import arange, array, pi, cos
import matplotlib.pyplot as plt
from Differential_class_Voltage import Equations
from Constants import hbar, e, m
import sys

def graph():
    w_x = 1/hbar
    w_y, w_c, B, theta, g, n = 2*w_x, 0*w_x, 0, pi/2, 0.5, 4

    Traces = 20 #Increments to increase the source drain voltage and number of energy level
    V_sd, V_sd_inc, V_sd_unit = 0, 0.5, hbar*w_x/e

    x_initial = arange(0, 15, 0.1)

    dG_values = []

    for i in range(0, Traces):
        equation = Equations(w_x, w_y, w_c, g, V_sd, B, theta)
        dG = 0.5*equation.T(n, x_initial) + 0.5*i
        dG_values.append(dG)
        V_sd = (V_sd + V_sd_inc)*V_sd_unit

    dG_values = array(dG_values)

    x_min, x_max = x_initial.min(), x_initial.max()
    dG_min, dG_max = dG_values.min(), dG_values.max()

    # View all Conductance on one graph
    fig, ax = plt.subplots()
    ax.set_title(r'Material Conductance Values', fontsize=20)
    ax.set_xlabel(r'Fermi Energy $(E_{F}-U_{0})/(\hbar \omega_{x})$', fontsize=20)
    ax.set_ylabel(r'Differential of the Conductance $\frac{dG}{dV_{sd}}$', fontsize=20)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(dG_min, dG_max + 0.25)

    plt.grid(True)

    for i in range(0, Traces):
        ax.plot(x_initial, dG_values[i])

    plt.show()

if __name__ == "__main__":
    graph()
