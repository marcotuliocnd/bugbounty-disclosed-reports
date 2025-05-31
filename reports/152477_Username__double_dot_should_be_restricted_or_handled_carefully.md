# Username .. (double dot) should be restricted or handled carefully

## Report Details
- **Report ID**: 152477
- **URL**: https://hackerone.com/reports/152477
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-07-20T10:23:48.235Z
- **Disclosed**: 2016-07-20T13:46:30.099Z

## Reporter
- **Username**: sh4dow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
If I change my username to "**test**" then as in normal case it will send a GET request to **/test/settings** but if I change my username to "**..**" (**double dot** within inverted commas)  then it will send GET request to /settings because /../settings will change to /settings and hence final GET request will be to /settings which will show a 404 page.
 I have attached a video as POC.

Regards!

## Attachments
- gratify.mp4
