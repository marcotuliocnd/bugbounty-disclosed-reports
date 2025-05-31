# User credentials are not strong on vault.uber.com

## Report Details
- **Report ID**: 128895
- **URL**: https://hackerone.com/reports/128895
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-07T06:41:20.923Z
- **Disclosed**: 2016-07-26T00:30:23.469Z

## Reporter
- **Username**: bugs3ra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
I was just trying to login vault.uber.com

I entered email **xx** and password **xx**,  I got loggedin to someones account.
I entered email **zz** and password **zz**,  I got loggedin to someones account.

It means passowrd complexity and length of username/email is not enforced. This allowed my to access the someones account. Since it contains payment related information, password complexity and email should be there.

## Attachments
No attachments
