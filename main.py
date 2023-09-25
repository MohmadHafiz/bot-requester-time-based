from requests import get, post
from random import randint
from _thread import start_new_thread
from time import sleep, localtime, strftime
from datetime import datetime

import requests

websites = [
    "https://pb.edu.bn",
    "https://instagram.com",
    "https://lms.pb.edu.bn"
]

# 6am - 8am > 2-4
# 9am - 11am > 5-25
# 12pm - 2pm > 4-6
# 3pm - 6pm > 5-20
# 7pm - 9pm > 5-10
# 10pm - 11pm > 2-5 
# 12am - 5am > 1-3

# 12 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 12 22 23 24
#                               1  2  3  4  5  6  7  8  9  10 11 12

thred_runnin = [
    {
        "min":6, "max":8, "t":[2,4], "p": "AM"
    },
    {
        "min":9, "max":12, "t":[5,25], "p": "AM"
    },
    {
        "min":1, "max":2, "t":[4,6], "p": "PM"
    },
    {
        "min":3, "max":6, "t":[5,20], "p": "PM"
    },
    {
        "min":7, "max":9, "t":[5,10], "p": "PM"
    },
    {
        "min":10, "max":12, "t":[2,5], "p": "PM"
    },
    {
        "min":1, "max":5, "t":[1,3], "p": "AM"
    },
]

methods = ["get", "post"]

Errs = 0

def get_time():
    t = localtime()
    ct = strftime("%H:%M")
    ct = str(ct)

    d = datetime.strptime(ct, "%H:%M")
    ct = str(d.strftime("%I:%M:%p"))
    return(ct.split(":"))

def send_req(web, method):
    global Errs

    h, m, p = get_time()
    sleep(randint(5, 10))

    err = False
    no_err = 0
    while True:
        try:
            if method == "post":
                r = get(www)

            elif method == "get":
                r = post(www)

            print(f"[+] REQ -> {web} | [{h}:{m} {p}][{method.upper()}][{r.status_code}][{len(r.text)}]");
            break

        except Exception as e:
            # print(e)
            # err = True
            no_err += 1
            if no_err >= 3:
                print(f"[!] DOWN? -> {web}")
            # Errs += 1
            sleep(3)
    
    if err:
        Errs -= no_err

while True:
    try:
        h, m, p = get_time()
        h = int(h)
        m = int(m)

        thred = None

        for i in thred_runnin:
            if i["p"] == p:
                if i["min"] <= h and i["max"] >= h:
                    thred = randint(i["t"][0], i["t"][1])

        if thred != None:
            for i in range(thred):
                www = websites[randint(0, len(websites)-1)]
                method = methods[randint(0, len(methods)-1)]

                # if Errs < 15:
                start_new_thread(send_req, (www, method,))
                # sleep(randint(1, 2))
                sleep(randint(3, 5))

    except KeyboardInterrupt:
        exit()