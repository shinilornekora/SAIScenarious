from matplotlib import pyplot as plt
import numpy as np

from .helpers import mainFormula

def startDrawScenario(theta1_values, J_values_noisy, theta1_min_noisy):
    plt.plot(theta1_values, J_values_noisy, label="С шумом")
    plt.axvline(x=theta1_min_noisy, color='r', linestyle='--', label=f'Минимум при theta1={theta1_min_noisy:.2f}')
    plt.title('Зависимость J(theta1) от theta1 (с шумом)')
    plt.xlabel('theta1')
    plt.ylabel('J(theta1)')
    plt.legend()
    plt.grid(True)
    plt.show()

def startCalcScenario():
    x = np.arange(1, 21)
    y = x

    theta_1_values = np.linspace(0, 2, 100)
    noise = np.random.uniform(-2, 2, size=y.shape)
    y_noisy = y + noise

    J_values_noisy = np.array([mainFormula(theta1, x, y_noisy) for theta1 in theta_1_values])

    theta1_min_noisy = theta_1_values[np.argmin(J_values_noisy)]

    return [theta_1_values, J_values_noisy, theta1_min_noisy]


def startNoisyScenario():
    print("Starting the noisy scenario...\n")
    
    print("Starting the calculation scenario...\n")
    theta_1_values, J_values_noisy, theta1_min_noisy = startCalcScenario()
    print("Successfully ended calculation scenario.")

    print("Starting the drawing scenario...\n")
    startDrawScenario(theta1_values=theta_1_values, J_values_noisy=J_values_noisy, theta1_min_noisy=theta1_min_noisy)
    print("Successfully ended drawing scenario.")

    print("Ended the noisy scenario.")
