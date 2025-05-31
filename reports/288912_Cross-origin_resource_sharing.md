# Cross-origin resource sharing

## Report Details
- **Report ID**: 288912
- **URL**: https://hackerone.com/reports/288912
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-11-09T18:08:30.767Z
- **Disclosed**: 2018-01-11T15:25:53.462Z

## Reporter
- **Username**: sureshbudharapu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information


###Issue:Cross-origin resource sharing: arbitrary origin trusted

The application implements an HTML5 cross-origin resource sharing (CORS) policy for this request that allows access from any domain.

The application allowed access from the requested origin https://hhgdhgjgbrg.com

Since the Vary: Origin header was not present in the response, reverse proxies and intermediate servers may cache it. This may enable an attacker to carry out cache poisoning attacks.
**Issue background:**
An HTML5 cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request.

Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.

If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.
 **remediation:**

Host:https://www.semrush.com
Path: /blog/ws/
remediation:Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.
Request:
` ` `
POST /blog/ws/?EIO=3&transport=polling&t=L-XUrv3&sid=GgyrWydG6cdnMzMxCIuZ HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Content-type: text/plain;charset=UTF-8
Referer: https://www.semrush.com/blog/
Content-Length: 38
Cookie: ███; blog_split=C; ref_code=__default__; usertype=Free-User; marketing=%7B%22user_cmp%22%3A%22%22%2C%22user_label%22%3A%22%22%7D; localization=%7B%22locale%22%3A%22en%22%7D; db=us; _ga=GA1.2.1264834051.1510222356; _gid=GA1.2.837455256.1510222356; utz=Asia%2FKolkata; userdata=%7B%22tz%22%3A%22GMT+5.5%22%2C%22ol%22%3A%22en%22%7D; visit_first=1510222356000; io=GgyrWydG6cdnMzMxCIuZ; wp13557=UWYYADDDDDDMAZHBYLB-JMKI-XKAU-IWWJ-LMUVHMXKWMYJDHAXJKTTX-HVXB-XUWC-BYVI-KCVBHMXYUVKBDlLtkNlo_Jht; __uvt=; uvts=6k5thF30VCHYVUCC; XSRF-TOKEN=alfdcNxz1SnLcbyeUDtBHc7p5i0IgSWjkrXL10C6; community-semrush=XX2llfwaopEzko3IlrC5VPaXpFuQMqQVJvo3mdzN; exp__cid=3d0fa57b-7bf2-4c65-9b04-dd93cda4bddc; __insp_wid=826279527; __insp_slim=1510241796546; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuc2VtcnVzaC5jb20vYXBpLWRvY3VtZW50YXRpb24v; __insp_targlpt=U0VNcnVzaCBBUEkgfCBTRU1ydXNoIEVuZ2xpc2g%3D; __insp_norec_sess=true; _gat=1; _uetsid=_ueta0786e6a
Connection: close
1.Origin: https://hhgdhgjgbxg.com

35:42["online","{\"user\":147782577}"]
` ` `
Response:
` ` ` 
HTTP/1.1 400 Bad Request
Server: nginx
Date: Thu, 09 Nov 2017 15:58:45 GMT
1.Content-Type: application/json
Connection: close
1.Access-Control-Allow-Credentials: true
1.Access-Control-Allow-Origin: https://hhgdhgjgbxg.com
X-Frame-Options: SAMEORIGIN always
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Length: 41

{"code":1,"message":"Session ID unknown"}
` ` `

**References:
Exploiting CORS Misconfigurations
**Vulnerability classifications**
CWE-942: Overly Permissive Cross-domain Whitelist


## Attachments
- www.semrush.com.avi
