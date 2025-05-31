# The username of an account can be ..

## Report Details
- **Report ID**: 243609
- **URL**: https://hackerone.com/reports/243609
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-06-27T12:11:53.127Z
- **Disclosed**: 2017-07-27T12:44:47.559Z

## Reporter
- **Username**: blake12356
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello,

## Description:

The username of an account can be set to `..`. This makes it impossible to view the public profile of this account.

## POC:

I have claimed the username `..` on the demo.weblate.org site. It is impossible to view this account's public profile page. 
Here is the public profile page: https://demo.weblate.org/user/../

## Mitigation

I recommend you filtering usernames to prevent them from starting with `.`.

Thanks!

## Attachments
No attachments
