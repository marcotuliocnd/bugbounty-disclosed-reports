# Login csrf.

## Report Details
- **Report ID**: 117195
- **URL**: https://hackerone.com/reports/117195
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-18T19:27:22.866Z
- **Disclosed**: 2017-08-21T13:29:29.202Z

## Reporter
- **Username**: diffender23
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi , 

There is no state parameter in bitbucket login request .

https://bitbucket.org/site/oauth1/authorize?oauth_token=ZmCHb7dnyYVYKTYRNt .

As you can see that there is no state parameter in above request there it is possible to exploit login csrf.


## Attachments
No attachments
