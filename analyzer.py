from scenarious.noised_scenario import startNoisyScenario
from scenarious.usual_scenario import startUsualScenario


def startCommonScenario():
    while True:
        scenario = input("Select scenario - U (USUAL) | N (NOISED): ")

        if (scenario == 'U'):
            startUsualScenario()
            continue
        
        if (scenario == 'N'):
            startNoisyScenario()
            continue

        break
    print("Program was closed successfully.")

startCommonScenario()
