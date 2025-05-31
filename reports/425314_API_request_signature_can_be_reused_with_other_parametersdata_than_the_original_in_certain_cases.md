# API request signature can be reused with other parameters/data than the original in certain cases

## Report Details
- **Report ID**: 425314
- **URL**: https://hackerone.com/reports/425314
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-18T10:35:37.715Z
- **Disclosed**: 2019-02-23T07:19:45.050Z

## Reporter
- **Username**: p4fg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gatecoin

## Vulnerability Information
If an attacker can intercept/see an API-request from a client who has a system-clock that is slightly ahead of the server time then the attacker can re-use the API request-signature towards the same URL (but with a different payload). This can for some of the endpoint lead to serious vulnerabilities.

This means that if an attacker can see a API-request from the user to create a read-only API-key, then the attacker can create a API-key with full privileges.

The system seems to be caching the signature for 300 seconds (5 minutes), any request with the same signature within this time will get the response:
```
HTTP 401
You are not authorized. The same request was already made within the same millisecond.
```

If the request timestamp is more than 5 minutes old, the system will reject the request (as per documentation):
```
HTTP 401
You are not authorized. The request timestamp must be within 5 minutes of the server time. Your request is -5.01693514166667 minutes compared to the server. Server time is currently Thursday, October 18, 2018 6:04:26 PM.
```

However, IF the original request comes from a computer with a system-clock that is ahead of the server by a few seconds, there exists a window of opportunity where the signature is removed from the cache AND the request time is less than 5 minutes from the server-time.

At this time it is possible to re-use the signature but with another payload (as the payload is, unfortunately, not part of the signature). 

In the enclosed python-example a read-only API key is created with a timestamp 3 seconds in the future. The script then waits until 299 seconds has passed and then starts sending a new request to create a API-key but with privileges to trade and withdraw. The first requests will get "You are not authorized. The same request was already made within the same millisecond." indicating that the signature is still cached, but after a few requests the signature will be removed from the cache and the request will go through, creating a API-key with all privileges.

A quick-fix would be to cache the signatures 10+ minutes instead of 5 minutes (as the first request in the worst-worst-worst case could be 5 minutes ahead of the server-time and the attacker then can use the signature until 5 minutes after server-time).

A proper fix of the problem would be to both cache 10+ minutes AND include the payload-data in the data that is signed. That way a replay/reuse attack would only repeat the operation with the same parameters.

## Impact

If an attacker can add a API with trading privileges, that key could enable the attacker to do unfavorable trades using the victims account (dump a coin with low liquidity or buy some coin at a very high price), and giving the attacker a potential to profit.

The same exploit could also be used to add a attacker-controlled withdraw-wallet, which in combination with a API-key with withdraw-privileges would lead to loss of funds.

## Attachments
- reuse_signature_gatecoin.py
