# Window.opener fix bypass

## Report Details
- **Report ID**: 317243
- **URL**: https://hackerone.com/reports/317243
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-02-17T23:18:23.078Z
- **Disclosed**: 2018-02-18T04:52:08.972Z

## Reporter
- **Username**: mishre
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
## Description 
Due to a recent report(https://hackerone.com/reports/306414) a fix was deployed in order to resolve the tabnabbing issue. However by using a line break the fix can be bypassed.

## Steps to reproduce
1) Browse to your Phabricator instance and create a new document.
2) Now paste in the following content 
```
[[ //google.com | aaa ]] 
```
and see that there is indeed a rel="noreferer" tag added by clicking preview and then viewing the DOM tree.
3) Now replace the document with the following content:
```
[[ /
/google.com | aaa ]] 
```
and see that no tag is added.

## Impact

An attacker can abuse this functionality to perform phishing attacks against users

## Attachments
No attachments
