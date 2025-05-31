# Reflected Xss

## Report Details
- **Report ID**: 758854
- **URL**: https://hackerone.com/reports/758854
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-15T11:55:35.616Z
- **Disclosed**: 2020-09-21T14:52:09.328Z

## Reporter
- **Username**: 0xelkomy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
>>hello security team i found reflected XSS in this subdomain https://███

POC:-
1-go in subdomain
2-go here 
https://███████/en/embeddedAuthRedirect.html?auth=javascript:alert("xElkomy")
3-Done

Image:-
███████
#xElkomy

## Impact

reflected cross-site scripting (XSS) operation with JavaScript, which runs in the client context. i can put malicious code in URL

## Attachments
No attachments
