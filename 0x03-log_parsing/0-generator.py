#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime
"""
lst = ['58.70.209.187 - [2017-02-05 23:28:50.564010] "GET /projects/260 HTTP/1.1" 401 708',
'125.218.201.102 - [2017-02-05 23:28:51.484960] "GET /projects/260 HTTP/1.1" 500 684',
'93.202.122.198 - [2017-02-05 23:28:52.060026] "GET /projects/260 HTTP/1.1" 500 1002',
'83.93.222.77 - [2017-02-05 23:28:52.920758] "GET /projects/260 HTTP/1.1" 200 551',
'186.161.131.204 - [2017-02-05 23:28:53.006680] "GET /projects/260 HTTP/1.1" 500 665',
'61.146.36.164 - [2017-02-05 23:28:53.792909] "GET /projects/260 HTTP/1.1" 401 299',
'70.139.77.18 - [2017-02-05 23:28:54.747004] "GET /projects/260 HTTP/1.1" 403 543',
'241.71.80.100 - [2017-02-05 23:28:55.573972] "GET /projects/260 HTTP/1.1" 500 222',
'219.109.138.129 - [2017-02-05 23:28:55.755290] "GET /projects/260 HTTP/1.1" 200 186',
'118.99.189.189 - [2017-02-05 23:28:56.091266] "GET /projects/260 HTTP/1.1" 403 278']
"""
lst = [
        '68.249.9.20 - [2017-02-05 23:31:22.452556] "GET /projects/260 HTTP/1.1" 200 711',
        'Hello',
        '99.196.100.39 - [2017-02-05 23:31:22.954433] "GET /projects/260 HTTP/1.1" 401 658',
        '128.230.61.246 - [2017-02-05 23:31:23.258076] "GET /projects/260 HTTP/1.1" Hello 292',
        '116.82.223.35 - [2017-02-05 23:31:24.112360] "GET /projects/260 HTTP/1.1" 301 842',
        'Holberton - [2017-02-05 23:31:25.003550] "GET /projects/260 HTTP/1.1" 400 12',
        '7.179.133.121 - [2017-02-05 23:31:25.003550] "GET /projects/260 HTTP/1.1" 400 12',
        '188.213.11.218-[2017-02-05 23:31:21.690755] "GET /projects/260 HTTP/1.1" 401 1000',
        '128.230.61.246 - [2017-02-05 23:31:23.258076] "GET /projects/260 HTTP/1.1" 301 292'
        ]
for i in range(len(lst)):
    sleep(random.random())
    # sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
    #     random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
    #     datetime.datetime.now(),
    #     random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
    #     random.randint(1, 1024)
    sys.stdout.write(lst[i]+'\n')
    sys.stdout.flush()
