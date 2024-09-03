from numpy import sqrt, exp, pi, arange, cos
import matplotlib.pyplot as plt
from Constants import hbar, e, m, mu_B

class Equations:
    def __init__ (self, w_x, w_y, g, w_c, V_sd, B, theta):
        self.w_x = w_x
        self.w_y = w_y
        self.V_sd = V_sd
        self.B = B
        self.theta = theta
        self.e = e
        self.m = m
        self.g = g
        self.w_c = w_c
        self.w = self.w_c**2 + self.w_y**2 - self.w_x**2

    def E_1(self):
        w_x = self.w_x
        w_y = self.w_y
        w = self.w

        E1 = hbar/(2*pi*sqrt(2))*((w**2 + 4*(w_x**2)*(w_y**2))**0.5 - w)**0.5

        return float(E1)

    def E_2(self):
        w_x = self.w_x
        w_y = self.w_y
        w = self.w

        E2 = hbar/(sqrt(2))*((w**2 + 4*(w_x**2)*(w_y**2))**0.5 + w)**0.5

        return float(E2)

    def Tf(self, n, x): #Forward Transmission

        w_x = self.w_x
        e = self.e
        V_sd = self.V_sd
        g = self.g
        B = self.B

        E_1 = self.E_1()
        E_2 = self.E_2()

        tf = (0.5*(0.5)*g*mu_B*exp((-B*(0.5)*g*mu_B + E_2*(n + 0.5) - 0.5*V_sd*e
        - hbar*x*w_x)/E_1)/(E_1*(exp((-B*(0.5)*g*mu_B + E_2*(n + 0.5) - 0.5*V_sd*e
        - hbar*x*w_x)/E_1) + 1)**2) + 0.5*(-0.5)*g*mu_B*exp((-B*(-0.5)*g*mu_B
        + E_2*(n + 0.5) - 0.5*V_sd*e - hbar*x*w_x)/E_1)/(E_1*(exp((-B*(-0.5)*g*mu_B
        + E_2*(n + 0.5) - 0.5*V_sd*e - hbar*x*w_x)/E_1) + 1)**2))

        return tf

    def Tb(self, n, x): #Backward Transmission

        w_x = self.w_x
        e = self.e
        V_sd = self.V_sd
        g = self.g
        B = self.B

        E_1 = self.E_1()
        E_2 = self.E_2()

        tb = (0.5*(0.5)*g*mu_B*exp((-B*(0.5)*g*mu_B + E_2*(n + 0.5) + 0.5*V_sd*e
        - hbar*x*w_x)/E_1)/(E_1*(exp((-B*(0.5)*g*mu_B + E_2*(n + 0.5) + 0.5*V_sd*e
        - hbar*x*w_x)/E_1) + 1)**2) + 0.5*(-0.5)*g*mu_B*exp((-B*(-0.5)*g*mu_B
        + E_2*(n + 0.5) + 0.5*V_sd*e - hbar*x*w_x)/E_1)/(E_1*(exp((-B*(-0.5)*g*mu_B
        + E_2*(n + 0.5) + 0.5*V_sd*e - hbar*x*w_x)/E_1) + 1)**2))

        return tb

    def T(self, n, x): #Total Transmission
        result = 0
        for i in range (0, n + 1):
            result = result + self.Tf(i, x) + self.Tb(i, x)

        return result
