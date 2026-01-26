#Weather Branch
import random

weather_profiles = {
    "Sunny": range(70, 101),
    "Partly cloudy": range(60, 85),
    "Overcast": range(50, 75),
    "Light rain": range(45, 70),
    "Heavy rain. Reduced speed for safety.": range(40, 65),
    "Thunderstorms": range(55, 80),
    "Foggy. Reduced speed for safety.": range(35, 60),
    "Really cold.": range(-14, 35),
    "Snowing and Icy. Reduced speed for safety.": range(-10, 32),
    "Cold and Windy": range(-14, 40)
}

weather = random.choice(list(weather_profiles.keys()))
temperature = random.choice(weather_profiles[weather])

print("🚗 Vehicle Status Update")
print(f"🌡️ Outside Temperature: {temperature}°F")
print(f"🌤️ Weather Condition: {weather}")

if temperature <= 40:
    print("📱 Weather Alert: Roads may be slow — consider leaving earlier.")

print("Drive safely.")