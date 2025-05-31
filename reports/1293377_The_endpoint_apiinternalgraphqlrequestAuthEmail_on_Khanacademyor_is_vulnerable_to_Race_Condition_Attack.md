# The endpoint /api/internal/graphql/requestAuthEmail on Khanacademy.or is vulnerable to Race Condition Attack.

## Report Details
- **Report ID**: 1293377
- **URL**: https://hackerone.com/reports/1293377
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-06T10:50:09.125Z
- **Disclosed**: 2022-03-22T21:31:22.779Z

## Reporter
- **Username**: sim4n6
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
## Summary 

The endpoint `/api/internal/graphql/requestAuthEmail` on `www.khanacademy.org` is vulnerable to a _Race condition attack_. That may cause a random e-mail user to receive an important amount of emails to **Finish signing up for Khan Academy** with invalid links. The attack is because _your web applications checks the state of a resource (endpoint) before using that resource, but the resource's state can change between the check and the use in a way that invalidates the results of the check. This can cause the software to perform invalid actions when the resource is in an unexpected state._  

## Steps to reproduce:

1. Connect to an account on www.khanacademy.org.
1. Go to your ** Profile name > Settings > Account tab > Linked accounts > Connect another email.**
1. Confirm your identity by providing your password.

█████

4. Write out a valid email, and then intercept the request using Burp Suite at least community edition when you click on **Send confirmation email**. Downgrade the HTTP communication protocol to `HTTP 1.1` and add the following header to the request : `X-Request: %s` (for the Turbo intruder extension).
5. Send the intercepted request to Turbo intruder burp suite extension, and use the following python code to perform the attack :

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, target.baseInput, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
```

6. Start the attack, the results are a lot of `200 OK` as can be shown in the following screenshot:

{F1401913}

As you can, I've send only 30 requests in a small time frame.  
7. The results is definitely an unwanted behavior. Where a random user, in our case `███` receives **30** emails inviting him to finish signing up for Khan-academy. 

{F1401914}

8. The invitation link within those e-mails are most invalid and produce the following error.

{F1401915}

9. This behavior is not expected by your system since if you try to add an already added email your get the following warning.

███████

## Impact

* The endpoint `/api/internal/graphql/requestAuthEmail` on [www.khanacademy.org](https://www.khanacademy.org) is vulnerable to a Race condition attack. That may cause a bombing e-mail a random user with an important amount of emails (in our PoC we had only 30 but it could be much more). The emails sent are **Finish signing up for Khan Academy** with mostly invalid links.

## Attachments
- 2.png
- 3.png
- 4.png
