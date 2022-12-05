import ODESolver
import numpy as np
import matplotlib.pyplot as plt

"""Example on using the ODESolver class hierarchy. We solve the
ODE for logistic growth:
u' = alpha*u*(1-u/R), u(0) = 0.1
A class is used to represent the right hand side function.
"""

class Logistic:
    def __init__(self,alpha,R):
        self.alpha = alpha
        self.R = R

    def __call__(self,u,t):
        return self.alpha*u*(1-u/self.R)


#initialize the ODE
alpha = 0.5
R = 5.0
U0 = 0.1
problem = Logistic(alpha,R)


#create an array of time points
time = np.linspace(0,20,200)

#initialize the solver object
solver = ODESolver.BackwardEuler(problem)
solver.set_initial_condition(U0)

#solve the problem
u,t = solver.solve(time)
plt.plot(t,u)
plt.xlabel('time')
plt.ylabel('u')
plt.title('Logistic growth, U0 = %g, alpha = %g, R = %g' %(U0,alpha, R))
plt.show()
