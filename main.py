import bargaining_problem as bp
import plot2d
from bargaining_problem.scalar_indev import *
import plot3d
import plots.utility as pltu
import numpy as np
import matplotlib.pyplot as plt




def u1(x, alpha):
    return x ** alpha


def u2(x, a, beta):
    return (a - x) ** beta


NDIGITS = 4
ALPHA_EQUAL_BETA_SOLUTIONS_LESS_1 = 'alpha_equal_beta_less_1.csv'
ALPHA_EQUAL_BETA_SOLUTIONS_MORE_1 = 'alpha_equal_beta_more_1.csv'
ALPHA_EQUAL_1_BETA_MORE_0_LESS_1 = 'alpha_equal_1_beta_more_0_less_1.csv'
ALPHA_EQUAL_1_BETA_MORE_0_MORE_1 = 'alpha_equal_1_beta_more_0_more_1.csv'
UTILITARIAN = 'utilitarian'
EGALITARIAN = 'egalitarian'
KALAI_SMORODINSKI = 'kalai_smorodinski'
NASH_ARBITRASIAN = 'nash_arbitrasian'

a_vals = [0.25, 0.46, 0.75, 1, 1.34, 2.5]
beta_vals_less_1 = [0.05, 0.25, 0.56, 0.78, 0.99]
beta_vals_more_1 = [1.05, 1.25, 1.56, 1.78, 1.99]




def main():

    a = 3
    alpha = 1.78
    beta = 1.53
    x = find_utilitarian_solution(u1_func=u1, u2_func=u2, u1_args=(alpha,), u2_args=(a, beta), bounds=(0,a))
    print(x)

    plot3d.plot_egalitarian_solution(0.56)
    # bp3dp.plot_utilitarian_solution(0.56)
    # plot3d.plot_kalai_smorodinski_solution(3)
    # bp3dp.plot_nash_arbitrasian_solution(0.56)



    alpha_equal_beta = 'alpha_equal_beta'
    alpha_1_beta_more_0 = 'alpha_1_beta_more_0'

    pltu.plot_egalitarian_solution_utility(3, alpha_1_beta_more_0)

    # plot2d.plot_egalitarian_solution(3, alpha_1_beta_more_0)
    # plot2d.plot_egalitarian_solution(0.56, alpha_1_beta_more_0)
    #
    # plot2d.plot_utilitarian_solution(3, alpha_1_beta_more_0)
    # plot2d.plot_utilitarian_solution(0.56, alpha_1_beta_more_0)
    #
    # plot2d.plot_kalai_smorodinski_solution(3, alpha_1_beta_more_0)
    # plot2d.plot_kalai_smorodinski_solution(0.56, alpha_1_beta_more_0)
    #
    # plot2d.plot_nash_arbitrasian_solution(3, alpha_1_beta_more_0)
    # plot2d.plot_nash_arbitrasian_solution(0.56, alpha_1_beta_more_0)


if __name__ == '__main__':
    main()
