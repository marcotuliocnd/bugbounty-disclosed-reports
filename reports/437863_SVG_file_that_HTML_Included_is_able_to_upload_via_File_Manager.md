# SVG file that HTML Included is able to upload via File Manager

## Report Details
- **Report ID**: 437863
- **URL**: https://hackerone.com/reports/437863
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-09T08:44:33.319Z
- **Disclosed**: 2019-04-20T05:49:28.258Z

## Reporter
- **Username**: hexife
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Concrete5 has the whitelist for restricting that malicious file is uploaded.
( concrete/config/concrete.php, Line no. 86~88 )

The extension whitelist allows to upload SVG file.

However, SVG can has the HTML elements in its code.
(Ref. https://www.w3.org/TR/SVG2/intro.html#W3CCompatibility )

If web browser accesses the SVG file that has the 'script' tag of HTML element  directly,
browser executes the JavaScript placed in SVG file.

Example SVG file likes below.
```
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 105">
<html><head><title>test</title></head><body><script>alert('xss');</script></body></html>
</svg>
```
It can be occur the XSS vulnerability.


* Test Scenario

1. Make the SVG
{F373015}

2. Login as administrator and select the File Manager feature.

3. Upload the file we made.
{F373008}

4. We can check the upload path in "Right click -> Properties"
{F373009}

5. For the test to triggering SVG file, we edit portfolio section.
Move to "portfolio > project Title #" and Edit / Add slides like this.
{F373010}

6. We can confirmed the execution of JavaScript in the SVG file.
{F373011}

Thank you for reading my report.

PS.
When I was the kid, My father gave me the crayon as the Christmas gift.

## Impact

Concrete5 prohibited  the upload the HTML files, but this method is bypass the file upload filtering.
Attacker who got the administrator authority can inject and hide malicious html tags to target service.

## Attachments
- 01-uploaded.png
- 02-confirmed.png
- 03-test.png
- 04-success.png
- 00-testfile.png
