# Cross site scripting - XSRF Token

## Report Details
- **Report ID**: 858255
- **URL**: https://hackerone.com/reports/858255
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-24T06:13:55.678Z
- **Disclosed**: 2020-06-14T10:40:47.524Z

## Reporter
- **Username**: a9hora
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Please follow below mentioned steps for reproducing the vulnerability.
1. Open URL: https://nextcloud.com/enterprise/buy/
2. Fill up valid name and email address and put payload in other fields.
    
    Payload/s:
			<img src="x" onload=alert(document.cookie);>
			<svg/onload=alert(document.cookie);>	
3. Submit it
4. Open email address you mentioned in the email field.
5. Open up the email source.
6. You will be prompted with xsrf-token.

## Impact

As an attacker is getting the xsrf-token, he can utilize it in later attack such as, CSRF.

## Attachments
- XSS-XSRF_Token_PoC.mp4
