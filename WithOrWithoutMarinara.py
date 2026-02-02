#main Branch
#BetaTestDev

#Welcome Branch
#Librearies Imported Here
import sys   # Used for writing output to the same line in the terminal
import time  # Used to add delays (sleep)
# Print developer and program info
print ("Welcome Branch - Developer: Liam Treat")
print("\nWelcome to YOUR DOOM / InfoTechCenter v.1.0")
# Loop control variable
x = 0
# Controls how many dots appear in the loading animation
ellipsis = 0
# Main boot-up loop (runs 20 times)
while x != 20:
    x += 1 # Increment loop counter
    ellipsisMessage = ("\033[33mInfoTechCenter OS Booting Up\033[0m" + "." * ellipsis) # Yellow-colored boot message with animated dots
    ellipsis += 1 # Increase number of dots shown
     # Rewrite the same line in the terminal for animation effect
    sys.stdout.write("\r\033[K" + ellipsisMessage)
     # Pause for half a second to control animation speed
    time.sleep(.5)
    # Reset dots after 3 to keep animation looping
    if ellipsis == 4:
        ellipsis = 0
         # Final message once boot sequence finishes
    if x == 20:
        print("\n\033[32mOperating System Booted Up - Print Scanned - Access Granted\033[0m")


# Weather Branch 
import random

# Weather profiles with temperature ranges
weather_profiles = {
    "Sunny": range(70, 101),
    "Partly Cloudy": range(60, 85),
    "Overcast": range(50, 75),
    "Light Rain": range(45, 70),
    "Heavy Rain": range(40, 65),
    "Thunderstorms": range(55, 80),
    "Foggy": range(35, 60),
    "Really Cold": range(-14, 35),
    "Snowing and Icy": range(-10, 32),
    "Cold and Windy": range(-14, 40)
}

# Speed rules based on weather (mph)
speed_profiles = {
    "Sunny": 65,
    "Partly Cloudy": 65,
    "Overcast": 60,
    "Light Rain": 55,
    "Heavy Rain": 45,
    "Thunderstorms": 45,
    "Foggy": 40,
    "Really Cold": 50,
    "Snowing and Icy": 35,
    "Cold and Windy": 50
}

# Calculate how much earlier (in minutes) to start/leave
def calculate_early_start_minutes(weather, temperature):
    if weather == "Snowing and Icy" or temperature <= 20:
        return 20
    if weather in ["Heavy Rain", "Thunderstorms", "Foggy"]:
        return 10
    if temperature <= 40:
        return 5
    return 0

# Select weather efficiently
weather_list = list(weather_profiles)
current_weather = random.choice(weather_list)
temperature = random.choice(weather_profiles[current_weather])

# Calculate driving behavior
vehicle_speed = speed_profiles[current_weather]
early_start_minutes = calculate_early_start_minutes(current_weather, temperature)

# Output
print("🚗 Vehicle Status Update")
print(f"🌡️ Outside Temperature: {temperature}°F")
print(f"🌤️ Weather Condition: {current_weather}")

print(f"🚦 Recommended Driving Speed: {vehicle_speed} mph")

# Notifications
if early_start_minutes > 0:
    print(f"⏰ Travel Advisory: Start your car {early_start_minutes} minutes earlier due to weather conditions.")

if current_weather in ["Heavy Rain", "Foggy", "Snowing and Icy", "Thunderstorms"]:
    print("📱 Safety Alert: Reduced speed due to hazardous road conditions.")

print("✅ Drive safely!")

