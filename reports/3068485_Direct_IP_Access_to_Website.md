# Direct IP Access to Website

## Report Details
- **Report ID**: 3068485
- **URL**: https://hackerone.com/reports/3068485
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-03-31T15:47:12.220Z
- **Disclosed**: 2025-04-11T08:54:33.545Z

## Reporter
- **Username**: ryomenshuvro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lichess

## Vulnerability Information
## Summary:
The website is accessible directly via its IP address (37.187.205.99), which may bypass domain-based security policies and expose potential misconfigurations.

## Steps To Reproduce:
1. Open a web browser and enter the IP address:
http://37.187.205.99
2. Observe that it loads the main website instead of rejecting the request or redirecting it to the proper domain.

##Expected Result:
The server should block direct IP access or redirect it to the proper domain.

##Actual Result:
The website is fully accessible via its IP address.

## Impact

1. Domain-based security policies (CSP, HSTS, cookies, etc.) might not be enforced, leading to potential security bypasses.

2. Possible certificate mismatch issues if HTTPS is used, making it easier for phishing attacks.

3. Firewall/hosting misconfigurations could expose internal infrastructure.

## Attachments
No attachments
