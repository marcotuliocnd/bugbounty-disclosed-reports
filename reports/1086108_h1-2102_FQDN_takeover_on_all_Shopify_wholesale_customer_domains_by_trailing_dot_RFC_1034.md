# [h1-2102] FQDN takeover on all Shopify wholesale customer domains by trailing dot (RFC 1034)

## Report Details
- **Report ID**: 1086108
- **URL**: https://hackerone.com/reports/1086108
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-24T18:18:49.096Z
- **Disclosed**: 2021-03-25T14:56:36.001Z

## Reporter
- **Username**: intidc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Due to a missing domain format check in Shopify's wholesale functionality, it is possible to serve arbitrary content on the customer's domain through existing DNS records already configured to work with Shopify. I only tested with domains that I own but as far as I understand, this would work with just any domain or subdomain that it set up to work with Shopify wholesale.

This exposes Shopify wholesale customers to several risk, similar to classic subdomain takeovers:
- Loss of domain integrity: attackers could host malicious content on the customer's domain
- Phishing attacks: attackers could use login/sign up page to capture PII and 
- Scams: scammers could recreate trusted wholesale shops, host them under the official domain and collect money

## Steps To Reproduce:

  - For the sake of this proof of concept, we'll take over my test wholesale shop at https://shop.inti.io/accounts/sign_in, which has it's CNAME set to `wholesale-shops.shopifyapps.com` (as requested by [the documentation](https://help.shopify.com/en/manual/online-sales-channels/wholesale/channel/wholesale-settings/domains)):

{F1170259}

In real-life attacks, attackers could perform reverse CNAME lookups through e.g. Alien Vault's OTX.

- Now log in as attacker and try to add `shop.inti.io` as a domain name in your preferences. **This will not work, because there's already a store attached to it**:

{F1170265}

- Attacker now sits down, takes a nip of coffee and reads [RFC 1034](https://www.ietf.org/rfc/rfc1034.txt). Attacker notices the following:

```
Since a complete domain name ends with the root label, this leads to a
printed form which ends in a dot.  We use this property to distinguish between:

   - a character string which represents a complete domain name
     (often called "absolute").  For example, "poneria.ISI.EDU."

   - a character string that represents the starting labels of a
     domain name which is incomplete, and should be completed by
     local software using knowledge of the local domain (often
     called "relative").  For example, "poneria" used in the
     ISI.EDU domain.
```

In theory, _all_ domain names should have a trailing dot at the end, but since literally no one does that both a domain name with and without a trailing dot will essentially result in the same records being served. Since Shopify does not implement DNS-based verification and only checks whether the record is already present, we can enter the trailing dot version of the domain name to bypass this check:

{F1170267}
{F1170268}

- Now attacker waits for a few minutes to allow the DNS / SSL changes to propagate. Depending on your browser's cache, it can take a while, but normally after a few minutes the malicious shop should pop up at `https://shop.inti.io./accounts/sign_in`.

## Final results

**Real store: `https://shop.inti.io/accounts/sign_in`**

{F1170269}

**Hijacked store: `https://shop.inti.io./accounts/sign_in`**

{F1170270}

##Note to triagers - I have released `shop.inti.io.` in my shopify so you can claim it and reproduce. This means that the hijacked store is no longer accessible. 

This could be done by anyone for any wholesale connected store, without having access to the DNS records.

## Recommended fix

Do not consider trailing dots when checking whether domain names already exist on your back-end

## Supporting Material/References:

*Trailing Dots in Domain Names, CHESHIRE S., http://www.dns-sd.org/trailingdotsindomainnames.html
* DOMAIN NAMES - CONCEPTS AND FACILITIES (RFC1034), MOCKAPETRIS P (Network Work Group), https://www.ietf.org/rfc/rfc1034.txt

## Impact

This exposes Shopify wholesale customers to several risk, similar to classic subdomain takeovers:
- Loss of domain integrity: attackers could host malicious content on the customer's domain
- Phishing attacks: attackers could use login/sign up page to capture PII and 
- Scams: scammers could recreate trusted wholesale shops, host them under the official domain and collect money

## Attachments
- Screenshot_2021-01-24_at_18.50.28.png
- Screenshot_2021-01-24_at_19.00.21.png
- Screenshot_2021-01-24_at_19.06.42.png
- Screenshot_2021-01-24_at_19.06.49.png
- Screenshot_2021-01-24_at_19.10.58.png
- Screenshot_2021-01-24_at_19.10.51.png
