# Path traversal leading to limited CSRF on GET requests on two endpoints

## Report Details
- **Report ID**: 301862
- **URL**: https://hackerone.com/reports/301862
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-01-02T23:06:32.919Z
- **Disclosed**: 2019-04-05T17:41:34.920Z

## Reporter
- **Username**: kapytein
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi team!

I've found more endpoints which are vulnerable to the limited CSRF stated in report https://hackerone.com/reports/99708. The endpoints cause a CSRF over GET requests, however, I've been unable to exploit it.

The following endpoints are vulnerable to this:

**Proof of Concept**

1. Visit https://hackerone.com/users/confirmation?confirmation_token=z2-aaa&invitation_token=/../../test or https://hackerone.com/users/password/new?invitation_token=/../../test (the two endpoints which are still vulnerable)
1. Inspect the network traffic via developer tools or an intercepting proxy, and notice a request being made to https://hackerone.com/test.json.

We can get HackerOne to authorize Slack within a team (as attempted to do so in report 99708), however due to the state parameter it will be hard to exploit that one unless an attacker is able to get the state parameter from the victim.

## Impact

As mentioned above, it will have a big impact on HackerOne if an attacker is able to get the state parameter of the victim to, as it would lead to reports being leaked.

## Attachments
No attachments
