# URI Obfuscation

## Report Details
- **Report ID**: 175529
- **URL**: https://hackerone.com/reports/175529
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-13T06:00:01.767Z
- **Disclosed**: 2016-10-15T02:40:09.971Z

## Reporter
- **Username**: ajdumanhug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Typically, when obfuscating a URL, you must trick someone into viewing a website they did not want to view by tempting them with something they are familiar with.

## Products affected: 

Latest Version of Brave in Windows

## Steps To Reproduce:
We can trick someone into viewing it like this:
http://example.com@sample.com
This will make the user think they are going to go to example.com, when really they are going to sample.com.

Live POC:
https://brave.com@secuna.ph/

They thought they will be redirect to brave.com but the page displays secuna.ph

I attached a picture and make sure to focus your eyes in the URL Address.

## Supporting Material/References:

{F127608}


## Attachments
- proof.png
