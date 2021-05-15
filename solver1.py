from math import *

def funct(x, y, s_dict, f):
    s_dict['x'] = x
    s_dict['y'] = y
    a=eval(f,s_dict)
    return a

def Kuntzmann_Butcher(y_a, a, h, n, s_dict, f):
     ########
     y = []
     t = a
     '''
     Формула отсюда https://books.google.co.uz/books?id=113xCAAAQBAJ&pg=PA204&lpg=PA204&dq=kuntzmann-butcher+method&source=bl&ots=bcK1gRqMRS&sig=ACfU3U1oLJ5frvd17D-jtUREhlw4o7wDXQ&hl=ru&sa=X&ved=2ahUKEwifkLDt6LjgAhXRw8QBHXMRDbgQ6AEwBHoECAgQAQ#v=onepage&q=kuntzmann-butcher%20method&f=false */
     страница 204
     '''
     #Барьеры
     rt15 = sqrt(15)
     a1 = (5 - rt15)/10.0
     a2 = 1.0/2
     a3 = (5 + rt15)/10.0
     b11 = 5.0/36
     b12 = 2.0/9 - rt15/15
     b13 = 5.0/36 - rt15/30
     b21 = 5.0/36 + rt15/24
     b22 = 2.0/9
     b23 = 5.0/36 - rt15/24
     b31 = 5.0/36 + rt15/30
     b32 = 2.0/9 + rt15/15
     b33 = 5.0/36
     c1 = 5.0/18
     c2 = 4.0/9
     c3 = 5.0/18
     ###########
     
     y.append(y_a)
     for i in range(n):
         k1 = h * funct(t + a1 * h, y[i], s_dict, f)
         k2 = h * funct(t + a2 * h, y[i], s_dict, f)
         k3 = h * funct(t + a3 * h, y[i], s_dict, f)
         err = abs(k1 - k2 - k3)

         #Гаусс - Лежандр
         while True:
             dk1 = k1 - h * funct(t + a1 * h, y[i] + b11 * k1 + b12 * k2, s_dict, f)
             dk2 = k2 - h * funct(t + a2 * h, y[i] + b21 * k1 + b22 * k2, s_dict, f)
             dk3 = k3 - h * funct(t + a3 * h, y[i] + b31 * k1 + b32 * k2, s_dict, f)

             err1 = abs(dk1 - dk2 - dk3)

             if err <= err1: break

             err = err1
             k1 = k1 - dk1
             k2 = k2 - dk2
             k3 = k3 - dk3

         y.append(y[i] + c1 * k1 + c2 * k2 + c3 * k3)
         t = t + h

     return y

def calc(a, b, h, y_a, eps, n, func):
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
    n = n+1
    test_1, test_2 = [], []
    h1 = h
    h2 = h * 0.1
    n1 = n
    n2 = 10 * n1
    index1 = 0
    index2 = 0
    flag = 1

    for i in range(n):
        test_1.append(0)
        test_2.append(0)

    while max_iter < 1:
        index1 = 0
        index2 = 0
        y = Kuntzmann_Butcher(y_a , a, h1, n1, s_dict, func)
        
        for i in range(n1):
            if (i % (float(n1) / n) == 0):
                test_1[index1] = y[i]
                index1 = index1 + 1

        y = []

        y = Kuntzmann_Butcher(y_a , a, h2, n2, s_dict, func)
        for i in range(n2):
            if (i % (float(n2) / n) == 0):
                test_2[index2] = y[i]
                index2 = index2 + 1


        for i in range(n):
            if abs(test_1[i] - test_2[i]) > eps:
                flag = 0
                break

        if flag == 1:
            y = test_1
            break

        n1 = n2
        n2 = 10 * n2
        h1 = h2
        h2 = h2 * 0.1
        
        max_iter = max_iter + 1

    if flag == 0:
        y = test_1

    r=[]
    for i in range(len(y)):
        r.append([round(a + h*i,5), round(y[i])])

    return r

