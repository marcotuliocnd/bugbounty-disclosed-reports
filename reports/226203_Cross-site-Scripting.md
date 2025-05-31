# Cross-site-Scripting

## Report Details
- **Report ID**: 226203
- **URL**: https://hackerone.com/reports/226203
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-04T21:39:30.322Z
- **Disclosed**: 2017-05-05T20:50:29.077Z

## Reporter
- **Username**: test_this
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
step:
1: goto https://bridge.cspr.ng/my/account of your account
2. in "Custom Profile field option" check the box and enter xss payload in "display name" field
       payload: "p<script>alert('xss')</script>"
3. update the information 
4. open the account in INTERNET EXPLORER 11 and xss will executed

note: here server is not sanitize the user input properly,
         payload will not work in firefox,chrome browser due to "content-security-policy"
         But internet explorer does not Support "Content-Security-Policy"  so xss will execut

this is stored xss and the display name will visible to everywhere, so its possible to account takeover of ther user

## Attachments
- payload.png
- source_code.png
- xss3.png
