# CSRF Attack leads to delete album at ████████

## Report Details
- **Report ID**: 2697588
- **URL**: https://hackerone.com/reports/2697588
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-09-04T13:25:49.043Z
- **Disclosed**: 2024-12-18T19:40:36.699Z

## Reporter
- **Username**: prakhar0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Through research, I discovered a CSRF vulnerability in one of the DoD asset **`███████`**

**NOTE: The previous report, I submitted was on a different subdomain (███).**

There is a **feature to create albums** for a media collection such as photos and videos. While performing some actions on it, I found that **there is NO CSRF verification when deleting albums.**

Additionally, the delete request is based on GET, So it'll more easier for an attacker to exploit it..

#### Vulnerable Request

```
GET /mediagallery/delete/id/{album_id} HTTP/2
Host: ██████████
Cookie: {YOUR SESSION}
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: https://█████/mediagallery/index
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

## Reference
https://hackerone.com/reports/2652190

## Impact

CSRF Attack
Delete users album

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
As an attacker, I only need to send the CSRF exploit to the victim to delete their album. That's it.

I'll mention in detail the steps required to reproduce the issue

For testing you can create an album by -
- Navigate to https://www.████████/image/8584351/tradoc-best-squad-competition , 
- From the **Options** 
- Click **Add to my albums**, from there you can create an album.

**Attacker's Account**
1 - From the attacker's account, Delete an album & intercept the request.
2 - Create a CSRF PoC & send it to Victim

**Victim's Account**
3 - The victim clicks on the attacker's exploit
4 - The victim album is deleted successfully.

## Suggested Mitigation/Remediation Actions
1 - Validate the request with CSRF Token.



## Attachments
No attachments
