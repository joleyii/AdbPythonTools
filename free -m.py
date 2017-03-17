import os
import sys
import datetime

import time

count = 1
while count < 2:
    time.sleep(1) #一秒钟请求一次
    command = "adb -s 172.168.9.36 shell free -m" #多个adb连接时使用-s 对单个
    p = os.popen(command)
    x = p.readlines()
    now = datetime.datetime.now() #获得当前时间
    z = now.strftime('%Y-%m-%d %H:%M:%S') + x[2] #输出的第二行是内存
    print(z)
    with open("free-m9.36 0316.txt", "a") as f: #存到某个位子
        f.write(z)
