# [intensedebate.com] XSS Reflected POST-Based on update/tumblr2/{$id}

## Report Details
- **Report ID**: 1040639
- **URL**: https://hackerone.com/reports/1040639
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-22T16:36:53.567Z
- **Disclosed**: 2021-01-23T10:13:32.887Z

## Reporter
- **Username**: fuzzme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
##Summary:
Hello, I have found an XSS Reflected POST-Based on `https://www.intensedebate.com/update/tumblr2/{$id}`.
The parameter $_POST['txtCode'] is reflected and is not sanitized.

To trigger the XSS an attacker need to create a site and invite the victim in their own site and give then full permissions, because the victim needs the `reinstall` functionality to trigger the XSS and the attacker need to know the id of `/update/tumblr2/{$id}`.

Vulnerable(s) URL:

```
POST /update/tumblr2/{$id}
```

Vulnerable(s) Parameter(s):

```
$_POST['txtCode'];
```

Payload :
```
</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=prompt(document.cookie)//>\x3e
```

##Steps to reproduce

You need two account

1. Login at ```intensedebate.com```
2. Create your own site at ```intensedebate.com/install```, and follow the instructions (use generic install)
3. Invite the victim account on your own site, and give then the full permissions
4. Setup the XSS POC, download the xss.html and open it with a text editor and change the `{id}` by own site id
5. Login in the second account, and open the xss.html 
6. And you will see the XSS pop-up

You can also follow me into the video POC.

Thank you, good bye.

## Impact

A attacker can perform a phishing attack or perform a CORS attack

## Attachments
- xss.html
- xss_.mp4
