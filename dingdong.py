#!/usr/bin/env python

import sys, os, playsound
from threading import Timer

if not sys.argv[1]:
    print "usage: python dingdong.py [ip range]"
    print "example: python dingdong.py 192.168.0.1-255"
    sys.exit()

iprange = sys.argv[1]
network = iprange.split(".")[0]+"."+iprange.split(".")[1]+"."+iprange.split(".")[2]
hostrange = [int(iprange.split(".")[3].split("-")[0]), int(iprange.split(".")[3].split("-")[1])]
hosts = []

class Host:
    def __init__(self, cim, upno, uje):
        self.ip = cim
        self.online = upno
        self.new = uje
    def ping(self): return os.system("ping -c 1 "+self.ip+" 2>&1 >/dev/null")
    def chnew(self, state): self.new = state

for k in range(0,100): print(" ")
print "starting dingdong.py v1.2"
print "targeting selected hosts... [ "+iprange+" ]"
for k in range(hostrange[0], hostrange[1]+1): hosts.append(Host(network + "." + str(k), False, True))
print "listening on "+str(len(hosts))+" host(s)"
while True:
    for k in hosts:
        isup = hosts[k].ping()
        if hosts[k].online:
            if isup != 0:
                avc = 0
                hosts[k].online = False
                print "[info] host disconnected: " + hosts[k].ip
                for i in range(0, len(hosts)-1):
                    if hosts[i].online: avc+=1
                print "online: "+str(avc)+" | offline: "+str(len(hosts)-avc)
        elif isup == 0 and hosts[k].new:
            hosts[k].online = True
            hosts[k].chnew(True)
            print "[info] greeting new host: " + hosts[k].ip
            Timer(3000, hosts[k].chnew(False)).start()
            playsound("Hering.mp3")
