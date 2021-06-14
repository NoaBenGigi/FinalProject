#part 1.2

import sympy as sp
from sympy import lambdify
from math import e
import math
x = sp.symbols('x')

def func(f,num): #return the y of the function
    x = sp.symbols('x')
    f = lambdify(x, f)
    return f(num)

def trapez(f, x0, xn, n):
    #f- function
    #x0- start point
    #xn - end point
    #n- number of Sections
    h = float((xn - x0)/n)
    result = (func(f,x0)/2) + (func(f,xn)/2)
    for i in range(1, n):
        result += func(f, x0) + (i * h)
    result = result * h
    return result

def simpson(f, x0, xn, n):
    h = (xn - x0) / n
    k = 0.0
    x = x0 + h
    y= math.ceil(n/2+1)
    for i in range(1, y):
        k += 4 * func(f,x)
        x += 2 * h
    x = x0 + 2 * h
    z= math.ceil(n/2)
    for i in range(1, z):
        k += 2 * func(f,x)
        x += 2 * h
    return (h / 3) * (func(f, x0) + func(f, xn) + k)

def romberg(f, x0, xn, n):
    new_matrix = list(range(n))
    for j in range(n):
        new_matrix[j] = list(range(n))
    for i in range(n):
        new_matrix[i][0] = trapez(f, x0, xn,pow(2,i))
        for j in range(0, i):
            new_matrix[i][j + 1] = ((4 * (j + 1) * new_matrix[i][j]) - new_matrix[i - 1][j]) / (4 * (j + 1) - 1)
            print("R[",i,",",j + 1,"]=",new_matrix[i][j + 1])



def main():
    f = sp.sin(x**2+5*x+6)/(2*e**-x)
    x0 = 0
    xn = 1
    print("Simpson for the function:")
    print("p(x)dx=",simpson(f, x0, xn, 4))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Romberg Integration: ")
    romberg(f,x0,xn,6)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()
