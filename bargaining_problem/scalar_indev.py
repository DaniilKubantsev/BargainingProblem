
from scipy.optimize import fsolve, minimize_scalar

def find_egalitarian_solution(
        u1_func,
        u2_func,
        u1_args: tuple,
        u2_args: tuple,
        u1_dis = 0.0,
        u2_dis = 0.0,
        initial_guess = 0.0
):
    if not isinstance(u1_args, tuple):
        u1_args = (u1_args,)

    if not isinstance(u2_args, tuple):
        u2_args = (u2_args,)

    def func(x):
        u1_value = u1_func(x, *u1_args)
        u2_value = u2_func(x, *u2_args)

        return u1_value - u2_value - u1_dis + u2_dis

    result = fsolve(func=func, x0=initial_guess)

    return result

def find_kalai_smorodinski_solution(
        u1_func,
        u2_func,
        u1_args: tuple,
        u2_args: tuple,
        bounds,
        u1_dis = 0.0,
        u2_dis = 0.0,
        initial_guess = 0.0
):
    if not isinstance(u1_args, tuple):
        u1_args = (u1_args,)

    if not isinstance(u2_args, tuple):
        u2_args = (u2_args,)

    def func(x):
        reverse_u1 = lambda x_val: -u1_func(x_val, *u1_args)
        reverse_u2 = lambda x_val: -u2_func(x_val, *u2_args)

        u1_max_result = minimize_scalar(
            fun=reverse_u1,
            bounds=bounds,
            method='bounded'
        )

        u2_max_result = minimize_scalar(
            fun=reverse_u2,
            bounds=bounds,
            method='bounded'
        )

        u1_max = -u1_max_result.fun
        u2_max = -u2_max_result.fun

        u1_value = u1_func(x, *u1_args)
        u2_value = u2_func(x, *u2_args)

        return (u1_value - u1_dis) / (u2_value - u2_dis) - (u1_max - u1_dis) / (u2_max - u2_dis)

    result = fsolve(func=func, x0=initial_guess)

    return result


def find_nash_arbitrasian_solution(
       u1_func,
       u2_func,
       u1_args: tuple,
       u2_args: tuple,
       bounds,
       u1_dis=0.0,
       u2_dis=0.0
):

    if not isinstance(u1_args, tuple):
        u1_args = (u1_args,)

    if not isinstance(u2_args, tuple):
        u2_args = (u2_args,)

    def func(x):
        u1_value = u1_func(x, *u1_args)
        u2_value = u2_func(x, *u2_args)

        return  -(u1_value - u1_dis)*(u2_value-u2_dis)

    max_result = minimize_scalar(
        fun=func,
        bounds=bounds,
        method='bounded'
    )

    return max_result.x



def find_utilitarian_solution(
      u1_func,
      u2_func,
      u1_args: tuple,
      u2_args: tuple,
      bounds,
):


    if not isinstance(u1_args, tuple):
        u1_args = (u1_args,)

    if not isinstance(u2_args, tuple):
        u2_args = (u2_args,)

    def func(x):
        u1_value = u1_func(x, *u1_args)
        u2_value = u2_func(x, *u2_args)

        return  -u1_value-u2_value

    max_result = minimize_scalar(
        fun=func,
        bounds=bounds,
        method='bounded'
    )

    return max_result.x