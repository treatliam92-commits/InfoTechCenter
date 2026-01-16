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

