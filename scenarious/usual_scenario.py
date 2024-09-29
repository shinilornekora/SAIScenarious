from matplotlib import pyplot as plt
import numpy as np

from .helpers import mainFormula

def startDrawScenario(theta1_values, J_values, theta1_min):
    plt.plot(theta1_values, J_values, label="Без шума")
    plt.axvline(x=theta1_min, color='r', linestyle='--', label=f'Минимум при theta1={theta1_min:.2f}')
    plt.title('J(theta1) от theta1 (usual)')
    plt.xlabel('theta1')
    plt.ylabel('J(theta1)')
    plt.legend()
    plt.grid(True)
    plt.show()

def startCalcScenario():
    x = np.arange(1, 21)
    y = x

    theta_1_values = np.linspace(0, 2, 100)
    J_values = np.array([mainFormula(theta1, x, y) for theta1 in theta_1_values])
    theta_1_min = theta_1_values[np.argmin(J_values)]

    return [theta_1_values, J_values, theta_1_min]


def startUsualScenario():
    print("Starting the usual scenario...\n")
    
    print("Starting the calculation scenario...\n")
    theta_1_values, J_values, theta_1_min = startCalcScenario()
    print("Successfully ended calculation scenario.")

    print("Starting the drawing scenario...\n")
    startDrawScenario(theta1_values=theta_1_values, J_values=J_values, theta1_min=theta_1_min)
    print("Successfully ended drawing scenario.")
    
    print("Ended the usual scenario.")

