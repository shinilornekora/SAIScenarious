import numpy as np

# Наша основная функция, спецификация сохранена.
def mainFormula(theta1, x, y):
    h = theta1 * x
    J = np.sum((h - y) ** 2)

    return J