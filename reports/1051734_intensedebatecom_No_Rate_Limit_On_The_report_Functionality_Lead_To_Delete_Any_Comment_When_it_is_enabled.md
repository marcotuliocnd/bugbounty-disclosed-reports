# [intensedebate.com] No Rate Limit On The report Functionality Lead To Delete Any Comment When it is enabled

## Report Details
- **Report ID**: 1051734
- **URL**: https://hackerone.com/reports/1051734
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-06T17:51:04.809Z
- **Disclosed**: 2021-01-23T10:13:16.191Z

## Reporter
- **Username**: fuzzme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello

## Summary:

I have found a no rate limit issue on the report functionality.
When you enabled the report functionality on your site, you can set a number of reports before deleting the comment reported.
By default, this functionality is unable, but if you enabled this and you set a $x number of reports before deleting the comment, an attacker can spamming this functionality and delete your comment.


## Steps To Reproduce:

1)  Login at `https://intensedebate.com`
2) Create your own site at `https://intensedebate.com/install`, and follow the instructions (use generic install)
3) After setup your site, go to `https://www.intensedebate.com/user-dashboard`, on click to `Moderate`.

 {F1106120}

4) Go to the comment setting by clicking to `Comments`

{F1106122}

5) Setup the Report functionality by checked the `Enable "Report this comment" button` and set a number of reports before deleting the comment to `10` and save it

{F1106130}

6) Go to your site and add a comment
7) With a other account go to your site, and report the comment manually x10 
8) After spam the Report functionality
9) Refresh the page, and you will see the comment is deleted


## POC 

The video POC `NoRateLimit.mp4`

Thank you,

Fuzzme.

## Impact

Delete any comment in any site when the report functionality is enabled

## Attachments
- step.png
- step1.png
- step2.png
- NoRateLimit.mp4
