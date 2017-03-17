import os
import sys
import datetime

import time

import subprocess

count = 1
while (count < 2):
    time.sleep(1)
    p1 = subprocess.Popen('adb -s 8400503444243c2309cd shell ps '
                          '| busybox grep -r com.yanjun',
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    x = p1.stdout.readlines()
    now = datetime.datetime.now()
    z = now.strftime('%Y-%m-%d %H:%M:%S') + str(x[0])
    print(z)
    with open("shine.shineplay.txt", "a") as f:
        f.write(z)
