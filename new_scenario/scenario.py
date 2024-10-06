from matplotlib import pyplot as plt
import random


def mainFormula(theta1, x, y):
    J = 0
    for i in range(len(x)):
        J += (theta1 * x[i] - y[i]) ** 2
    return J


def littleFormula(theta0, theta1, x):
    return theta0 + theta1 * x


def startCalcScenarioNoised():
    x = list(range(1, 21))
    y = x

    theta_1_values = [i / 50 for i in range(40, 60)]
    
    noise = [random.uniform(-2, 2) for _ in range(len(y))]
    y_noisy = [y[i] + noise[i] for i in range(len(y))]

    J_values_noisy = [mainFormula(theta1, x, y_noisy) for theta1 in theta_1_values]

    min_J = J_values_noisy[0]
    theta1_min_noisy = theta_1_values[0]
    for i in range(1, len(J_values_noisy)):
        if J_values_noisy[i] < min_J:
            min_J = J_values_noisy[i]
            theta1_min_noisy = theta_1_values[i]

    return [theta_1_values, J_values_noisy, theta1_min_noisy]


def startCalcScenarioUsual():
    x = list(range(1, 21))
    y = x

    theta_1_values = [i / 50 for i in range(40, 60)]
    J_values = [mainFormula(theta1, x, y) for theta1 in theta_1_values]

    min_J = J_values[0]
    theta1_min = theta_1_values[0]
    for i in range(1, len(J_values)):
        if J_values[i] < min_J:
            min_J = J_values[i]
            theta1_min = theta_1_values[i]

    return [theta_1_values, J_values, theta1_min]


def startMinCalc():
    usualThetaValues, usualJValues, usualThetaMin = list(startCalcScenarioUsual())
    noisedThetaValues, noisedJValues, noisedThetaMin = list(startCalcScenarioNoised())

    # Отображаем обычную часть
    plt.plot(usualThetaValues, usualJValues, label="Без шума")
    plt.axvline(x=usualThetaMin, color='r', linestyle='--', label=f'Минимум при theta1={usualThetaMin:.2f}')   

    # Отображаем зашумленную часть
    plt.plot(noisedThetaValues, noisedJValues, label="С шумом")
    plt.axvline(
        label=f'Минимум при theta1={noisedThetaMin:.2f}',
        x=noisedThetaMin, 
        color='r', 
        linestyle='--'
    )

    # Общее, для красоты
    plt.title('Зависимость J(theta1) от theta1')
    plt.xlabel('theta1')
    plt.ylabel('J(theta1)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return noisedThetaMin


def startApproxScenario(minimalNoisedTheta):
    plt.figure(figsize=(10, 6))

    xi = list(range(1, 15))
    xi_nsd = list(range(1, 15))
    yi = xi
    yi_nsd = xi_nsd

    noise = [random.uniform(-2, 2) for _ in xi_nsd]
    yi_noised = [(y_value + noise_value) for y_value, noise_value in zip(yi_nsd, noise)]

    theta1_values = [0.5, 0.8, 1.0, 1.2, 1.5]

    plt.scatter(xi, yi, color='black', label='EXPERIMENTAL_DATA')
    plt.scatter(xi_nsd, yi_noised, color='blue', label='EXPERIMENTAL_DATA_NOISED')

    for theta1 in theta1_values:
        h = [littleFormula(0, theta1, x) for x in xi]
        plt.plot(xi, h, label=f'h(x) = {theta1} x')

    h_NSD = [littleFormula(0, minimalNoisedTheta, x) for x in xi]
    plt.plot(xi, h_NSD, label=f'h(x) = {minimalNoisedTheta} x [NOISED]', color="purple")
    
    plt.xlabel('x')
    plt.ylabel('h(x)')

    plt.xticks(range(1, 15, 1))
    plt.yticks(range(1, 15, 1))

    plt.title('Approximate h(x) for different θ₁')
    plt.legend()
    plt.grid(True)
    plt.show()


def mainScenario():
    minimalNoisedTheta = startMinCalc()
    startApproxScenario(minimalNoisedTheta)


mainScenario()