# dingdong.py v1.0

daemon listening to lan ip connections and makes a sound at new host

1. cd dingdong/
2. pip install -r requirements.txt
3. python dingdong.py |network| |start| |end|

$ python dingdong.py 192.168.1 100 108
starting dingdong.py v1.0
targeting selected hosts... [192.168.1.100-108]
listening for connections...
[info] greeting new host: 192.168.1.100
[info] greeting new host: 192.168.1.103
[info] greeting new host: 192.168.1.104
[info] greeting new host: 192.168.1.102
[info] host disconnected: 192.168.1.102
online: 3 | offline: 6
