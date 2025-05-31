# RTL override char allowed at khanacademy redirect page

## Report Details
- **Report ID**: 641640
- **URL**: https://hackerone.com/reports/641640
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-12T16:29:52.550Z
- **Disclosed**: 2019-08-02T21:57:22.805Z

## Reporter
- **Username**: d3f4u17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
##Summary

Attacker can embed `RTLO` character at the following URL https://www.khanacademy.org/computer-programming/link_redirector?url= to trick the user to download suspicious files.

##Steps to reproduce
 
* Visit https://www.khanacademy.org/computer-programming/link_redirector?url=
* add the following payload to the url parameter `https://example.com/so%E2%80%AEgnp.exe`
[https://www.khanacademy.org/computer-programming/link_redirector?url=https://example.com/so%E2%80%AEgnp.exe](https://www.khanacademy.org/computer-programming/link_redirector?url=https://example.com/so%E2%80%AEgnp.exe)
* After visiting the URL you will see the following link appearing on the page, which appears to be a link to a png file.
{F527747}
* Click on the link and you will be redirected to an executable file.
{F527750}

##Additional Payloads

Attacker can even spoof the domain name by adding the following value to the `url` parameter 
`https://google.com@%E2%80%AE@moc.rettiwt`
{F527754}
When the user will click on the link the user will be redirected to `https://moc.rettiwt/` which is a completely different host.

I have also tested some other malformed URLs which can fool user to redirect to other hosts
```
https://google.com@"twitter.com
https://google.com@'twitter.com
https://google.com@/twitter.com
https://google.com@'#twitter.com (Different domain)
```

##Mitigation

Filter out all the unnecessary special symbols from the URL along with the RTLO char.

##References
 #299403
 #298
[RIGHT TO LEFT OVERRIDE](https://codepoints.net/U+202E)

## Impact

* This can be used to spoof URLs on khanacademy. 
* can be used to fool users to download malicious files.

## Attachments
- rtlo.png
- rtlo2.png
- rtlo3.png
