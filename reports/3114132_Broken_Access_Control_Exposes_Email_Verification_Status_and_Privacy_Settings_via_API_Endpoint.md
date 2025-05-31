# Broken Access Control Exposes Email Verification Status and Privacy Settings via API Endpoint

## Report Details
- **Report ID**: 3114132
- **URL**: https://hackerone.com/reports/3114132
- **State**: Closed
- **Severity**: low
- **Submitted**: 2025-04-26T22:54:16.984Z
- **Disclosed**: 2025-04-29T12:45:03.155Z

## Reporter
- **Username**: ctrl_cipher
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
The /api/v1/users/{username} endpoint leaks sensitive email-related metadata (e.g., is_email_confirmed, is_email_public) without proper authorization checks. Attackers can abuse this to:
Identify verified/active accounts for targeted attacks.
Determine users’ email privacy preferences (even if the email itself is hidden).
This behavior allows me to distinguish whether an account's email address is confirmed or not.

#Steps to Reproduce
1. Authenticate as a valid user (e.g. user/current).
2. Intercept a request to your own profile:
>GET /api/v1/users/attacker_user HTTP/2  
Host: wakatime.com  
Cookie: 
3. Modify the username in the URL to access another user’s data:
>GET /api/v1/users/<any name> HTTP/2  
Host: wakatime.com  
Cookie: 
4. Observe the response:
>{
  "is_email_confirmed": true,
  "is_email_public": false,
  "public_email": null,
  // ... other sensitive fields
}

## Impact

Account Enumeration:
Attackers can confirm valid/verified accounts (is_email_confirmed: true), enabling targeted credential stuffing or phishing.

Privacy Violations:
Knowing a user’s email privacy preference (is_email_public: false) leaks their intent to keep their email private.

Attack Surface Expansion:
Combined with other vulnerabilities (e.g., password reset flaws), attackers can prioritize high-value accounts.

## Attachments
- poc1.jpg
- poc2.jpg
