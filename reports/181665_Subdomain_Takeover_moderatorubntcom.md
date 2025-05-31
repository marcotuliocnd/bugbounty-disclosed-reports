# Subdomain Takeover (moderator.ubnt.com)

## Report Details
- **Report ID**: 181665
- **URL**: https://hackerone.com/reports/181665
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-11T22:43:02.878Z
- **Disclosed**: 2017-02-06T08:31:51.441Z

## Reporter
- **Username**: madrobot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Hello __Team__

This report is same as #179110

One of your subdomain http://moderator.ubnt.com is pointing towards
```
216.58.203.243    moderator.ubnt.com
216.58.203.243    ghs.google.com
216.58.203.243    ghs.l.google.com
```
{F134183}
And it is unclaimed

When I open it 
it is showing 

{F134184}

__Impact__ :-
An attacker can claim this subdomain by requesting a process of registering this abandoned subdomain to his name.

And attacker can fully take over this subdomain and do whatever he wants. this can cause huge damage to the website's main domain as well as to the company.

I Recommend removing  the Cname and DNS connecting to it.

You can read about this sort of attacks here : https://www.siteground.com/tutorials/googleapps/google_calendar.htm

To clarify your doughs I just added video POC

>1ST Video Is about how I am able to claim it https://youtu.be/51Ku4cGbijE
>2ND Video is proof when trying to claim it for the second time https://youtu.be/GJcWsHJj8aE

## Attachments
- ubnt_sb1.png
- ubnt_sb2.png
