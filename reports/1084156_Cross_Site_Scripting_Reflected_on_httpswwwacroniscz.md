# Cross Site Scripting (Reflected) on https://www.acronis.cz/

## Report Details
- **Report ID**: 1084156
- **URL**: https://hackerone.com/reports/1084156
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-22T07:48:16.769Z
- **Disclosed**: 2021-11-17T10:00:49.225Z

## Reporter
- **Username**: darkdream
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Summary
You can post javascript and html code in form fields

steps :
1-go to vulnerability link : https://www.acronis.cz/poptavka-acronis/
2- enter this javascript code "><script>alert(1);</script> in form field for xss and enter <a+href="https://bing.com">Test</a> for html injection.

## Impact

Impact
1- Cookie stealing
2- Pishing attacks
3- URL redirection

## Attachments
No attachments
