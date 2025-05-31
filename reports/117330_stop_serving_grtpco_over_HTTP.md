# stop serving grtp.co over HTTP

## Report Details
- **Report ID**: 117330
- **URL**: https://hackerone.com/reports/117330
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-02-19T12:46:04.185Z
- **Disclosed**: 2016-07-15T05:15:09.545Z

## Reporter
- **Username**: secbughunter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Target Domain: grtp.co

1 Issue Details: Service available on HTTP
As per the policy details under scope on HackerOne portal(https://hackerone.com/gratipay), the 'grtp.co'. should be available only on port 443 or HTTPS protocol. However grtp.co service is running on port 80 too (i.e., running on HTTP protocol even). As we know this can leak lot of information about your target customers.

Side effects:
URL1) https://github.com/gratipay/grtp.co/blob/master/README.md#examples

From the above URL1 page details: you are referring to URLs of grtp.co which targets to HTTP based URLs instead of HTTPS.
Example code taken from URL 1 mentioned above:
<script data-gratipay-username="rummik"
  data-gratipay-widget="button"
  src="//grtp.co/v1.js" async></script>


Solution: If we have HTTPS already, what ever the services we host on out web sites should points towards HTTPS URIs/URLs, but not to HTTP based URIs/URLs. This way we can achieve 100% encrypted communication & guaranty end user's safety. If not an attacker can learn that a about of user's activity happening on HTTP and can setup a fake DNS record to drive "grtp.co/v1.js" or "grtp.co/xxxx" kind of requests to malicious domain and can serve infected java script files making them fall as his/her pray.

2 Issue Details: Information Disclosure

Leaking lot of technical details during discussions with H1 researchers
Example: https://hackerone.com/reports/116352

The above issue # 1 was identified while reading the report. That is why I am submitting both issues under one report.

Solution: Keep the details as crispy as possible while sharing with H1 researchers. Social Engineering is another possibility where a malicious researcher can make you leak more info.


## Attachments
No attachments
