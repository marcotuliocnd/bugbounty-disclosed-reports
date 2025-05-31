# "More on Wikipedia" link disclose "Referrer" and leak `window.opener` reference for arbitrary websites

## Report Details
- **Report ID**: 409518
- **URL**: https://hackerone.com/reports/409518
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-13T22:58:28.376Z
- **Disclosed**: 2019-04-30T06:08:30.542Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
## Summary:

### "Referrer" leak

`http://` link to Wikipedia transferring `Referrer` header allows a remote attacker with MITM access to sniff Referrer URL for important tokens after following  "More on Wikipedia" link.

### Controllable page [MITM] with `window.opener` pointing to the navigation-initiated webpage

`http://` link "More on Wikipedia" allows a remote attacker with MITM access to obtain a `window.opener`reference to the website initiating new window opening.

## Description:

Grammarly extension shows a card with a meaning of the currently focused word on dblclick.
Some of these cards have "More on Wikipedia" link depending on the selected word. (e.g., AFAIR "our" word).
"More on Wikipedia" link is an HTTP link that discloses referrer and opener to the  Wikipedia.
Since it's an HTTP link, a remote attacker could use MITM attack to hijack "Referrer" and `window.opener`.

## Browsers Verified In:

Chrome: 68.0.3440.106
Grammarly: 14.868.1844

## Steps To Reproduce:

**IMPORTANT:** Luckily for Grammarly, Wikipedia enables HSTS for all further requests, so you'll need a clean browser to repro this vulnerability.

### `Referrer`

0. Setup MITM. e.g., by modifying `/etc/hosts`: `127.0.0.1 en.wikipedia.org`. Make sure no HSTS enabled for Wikipedia.
1. Start `referrer-mitm.js`
2. Go to an arbitrary webpage
3. Find a `<grammarly-card>` with "More on Wikipedia" link (e.g., "Our"/"Your" words should work)
4. Follow the link
5. Alert on `http://en.wikipedia.org` with referrer

### `window.opener` hijacking

0. Setup MITM. e.g., by modifying `/etc/hosts`: `127.0.0.1 en.wikipedia.org`. Make sure no HSTS enabled for Wikipedia.
1. Start `opener-mitm.js`
2. Go to an arbitrary webpage
3. Find a `<grammarly-card>` with "More on Wikipedia" link
4. Follow the link
5. `window.opener` navigates to `https://github.com/Metnew/uxss-db`

**NOTE:** You could play with #405056 to pwn websites that don't share `window.opener` by default. #409400 is also great.

## Supporting Material/References:

- Exploits attached

## Impact

### Referrer

A remote attacker with a MITM access could sniff URL of the active webpage after user will follow "More on Wikipedia" link.

**RESULT:** #738 and #6884 show how leaked "Referrer" could lead to a leak of sensitive info (tokens in URLs, sensitive URL  params, etc.).

The impact is the same, however, it spreads on all websites, ignoring their level of defence.

### `window.opener`

Leaked `window.opener` allows exploiting vulnerabilities relying on `window.opener` such as #409400 and #405056 on arbitrary origins, ignoring the level of defense of the webpages.

**RESULT:** Attacker obtains access to previously unexploitable pages those don't share `opener`.


### Summary

The vulnerability requires a particular (high) level of user assistance: not all cards have "More on Wikipedia" link + navigation required.

 > I hope I correctly estimated a CVSS v3  score (5.2): Low Integrity (`window.opener`) + Low Confidentiality (Referrer may disclose sensitive info) + High attack complexity. However, the score may not reflect the actual severity as usual (sadly for me, it's much closer to "Low", because of HSTS on Wikipedia).

The vulnerability  is interesting, mostly because of `window.opener` reference, but in very rare cases "Referrer" may become even a more powerful attack vector.

## Attachments
- referrer-mitm.js
- opener-mitm.js
