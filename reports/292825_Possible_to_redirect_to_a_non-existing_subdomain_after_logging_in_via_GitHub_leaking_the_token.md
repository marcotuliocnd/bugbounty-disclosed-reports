# Possible to redirect to a (non-existing) subdomain after logging in via GitHub (leaking the token)

## Report Details
- **Report ID**: 292825
- **URL**: https://hackerone.com/reports/292825
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-11-24T19:06:06.369Z
- **Disclosed**: 2017-11-25T16:11:16.855Z

## Reporter
- **Username**: jackds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
# Summary
To comment on an article a user has the option to login using his Github account. After logging in the user is normally redirect back to the URL he came from. I found out that it is also possible to redirect to a non-existing subdomain of edoverflow.com. It looks like the whitelist for the OAuth flow is not configured properly.

# Vulnerability Details
For logging in using the OAuth login flow the following URL is used: https://github.com/login/oauth/authorize?client_id=5f45cc999f7812d0b6d2&redirect_uri={url}&scope=public_repo . The redirect_uri parameter is matched against the configured URLs in the OAuth Application settings. I'm not sure how this is configured for this app, but it seems possible to redirect to a subdomain as well.

# Steps To Reproduce:

  1. Go to https://github.com/login/oauth/authorize?client_id=5f45cc999f7812d0b6d2&redirect_uri=https%3A%2F%2Fnonexisting.edoverflow.com&scope=public_repo
  2. Login using your Github account
  3. You are now redirected to nonexisting.edoverflow.com?code={code}

# Impact
Impact is limited as it is still only possible to redirect to a subdomain. In order to carry out an attack the attackers needs to find a vulnerable subdomain first. 

# Supporting Material/References
-

## Impact

If the target URL is vulnerable in any way the attacker might be able to actually steal a login-token.

## Attachments
No attachments
