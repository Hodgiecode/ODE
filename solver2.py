from math import *

def func(x, y1, y2, s_dict, f, p, q):
    s_dict['x'] = x
    f_x = eval(f, s_dict)
    p_x = eval(p, s_dict)
    q_x = eval(q, s_dict)

    return f_x - q_x * y1 - p_x * y2
    

def Runge_Kutta(f0, a, h, n, f1, val, s_dict, f, p, q):
    y2 = []
    y1 = []

    y1.append(f0)
    y2.append(val)

    for i in range(n):
        x = a + h*i
        m1 = h*y2[i]
        k1 = h*func(x, y1[i], y2[i], s_dict, f, p, q)

        m2 = h*(y2[i] + k1/2.0)
        k2 = h*func(x + h/2.0, y1[i]+m1/2.0,  y2[i]+k1/2.0, s_dict, f, p, q)

        m3 = h*(y2[i] + k2/2.0)
        k3 = h*func(x + h/2.0, y1[i]+m2/2.0, y2[i]+(k2/2.0), s_dict, f, p, q)

        m4 = h*(y2[i] + k3)
        k4 = h*func(x + h, y1[i]+m3, y2[i]+k3, s_dict, f, p, q)

        y1.append(y1[i]+(m1 + 2*(m2+m3)+m4)/6.0)
        y2.append(y2[i]+(k1 + 2*(k2 + k3)+k4)/6.0)

    return y1

def shoot(y_a, a, h, n, f1, val, s_dict, f, p, q):
	y1 = Runge_Kutta(y_a, a, h, n, f1, val, s_dict, f, p, q)
	return y1[n] - f1, y1
    
def iteration(a, b, f0, f1, n, s_dict, f, p, q):
    delta_func = 0
    border = 0.00000001

    derivative_f = 0

    h = (b-a)/float(n)
    test_x_1 = -10
    test_x_2 = 10

    while True:
        func_1, y11 = shoot(f0, a, h, n, f1, test_x_1, s_dict, f,p,q)
        func_2, y12 = shoot(f0, a, h, n, f1, test_x_2, s_dict, f,p,q)

        if (func_1*func_2 > 0): break

        test_x_3 = (test_x_1 + test_x_2) / 2
        func_3, y13 = shoot(f0, a, h, n, f1, test_x_3, s_dict, f,p,q)

        if (func_3*func_1 > 0): test_x_1 = test_x_3
        if (func_3*func_2 > 0): test_x_2 = test_x_3
        if ((abs(func_1) < border) or (abs(func_2) < border)): break
		
    return y12

def calc(a, b, f0, f1, eps, n, f, p, q):
    #########
    s_lst=['acos','asin','atan','atan2','ceil','cos','cosh','degrees','e','exp','fabs','floor','fmod','frexp','hypot','ldexp','log','log10',
            'modf','pi','pow','radians','sin','sinh','sqrt','tan','tanh']

    s_dict = dict([(k,locals().get(k,None)) for k in s_lst])
    s_dict['pi'] = pi
    s_dict['exp'] = exp
    s_dict['abs'] = fabs
    s_dict['sin'] = sin
    s_dict['cos'] = cos
    s_dict['tan'] = tan
    s_dict['log'] = log
    s_dict['log10'] = log10
    s_dict['tan'] = tan
    s_dict['sqrt'] = sqrt
    s_dict['asin'] = asin
    #################
    
    max_iter = 0

    ########
    h = (b-a)/float(n)
    test_1, test_2 = [], []
    h1 = h
    h2 = h * 0.1
    n1 = n
    n2 = 10 * n1
    index1 = 0
    index2 = 0
    flag = 1

    y = iteration(a, b, f0, f1, n, s_dict, f, p, q)

    r = []
    for i in range(len(y)):
        r.append([a + h*i, y[i]])
    
    return r

#calc(1,3,1,27,0.000001,40,"0","1/x","-9/(x*x)")
