import ODESolver
import numpy as np
import matplotlib.pyplot as plt

class ElectricCircuit :
    def __init__(self,L,R,C):
           self.L, self.R, self.C = L, R, C

    def __call__(self, u, t):
        L, R, C = self.L, self.R, self.C

        def E(t):
            return 2*np.sin(np.sqrt(3.5)*t)

        I = u[0]; Q = u[1]
        du_Q = I
        du_I = (E(t)-R*I-(Q/C))/L
        return np.array([du_I, du_Q])


L = 1
omega = np.sqrt(3.5)
dt = 2*np.pi/(60*omega)
period = (2*np.pi)/omega
C = 0.25
R = 0.2
U0 = (1, 1)

t = np.linspace(0, 10*period, 10000)

electric = ElectricCircuit(L, R, C)

solver = ODESolver.ForwardEuler(electric)
solver.set_initial_condition(U0)

u, t = solver.solve(t)

plt.plot(t, u)
plt.xlabel('time')
plt.ylabel('u')
plt.legend()
plt.show()
