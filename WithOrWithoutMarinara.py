#Gasoline Branch
# def = Short for define. It tells Python you’re about to define a function.
#
def gas_tank_level (current_amount, tank_capacity):
    percent_full = (current_amount / tank_capacity) * 100
    return round(percent_full, 1)

current_gas = float(input("Enter current gas amount: "))
tank_capacity = float(input("Enter total tank capacity: "))

level = gas_tank_level(current_gas, tank_capacity)
print(f"Gas tank level: {level}%")