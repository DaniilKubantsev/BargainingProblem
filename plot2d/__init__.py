from bargaining_problem.scalar_indev import *
import numpy as np
import matplotlib.pyplot as plt

def u1(x, alpha):
    return x ** alpha


def u2(x, a, beta):
    return (a - x) ** beta

def plot_egalitarian_solution(a, case):
    beta_vals = np.linspace(0, 2, 100)
    solution_vals = []
    label_str = ''

    fig, ax = plt.subplots()

    if case == 'alpha_equal_beta':
        for beta in beta_vals:
            sol = find_egalitarian_solution(u1, u2, u1_args=(beta,), u2_args=(a, beta), initial_guess=a / 2)
            solution_vals.append(sol)
            label_str = '$\\alpha=\\beta$'
    elif case =='alpha_1_beta_more_0' :
        for beta in beta_vals:
            sol = find_egalitarian_solution(u1, u2, u1_args=(1,), u2_args=(a, beta), initial_guess=a / 2)
            solution_vals.append(sol)
            label_str = '$\\beta$'
    else:
        err_str = f'UNKNOWN CASE: {case}'
        raise 'UNKNOWN CASE'


    plt.plot(beta_vals, solution_vals)

    ax.set_title('Эгалитарное решение')
    ax.set_ylabel('$x^E$')
    ax.set_xlabel(label_str)


    plt.show()


def plot_utilitarian_solution(a, case):
    beta_vals = np.linspace(0, 2, 200)
    solution_vals = []
    label_str = ''

    fig, ax = plt.subplots()

    if case == 'alpha_equal_beta':
        for beta in beta_vals:
            sol = find_utilitarian_solution(u1_func=u1, u2_func=u2, u1_args=(beta,), u2_args=(a, beta), bounds=(0,a))
            solution_vals.append(sol)
            label_str = '$\\alpha=\\beta$'
    elif case =='alpha_1_beta_more_0' :
        for beta in beta_vals:
            sol = find_utilitarian_solution(u1_func=u1, u2_func=u2, u1_args=(1,), u2_args=(a, beta), bounds=(0,a))
            if beta > 1: sol = 0
            solution_vals.append(sol)
            label_str = '$\\beta$'
    else:
        err_str = f'UNKNOWN CASE: {case}'
        raise 'UNKNOWN CASE'


    plt.plot(beta_vals, solution_vals)

    ax.set_title('Утилитарное решение')
    ax.set_ylabel('$x^U$')
    ax.set_xlabel(label_str)


    plt.show()

def plot_kalai_smorodinski_solution(a, case):
    beta_vals = np.linspace(0, 2, 200)
    solution_vals = []
    label_str = ''

    fig, ax = plt.subplots()

    if case == 'alpha_equal_beta':
        for beta in beta_vals:
            sol = find_kalai_smorodinski_solution(u1_func=u1, u2_func=u2, u1_args=(beta,), u2_args=(a, beta), bounds=(0,a), initial_guess=a/2)
            solution_vals.append(sol)
            label_str = '$\\alpha=\\beta$'
    elif case =='alpha_1_beta_more_0' :
        for beta in beta_vals:
            sol = find_kalai_smorodinski_solution(u1_func=u1, u2_func=u2, u1_args=(1,), u2_args=(a, beta), bounds=(0,a), initial_guess=a/2)
            solution_vals.append(sol)
            label_str = '$\\beta$'
    else:
        err_str = f'UNKNOWN CASE: {case}'
        raise 'UNKNOWN CASE'


    plt.plot(beta_vals, solution_vals)

    ax.set_title('Решение Калай-Смородинского')
    ax.set_ylabel('$x^{KS}$')
    ax.set_xlabel(label_str)


    plt.show()



def plot_nash_arbitrasian_solution(a, case):
    beta_vals = np.linspace(0, 2, 200)
    solution_vals = []
    label_str = ''

    fig, ax = plt.subplots()

    if case == 'alpha_equal_beta':
        for beta in beta_vals:
            alpha = beta
            sol = find_nash_arbitrasian_solution(u1_func=u1, u2_func=u2, u1_args=(1,), u2_args=(a, alpha), bounds=(0,a))
            solution_vals.append(sol)
            label_str = '$\\alpha=\\beta$'
    elif case =='alpha_1_beta_more_0' :
        for beta in beta_vals:
            alpha = 1
            sol = find_nash_arbitrasian_solution(u1_func=u1, u2_func=u2, u1_args=(1,), u2_args=(a, beta), bounds=(0,a))
            solution_vals.append(sol)
            label_str = '$\\beta$'
    else:
        err_str = f'UNKNOWN CASE: {case}'
        raise 'UNKNOWN CASE'


    plt.plot(beta_vals, solution_vals)

    ax.set_title('Арбитражное решение Нэша')
    ax.set_ylabel('$x^{NE}$')
    ax.set_xlabel(label_str)


    plt.show()