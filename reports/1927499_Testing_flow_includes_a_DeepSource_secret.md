# Testing flow includes a DeepSource secret

## Report Details
- **Report ID**: 1927499
- **URL**: https://hackerone.com/reports/1927499
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-03-31T14:07:19.824Z
- **Disclosed**: 2023-04-11T10:40:02.683Z

## Reporter
- **Username**: triplesided
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
The testing workflow (https://github.com/WeblateOrg/wlc/blob/main/.github/workflows/test.yml) has a DeepSource secret included which would allow a malicious actor to use the DeepSource cli and access parts of the repo (https://deepsource.io/docs/cli/usage).

Recommended usage would be to create a GitHub action environment secret and call this at runtime.
https://deepsource.io/docs/analyzer/test-coverage#with-github-actions

## Impact

Access to the DeepSource environment is gained through the token with the malicious actor able to report artifacts to DeepSource.

## Attachments
No attachments
