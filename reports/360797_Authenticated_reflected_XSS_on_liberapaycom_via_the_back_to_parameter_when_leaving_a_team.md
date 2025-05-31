# Authenticated reflected XSS on liberapay.com via the back_to parameter when leaving a team.

## Report Details
- **Report ID**: 360797
- **URL**: https://hackerone.com/reports/360797
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-01T13:46:52.416Z
- **Disclosed**: 2018-06-02T13:18:47.669Z

## Reporter
- **Username**: techguynoob
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
###Poc :

<https://en.liberapay.com/jio/membership/leave?back_to=http://example.com/>

Click the cancel button its redirect to 3rd party site.


Regards,
techguy

## Impact

This vulnerability could redirect users to the attackers websites for phishing attacks.

## Attachments
No attachments
