from bargaining_problem.scalar_indev import *
import numpy as np
import matplotlib.pyplot as plt

def u1(x, alpha):
    return x ** alpha


def u2(x, a, beta):
    return (a - x) ** beta

def plot_egalitarian_solution_utility(a, case):
    beta_vals = np.linspace(0, 2, 100)
    solution_vals = []
    utility_1 = []
    utility_2 = []
    label_str = ''

    fig, ax = plt.subplots()

    if case == 'alpha_equal_beta':
        for beta in beta_vals:
            alpha = beta
            sol = find_egalitarian_solution(u1, u2, u1_args=(alpha,), u2_args=(a, beta), initial_guess=a / 2)
            solution_vals.append(sol)
            utility_1.append(u1(sol,alpha))
            utility_2.append(u2(sol, a, beta))
            label_str = '$\\alpha=\\beta$'
    elif case =='alpha_1_beta_more_0' :
        for beta in beta_vals:
            alpha = 1
            sol = find_egalitarian_solution(u1, u2, u1_args=(alpha,), u2_args=(a, beta), initial_guess=a / 2)
            solution_vals.append(sol)
            utility_1.append(u1(sol, alpha))
            utility_2.append(u2(sol, a, beta))
            label_str = '$\\beta$'
    else:
        err_str = f'UNKNOWN CASE: {case}'
        raise 'UNKNOWN CASE'


    plt.plot(beta_vals, utility_1, color='r', alpha=0.5)
    plt.plot(beta_vals, utility_2, color='g', alpha=0.5)
    ax.set_title('Эгалитарное решение')
    ax.set_ylabel('utility')
    ax.set_xlabel(label_str)


    plt.show()