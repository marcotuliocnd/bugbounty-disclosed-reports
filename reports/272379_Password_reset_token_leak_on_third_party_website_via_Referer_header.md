# Password reset token leak on third party website via Referer header

## Report Details
- **Report ID**: 272379
- **URL**: https://hackerone.com/reports/272379
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-27T12:35:22.111Z
- **Disclosed**: 2017-09-27T17:34:07.598Z

## Reporter
- **Username**: akaash_pantherdefence
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aspen

## Vulnerability Information
Hi Security Team,
*******************************************
#Description

It has been identified that the application is leaking referrer token to third party sites. In this case it was found that the password reset token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the token and reset the passwords of the victim.

#Steps To Reproduce:-
1) Request a password reset link for a valid account
2) Click on the reset link
3) Before resetting the password click on the github link footer section
4) You will notice the following request in burpsuit

#REQUEST:
GET /rtfd/readthedocs.org HTTP/1.1
Host: github.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://readthedocs.org/accounts/password/reset/key/1zp5-4pt-8163732eb05d188994ec/
Cookie: COOKIE
Connection: close
Upgrade-Insecure-Requests: 1


As you can see in the referrer the reset token is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can compromise the user accounts easily.
{F224492}

#Solution:
For remediation, you should stop the third party sites to show the referrer header by adding rel="noopener noreferrer" to external links in the footer. or check the reference below.

Ref: https://mathiasbynens.github.io/rel-noopener/
*************************************************************
Best Regards
*Akaash Sharma :)*


## Attachments
- POC_img.jpg
