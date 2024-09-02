from numpy import sqrt, exp, pi, arange, cos
import matplotlib.pyplot as plt
from Constants import hbar, e, m, mu_B

class Equations:
    def __init__ (self, w_x, w_y, g, V_sd, B, theta):
        self.w_x = w_x
        self.w_y = w_y
        self.V_sd = V_sd
        self.B = B
        self.theta = theta
        self.e = e
        self.m = m
        self.g = g

    def w_c(self):
        e = self.e
        B = self.B
        theta = self.theta
        m = self.m

        w_c = e * B * cos(theta) / m

        return float(w_c)

    def w(self):
        w_c = self.w_c()
        w_x = self.w_x
        w_y = self.w_y

        w = w_c**2 + w_y**2 - w_x**2

        return float(w)

    def E_1(self):
        w_x = self.w_x
        w_y = self.w_y
        w = self.w()

        E1 = hbar/(2*pi*sqrt(2))*((w**2 + 4*(w_x**2)*(w_y**2))**0.5 - w)**0.5

        return float(E1)

    def E_2(self):
        w_x = self.w_x
        w_y = self.w_y
        w = self.w()

        E2 = hbar/(sqrt(2))*((w**2 + 4*(w_x**2)*(w_y**2))**0.5 + w)**0.5

        return float(E2)

    def z(self, S): #Zeeman term
        g = self.g
        B = self.B
        return g*mu_B*S*B

    def Tf(self, n, x): #Forward Transmission
        S_up = 0.5 #Spin terms
        S_down = -0.5
        w_x = self.w_x
        e = self.e
        V_sd = self.V_sd

        E_1 = self.E_1()
        E_2 = self.E_2()

        tf = (0.5*(1 + exp(-(hbar*w_x*x + 0.5*e*V_sd -(n + 0.5)*E_2 + self.z(S_up))/E_1))**(-1)
        + 0.5*(1 + exp(-(hbar*w_x*x + 0.5*e*V_sd -(n + 0.5)*E_2 + self.z(S_down))/E_1))**(-1))

        return tf

    def Tb(self, n, x): #Backward Transmission
        S_up = 0.5 #Spin terms
        S_down = -0.5
        w_x = self.w_x
        e = self.e
        V_sd = self.V_sd

        E_1 = self.E_1()
        E_2 = self.E_2()

        tb = (0.5*(1 + exp(-(hbar*w_x*x - 0.5*e*V_sd -(n + 0.5)*E_2 + self.z(S_up))/E_1))**(-1)
        + 0.5*(1 + exp(-(hbar*w_x*x - 0.5*e*V_sd -(n + 0.5)*E_2 + self.z(S_down))/E_1))**(-1))

        return tb

    def T(self, n, x): #Total Transmission
        result = 0
        for i in range (0, n + 1):
            result = result + self.Tf(i, x) + self.Tb(i, x)

        return result
