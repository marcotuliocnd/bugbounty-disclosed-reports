# Clickjacking mercantile.wordpress.org

## Report Details
- **Report ID**: 264125
- **URL**: https://hackerone.com/reports/264125
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-28T19:32:45.466Z
- **Disclosed**: 2017-09-08T15:03:44.842Z

## Reporter
- **Username**: villagelad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
A Clickjaking Issue had been previously reported by  "giantfire" on Aug 9th (19 days ago) and the issue was fixed by "iandunn" on Aug 25th (3 days ago) and the same disclosed on Aug 28th. Here the affected URL is- https://mercantile.wordpress.org/

"iandunn closed the report and changed the status to Resolved.
Aug 25th (3 days ago)

The site is sending X-Frame-Options: SAMEORIGIN for front end requests now. Thanks for the report. I'll request disclosure and chat with the team to see if this qualifies for a bounty."


But the issue is still live. So here's my report. I found some others endpoints as well which can be Clickjacked easily.

Hello Team,
I am Mohammed Israil,17 found some security issue which are not very critical but can affect the system/service in future. So without delaying. I am reporting this issue hope you'll understand and implement some fix as soon as possible.

Vulnerability Type: Clickjacking (user-interface or UI redressing and IFRAME overlay) 

Affected URLs:
https://mercantile.wordpress.org/
https://mercantile.wordpress.org/#
https://mercantile.wordpress.org/product-category/accessories/
https://mercantile.wordpress.org/faq/
https://mercantile.wordpress.org/product-category/apparel/?subcat=women
https://mercantile.wordpress.org/product-category/apparel/?subcat=youth
https://mercantile.wordpress.org/product-category/apparel/?subcat=unisex


Description: Clickjacking, also known as a "UI redress attack", is when an attacker uses multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the the top level page. Thus, the attacker is "hijacking" clicks meant for their page and routing them to another page, most likely owned by another application, domain, or both. 

Reason: X-Frame-Options header is not included in the HTTP response to protect against 'ClickJacking' attacks.

Evidence: I attached a screenshot as well, Please check that.

Solution: There are two main ways to prevent clickjacking:

    Sending the proper X-Frame-Options HTTP response headers that instruct the browser to not allow framing from other domains
    Employing defensive code in the UI to ensure that the current frame is the most top level window

Most modern Web browsers support the X-Frame-Options HTTP header. Ensure it's set on all web pages returned by your site (if you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. ALLOW-FROM allows specific websites to frame the web page in supported web browsers).

Reference: http://blogs.msdn.com/b/ieinternals/archive/2010/03/30/combating-clickjacking-with-x-frame-options.aspx



Thank You




## Attachments
No attachments
