# █████ - DOM-based XSS

## Report Details
- **Report ID**: 376027
- **URL**: https://hackerone.com/reports/376027
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-03T13:56:25.903Z
- **Disclosed**: 2019-12-02T19:08:18.562Z

## Reporter
- **Username**: yumi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings, 

I've discovered a DOM-based XSS at **██████**

**_Proof of concept:_**

**1.** Go to https://███/█████/home/troubleshoot.html?lang=en&returnUrl=https://█████/███████/home/signin.html?returnUrl=https%3A//████/██████████/home/user.html

**2.** In the username field, add the following code:
```
--><button/autofocus/onfocus=Function("confirm`1`")();//name="XSS
```

**3.** The javascript code is correctly executed 

████████

On a side note, the vulnerability work on all moderns browsers (Firefox, Chrome, Opera ...).

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website. 

Thanks for your attention and let me know if you need anything.
Regards, Yumi

## Attachments
No attachments
