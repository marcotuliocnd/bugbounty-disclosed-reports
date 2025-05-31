# WordPress Automatic Update Protocol Does Not Authenticate Updates Provided by the Server

## Report Details
- **Report ID**: 228854
- **URL**: https://hackerone.com/reports/228854
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-16T15:51:39.377Z
- **Disclosed**: 2019-07-22T16:21:59.487Z

## Reporter
- **Username**: paragonie-scott
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
When the WordPress automatic update process is initiated (likely via `wp-cron.php`), this is the path the code takes:

* https://github.com/WordPress/WordPress/blob/4a6f90db58a935abb688cfb91b391dffeda7b35c/wp-admin/includes/class-wp-upgrader.php#L242-L283
* https://github.com/WordPress/WordPress/blob/38347d7c580be4cdd8476e4bbc653d5c79ed9b67/wp-admin/includes/file.php#L482-L525
* https://github.com/WordPress/WordPress/blob/9f4bbcdb7896a7baba9eb88add281f3fbcdec0ef/wp-includes/http.php#L67-L71
* https://github.com/WordPress/WordPress/blob/76d77e927bb4d0f87c7262a50e28d84e01fd2b11/wp-includes/class-http.php#L597-L613
* https://github.com/WordPress/WordPress/blob/76d77e927bb4d0f87c7262a50e28d84e01fd2b11/wp-includes/class-http.php#L95-L425

The only integrity check that is provided is that the `Content-MD5` header sent by the WordPress server is [checked against the MD5 checksum of the file](https://github.com/WordPress/WordPress/blob/38347d7c580be4cdd8476e4bbc653d5c79ed9b67/wp-admin/includes/file.php#L515-L522) (which, if omitted by the server, the WordPress site will silently disregard).

There is no code signing in place. As a consequence, an attacker who has fully compromised the WordPress update server can issue updates to any WordPress install on the Internet that hasn't disabled automatic updates.

I have previously reported this [to the WordPress Trac](https://core.trac.wordpress.org/ticket/39309), along with a proposed solution (Ed25519 signature verification + update hash commitment to a Merkle tree, similar to Mozilla's [Binary Transparency](https://wiki.mozilla.org/Security/Binary_Transparency) project). However, the Powers That Be deemed it a low priority issue, and the rest of the WP core team responded one of two ways:

1. "I don't understand cryptography, so I won't be much help here."
2. "I'm already overworked and can't find the time or energy to touch this."

I hope that, by reporting this to HackerOne, it can be given the attention it requires from people with the time/energy availability and the crypto/security expertise to make a solution happen.

This problem was [narrowly missed before](https://www.wordfence.com/blog/2016/11/hacking-27-web-via-wordpress-auto-update/). I'd like to see it gets fixed before the rest of the Internet has to contend with a DDoS botnet that consists of >20% of the top 10 million websites. I don't imagine many networks would survive such an attack.

## Attachments
No attachments
