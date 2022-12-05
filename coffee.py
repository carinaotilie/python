import numpy as np
import ODESolver
import matplotlib.pyplot as plt

class Problem:
    def __init__(self, h, Ts):
        self.h = h
        self.Ts = Ts

    def __call__(self, T, t):
        h = self.h
        Ts = self.Ts

        return (-h*(T - Ts))

    def terminate(self, T, t, step_no):
        #return true when asymptotic value R is reached
        tol = self.Ts * 0.01
        return abs(T[step_no] - self.Ts) < tol


def estimate_h(t1, Ts, T0, T1):
    return (T1-T0)/(t1*(Ts-T0))


for Ts in [20, 25]:
    T0 = 95; T1 = 92; t1 = 15
    h = estimate_h(t1, Ts, T0, T1)
    problem = Problem(h, Ts)
    solver = ODESolver.ForwardEuler(problem)
    solver.set_initial_condition(95)
    timepoints = np.linspace(0, 15, 1000)
    T, t = solver.solve(timepoints, terminate = problem.terminate)

plt.plot(t, T)
plt.show()
