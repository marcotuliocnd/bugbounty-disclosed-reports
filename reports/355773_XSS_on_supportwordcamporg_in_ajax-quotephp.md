# XSS on support.wordcamp.org in ajax-quote.php

## Report Details
- **Report ID**: 355773
- **URL**: https://hackerone.com/reports/355773
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-05-21T23:10:18.324Z
- **Disclosed**: 2018-07-23T15:06:06.875Z

## Reporter
- **Username**: mopman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi,
There is an XSS vulnerability in ajax-quote.php on http://support.wordcamp.org. It can be demonstrated with the attached POC - this needs to be run in Firefox to execute, as it's super basic and XSS Auditor will catch it (but with multiple parameters, even with one of them filtered, it's likely that one could be crafted that would work in Chrome, too).

I would quite like to check out that SupportPress application in more detail, but it's quite hard to install :( Seems to not work out of the box for me - so for now, just an XSS.

## Impact

An attacker who could trick an authenticated user into visiting their webpage/link could perform any action on behalf of that user. Cookie theft seems unlikely as, from a brief scan of the code (I can't login) I think it uses httponly on the important cookies.

## Attachments
- testpost.html
