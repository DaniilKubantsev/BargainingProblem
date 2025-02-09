import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import bargaining_problem as bp

def calc_us(a_list: list, alpha_list: list, beta_list: list):
    complex_solutions_params = []
    complex_solutions_count = 0

    for a in a_list:
        for beta in beta_list:
            for alpha in alpha_list:
                s = bp.utilitarian(a=a, alpha=alpha, beta=beta)

                if s == 'COMPLEX_NUMBER':
                    complex_solutions_params.append((a, alpha, beta))
                    complex_solutions_count += 1

                print(f'A = %-7.3f \t alpha = %-7.3f \t beta = %-7.3f \t kss = {s}' %  (a, alpha, beta))

    print(f'complex solutions count: {complex_solutions_count}')

    if complex_solutions_count > 0:
        print('complex solution params:')
        for params in complex_solutions_params:
            print(params)

def calc_es(a_list: list, alpha_list: list, beta_list: list):
    complex_solutions_params = []
    complex_solutions_count = 0

    for a in a_list:
        for beta in beta_list:
            for alpha in alpha_list:
                s = bp.egalitarian(a=a, alpha=alpha, beta=beta)

                if s == 'COMPLEX_NUMBER':
                    complex_solutions_params.append((a, alpha, beta))
                    complex_solutions_count += 1

                print(f'A = %-7.3f \t alpha = %-7.3f \t beta = %-7.3f \t es = {s}' %  (a, alpha, beta))

    print(f'complex solutions count: {complex_solutions_count}')

    if complex_solutions_count > 0:
        print('complex solution params:')
        for params in complex_solutions_params:
            print(params)

def calc_nas(a_list: list, alpha_list: list, beta_list: list):
    solutions = []

    complex_solutions_params = []
    complex_solutions_count = 0

    for a in a_list:
        for beta in beta_list:
            for alpha in alpha_list:
                s = bp.nash_arbitration(a=a, alpha=alpha, beta=beta)

                if s == 'COMPLEX_NUMBER':
                    complex_solutions_params.append((a, alpha, beta))
                    complex_solutions_count += 1
                    solutions.append(np.inf)
                else:
                    # print(f'A = %-7.3f \t alpha = %-7.3f \t beta = %-7.3f \t nas = {s}' %  (a, alpha, beta))
                    solutions.append(s)

    # print(f'complex solutions count: {complex_solutions_count}')
    #
    # if complex_solutions_count > 0:
    #     print('complex solution params:')
    #     for params in complex_solutions_params:
    #         print(params)

def calc_kss(a_list: list, alpha_list: list, beta_list: list):
    solutions = []

    for a in a_list:
        for beta in beta_list:
            for alpha in alpha_list:
                x, y = bp.kalai_smorodinsky(a=a, alpha=alpha, beta=beta)
                solutions.append([x, y, a, alpha, beta])

    np_solutions = np.array(solutions, dtype='float').transpose()

    return {
        'x': np_solutions[0],
        'y': np_solutions[1],
        'A': np_solutions[2],
        'alpha': np_solutions[3],
        'beta': np_solutions[4]
    }


def main():
    alpha_list = [-1.5, -0.7, 0, 0.5, 1, 2]
    beta_list = [-1.5, -0.7, 0, 0.5, 1, 2]
    a_list = [-5, -2, 2, 5]

    # alpha_list = [-0.5, 0, 0.5]
    # beta_list = [-0.5, 0, 0.5]
    # a_list = [-5, 2, 5]

    # calc_solutions(a_list=a_list, alpha_list=alpha_list, beta_list=beta_list)
    kss_solutions = calc_kss(a_list=a_list, alpha_list=alpha_list, beta_list=beta_list)
    print(kss_solutions)

    x_vals = kss_solutions['x']
    y_vals = kss_solutions['y']
    plt.scatter(x_vals, y_vals)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # x_vals = kss_solutions['x']
    # y_vals = bp.u1(x=kss_solutions['x'], alpha=kss_solutions['alpha'])
    # z_vals = bp.u2(x=kss_solutions['x'], a=kss_solutions['A'], beta=kss_solutions['beta'])
    #
    # ax.scatter(x_vals, y_vals, z_vals, c='b', marker='o')
    # ax.set_xlabel('X-axis')
    # ax.set_ylabel('Y-axis')
    # ax.set_zlabel('Z-axis')
    plt.show()

    # calc_es(a_list=a_list, alpha_list=alpha_list, beta_list=beta_list)
    # calc_us(a_list=a_list, alpha_list=alpha_list, beta_list=beta_list)
    # calc_nas(a_list=a_list, alpha_list=alpha_list, beta_list=beta_list)




def calc_solutions(a_list: list, alpha_list: list, beta_list: list):
    complex_solutions_params = []
    complex_solutions_count = 0

    for a in a_list:
        for beta in beta_list:
            for alpha in alpha_list:
                kss = bp.kalai_smorodinsky(a=a, alpha=alpha, beta=beta)
                es = bp.egalitarian(a=a, alpha=alpha, beta=beta)
                nas = bp.nash_arbitration(a=a, alpha=alpha, beta=beta)
                us = bp.utilitarian(a=a, alpha=alpha, beta=beta)

                if "COMPLEX NUMBER" in [kss, es, nas, us]:
                    complex_solutions_params.append((a, alpha, beta))
                    complex_solutions_count += 1

                print(f'A = %-7.3f \t alpha = %-7.3f \t beta = %-7.3f \t kss = {kss} \t es = {es} \t nas = {nas} \t us = {us}' % (a, alpha, beta))

    print(f'complex solutions count: {complex_solutions_count}')

    if complex_solutions_count > 0:
        print('complex solution params:')
        for params in complex_solutions_params:
            print(params)


if __name__ == '__main__':
    main()