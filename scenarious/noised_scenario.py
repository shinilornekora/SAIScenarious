from matplotlib import pyplot as plt
import random

def mainFormula(theta1, x, y):
    J = 0
    for i in range(len(x)):
        J += (theta1 * x[i] - y[i]) ** 2
    return J


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
    x = list(range(1, 21))
    y = x

    theta_1_values = [i / 50 for i in range(101)]
    
    random.seed(42)
    noise = [random.uniform(-2, 2) for _ in range(len(y))]
    y_noisy = [y[i] + noise[i] for i in range(len(y))]

    J_values_noisy = [mainFormula(theta1, x, y_noisy) for theta1 in theta_1_values]

    min_J = J_values_noisy[0]
    theta1_min_noisy = theta_1_values[0]
    for i in range(1, len(J_values_noisy)):
        if J_values_noisy[i] < min_J:
            min_J = J_values_noisy[i]
            theta1_min_noisy = theta_1_values[i]

    return theta_1_values, J_values_noisy, theta1_min_noisy


def startNoisyScenario():
    print("Starting the noisy scenario...\n")
    print("Starting the calculation scenario...\n")
    theta_1_values, J_values_noisy, theta1_min_noisy = startCalcScenario()
    print("Successfully ended calculation scenario.")

    print("Starting the drawing scenario...\n")
    startDrawScenario(theta1_values=theta_1_values, J_values_noisy=J_values_noisy, theta1_min_noisy=theta1_min_noisy)
    print("Successfully ended drawing scenario.")

    print("Ended the noisy scenario.")

