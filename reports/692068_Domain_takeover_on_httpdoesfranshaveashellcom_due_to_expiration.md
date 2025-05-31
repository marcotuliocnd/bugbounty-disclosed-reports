# Domain takeover on http://doesfranshaveashell.com/ due to expiration

## Report Details
- **Report ID**: 692068
- **URL**: https://hackerone.com/reports/692068
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-10T22:29:06.427Z
- **Disclosed**: 2019-09-11T09:20:38.379Z

## Reporter
- **Username**: magic_spell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
###Summary

Hi Ed,

I'm not so sure if registrar inform your domain had expired or it will auto renew upon reaching. To be safe, I decide to manual inform you.

###Step to Reproduce

So lately I notice that http://doesfranshaveashell.com/ is no longer operate. It will show some advertisements there.

{F579676}



 It was expired on 2019-09-02. Latest status is `clientTransferProhibited`, which is currently locked for being transferable to another host party. Which I believe is a good news.

{F579687}
https://www.whois.com/whois/doesfranshaveashell.com

So PoC is that I'll get 404 page return by current time as I going http://doesfranshaveashell.com/keybase.txt.
{F579688}


Here is the PoC cache page I able to pull out, 28 August 2019 from Google storage. Not sure how long cache page serving soon.
{F579691}

###Scenario of exploit
As latest status is `clientTransferProhibited`, which  limit the security risk. Exploit person usually perform another typosquatting attack.

As quoted phrases from https://www.namecheap.com/security/domain-phishing-security-attacks-guide/

1. Typosquatting

```
Singular and Plural Versions - Buy both versions of your domain name to be on the safe side, portland-car-repair.com and portland-car-repairers.com for example.
```

Exploit person will buy doesfranhaveashell.com at $9.88/year to trick user. They can craft same page just like the previous cache page, add extra new features & declare that real doesfranshaveashell.com no longer in operating since expired reach out, by making official statement. It fact it just missing a letter 's' from initial domain.

Here is the order summary & cost;
{F579708}

Exploit person could perform variant of attack, example stealing cookies from victim session, or perform UI redress attack. They can frame out target page they like to trick user redirected links from doesfranhaveashell.com . 
Or create imitation login forms to steal victim real username account & password, by claiming will send 
monthly newsletters to subscriber. Or registered account could benefit some gift.

When doesfranshaveashell.com change status to release, they will purchase immediately to takeover this domain from owner, which is you.

___
As I am not sure how long is the grace period available by registrar. Some registrar offer days, one week, or up to months. While some offer extra redemption period as well to customer.




Nevertheless, hope this could help as a small reminder that your domain recently expired.

Best regards,

## Impact

- Not timely renewed or restored after expiration, domain might be made purchase available for others registration on a first-come-first-served basis.
- Pass out grace period might release status to be ready purchase by exploit person to takeover domain

## Attachments
- registrar.png
- Domain_info.png
- keybase_404.png
- Keybase_cache.png
- Exploit.png
