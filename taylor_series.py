import numpy as np

def taylor_exp_diffeq(x, N):
    s = 1
    e, a = np.zeros(N+1)
    e[0] = 0
    a[0] = 1
    for n in range(N):
        e[n+1] = e[n] + a[n]
        a[n+1] = (x/n)*a[n]

    return e
