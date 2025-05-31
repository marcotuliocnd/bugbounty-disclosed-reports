#  Site information's Display Name section vulnerable for XSS attacks and HTML Injections.

## Report Details
- **Report ID**: 1554888
- **URL**: https://hackerone.com/reports/1554888
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-04-29T19:56:51.683Z
- **Disclosed**: 2022-05-16T13:59:43.887Z

## Reporter
- **Username**: sawrav-chowdhury
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:

Hi, 

Greetings. I have found that site information's Display Name section on the try.pressable.com is vulnerable for potential  XSS attacks and HTML Injections.

## Steps To Reproduce:
1. Visit https://try.pressable.com
2. Create a new site.
3. On the  Display Name section, put the XSS / HTML Injection payloads.
4. XSS will be triggered/ Injected HTML will be reflected.

XSS Payload:  "><img src=x onerror=javascript:alert(document.cookie)>

HTML Payload: 
<form action="/action_page.php">
<label for="fname">First name:</label>
<input type="text" id="fname" name="fname"><br><br>
<label for="lname">Last name:</label>
<input type="text" id="lname" name="lname"><br><br>
<input type="submit" value="Submit">
</form>

## Supporting Material/References:
POC Video attached

## Impact

Due to these vulnerabilities, attacker can easily divert victims to their malicious site and able to get credentials of victims.

## Attachments
- POC-_VIDEO.mp4
