# Javascript Payload reflected Back in Report Embed Code

## Report Details
- **Report ID**: 284082
- **URL**: https://hackerone.com/reports/284082
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-30T07:13:24.858Z
- **Disclosed**: 2017-12-12T14:53:09.069Z

## Reporter
- **Username**: zubair
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
1)Create new Report template 
2)Spoof its name with payload "></div> My Report <script type="text/javascript">alert(document.cookie);</script><div id="
3)Visit Back to your library list https://infogram.com/app/#/library
4)Select The Created report and click view on web,Click the Share Button
5)Copy & embed the code somewhere in html file you ll triage the Javascript exceution


The Payload is reflected in embed code and can compromise the embed code user's PRivacy.

Fix:Report/Project name need to be escaped properly

For reproduction of issue use:
https://infogram.com/greaterreport-classic-lessdivgreaterlessscriptgreateralerttestlessscriptgreater-1g0gmjzqk1y3p1q


## Attachments
- 1.PNG
- 2.PNG
- 3.PNG
- 4.PNG
