# Race condition in performing retest allows duplicated payments

## Report Details
- **Report ID**: 429026
- **URL**: https://hackerone.com/reports/429026
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-26T01:04:15.852Z
- **Disclosed**: 2018-12-27T12:12:56.622Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary

There exists a race condition in performing retests. By executing multiple requests to confirm a retest at the same time, a malicious user is paid multiple times for the retest. This allows for stealing money from HackerOne, which could go unnoticed by both HackerOne and the attacker (me).

## Steps to Reproduce

1. Receive a retest request email from HackerOne.
2. Intercept the request to retest the email. Right click the request in Burp Suite and select `Copy as curl command`.
3. Execute the request on the command line in the form `(request) & (request) & ...`. In testing, I executed the command 5 times.
4. Scroll to the bottom of https://hackerone.com/settings/bounties. The payment will appear under the `Retest payments` sections and may be repeated.
5. Wait a few weeks. If successful, a callback from HackerOne will be received (in this case from @michiel):

    {F366191}

6. Check your bank account statements. Observe that a $500 payment was sent from HackerOne 2 weeks ago, demonstrating that the race condition was successful:

{F366192}

## Impact

This allows an attacker to exploit the retesting feature to steal many times more money. Given that this went unnoticed by both the attacker and HackerOne for over 2 weeks, this has the potential to be exploited multiple times to steal money from HackerOne.

## Attachments
- Screen_Shot_2018-10-25_at_5.58.17_PM.png
- IMG_3755.png
