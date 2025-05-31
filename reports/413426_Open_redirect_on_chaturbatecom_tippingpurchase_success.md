# Open redirect on chaturbate.com (tipping/purchase_success)

## Report Details
- **Report ID**: 413426
- **URL**: https://hackerone.com/reports/413426
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-24T15:35:42.663Z
- **Disclosed**: 2018-10-25T01:42:34.430Z

## Reporter
- **Username**: glc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hi,

I would like to report an open redirect issue on `https://chaturbate.com/`


## Description

An attacker can redirect a user to any external website using the parameter `prejoin_data`, this parameter seems to miss sanitization.


## Steps to Reproduce

Visit the following url:
https://64.38.230.2/tipping/purchase_success/?product_code=4137&prejoin_data=domain%2Fpoc.10degres.net
This will redirect you to my website `http://poc.10degres.net`

**Browsers Verified In:**
* Firefox 56.0, Ubuntu 16.04


## PoC

{F350390}

## Impact

By modifying untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials. Because the server name in the modified link is identical to the original site, phishing attempts may have a more trustworthy appearance.


## Remediation

Use a whitelist approach to allow redirection to trusted domains.


## See also

https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet




Best regards,

Gwen

## Attachments
- 20180924-open-redirect.png
