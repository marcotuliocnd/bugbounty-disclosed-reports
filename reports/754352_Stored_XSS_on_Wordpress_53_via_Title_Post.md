# Stored XSS on Wordpress 5.3 via Title Post

## Report Details
- **Report ID**: 754352
- **URL**: https://hackerone.com/reports/754352
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-09T13:22:18.762Z
- **Disclosed**: 2019-12-10T09:58:14.881Z

## Reporter
- **Username**: muhammaddaffa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
I have identified a WordPress security vulnerability , a Stored XSS vulnerability that affects latest version of WordPress (5.3)

POC:
1) Login to wordpress website
2) Make a post with title payload xss like example <script>alert(document.domain);</script>
3) Publish then open the post, XSS Will trigger

## Impact

Can stealing cookie user

## Attachments
- wp1.png
- daffa.info.png
