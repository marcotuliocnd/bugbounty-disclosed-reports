# Incorrect param parsing in Digits web authentication

## Report Details
- **Report ID**: 126522
- **URL**: https://hackerone.com/reports/126522
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-28T16:57:50.738Z
- **Disclosed**: 2018-08-18T05:57:12.114Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an issue on Digits web authentication which allows attackers to retrieve the OAuth credential data of an application victims authorized.

#Detail
Digits web authentication has strict validation on *host* and *callback_url*. On the server side, the values are compared with the registered domain. However, on the client side, the way parameters are parsed has a wrong assumption. Specifically, 
in https://cdn.digits.com/45ed91c4cf9b6bb7465c27574b16910df8a86d2e_1458327827406/javascripts/popup.js

```javascript
              return window.location.search.slice(1).split("&").forEach(function(e) {
                    var n = e.split("=");
                    t[n[0]] = window.unescape(n[1])
                })
```

The above code snippet is responsible to convert query string into parameters, which assumes that the param delimiter has to be ampersand (&). In fact, the server side also accepts semi-colon (;) as param delimiter. For example:
> https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE;host=https%3A%2F%2Fwww.periscope.tv

is the same as 

> https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fwww.periscope.tv

This creates a problem because from the server's perspective, ```a=b;c=d``` is two different parameters *a* and *c*, while the client thinks there is only one parameter *a* with value *b;c=d*. Attacker can evade the validation by append `;@attacker.com` in the corresponding param. Such bypass looks like this:

> https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fwww.periscope.tv;@attacker.com

The server side thinks the  *host* parameter is ```https://www.periscope.tv```, while for client side it is ```https://www.periscope.tv;@attacker.com```.

The funky URL in browser perspective looks like this:

```
https://www.periscope.tv;@attacker.com
--------\    authority   /\ hostname /
```

Therefore attacker successfully control the destination domain to his/her controlled site.

#PoC
1. Prepare a Periscope account which is associated with a phone number
2. Login to Periscope using the phone number with digits web login flow: https://innerht.ml/pocs/digits-validation-bypass/
3. After that your account will be renamed as "Pwn3d"

#Fix
In addition to ampersand, also treat semi-colon as param delimiter. A sample patch would be to change
```javascript
window.location.search.slice(1).split("&")
```
to
```javascript
window.location.search.slice(1).split(/[&;]/)
```

## Attachments
No attachments
