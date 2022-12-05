import numpy as np
import matplotlib.pyplot as plt
import ODESolver


class Decay:
    def __init__(self, a):
        self.a = a

    def __call__ (self, u, t):
        return -self.a*u

u0 = 1
a = (np.log(2)/5600)
decay = Decay(a)

#create array of time points, years
t = np.linspace(0, 20000, 500)

solver = ODESolver.BackwardEuler(decay)
solver.set_initial_condition(u0)

u_exact = np.exp(-a*t)

u, t = solver.solve(t)

plt.plot(t, u, 'r--', label = 't vs u, numerical solution')
plt.plot(t, u_exact, 'b--', label = 't vs u_exact, exact value')
plt.xlabel('time')
plt.ylabel('u')
plt.title('Simulation radioactive decay')
plt.legend()
plt.show()
