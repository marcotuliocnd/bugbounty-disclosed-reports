# GET /api/v2/url_info endpoint is vulnerable to Blind SSRF

## Report Details
- **Report ID**: 1057531
- **URL**: https://hackerone.com/reports/1057531
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-12T17:01:03.517Z
- **Disclosed**: 2020-12-15T13:03:15.978Z

## Reporter
- **Username**: atc_h1h1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
GET /api/v2/url_info endpoint is vulnerable to Blind SSRF. I am able to hit both Internal and External services via **url** parameter by replacing with internal and external url.

## Platform(s) Affected:
https://www.tumblr.com/

## Steps To Reproduce:

  1. Login to https://www.tumblr.com/
  2. Follow any blog and intercept request via Proxy

Request :

GET /api/v2/url_info?url={{}}&fields%5Bblogs%5D=avatar%2Cname%2Ctitle%2Curl%2Cdescription_npf%2Ctheme%2Cuuid%2Ccan_be_followed%2C%3Ffollowed%2C%3Fis_member%2Cshare_likes%2Cshare_following%2Ccan_subscribe%2Ccan_message%2Csubscribed%2Cask%2C%3Fcan_submit%2C%3Fis_blocked_from_primary%2C%3Fadvertiser_name%2C%3Ftop_tags%2C%3Fprimary HTTP/1.1
Host: www.tumblr.com 

Response:
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

3. Now replace **url** parameter to your controller server url and send it.
4. You will get request to your server.

I could get verify it via IP Address: **74.114.154.11**
NetRange:       74.114.152.0 - 74.114.155.255
CIDR:           74.114.152.0/22
NetName:        AUTOMATTIC
NetHandle:      NET-74-114-152-0-1
Parent:         NET74 (NET-74-0-0-0-0)
NetType:        Direct Assignment
OriginAS:       AS2635
Organization:   Automattoque (AU-187)
RegDate:        2017-04-20
Updated:        2017-04-21
Ref:            https://rdap.arin.net/registry/ip/74.114.152.0

OrgName:        Automattoque
OrgId:          AU-187
Address:        P.O. Box 997
City:           Halifax
StateProv:      NS
PostalCode:     B3J 2X2
Country:        CA
RegDate:        2015-11-25
Updated:        2017-04-21
Ref:            https://rdap.arin.net/registry/entity/AU-187

5. Now replace it with localhost url -> http://127.0.0.1:9090 and see response will be 404 but based on response time, port status can be identified.

Limited Internal and External SSRF is performed. Attacker can target internal services by sending requests in bulk via mentioned endpoint.
Attacker can get ports status by fuzzing or intruder attacker based on response time.
Attacker would be able to target internal services and try to exhaust/target internal infrastructure.

**Remediation Strategies :**

1. **Only white listed URLs should be allowed for this endpoint. As user can only follow tumblr blogs, there would be some sort of filter mechanism to whitelist tumblr blogs. Any other URLs should be blocked.**
2. **Not only for this API endpoint, any localhost URLs provided by user should be blocked.**
2. **Any Out-of-band request from tumblr should be sent via CLIENT only. Here  in this case, server is requesting user controller URL input and requesting resource which is exposing internal IP details.**

## Impact

Attacker can get ports status by fuzzing or intruder attacker based on response time.
Attacker would be able to target internal services and try to exhaust/target internal infrastructure.

## Attachments
No attachments
