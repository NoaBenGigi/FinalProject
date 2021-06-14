#Part 17.1
import math
import sympy as sp
from sympy.utilities.lambdify import lambdify
import datetime as dt

from sympy.testing import pytest
from math import log, cos
from math import e
x = sp.symbols('x')

def func(f,num): #return the y of the function
    x = sp.symbols('x')
    f = lambdify(x, f)
    return f(num)

def calculate_derivative(f):
    x = sp.symbols('x')
    my_f1 = sp.diff(f, x)
    return my_f1

def Bisection_Method(method,start_point, end_point, epsi= 0.00001):
    #calculate num of iterations
    y = epsi / (end_point - start_point)
    z= (-1) * math.log(y, math.e)
    k= (z // math.log(2, math.e)) + 1
    #__________________________________
    numOfIterations = 0
    while (abs(end_point - start_point) > epsi and numOfIterations < k):
        numOfIterations += 1
        c = (start_point + end_point) / 2
        print("Iteration number", numOfIterations, "    a=", round(start_point, 5), "    b=",
              round(end_point, 5), "    c=",round(c, 5))
        if func(method, start_point) * func(method, c) > 0:
            start_point = c
        else:
            end_point = c
    print("number of iterations for finding bisection:", k)
    print("Final Answer:")
    return EndOfCal(round(c,4))


def little_ranges_bisection(method, start_point, end_point):
    derivative = calculate_derivative(method)
    start_point -=0.1
    temporary_end = start_point + 0.1
    temporary_end = round(temporary_end, 2)#to numbers after dot
    while round(start_point, 2) < end_point:
        if func(method,start_point) * func(method,temporary_end) <0:#check the range on the method

            Bisection_Method(method, start_point, temporary_end)
        if func(method, temporary_end) == 0.0:
            # check the range on the derivative
            EndOfCal(round(temporary_end,4))
            print("Number of iterations = 0")
            print("_________________________________________________________")
            start_point += 0.1
            start_point = round(start_point, 2)
            temporary_end += 0.1
            temporary_end = round(temporary_end, 2)

        start_point += 0.1
        start_point = round(start_point, 2)
        temporary_end += 0.1
        temporary_end = round(temporary_end, 2)


def little_ranges_with_secant(method, start_point, end_point):
    derivative = calculate_derivative(method)
    start_point -= 0.1
    temporary_end = start_point + 0.1
    temporary_end = round(temporary_end, 2)  # to numbers after dot
    while round(start_point, 2) < end_point:
        if func(method, start_point) * func(method, temporary_end) < 0:  #check the range
             secant_method(method, start_point, temporary_end)
        if func(method, temporary_end) == 0.0:
            # check the range on the derivative
            EndOfCal(round(temporary_end,4))
            print("Number of iterations = 0")
            print("_________________________________________")
            start_point += 0.1
            start_point = round(start_point, 2)
            temporary_end += 0.1
            temporary_end = round(temporary_end, 2)
        start_point += 0.1
        start_point = round(start_point, 2)
        temporary_end += 0.1
        temporary_end = round(temporary_end, 2)

def secant_method(method, start_point, end_point, epsi=0.0001):
    derivative = calculate_derivative(method)
    x0 = start_point
    x1 = end_point
    numOfIterations = 1
    while (abs(x1 - x0) > epsi and numOfIterations <= 101):
        xr_1 = x0
        x0 = x1
        x1 = (xr_1 * func(method, x0)- x0 * func(method, xr_1))/(func(method, x0)-func(method, xr_1))
        print("Iteration number", numOfIterations, "    Xr+1=", round(x1, 5), "    Xr=", round(x0, 5),
              "    Xr-1=",
              round(xr_1, 5))
        numOfIterations += 1
    if (numOfIterations >= 100):
        return "This part does not converge"
    else:
        print("num of iteration for finding bisection:", numOfIterations-1)
        print("Final Answer:")
        EndOfCal(round(x1,4))

def EndOfCal(end):
    i = 0
    if end < 0:
        i = 1
        end = abs(end)
    day = (format(dt.datetime.today().day))
    hour = (format(dt.datetime.today().hour))
    minute = (format(dt.datetime.today().minute))
    temp = 1 / 100000
    end = str(end) + "00000"
    print("x=", str(end)+day+hour+minute)



def main():
    f = f = (x ** 2 * e ** (-x ** 2 -5 * x - 3)) * (3 * x - 1)
    start_point=0
    end_point=1.5
    print("Question number 17.1 ")
    print("Bisection Method:")
    print("~~~~~~~~~~~~~~~~~~")
    little_ranges_bisection(f,start_point, end_point)
    print("-----------------------------------------------------------")
    print("Secant Method:")
    print("~~~~~~~~~~~~~~")
    little_ranges_with_secant(f, start_point, end_point)

if __name__ == "__main__":
    main()