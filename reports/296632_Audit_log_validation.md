# Audit log validation

## Report Details
- **Report ID**: 296632
- **URL**: https://hackerone.com/reports/296632
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-12-10T04:08:59.173Z
- **Disclosed**: 2018-08-28T08:07:11.549Z

## Reporter
- **Username**: mur90210
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
## Issue ##
For the docker image (git clone https://github.com/WeblateOrg/docker.git weblate-docker), the IP address in the audit log (in the user's profile, and in the administration console) can be forged using the `X-Forwarded-For` header during the login process.

This does not affect http://demo.weblate.org/.

For http://demo.weblate.org/, `User-Agent: '"<b>test` was accepted. This will not lead to XSS issues, but could potentially be an issue if the input is used elsewhere, such as a database query.

## Impact

## Consequence ##
When using the docker image, it may be possible to spoof audit log entries. If an account were compromised, it may be more difficult to determine this from the audit log entries.

## Attachments
No attachments
