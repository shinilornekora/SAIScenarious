from matplotlib import pyplot as plt
from .helpers import littleFormula

import random

def _startApproxNoisedScenario():
    xi = list(range(1, 21))
    yi = xi

    noise = [random.uniform(-2, 2) for _ in xi]
    yi_noised = [(y_value + noise_value) for y_value, noise_value in zip(yi, noise)]

    theta1_values = [0.5, 0.8, 1.0, 1.2, 1.5]
    plt.figure(figsize=(10, 6))
    plt.scatter(xi, yi_noised, color='black', label='EXPERIMENAL_DATA')
    for theta1 in theta1_values:
        h = [littleFormula(0, theta1, x) for x in xi]
        plt.plot(xi, h, label=f'h(x) = {theta1} x')
    plt.xlabel('x')
    plt.ylabel('h(x)')
    plt.title('Approximate h(x) for different θ₁')
    plt.legend()
    plt.grid(True)
    plt.show()


def startApproxNoisedScenario():
    _startApproxNoisedScenario()
