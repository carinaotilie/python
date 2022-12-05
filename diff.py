from math import sin

def diff(f, x, h):
    f_x = f(x)
    df = (f(x+h)-f(x))/h
    return f_x, df

func = lambda x: sin(x)
f, df = diff(func, 0, 0.001)
print('%-20.3f %.3f' % (f, df))

#print(diff(sin, 0.0, 0.001))
