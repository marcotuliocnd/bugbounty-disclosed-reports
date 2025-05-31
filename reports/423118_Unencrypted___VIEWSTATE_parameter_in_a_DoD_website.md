# Unencrypted __VIEWSTATE parameter in a DoD website

## Report Details
- **Report ID**: 423118
- **URL**: https://hackerone.com/reports/423118
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-12T21:03:39.953Z
- **Disclosed**: 2020-05-14T17:43:23.942Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi there i realise that the information passing to the server in the subdomain http://████████ can be seen without any encryption thought the __VIEWSTATE Parameter.

To reduce the change of someone interception the information the parameter should be encrypted due to the sensivity of the information passing thought there.

POC:
Well this quiet easy to explore it.
Go to the following website with burp turned on:
url: https://█████/

Intercept the traffic and check the response from the __VIEWSTATE parameter
and you will see the information passing in cleartext 

viewstate.jpg

Recommendations.
The __VIEWSTATE variable cipher is recommended in the application settings
(web.config).

References:
http://msdn.microsoft.com/en-us/library/ms178199(v=vs.85).aspx
https://www.acunetix.com/vulnerabilities/web/unencrypted-__viewstate-parameter

Best Regards Miguel Santareno

## Impact

It depends on the information passing around but for what can i see this is still a medium stuff

## Attachments
No attachments
