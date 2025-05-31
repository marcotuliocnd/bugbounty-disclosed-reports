# Option method enabled in kartpay Webservers

## Report Details
- **Report ID**: 642862
- **URL**: https://hackerone.com/reports/642862
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-14T09:57:43.962Z
- **Disclosed**: 2019-08-28T15:31:29.878Z

## Reporter
- **Username**: lollol1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kartpay

## Vulnerability Information
HTTP OPTIONS method is enabled on this web server. The OPTIONS method provides a list of the methods that are supported by the web server, it represents a request for information about the communication options available on the request/response chain identified by the Request-URI.

Domain :
merchant.kartpay.com

## Impact

The issue was not critical, as the impact of using other methods than GET and POST in this domain is nearly nonexistent. The bounty reflects the criticality of the issue.

## Attachments
- options_method.png
