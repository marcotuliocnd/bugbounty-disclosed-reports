# Extract Billing admin email address using random team id

## Report Details
- **Report ID**: 225831
- **URL**: https://hackerone.com/reports/225831
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-03T13:41:31.790Z
- **Disclosed**: 2017-07-23T10:29:47.965Z

## Reporter
- **Username**: csanuragjain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dashlane

## Vulnerability Information
Any user can extract and enumerate email address of dashlane members.

**Steps to reproduce**

1) Login to console.dashlane.com (Register using https://www.dashlane.com/business/try)
2) Click on Manage Users while intercepting request in Burp
3) Look for a request to https://ws1.dashlane.com/1/teamPlans/getTeamLastUpdateTs 
4) Note down the body param values for login and uki
5) Send the request from Step3 to Burp Repeater
6) Change the request uri to https://ws1.dashlane.com/1/teamPlans/members in repeater. Also change body param to below:

limit=0&login=<login from Step4>&orderBy=login&teamId=<Team for which you want billing admin email>&uki=<uki from Step4>

7) Forward the request
8) Notice the response. The value of billingAdmins contains the billing address of the team given in Step6
9) Repeat Step6 with different team id to extract all admin emails

**Mitigation**
Do not include email information for unauthorized team id.

## Attachments
- mailaddress.PNG
