# dingdong.py v1.2

dingdong.py is a daemon listening for new connections in your local network and dings the bell mp3 at a new device so it works as an auto doorbell

To work as an exact automatic doorbell the devices should have already have your wifi

# installation

0. git clone https://github.com/3ddm3g/dingdong
1. cd dingdong/
2. apt-get install omxplayer
3. python dingdong.py |ip range|

# misc

yea it uses omxplayer because my old raspberry pi cannot run playsound
