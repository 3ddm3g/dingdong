#!/usr/bin/env python

import sys, os, time, socket
from playsound import playsound

for k in range(1, 3):
    if not sys.argv[k]:
        print "usage: python dingdong.py [network] [start] [end]"
        print "example: python dingdong.py 192.168.1 0 255"
        sys.exit()

if int(sys.argv[2]) > 255 or int(sys.argv[3]) > 255 or int(sys.argv[2]) < 0 or int(sys.argv[3]) < 0:
    print "start end max 0 - 255"
    for k in range(2, 4): print sys.argv[k]+" "+str(k)
    sys.exit()
else:
    try: socket.inet_aton(sys.argv[1])
    except socket.error:
        print "szar network ip"
        sys.exit()

network = sys.argv[1]
check_range = [int(sys.argv[2]), int(sys.argv[3])]
refresh = 0

hosts = []
online = []
def target(lowtres, hightres):
    for k in range(lowtres, hightres+1):
        hosts.append(network + "." + str(k))

def ping(host): return os.system("ping -c 1 "+host+" 2>&1 >/dev/null")

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

#
#os.clear()
print "starting dingdong.py v1.0"
print "targeting selected hosts... ["+sys.argv[1]+"."+sys.argv[2]+"-"+sys.argv[3]+"]"
target(check_range[0], check_range[1])
#for k in range(0, len(hosts)-1): print hosts[k]
print "listening for connections..."
while True:
    for k in range(0, len(hosts)-1):
        feva = ping(hosts[k])
        if hosts[k] in online:
            if feva != 0:
                online.remove(hosts[k])
                print "[info] host disconnected: " + hosts[k]
		os.system("omxplayer -p -o local Guap.mp3 2>&1 >/dev/null")
                print "online: "+str(len(online))+" | offline: "+str(len(hosts)-len(online))
                #for k in range(0, len(hosts)-1): print hosts[k] + " | " + online[k]
        elif feva == 0:
            online.append(hosts[k])
            print "[info] greeting new host: " + hosts[k]
            os.system("omxplayer -p -o local Hering.mp3 2>&1 >/dev/null")
	    if refresh > 0: time.sleep(refresh)
#
