from bargaining_problem.scalar_indev import *
import numpy as np
import matplotlib.pyplot as plt

def u1(x, alpha):
    return x ** alpha


def u2(x, a, beta):
    return (a - x) ** beta

def plot_egalitarian_solution(a):
    alpha_vals = np.linspace(0, 2, 30)
    beta_vals = np.linspace(0, 2, 30)


    xe_vals = np.zeros((len(alpha_vals), len(beta_vals)))
    alpha_beta_line = []

    for i, alpha in enumerate(alpha_vals):
        for j, beta in enumerate(beta_vals):
            xe = find_egalitarian_solution(u1, u2, u1_args=(alpha,), u2_args=(a, beta), initial_guess=a / 2)
            xe_vals[j, i] = xe




            if alpha == beta: alpha_beta_line.append(xe)

    alpha_mesh, beta_mesh = np.meshgrid(alpha_vals, beta_vals)


    ax = plt.axes(projection='3d')
    c_map = plt.get_cmap('cividis')


    ax.plot_surface(alpha_mesh, beta_mesh, xe_vals, cmap=c_map, alpha=0.7)
    ax.plot3D(alpha_vals, alpha_vals, alpha_beta_line , color='blue')

    ax.set_xlabel('$\\alpha$')
    ax.set_ylabel('$\\beta$')
    ax.set_zlabel('$x^E$')

    plt.show()




def plot_utilitarian_solution(a):
    alpha_vals = np.linspace(0, 2, 30)
    beta_vals = np.linspace(0, 2, 30)


    solution_vals = np.zeros((len(alpha_vals), len(beta_vals)))
    alpha_beta_line = []
    alpha_1_beta_0_curve = []

    for i, alpha in enumerate(alpha_vals):
        for j, beta in enumerate(beta_vals):
            solution = find_utilitarian_solution(u1_func=u1, u2_func=u2, u1_args=(alpha,), u2_args=(a, beta), bounds=(0,a))
            solution_vals[j, i] = solution

            sol = find_utilitarian_solution(u1_func=u1, u2_func=u2, u1_args=(1,), u2_args=(a, beta), bounds=(0, a))
            alpha_1_beta_0_curve.append(sol)

            if alpha == beta: alpha_beta_line.append(solution)

    alpha_mesh, beta_mesh = np.meshgrid(alpha_vals, beta_vals)


    ax = plt.axes(projection='3d')
    c_map = plt.get_cmap('cividis')


    ax.plot_surface(alpha_mesh, beta_mesh, solution_vals, cmap=c_map, alpha=0.7)
    ax.plot3D(alpha_vals, alpha_vals, alpha_beta_line , color='blue')
    ax.plot3D(np.ones(len(alpha_vals)), beta_vals, alpha_1_beta_0_curve[:30], color='blue')

    ax.set_xlabel('$\\alpha$')
    ax.set_ylabel('$\\beta$')
    ax.set_zlabel('$x^U$')

    plt.show()

def plot_kalai_smorodinski_solution(a):
    alpha_vals = np.linspace(0, 2, 30)
    beta_vals = np.linspace(0, 2, 30)


    solution_vals = np.zeros((len(alpha_vals), len(beta_vals)))
    alpha_beta_line = []
    alpha_1_beta_0 = []

    for i, alpha in enumerate(alpha_vals):
        for j, beta in enumerate(beta_vals):
            solution = find_kalai_smorodinski_solution(u1_func=u1, u2_func=u2, u1_args=(alpha,), u2_args=(a, beta), bounds=(0,a), initial_guess=a/2)
            solution_vals[j, i] = solution
            if alpha == beta: alpha_beta_line.append(solution)

    alpha_mesh, beta_mesh = np.meshgrid(alpha_vals, beta_vals)

    for beta in beta_vals:
        sol = find_kalai_smorodinski_solution(u1_func=u1, u2_func=u2, u1_args=(1,), u2_args=(a, beta), bounds=(0, a),
                                              initial_guess=a / 2)
        alpha_1_beta_0.append(sol)

    ax = plt.axes(projection='3d')
    c_map = plt.get_cmap('cividis')


    ax.plot_surface(alpha_mesh, beta_mesh, solution_vals, cmap=c_map, alpha=0.7)
    ax.plot3D(alpha_vals, alpha_vals, alpha_beta_line , color='blue')
    ax.plot3D(np.ones(len(alpha_vals)), beta_vals, alpha_1_beta_0, color='blue')

    ax.set_xlabel('$\\alpha$')
    ax.set_ylabel('$\\beta$')
    ax.set_zlabel('$x^{KS}$')

    plt.show()


def plot_nash_arbitrasian_solution(a):
    alpha_vals = np.linspace(0, 2, 30)
    beta_vals = np.linspace(0, 2, 30)


    solution_vals = np.zeros((len(alpha_vals), len(beta_vals)))
    alpha_beta_line = []
    alpha_1_beta_0=[]

    for i, alpha in enumerate(alpha_vals):
        sol = find_nash_arbitrasian_solution(u1_func=u1, u2_func=u2, u1_args=(1,), u2_args=(a, alpha), bounds=(0,a))
        alpha_1_beta_0.append(sol)
        for j, beta in enumerate(beta_vals):
            solution = find_nash_arbitrasian_solution(u1_func=u1, u2_func=u2, u1_args=(alpha,), u2_args=(a, beta), bounds=(0,a))
            solution_vals[j, i] = solution
            if alpha == beta: alpha_beta_line.append(solution)

    alpha_mesh, beta_mesh = np.meshgrid(alpha_vals, beta_vals)


    ax = plt.axes(projection='3d')
    c_map = plt.get_cmap('cividis')


    ax.plot_surface(alpha_mesh, beta_mesh, solution_vals, cmap=c_map, alpha=0.7)
    ax.plot3D(alpha_vals, alpha_vals, alpha_beta_line , color='blue')
    ax.plot3D(np.ones(len(alpha_vals)), alpha_vals, alpha_1_beta_0, color='blue')

    ax.set_xlabel('$\\alpha$')
    ax.set_ylabel('$\\beta$')
    ax.set_zlabel('$x^{NE}$')

    plt.show()



def test(a):
    beta_vals = np.linspace(0, 2, 30)
    alpha_vals = np.ones(30)
    alpha_1_beta_0 = []

    for beta in beta_vals:
        alpha = 1
        sol = find_utilitarian_solution(u1_func=u1, u2_func=u2, u1_args=(alpha,), u2_args=(a, beta), bounds=(0,a))
        alpha_1_beta_0.append(sol)

    ax = plt.axes(projection='3d')
    ax.plot3D(alpha_vals, beta_vals, alpha_1_beta_0)
    plt.show()