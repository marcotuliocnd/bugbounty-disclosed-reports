# Attacker with an Old account might still be able to DoS ctf.hacker101.com by sending a Crafted request 

## Report Details
- **Report ID**: 861170
- **URL**: https://hackerone.com/reports/861170
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-28T07:47:15.751Z
- **Disclosed**: 2020-05-25T04:01:51.385Z

## Reporter
- **Username**: iamr0000t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:** by sending a crafted request on ctf.hacker101.com a very long delay with a response of error 502 has been observed
I suspect that if I made this request on multiple tabs on my browser concurrently, it may cause ctf.hacker101.com to crash thats why I  haven't tried it.

**Description:** By changing  "accept encoding" and "user agent"  headers,  and sending a crafted request to ctf.hacker101.com 
a very long delay along with the response of error 502 has been observed. 


###Request Used ###
```
GET /group HTTP/1.1
Host: ctf.hacker101.com
User-Agent: Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, gzip,deflate,br
Referer: https://ctf.hacker101.com/group
Connection: close
Cookie: ███████
Upgrade-Insecure-Requests: 1

```

###Response Recieved### (after delay of 46 Seconds)
```
HTTP/1.1 502 Bad Gateway
Date: Tue, 28 Apr 2020 07:18:17 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Set-Cookie: ███
Set-Cookie: cf_use_ob=443; path=/; expires=Tue, 28-Apr-20 07:18:47 GMT
Expires: Thu, 01 Jan 1970 00:00:01 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
X-Frame-Options: SAMEORIGIN
CF-RAY: ███
Server: cloudflare
cf-request-id: ███
Content-Length: 4140

<!DOCTYPE html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en-US"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en-US"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en-US"> <!--<![endif]-->
<head>
<meta http-equiv="refresh" content="0">

<title>ctf.hacker101.com | 502: Bad gateway</title>
<meta charset="UTF-8" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
<meta name="robots" content="noindex, nofollow" />
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1" />
<link rel="stylesheet" id="cf_styles-css" href="/cdn-cgi/styles/cf.errors.css" type="text/css" media="screen,projection" />
<!--[if lt IE 9]><link rel="stylesheet" id='cf_styles-ie-css' href="/cdn-cgi/styles/cf.errors.ie.css" type="text/css" media="screen,projection" /><![endif]-->
<style type="text/css">body{margin:0;padding:0}</style>




</head>
<body>
<div id="cf-wrapper">

    

    <div id="cf-error-details" class="cf-error-details-wrapper">
        <div class="cf-wrapper cf-error-overview">
            <h1>
              
              <span class="cf-error-type">Error</span>
              <span class="cf-error-code">502</span>
              <small class="heading-ray-id">Ray ID: 58af01057a3bdf57 &bull; 2020-04-28 07:18:17 UTC</small>
            </h1>
            <h2 class="cf-subheadline">Bad gateway</h2>
        </div><!-- /.error-overview -->
        
        <div class="cf-section cf-highlight cf-status-display">
            <div class="cf-wrapper">
                <div class="cf-columns cols-3">
                  
<div id="cf-browser-status" class="cf-column cf-status-item cf-browser-status ">
  <div class="cf-icon-error-container">
    <i class="cf-icon cf-icon-browser"></i>
    <i class="cf-icon-status cf-icon-ok"></i>
  </div>
  <span class="cf-status-desc">You</span>
  <h3 class="cf-status-name">Browser</h3>
  <span class="cf-status-label">Working</span>
</div>

<div id="cf-cloudflare-status" class="cf-column cf-status-item cf-cloudflare-status ">
  <div class="cf-icon-error-container">
    <i class="cf-icon cf-icon-cloud"></i>
    <i class="cf-icon-status cf-icon-ok"></i>
  </div>
  <span class="cf-status-desc">Mumbai</span>
  <h3 class="cf-status-name">Cloudflare</h3>
  <span class="cf-status-label">Working</span>
</div>

<div id="cf-host-status" class="cf-column cf-status-item cf-host-status cf-error-source">
  <div class="cf-icon-error-container">
    <i class="cf-icon cf-icon-server"></i>
    <i class="cf-icon-status cf-icon-error"></i>
  </div>
  <span class="cf-status-desc">ctf.hacker101.com</span>
  <h3 class="cf-status-name">Host</h3>
  <span class="cf-status-label">Error</span>
</div>

                </div>
              
            </div>
        </div><!-- /.status-display -->

        <div class="cf-section cf-wrapper">
            <div class="cf-columns two">
                <div class="cf-column">
                    <h2>What happened?</h2>
                    <p>The web server reported a bad gateway error.</p>
                </div>
              
                <div class="cf-column">
                    <h2>What can I do?</h2>
                    <p>Please try again in a few minutes.</p>
                </div>
            </div>
              
        </div><!-- /.section -->

        <div class="cf-error-footer cf-wrapper">
  <p>
    <span class="cf-footer-item">Cloudflare Ray ID: <strong>58af01057a3bdf57</strong></span>
    <span class="cf-footer-separator">&bull;</span>
    <span class="cf-footer-item"><span>Your IP</span>: 182.70.148.191</span>
    <span class="cf-footer-separator">&bull;</span>
    <span class="cf-footer-item"><span>Performance &amp; security by</span> <a href="https://www.cloudflare.com/5xx-error-landing?utm_source=error_footer" id="brand_link" target="_blank">Cloudflare</a></span>
    
  </p>
</div><!-- /.error-footer -->


    </div><!-- /#cf-error-details -->
</div><!-- /#cf-wrapper -->
</body>
</html>

```
### Steps To Reproduce

1. open ctf.hacker101.com.
2. login to a test account .
3. you can use my account as well , 
4. NOTE: I think number of groups the test user has created should be alot (like i have around 3000+ ).
5. send the request I have pasted above with the same crafted headers .
6.observe the long delay of around 40-50 seconds and the 502 response .

7.note that if this request is sent multiple times the sever can crash (but i haven't tried it , because i am trying to practice safe testing)
Thank you
### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 * 

### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?

yes/no

## Impact

attacker can dos ctf.hacker101.com they just require an old account with nice number of groups (like mine )
Note: I stopped immediately when I observed the delay and response 502 ,I am pretty sure I can dos it even without intruder and just by opening multiple tabs in browser . but I haven't tried it yet  because I am trying to  improve myself  and practice safe testing
thank you

## Attachments
No attachments
