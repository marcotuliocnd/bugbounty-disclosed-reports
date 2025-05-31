# █████ - DOM-based XSS

## Report Details
- **Report ID**: 377264
- **URL**: https://hackerone.com/reports/377264
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-04T21:32:33.041Z
- **Disclosed**: 2019-12-02T19:09:19.671Z

## Reporter
- **Username**: yumi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings, 

I've discovered a DOM-based XSS at **███**

**_Proof of concept:_**

**1.** Go to https://████/█████████/home/troubleshoot.html?lang=en
**2.** In the username field, add the following code:

```
--><button/autofocus/onfocus=Function("confirm`1`")();//name="XSS
```

**3.** The javascript code is correctly executed:

██████

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

Thanks for your attention and let me know if you need anything.
Regards, Yumi

## Attachments
No attachments
