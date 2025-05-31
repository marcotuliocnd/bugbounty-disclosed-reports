# Authorization for wp-admin directory are vulnerable to brute force.

## Report Details
- **Report ID**: 788420
- **URL**: https://hackerone.com/reports/788420
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-03T18:44:10.022Z
- **Disclosed**: 2020-02-05T15:40:31.375Z

## Reporter
- **Username**: brumens
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
The domain https://my.stripo.email in the directory /wp-admin are not blocking amount of request in the authorization form, this leads to bruteforce attack. Where the attacker are able to guess tons of passwords without getting blocked or the password field gets locked.
This attack make it possible to gain access as an admin extremely easy and quick to get a successfully login.

To test this security issue you need to visit the link https://my.stripo.email in the directory /wp-admin
Install a bruteforce tool like: Burp intruder, Wfuzz, Hydra, Ncrack
I personality use Wfuzz and Burp.

Wfuzz command in Linux terminal: wfuzz -c -w /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -u https://my.stripo.email/wp-admin -d "Authorization: Basic admin:FUZZ" 

Supported links and fix tips:
https://owasp.org/www-community/attacks/Brute_force_attack
https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks

This Pictures below show status from my program as you can see with Wfuzz it hitted around 3000 passwords in like 40 secounds (calculated approximately.)
My Burp suite shows more exact response from your server.

## Impact

Get access to anadmin login quickly and while logged in the attacker can do whatever an admin can.

## Attachments
No attachments
