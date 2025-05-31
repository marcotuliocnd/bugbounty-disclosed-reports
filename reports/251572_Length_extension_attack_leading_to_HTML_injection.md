# Length extension attack leading to HTML injection

## Report Details
- **Report ID**: 251572
- **URL**: https://hackerone.com/reports/251572
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-20T10:22:27.318Z
- **Disclosed**: 2017-09-01T14:02:50.489Z

## Reporter
- **Username**: b1t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
At the profile setting page where I can set my personal website I found this url:
*https://www.zomato.com/redirect?u=xxx&t=yyy*
Where `xxx` is the `url` that we can control and `yyy` is the `hash`. Through out blackbox testing I find out that if md5(`somescret` + `url`) == t then the redirect is allowed. This is vulnable to <https://blog.skullsecurity.org/2012/everything-you-need-to-know-about-hash-length-extension-attacks>. With this vulnerability I can append what ever I want into the `url` in `u` variable.  <https://www.zomato.com/redirect?u=http%3A//a.c%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%E8%00%00%00%00%00%00%00%3Cstyle%3Ebody%7Bbackground-color%3A%20black%3B%7D%3C/style%3E%3Cmarquee%20bgcolor%3D%23000000%3E%3Cfont%20color%3D%2300FF00%3Eb1t%20%3D%2C%3D%3C/font%3E%3C/marquee%3E&t=cb3efc9cbeb3d7b84dfc5cb2bef5a3c4>. As a result I can inject arbitrary HTML content into your page because of the `Redirecting you to...` message and there is no escaping on this page. At first I was aiming at an `XSS` but your `WAF` blocks all my attemps, a more skilled attacker may be able to bypass it. Because the nullbyte in `url` breaks your `Refresh` header the page won't redirect anymore and display my injected content. Visit the `poc` above and look at the request and response you will have a clearer view of what happened. A correct fix for this would be using a `correct ``HMAC` implementation not just simple `md5(secret+message)`. There is an attachment script below which I used to exploit the vulnerability. You have get <https://github.com/iagox86/hash_extender> to be able to use the script.

## Attachments
- exploit.py
