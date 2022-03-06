# Code to produce plots in the notebook.

#  %matplotlib notebook
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from math import erf

def f(x):
    return np.exp(-x**2)

def plot_riemann_midpoint(N):
    '''
    Creates plots for the Riemann sums and midpoint rule,
    with N subdivisions of the interval [a, b].
    '''
    # Create an x-axis with 100 points and estimate the function
    a, b = 0, 3
    x_plot = np.linspace(a, b, 100)
    f_plot = f(x_plot)

    # Plot the function
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    ax[0].plot(x_plot, f_plot, 'k-')
    ax[1].plot(x_plot, f_plot, 'k-')
    ax[2].plot(x_plot, f_plot, 'k-')

    # Create the nodes for Riemann sums
    #  N = 6
    x_node = np.linspace(a, b, N+1)
    f_node = f(x_node)

    # Plot the rectangles for left and right sums
    h = (b - a) / N
    for k in range(N):
        rect = patches.Rectangle((x_node[k], 0), h, f_node[k], edgecolor='k')
        ax[0].add_patch(rect)
        
        rect = patches.Rectangle((x_node[k], 0), h, f_node[k+1], edgecolor='k')
        ax[1].add_patch(rect)
        
    # Plot the nodes
    ax[0].plot(x_node[:-1], f_node[:-1], 'rx')
    ax[1].plot(x_node[1:], f_node[1:], 'rx')

    # Estimate the integral
    left_I = np.sum(h * f_node[:-1])
    right_I = np.sum(h * f_node[1:])

    # Create the nodes for midpoint rule
    x_node = np.linspace(a + 0.5*h, b -0.5*h, N)
    f_node = f(x_node)

    # Plot the rectangles
    for k in range(N):
        rect = patches.Rectangle((x_node[k] - 0.5*h, 0), h, f_node[k], edgecolor='k')
        ax[2].add_patch(rect)

    # Plot the nodes
    ax[2].plot(x_node, f_node, 'rx')

    # Estimate the integral
    midpoint_I = np.sum(h * f_node)

    # Label the plots
    ax[0].set_xlabel(r'$x$')
    ax[1].set_xlabel(r'$x$')
    ax[2].set_xlabel(r'$x$')
    ax[0].set_ylabel(r'$f(x)$')

    ax[0].set_title('Left Riemann sum')
    ax[1].set_title('Right Riemann sum')
    ax[2].set_title('Midpoint rule')

    plt.show()

    # Exact value of the integral
    I_exact = np.sqrt(np.pi) / 2 * (erf(b) - erf(a))

    print(f'Exact: {I_exact:.4f}\nLeft Riemann: {left_I:.4f}')
    print(f'Right Riemann: {right_I:.4f}\nMidpoint: {midpoint_I:.4f}')



def trapezoid(N):
    '''
    Estimates the integral using trapezoid rule.
    '''
    # Create an x-axis with 100 points and estimate the function
    a, b = 0, 3
    x_plot = np.linspace(a, b, 100)
    f_plot = f(x_plot)

    # Create the nodes
    h = (b - a) / N
    x_node = np.linspace(a, b, N + 1)
    f_node = f(x_node)

    # Plot the function
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x_plot, f_plot, 'k-')

    # Plot the trapezoids
    for k in range(N):
        verts = [[x_node[k], 0], [x_node[k+1], 0],
                 [x_node[k+1], f_node[k+1]], [x_node[k], f_node[k]]]
        trapz = patches.Polygon(verts, h, edgecolor='k')
        ax.add_patch(trapz)

    # Plot the nodes
    ax.plot(x_node, f_node, 'rx')

    # Label the plots
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$f(x)$')
    ax.set_title('Trapezoid rule')

    plt.show()

    # Estimate the integral
    trapezoid_I = np.sum(0.5 * h * (f_node[:-1] + f_node[1:]))

    # Exact value
    I_exact = np.sqrt(np.pi) / 2 * (erf(b) - erf(a))

    print(f'Exact: {I_exact:.5f}\nTrapezoid: {trapezoid_I:.5f}')