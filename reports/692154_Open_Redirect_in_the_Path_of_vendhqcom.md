# Open Redirect in the Path of vendhq.com

## Report Details
- **Report ID**: 692154
- **URL**: https://hackerone.com/reports/692154
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-11T05:17:31.445Z
- **Disclosed**: 2019-10-31T00:23:42.098Z

## Reporter
- **Username**: zoidsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vend_vdp

## Vulnerability Information
**Summary:** 
There is an open redirection vulnerability in the path of 
```
https://www.vendhq.com/
```

**Description:**
An attacker can redirect anyone to malicious sites.

## Steps To Reproduce:

Type in this URL:

```
https://www.vendhq.com//evil.com/
```

As, you can see it redirects to that website when you inject this payload:
 ```
//evil.com/
```

evil.com was used as an example but this could be any website note, the `//` is the bypass.



## Supporting Material/References:

  * https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html

## Impact

* Attackers can serve malicious websites that steal passwords or download ransomware to their victims machine due to a redirect and there are a heap of other attack vectors.

## Attachments
- 2019-09-11_15-10-24.mkv
