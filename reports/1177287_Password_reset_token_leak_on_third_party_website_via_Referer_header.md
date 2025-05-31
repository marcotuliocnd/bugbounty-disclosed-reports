# Password reset token leak on third party website via Referer header

## Report Details
- **Report ID**: 1177287
- **URL**: https://hackerone.com/reports/1177287
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-27T17:15:20.204Z
- **Disclosed**: 2021-08-10T15:20:42.492Z

## Reporter
- **Username**: n1had
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:

It has been identified that the application is leaking referrer token to third party sites. In this case it was found that the password reset token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the token and reset the passwords of the victim.

## Steps To Reproduce:

1) Request a password reset link for a valid account
2) Click on the reset link
3) Before resetting the password click on webiste
4) You will notice the following request in burpsuite


```
POST /events/1/NRJS-cb3c976936ae1bbb096?a=429165133&sa=1&v=1194.94d5a62&t=Unnamed%20Transaction&rst=56534&ck=1&ref=https://app.upchieve.org/setpassword/e2d710c6e099bf07d63507602a44c176 HTTP/1.1
Host: bam.nr-data.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0
Accept: */*
Accept-Language: en-US,en;q=0.5

```

## Impact

Password reset token leak on third party website via Referer header

## Attachments
- 3rbParty.JPG
