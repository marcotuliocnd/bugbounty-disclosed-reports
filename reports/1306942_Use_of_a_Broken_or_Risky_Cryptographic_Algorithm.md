# Use of a Broken or Risky Cryptographic Algorithm

## Report Details
- **Report ID**: 1306942
- **URL**: https://hackerone.com/reports/1306942
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-16T15:14:50.403Z
- **Disclosed**: 2021-09-15T12:51:43.134Z

## Reporter
- **Username**: 418sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
revive-adserver utilizes a PRNG for session-token generation, this means that an attacker could theoretically be able to generate session tokens at random and take over accounts at random.

[This function does not generate cryptographically secure values, and should not be used for cryptographic purposes.](https://www.php.net/manual/en/function.uniqid.php)

Location: https://github.com/revive-adserver/revive-adserver/blob/6e665eac9b20ff21c167eae420b73a976f3bb52a/www/admin/lib-sessions.inc.php#L228

References: https://www.php.net/manual/en/function.uniqid.php

## Impact

This vulnerability is capable of allowing mass account takeover by having attackers generate other users' session tokens.

## Attachments
No attachments
