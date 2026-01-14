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
    ellipsisMessage = ("InfoTechCenter OS Booting Up" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + ellipsisMessage + "   ")
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Print Scanned - Access Granted")