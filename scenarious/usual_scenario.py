from matplotlib import pyplot as plt
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
    x = list(range(1, 21))
    y = x

    theta_1_values = [i / 50 for i in range(101)]
    J_values = [mainFormula(theta1, x, y) for theta1 in theta_1_values]

    min_J = J_values[0]
    theta1_min = theta_1_values[0]
    for i in range(1, len(J_values)):
        if J_values[i] < min_J:
            min_J = J_values[i]
            theta1_min = theta_1_values[i]

    return theta_1_values, J_values, theta1_min


def startUsualScenario():
    print("Starting the usual scenario...\n")
    print("Starting the calculation scenario...\n")
    theta_1_values, J_values, theta_1_min = startCalcScenario()
    print("Successfully ended calculation scenario.")

    print("Starting the drawing scenario...\n")
    startDrawScenario(theta1_values=theta_1_values, J_values=J_values, theta1_min=theta_1_min)
    print("Successfully ended drawing scenario.")

    print("Ended the usual scenario.")

