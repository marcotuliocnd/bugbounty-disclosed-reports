# OAuth `redirect_uri` bypass using IDN homograph attack resulting in user's access token leakage

## Report Details
- **Report ID**: 861940
- **URL**: https://hackerone.com/reports/861940
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-29T03:28:11.813Z
- **Disclosed**: 2020-06-18T14:33:06.668Z

## Reporter
- **Username**: yassineaboukir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
## Issue Summary:
It was found that SEMrush OAuth implementation fails to properly validate the value of `redirect_uri` parameter which was bypassed using IDN homograph attack which results in leaking the user's access token to an attacker-controlled domain name.

IDN homography attack exploits the fact that many different characters look alike such as `semrush.com` is different from `sеmrush.com` because in the latter we used the Cyrillic letter `е` which looks exactly like the latin `e`.

Similarly, all below domain names will be treated as valid since the backend is somehow not idempotent since it will be fooled to map those to `semrush.com`.

```
- sémrush.com
- sêmrush.com
- sèmrûsh.com
- šemrush.com
- etc.
```

## Proof of concept:

  1. Authenticate to your account then browse to (*Note the `redirect_uri` is set to `oauth.šemrush.com`*):

```
https://oauth.semrush.com/oauth2/authorize?response_type=code&scope=user.info,projects.info,siteaudit.info&client_id=seoquake&redirect_uri=https://oauth.šemrush.com/oauth2/success
```

  2 . Once you approve the SEMrush application, your OAuth code will be sent to `oauth.šemrush.com` which is equivalent to `oauth.xn--emrush-9jb.com` since the browser will translate it to the punycode version which is way to represent IDNs with characters (A-Z, 0-9) supported by DNS.

████

The attacker will simply register the following domain name `xn--emrush-9jb.com` for this purpose. See:

█████

## Impact

As demonstrated earlier, a successful attack will result in leaking the user's OAuth code to an attacker-controlled domain name giving them unauthorized access to properties and data of the user's account.

Regards,
Yassine Aboukir

## Attachments
No attachments
