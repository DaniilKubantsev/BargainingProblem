from scipy.optimize import fsolve, minimize_scalar
import numpy as np

EXCEPTION_VALUE = np.nan, np.nan

#целевые фунции
def u1(x: float, alpha: float):
    # res = np.pow(x, alpha)
    # if np.iscomplex(res): raise ValueError("Complex number")
    # return res
    return np.power(x, alpha)

def u2(x: float, a: float, beta: float):
    # res = np.pow((a - x), beta)
    # if np.iscomplex(res): raise ValueError("Complex number")
    # return res
    return np.power((a - x), beta)






#функции решений
def nash_arbitration(a, alpha, beta):
    def f(x):
        u1_val = u1(x=x, alpha=alpha)
        u2_val = u2(x=x, a=a, beta=beta)
        return -(u1_val * u2_val)

    bounds = (0, a)
    if a < 0: bounds = (a, 0)

    try:
        solution = minimize_scalar(f, bounds=bounds, method='bounded')
        x, y = float(solution.x), float(f(solution.x))
        return x, y
    except ValueError:
        return EXCEPTION_VALUE
    except TypeError:
        return EXCEPTION_VALUE


def utilitarian(a, alpha, beta):
    def f(x):
        u1_val = u1(x=x, alpha=alpha)
        u2_val = u2(x=x, a=a, beta=beta)

        return -(u1_val + u2_val)

    bounds = (0, a)
    if a < 0: bounds = (a, 0)

    try:
        solution = minimize_scalar(f, bounds=bounds, method='bounded')
        x, y = float(solution.x), float(f(solution.x))
        return x, y
    except ValueError:
        return EXCEPTION_VALUE
    except TypeError:
        return EXCEPTION_VALUE

def kalai_smorodinsky(a, alpha, beta):
    def f(x):
        try:
            a_val = np.power(a, alpha - beta)
            u1_val = u1(x=x, alpha=alpha)
            u2_val = u2(x=x, a=a, beta=beta)
            return u1_val / u2_val - a_val
        except ValueError as e:
            raise ValueError


    try:
        x_initial_guess = a / 2
        solution = fsolve(f, x_initial_guess)[0]
        x, y = float(solution), float(f(solution))
        return x, y
    except ValueError:
        return EXCEPTION_VALUE
    except TypeError:
        return EXCEPTION_VALUE


def egalitarian(a, alpha, beta):
    def f(x):
        u1_val = u1(x=x, alpha=alpha)
        u2_val = u2(x=x, a=a, beta=beta)
        return u1_val - u2_val

    try:
        x_initial_guess = a / 2
        solution = fsolve(f, x_initial_guess)[0]
        x, y = solution, f(solution)
        return x, y
    except ValueError:
        return EXCEPTION_VALUE
    except TypeError:
        return EXCEPTION_VALUE




