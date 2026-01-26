#Weather Branch
import random

weather_profiles = {
    "Sunny": range(70, 101),
    "Partly cloudy": range(60, 85),
    "Overcast": range(50, 75),
    "Light rain": range(45, 70),
    "Heavy rain": range(40, 65),
    "Thunderstorms": range(55, 80),
    "Foggy": range(35, 60),
    "Snowing": range(-10, 35),
    "Windy": range(30, 70)
}

weather = random.choice(list(weather_profiles.keys()))
temperature = random.choice(weather_profiles[weather])

print("🚗 Vehicle Status Update")
print(f"🌡️ Outside Temperature: {temperature}°F")
print(f"🌤️ Weather Condition: {weather}")
print("Drive safely.")
