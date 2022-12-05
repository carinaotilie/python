import numpy as np

def RungeKutta2(f, U0, T, n):
    dt = T/n
    t = np.linspace(0, T, n+1)
    u = np.zeros(len(t))
    u[0] = U0
    for k in range(n+1):
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u[k+1] = u[k] + K2

    return u, t

class RungeKutta2(ForwardEuler):
    def advance(self):
        f, t, u, k = self.f, self.t, self.u, self.k
        dt = t[k+1] - t[k]
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        return u[k] + K2
