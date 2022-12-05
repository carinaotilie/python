from ODESolver import *
import numpy as np
import matplotlib.pyplot as plt


class Decay:
    def __init__(self, tau_a, tau_b):
        self.tau_a = tau_a
        self.tau_b = tau_b
        #tar inn parametre og lagrer

    def __call__(self, u, t): #argumenter alltid være u og t
    #self om t ikke inngår! alltid u, t med
        u_a = u[0]
        u_b = u[1]
        tau_a = self.tau_a
        tau_b = self.tau_b

        du_a = u_b/tau_b - u_a/tau_a
        du_b = u_a/tau_a - u_b/tau_b
        return du_a, du_b

problem = Decay(tau_a = 8, tau_b = 40)
solver = RungeKutta4(problem) #kallbar funksjon!

dt = 10.0/60 #tidssteg
t_stop = 150
n = round(t_stop/dt) #round avslutter til nærmeste heltall
t = np.linspace(0, t_stop, n+1)
U0 = (1,1)
solver.set_initial_condition(U0)
u, t = solver.solve(t)

plt.plot(t,u)
plt.show()
