# Bypassing Digits bridge origin validation

## Report Details
- **Report ID**: 110467
- **URL**: https://hackerone.com/reports/110467
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-13T14:14:24.338Z
- **Disclosed**: 2017-04-30T15:41:17.220Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an issue in the bridge proxy in Digits which allows attacker to retrieve the OAuth credential data of an application victims authorized.

#Detail
In the Digits Web SDK, the method [getLoginStatus](https://docs.fabric.io/web/digits/getting-started.html#set-up-digits-authentication) can be used to retrieve the OAuth credential data of an application if the user has already logged in Digits and authorized the app. The way it works is to inject an hidden iframe (I call it bridge because the URL is https://www.digits.com/bridge) which acts like a proxy into the webpage and communicate using *postMessage*. Once the bridge receives the *getLoginStatus* command, it will make an AJAX request to /login_status and the response will contain the OAuth credential data of the user of an application. Then, the bridge will send back the data via *postMessage* to parent window.

For example:

```
+----------------------------------------------------------------------------------+
| https://www.periscope.tv/                                                        |
+----------------------------------------------------------------------------------+
|                                                                                  |
|  +----------------------------------------------------------------------------+  |
|  | https://www.digits.com/bridge?consumer_key=.&host=https://www.periscope.tv |  |
|  +----------------------------------------------------------------------------+  |
|  |                                                                            |  |
|  |                      ^                           +                         |  |
|  +----------------------------------------------------------------------------+  |
|                         |                           |                            |
|                         |                           |                            |
|                         |                           |                            |
|                         |                           |                            |
|                         |                           |                            |
|                         +                           v                            |
|                   getLoginStatus             OAuth Credential                    |
|                                                                                  |
+----------------------------------------------------------------------------------+
```

If https://www.periscope.tv/ invokes *Digits.getLoginStatus()*, then an iframe will be injected where the *host* parameter is the invoker origin.

There's a protection in place which validates whether the *host* parameter provided matches the application registered domain. For example, ```/bridge?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https://www.periscope.tv``` passes while ```/bridge?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https://attacker.com``` fails. This prevents others to use the same *consumer_key* to pretend to be the legit application to issue the command.

However, **there is no validation to check whether the page which embeds the bridge proxy is from the registered domain**. In other words, attacker can manually embed ```/bridge?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https://www.periscope.tv``` into his/her webpage and issue command on behalf of the legit application.

#Impact
It affects every application that has integrated Digits, and even official application (Periscope). Attacker can abuse the flaw to login to victim's account on the affected applications. In addition, this attack **does not require user interaction**. The only prerequisite is that the victim has already logged in Digits and authorized the application.

#PoC
1. Prepare a Periscope account which is associated with a phone number, and make sure you have logged in Digits (https://www.digits.com/signin) with that number
2. Go to http://innerht.ml/pocs/digits-bridge-origin-validation-bypass/
3. Wait for a while
4. You Periscope account will be renamed as "Pwn3d"

Video demo: https://vimeo.com/151646523 (password: proxy)

And as always, since it does not require user interaction, it can be put into a player card to achieve maximum stealthiness.

#Fix
It would be ideal to employ CORS instead of postMessage + proxy for that purpose. An alternative fix would be to check whether the page embedding the bridge proxy is from the registered domain by comparing referrer (pretty unsound though).

## Attachments
No attachments
