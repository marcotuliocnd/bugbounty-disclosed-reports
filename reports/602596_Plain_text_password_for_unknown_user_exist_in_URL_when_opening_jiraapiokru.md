# Plain text password for 'unknown' user exist in URL when opening jira.apiok.ru

## Report Details
- **Report ID**: 602596
- **URL**: https://hackerone.com/reports/602596
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-06T21:06:59.152Z
- **Disclosed**: 2019-06-17T15:25:55.439Z

## Reporter
- **Username**: exadmin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ok

## Vulnerability Information
Documentation at https://api.mail.ru/docs/guides/billing/ 
has a link to http://apiok.ru/jira/documents/ 
which redirects to https://jira.apiok.ru/secure/CreateIssue.jspa?pid=-2&os_username=unknown&os_password=X7:1OEh3

This pair of username & password - is effective login & password to JIRA system and allows to create new tickets/save filters/upload attachments (which can be used to provide malicious content)


I admit it can be incorrect realization of anonymouse tickets submission (which is possible at least since Fbe, 2016 https://confluence.atlassian.com/jirakb/how-to-allow-users-to-create-issues-anonymously-192551.html)

## Impact

Plain password text can help to undestand pattern of password generation for other accounts
Fishing is posible using official link to apiok.ru subdomain, i.e. http://jira.apiok.ru/secure/temporaryattachment/1585b6ba1084b134047a663dd8e698efc3a87e21/temp236609509878930861_test.png (and here can be png-bob for example which is accessible for everyone)

## Attachments
No attachments
