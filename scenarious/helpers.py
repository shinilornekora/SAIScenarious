import numpy as np

# Наша основная функция, спецификация сохранена.
def mainFormula(theta1, x, y):
    J = 0
    for i in range(len(x)):
        J += (theta1 * x[i] - y[i]) ** 2
    return J

def littleFormula(theta0, theta1, x):
    return theta0 + theta1 * x
