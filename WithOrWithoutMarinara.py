# Gasoline Branch - Conditional Logic Simplified
import random

# -----------------------------
# Gas tank status
# -----------------------------
def random_gas_tank_status(tank_capacity=50):
    current_amount = random.uniform(0, tank_capacity)
    percent_full = round((current_amount / tank_capacity) * 100, 1)

    print(f"⛽ Gas tank level: {percent_full}%")

    return percent_full


# -----------------------------
# Simulated nearby gas stations
# -----------------------------
gas_stations = [
    {"name": "Shell", "price": round(random.uniform(2.4, 3.7), 2), "distance": round(random.uniform(1, 30), 1)},
    {"name": "Chevron", "price": round(random.uniform(2.4, 3.7), 2), "distance": round(random.uniform(1, 30), 1)},
    {"name": "Exxon", "price": round(random.uniform(2.4, 3.7), 2), "distance": round(random.uniform(1, 30), 1)},
    {"name": "BP", "price": round(random.uniform(2.4, 3.7), 2), "distance": round(random.uniform(1, 30), 1)},
    {"name": "Costco Gas", "price": round(random.uniform(2.4, 3.7), 2), "distance": round(random.uniform(1, 30), 1)}
]


# -----------------------------
# Find best gas station with expanding radius
# -----------------------------
def find_best_gas_station():
    search_radius = 10
    max_radius = 25
    radius_step = 5

    while search_radius <= max_radius:
        valid_stations = [
            station for station in gas_stations
            if 2.50 <= station["price"] <= 3.50
            and station["distance"] <= search_radius
        ]

        if valid_stations:
            return sorted(valid_stations, key=lambda x: (x["price"], x["distance"]))[0]

        search_radius += radius_step

    return None


# -----------------------------
# Calculate wake-up adjustment
# -----------------------------
def calculate_wakeup_adjustment(distance, fuel_percent):
    extra_minutes = int(distance * 2)

    if fuel_percent < 15:
        extra_minutes += 10
    elif fuel_percent < 25:
        extra_minutes += 5

    return extra_minutes


# -----------------------------
# Main execution
# -----------------------------
fuel_percent = random_gas_tank_status()

# If gas is good, say nothing else
if fuel_percent >= 25:
    print("✅ Drive safe!")
else:
    best_station = find_best_gas_station()

    if best_station:
        print("\n⛽ Recommended Gas Station")
        print(f"🏪 Name: {best_station['name']}")
        print(f"💲 Price: ${best_station['price']} / gallon")
        print(f"📍 Distance: {best_station['distance']} miles away")

        wakeup_minutes = calculate_wakeup_adjustment(
            best_station["distance"], fuel_percent
        )

        print(f"⏰ Wake-Up Advisory: Wake up {wakeup_minutes} minutes earlier to get gas.")
    else:
        print("⚠️ No suitable gas stations found — plan accordingly.")
