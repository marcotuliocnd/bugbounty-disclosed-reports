# [network.informatica.com] The login form XSS via the referer value

## Report Details
- **Report ID**: 190016
- **URL**: https://hackerone.com/reports/190016
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-10T00:47:35.155Z
- **Disclosed**: 2017-05-22T04:08:13.461Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
The **referer** parameter value https://network.informatica.com/login!input.jspa?referer=%ref% is inserted into the Javascript code

```javascript
if (pageURL.indexOf("login!input.jspa?referer=") > -1 || pageURL.indexOf("login.jspa?referer=") > -1) {
	finalPageURL='%ref%';
}
```
and used in further redirection without validation:

```javascript
InfaAutoLogin.authenticateUser(response.id, finalPageURL, {
	callback:function(responseMap) {
		if(responseMap['status'] === 'success') {
			document.location = responseMap['location'];
		}
		else {
			sessionStorage.setItem('autoLoginType', responseMap['statusMsg']);
		}
	}
});
```

This means an attacker can put JS links there, which will cause script execution in the victim's browser:

1. Log into your Informatica Network account
2. Go to https://network.informatica.com/login!input.jspa?referer=javascript:alert(document.domain)

{F142238}

Tested with latest Firefox and Chrome.


## Attachments
- inf_nw_xss.png
