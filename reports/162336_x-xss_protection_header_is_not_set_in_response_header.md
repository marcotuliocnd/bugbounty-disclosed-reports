# x-xss protection header is not set in response header

## Report Details
- **Report ID**: 162336
- **URL**: https://hackerone.com/reports/162336
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-23T08:05:55.552Z
- **Disclosed**: 2017-07-10T10:01:10.078Z

## Reporter
- **Username**: karthic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
URL : http://inside.gratipay.com/

Description : 
This header enables the Cross-site scripting (XSS) filter built into most recent web browsers. It's usually enabled by default anyway, so the role of this header is to re-enable the filter for this particular website if it was disabled by the user. This header is supported in IE 8+, and in Chrome (not sure which versions). The anti-XSS filter was added in Chrome 4. Its unknown if that version honored this header.

Solution : Need to set X-XSS-Protection: 1; mode=block in response header

## Attachments
- xss_header_is_not_present_in_response_header.png
