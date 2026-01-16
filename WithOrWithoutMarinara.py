#Welcome Branch
#Librearies Imported Here
import sys
import time
print ("Welcome Branch - Developer: Liam Treat")
print("\nWelcome to YOUR DOOM / InfoTechCenter v.1.0")
x = 0
ellipsis = 0
while x != 20:
    x += 1
    ellipsisMessage = ("\033[33mInfoTechCenter OS Booting Up\033[0m" + "." * ellipsis)
    wellipsisMessage = ("   ")
    ellipsis += 1
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\033[32mOperating System Booted Up - Print Scanned - Access Granted\033[0m")