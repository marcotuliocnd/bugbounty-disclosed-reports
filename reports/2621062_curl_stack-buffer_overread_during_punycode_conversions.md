# curl: stack-buffer overread during punycode conversions

## Report Details
- **Report ID**: 2621062
- **URL**: https://hackerone.com/reports/2621062
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-07-24T07:19:07.269Z
- **Disclosed**: 2024-09-22T20:31:25.013Z

## Reporter
- **Username**: z2_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hello, I would like to report a vulnerability here, initially reported by me to the curl project.

HackerOne report: https://hackerone.com/reports/2604391
CVE: CVE-2024-6874
Advisory:  https://curl.se/docs/CVE-2024-6874.html
Severity: Low

## Impact

When converting the domain name of a URL from/to punycode with libcurl's URL API, libcurl reads past the bounds of a stack-buffer and includes
adjacent stack-memory in the conversion result. This potentially leaks pointer values.

## Attachments
No attachments
