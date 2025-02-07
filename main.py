from scipy.optimize import fsolve, minimize_scalar
import pandas as pd

class Solution:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#целевые фунции
def u1(x: float, alpha: float):
    return x ** alpha

def u2(x: float, A: float, beta: float):
    return (A - x) ** beta


#функции решений
def utilitarian(A, alpha, beta):
    def f(x, A, alpha, beta):
        return -(u1(x=x, alpha=alpha) + u2(x=x, A=A, beta=beta))

    bounds = (0, A)
    if A < 0: bounds = (A, 0)

    solution = float(minimize_scalar(f, bounds=bounds, method='bounded', args=(A, alpha, beta)).x)
    return Solution(x=solution, y=-f(solution, A, alpha, beta))

def kalai_smorodinsky(A, alpha, beta):
    def f(x, A, alpha, beta):
        return u1(x=x, alpha=alpha) / u2(x=x, A=A, beta=beta) - A ** (alpha - beta)

    x_initial_guess = A / 2
    #solution = float(fsolve(f, x_initial_guess, args=(A, alpha, beta))[0])

    try:
        solution = fsolve(f, x_initial_guess, args=(A, alpha, beta))
        return Solution(x=solution, y=f(solution, A, alpha, beta))
    except:
        return 'ERROR'



def nash_arbitration(A, alpha, beta):
    def f(x, A, alpha, beta):
        return -(u1(x=x, alpha=alpha) * u2(x=x, A=A, beta=beta))

    bounds = (0, A)
    if A < 0: bounds = (A, 0)

    solution = float(minimize_scalar(f, bounds=bounds, method='bounded', args=(A, alpha, beta)).x)
    return Solution(x=solution, y=-f(solution, A, alpha, beta))

def egalitarian(A, alpha, beta):
    def f(x, A, alpha, beta):
        return u1(x=x, alpha=alpha) - u2(x=x, A=A, beta=beta)

    x_initial_guess = A / 2
    solution = fsolve(f, x_initial_guess, args=(A, alpha, beta))[0]
    return Solution(x=solution, y=f(solution, A, alpha, beta))



def main():
    alpha_list = [-1.5, -0.7, 0, 0.5, 1, 2]
    beta_list = [-1.5, -0.7, 0, 0.5, 1, 2]
    A_list = [-10, -2, 2, 5, 8]

    i = 0

    for A in A_list:
        for beta in beta_list:
            for alpha in alpha_list:
                i += 1
                es = egalitarian(A=A, alpha=alpha, beta=beta)
                nas = nash_arbitration(A=A, alpha=alpha, beta=beta)
                kss = kalai_smorodinsky(A=A, alpha=alpha, beta=beta)
                us = utilitarian(A=A, alpha=alpha, beta=beta)

                print()
                print(f'A = {A}\t alpha = {alpha} \t beta = {beta}')
                print('egalitarian solution', es)
                print('nash arbitration solution', nas.x)
                print('kalai smorodinsky solution', kss)
                print('utilitarian solution', us.x)

    print(i)

if __name__ == '__main__':
    main()