#Gasoline Branch
# 
import random
# def = Short for define. It tells Python you’re about to define a function.
def random_gas_tank_status(tank_capacity=50):
    current_amount = random.uniform(0, tank_capacity)
    percent_full = (current_amount / tank_capacity) * 100
    percent_full = round(percent_full, 1)

    print(f"⛽ Gas tank level: {percent_full}%")

    if percent_full < 25:
        print("⚠️ Low fuel — please go to the gas station.")
    if percent_full > 25:
        print ("Looking good. Drive safe :)")

# Example usage
random_gas_tank_status()