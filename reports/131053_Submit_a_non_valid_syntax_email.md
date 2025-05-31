# Submit a non valid syntax email

## Report Details
- **Report ID**: 131053
- **URL**: https://hackerone.com/reports/131053
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-15T11:01:53.521Z
- **Disclosed**: 2017-08-21T13:28:04.878Z

## Reporter
- **Username**: drstache
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
At https://gratipay.com/USER/emails/ you can submit a non valid email.
To do it you only need to change `type="email"` in `type="text"` , you are using a filter, but special chars pass though, as you can see in the screenshots.

## Attachments
- gratipay-com_2.PNG
- gratipay-com_3.PNG
- gratipay-com_1.PNG
