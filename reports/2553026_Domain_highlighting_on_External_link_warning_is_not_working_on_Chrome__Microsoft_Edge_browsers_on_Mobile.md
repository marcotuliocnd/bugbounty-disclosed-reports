# Domain highlighting on External link warning is not working on Chrome & Microsoft Edge browsers on Mobile

## Report Details
- **Report ID**: 2553026
- **URL**: https://hackerone.com/reports/2553026
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-17T14:59:39.249Z
- **Disclosed**: 2025-03-13T17:34:16.704Z

## Reporter
- **Username**: sarthakbhingare015
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
There have been multiple issues with External Link Warning in the past. Sometimes it's Homograph, sometimes more than 2 slashes in link, sometimes domain highlighting and/or weird markdown. And these all have been fixed.

Recently, I've noticed a strange issue with Chrome and Edge browsers on mobile. The highlighting of domains doesn't work at all on External Link Warning interstitial page. None of the links are highlighted. Similar issues were fixed in the past by HackerOne (you can see the bug references below). It seems like these problems have appeared again in the code.

### Steps To Reproduce

1. Log into your account on your mobile from either Latest version of Microsoft Edge browser or Google Chrome.
1. Click on links mentioned below in **Impact** section.
1. Observe that none External link warning interstitial page highlights domain.

## Test cases: Google Chrome, Microsoft Edge & Firefox👇

- Below are the images from Chrome browser along with Chrome's details:
{F3363744} {F3363747} {F3363766}

- Below are the images from Microsoft Edge browser along with Edge's details:
{F3362316} {F3362317} {F3363753}

- Below are the images from Firefox Browser along with Firefox's details:
{F3362321} {F3362323} {F3363752}

## Impact

- https://google.com@1234567890/download/safest_file: Browsers automatically convert decimal to IP address. Upon clicking the link from mobile on Edge or Chrome browser, nothing is highlighted in External link warning interstitial page, as a result user may be fooled thinking that it is redirected to **google.com** but in reality it will be redirected to a attacker's controlled server.
- www.hackerone.com%2Fbugs%3Fsubject=user&report_id=81070&view=all&substates%5B%5D=new&substates%5B%5D=triaged&substates%5B%5D=needs-more-info&substates%5B%5D=resolved&substates%5B%5D=not-applicable&substates%5B%5D=informative&substates%5B%5D=duplicate&substates%5B%5D=spam&text_query=@evil.com/&sort_type=latest_activity&sort_direction=descending&limit=25&page=1: This is a clever URL to trick user thinking that it is being redirected to a valid website. But in reality it is being redirected to **evil.com**.

The domain highlighting functionality is meant to let users know where is the browser redirecting upon proceeding. But in Edge & Chrome browser on Mobile, this functionality is not working as intended. As a result a malicious actors would take advantage of this to fool users into redirecting to malicious sites.

## Reference bugs fixed in past by HackerOne
#113070 - Multiple issues with Markdown and URL parsing
#59469 - Fake URL + Additional vectors for homograph attack
#271324 - Homograph fix Bypass 

## Attachments
- Screenshot_2024-06-17-09-08-05-26_df198e732186825c8df26e3c5a10d7cd.jpg
- Screenshot_2024-06-17-09-08-00-08_df198e732186825c8df26e3c5a10d7cd.jpg
- Screenshot_2024-06-17-08-59-19-08_3aea4af51f236e4932235fdada7d1643.jpg
- Screenshot_2024-06-17-09-08-35-85_3aea4af51f236e4932235fdada7d1643.jpg
- Screenshot_2024-06-17-19-22-35-73_40deb401b9ffe8e1df2f1cc5ba480b12.jpg
- Screenshot_2024-06-17-19-24-25-06_40deb401b9ffe8e1df2f1cc5ba480b12.jpg
- Screenshot_2024-06-17-19-25-43-65_3aea4af51f236e4932235fdada7d1643.jpg
- Screenshot_2024-06-17-19-26-06-12_df198e732186825c8df26e3c5a10d7cd.jpg
- Screenshot_2024-06-14-20-46-17-32_40deb401b9ffe8e1df2f1cc5ba480b12.jpg
