# The endpoint '/test/webhooks' is vulnerable to DNS Rebinding

## Report Details
- **Report ID**: 1379656
- **URL**: https://hackerone.com/reports/1379656
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-24T12:45:23.942Z
- **Disclosed**: 2022-03-22T21:56:45.736Z

## Reporter
- **Username**: sim4n6
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
## Summary:

DNS rebinding attack is a method of switching the resolution of domain names as wished by the attacker. The aim is to lure the web app to a different IP address/host.  In this attack, and particularly in our case, a malicious server will first perform a domain name resolution to the IP address of `178.62.122.208` (a random HTTP server that is valid as a Web-hook for Omise web-app) and than rebind to an internal IP address `127.0.0.1`, thus, bypassing firewall protection.  

The malicious link is `https://A.178.62.122.208.1time.127.0.0.1.1time.repeat.rebind.network/webhook5` can be depicted as follow:
  1. Initial resolution of the IP address will point to `178.62.122.208` for the first time.
  2. The second time, the malicious DNS server will resolve to `127.0.0.1` for one time.
  3.The next time the DNS server will switch back the first IP address. And so on.

When a user uses a private IP address an error will be displayed, the web app recognizes that the web-hook endpoint is either insecure or forbidden.
However, DNS rebinding attack will bypass this protection.

## Steps To Reproduce:

  1. Create an account at Omise.co and go to <https://dashboard.omise.co/test/webhooks>
  1. Add the following endpoint `https://A.178.62.122.208.1time.127.0.0.1.1time.repeat.rebind.network/webhook5` as an external web-hook.

In case, the malicious DNS server resolves initially the previous URL to `127.0.0.1` you will get this error:

  {F1491842}

In case, it resolves initially to the other IP address. It will be saved.

{F1491844}  

## Supporting Material/References:

  * <https://hackerone.com/reports/508459>
  * <https://github.com/brannondorsey/whonow>

## Impact

This is a Blind SSRF, since the malicious URL induces the server side to perform a request to an internal endpoint each time a recent activity is fired such as *Create a recipient*. Furthermore, the malicious URL can be further personalized (replace `webhook5` with `else/internal` to get `https://127.0.0.1/else/internal`).

## Attachments
- w1.png
- w2.png
