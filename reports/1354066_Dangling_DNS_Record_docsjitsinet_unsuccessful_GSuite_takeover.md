# Dangling DNS Record docs.jitsi.net (unsuccessful GSuite takeover)

## Report Details
- **Report ID**: 1354066
- **URL**: https://hackerone.com/reports/1354066
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-09-28T19:06:59.167Z
- **Disclosed**: 2023-04-03T00:36:41.823Z

## Reporter
- **Username**: bababounty99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: 8x8-bounty

## Vulnerability Information
HI Team , it is possible for a Attacker to do Sub-domain takeover - http://docs.jitsi.net/

As we can see in the Screenshot it is 404 and belongs to ghs google

As I tried claiming the domain it was possible for me to claim it by using workspace .

Hence it is possible to do Sub-domain Takeover

## Impact

An attacker can claim this subdomain by requesting a process of registering this abandoned subdomain to his name.
And attacker can fully take over this subdomain and do whatever he wants. this can cause huge damage to the website's main domain as well as to the company.
I Recommend removing  the Cname and DNS connecting to it.

You can read about this sort of attacks here : https://www.siteground.com/tutorials/googleapps/google_calendar.htm

## Attachments
- 2.png
- 1.png
- 3.png
- 4.png
- 6.png
- 5.png
