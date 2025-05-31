# Google dork lead to unsubscribe anyone from all Banfield emails

## Report Details
- **Report ID**: 2055081
- **URL**: https://hackerone.com/reports/2055081
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-07T14:04:18.699Z
- **Disclosed**: 2023-08-30T15:45:38.308Z

## Reporter
- **Username**: ractiurd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
## Summary:
Hi there,

while checking on shodan i found an ip "█████████" which was issued to ███████.

and this was giving me 404 status code. while checking on web archive i found out some link like:

████████

when i did a google search i found out the endpoint for unsubscribe where i can unsubscribe any banfield users from their email without authentication and authorization.

endpoint: ███?EmailAddress██████████████████████████████████

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. do a google dork site:█████
  1.click on second link and it will direct you to ███████?EmailAddress██████████████████
  1. put authenticated user email and confirm. This will lead to unsubscribe them from banfield emails.

For user enum or email enum this can be done from 

POST /Security/SendClientIdMail HTTP/2
Host: █████
Cookie: ████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
Accept: */*
Accept-Language: en-US,en;q███████████0.5
Accept-Encoding: gzip, deflate
Referer: ████████-Type: application/x-www-form-urlencoded; charset█████████████████utf-8
X-Requested-With: XMLHttpRequest
Content-Length: 159
Origin: ███████████
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

__RequestVerificationToken███████████████&email███████████████████████████████&returnUrl█████

On this there is no rate limit so email enum can be done.

## Supporting Material/References:
████████████████

  * [attachment / reference]
I added screen shot as a proof of concepts. 

Thank you very much. Wish you a good day.

## Impact

Can unsubscribe anyone from all Banfield emails

## Attachments
No attachments
