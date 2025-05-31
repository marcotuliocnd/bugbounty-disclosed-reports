# HTML Injection on "polls" app - comments section (possibly XSS)

## Report Details
- **Report ID**: 1108420
- **URL**: https://hackerone.com/reports/1108420
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-02-21T20:27:44.707Z
- **Disclosed**: 2021-03-31T10:27:10.651Z

## Reporter
- **Username**: supr4s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi everyone,

On latest version of Polls app (1.7.5), I noticed a lack of user input filtering for the "Description" part of the survey. An HTML injection is therefore possible. I tried to inject JavaScript code to get an XSS but I didn't succeed. Certainly someone better than me will be able to do it.

## Phishing

Knowing that you can inject HTML, you can do cool stuff like phishing with the following code : 

```
<br/> <br/><br/><br/><br/><br/><marquee><p style="color:red;"><b>!!!!! IMPORTANT message from Nextcloud administrator !!!!!!</b></p></marquee><br/><br/> A security issue was found last night.<br/> <p style="color:green;">Please go to manually on <a><b>changing-password.cloud.evil.com</a></b> to reset your password.</p> <b><p style="color:red;">Thank you in advance for doing so as soon as possible. </p></b><br/><br/><i>The IT team.</i></b><br/><br/> <br/><br/><br/> <b><marquee><p style="color:red;">!!!!! IMPORTANT message from Nextcloud administrator !!!!!!</b></p></marquee><br/><br/><br/><br/> <br/><br/>
```

And the website changing-password.cloud.evil.com would first ask for entering the user's current password, before he enters his new password => password retrieved from the attacker's server

**Proof-of-concept :** https://███/apps/polls/s/cxXkCK9LRXIKu5Oq



## DoS (client side)

You can also make the user's PC spit by loading an infinite number of iframes. 

**Proof-of-concept (Warning, may crash your PC) :** https://███████/apps/polls/s/WKGKWHEFSSvPsHyC

## Impact

- Attract the user to redirect him to a malicious page and steal his personal identifiers
- Client-side DoS
- And many other things are possible by injecting HTML code at will and without filtering

In my opinion, I don't think it's a good thing to let the user add HTML code as he wants without being worried!

Regards,
Supras

## Attachments
- HTMLi_1.png
