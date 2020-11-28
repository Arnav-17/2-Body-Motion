import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter the number of steps\n"))
s = int(n/2)


def f(r, u, t):
    return 1/r**3-1/r**2  # Equation of r


def g(theta, r, t):
    return 1/r**2  # Equation of theta


x_graph = []
y_graph = []

# r and theta are polar coordinates
# u = derivative of r wrt t
# r_0 = initial value of r
# theta_0 = initial value of theta
# t_0 = initial time
# h = time step

x1 = []
y1 = []


def func(r_0, theta_0, u_0, t_0, h):
    x = -0.80  # initial value of x
    y = 0      # initial value of y
    for i in range(1, n + 1):
        m1 = h * u_0
        k1 = h * f(r_0, u_0, t_0)
        l1 = h * g(theta_0, r_0, t_0)
        m2 = h * (u_0 + 0.5 * k1)
        k2 = h * f(r_0 + 0.5 * m1, u_0 + 0.5 * k1, t_0 + 0.5 * h)
        l2 = h * g(theta_0 + 0.5 * l1, r_0 + 0.5 * k1, t_0 + 0.5 * h)
        m3 = h * (u_0 + 0.5 * k2)
        k3 = h * f(r_0 + 0.5 * m2, u_0 + 0.5 * k2, t_0 + 0.5 * h)
        l3 = h * g(theta_0 + 0.5 * l2, r_0 + 0.5 * k2, t_0 + 0.5 * h)
        m4 = h * (u_0 + k3)
        k4 = h * f(r_0 + m3, u_0 + k3, t_0 + h)
        l4 = h * g(theta_0 + l3, r_0 + k3, t_0 + h)
        r_0 += (m1 + 2 * m2 + 2 * m3 + m4) / 6
        u_0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        theta_0 += (l1 + 2 * l2 + 2 * l3 + l4) / 6
        x = r_0 * np.cos(theta_0)
        y = r_0 * np.sin(theta_0)
        t_0 += h
        x_graph.append(x)
        y_graph.append(y)
    plt.plot(x_graph,y_graph)
    plt.title('Motion of Earth')
    plt.show()
    return x, y


dist_arr = []


def di():
    func(0.98, -np.pi, 0, 0, 0.001)
    dist = 0
    for i in range(n-1):
        d = np.sqrt((x_graph[i+1] - x_graph[i]) ** 2 + (y_graph[i+1] - y_graph[i]) ** 2)
        dist += d
    return print(f'distance travelled = {dist}, coordinates = {(x_graph[n-1], y_graph[n-1])}')

print(di())