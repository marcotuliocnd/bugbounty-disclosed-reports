# XSS found in https://www.████████.mil

## Report Details
- **Report ID**: 2853410
- **URL**: https://hackerone.com/reports/2853410
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-11-20T08:01:52.709Z
- **Disclosed**: 2025-01-24T14:44:48.592Z

## Reporter
- **Username**: thpless
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Dear DoD Team

I found another reflected cross site script in one of your web apps. 

As a proof of concept you can use the following link.
https://www.███.mil/?code=%27;prompt(%27XSS%27);//

Best
@thpless

## Impact

Reflected XSS allows attackers to inject malicious scripts into a web application, which execute in the user's browser when triggered (e.g., via a malicious link). This can lead to theft of sensitive data like cookies, session tokens, or credentials, and may enable phishing or session hijacking. Additionally, attackers can manipulate the webpage to execute malicious actions, such as keylogging or redirecting users to harmful sites.

## System Host(s)
www.██████.mil

## Affected Product(s) and Version(s)
webserver

## CVE Numbers


## Steps to Reproduce
### PoC

https://www.████████.mil/?code=%27;prompt(%27XSS%27);//

## Suggested Mitigation/Remediation Actions
*** To prevent the execution of JavaScript code, you would need to sanitize the output (replace the character ' with \'). ***

In this case there are three injection points on the site

```html
<script type="text/javascript">

function getUnitOfAssignment() {
	var uoa = '';
/*	
	if(document.cookie) {
		var cookiearray = document.cookie.split(';');
	
		// Now take key value pair out of this array
		for(var i=0; i<cookiearray.length; i++) {
		   name = cookiearray[i].split('=')[0];
		   value = cookiearray[i].split('=')[1];
		   if(name == 'uoa') {
			   uoa = value;
		   }
		}
	}
*/	
	return uoa;
}

function processUserLogon(action) {
	if(action == 'logon') {
		var e = document.getElementById("environment");
		env = e.options[e.selectedIndex].value;
		var logonIdParam = "";
		var userTypeParam = "";
		if(document.getElementById("logonId") != null) {
			logonIdParam = "&logonId=" + document.getElementById("logonId").value;
		}
		if(document.getElementById("userType") != null) {
			var userType = document.getElementById("userType");
			userTypeParam = "&userType=" + userType.options[userType.selectedIndex].value;
		}
		
		var uoa = getUnitOfAssignment();
		
		window.location.href = 'https://' + env + '/webapp/wcs/stores/servlet/ProcessUserSSO?catalogId=10051&langId=-1&storeId=' + 10801
			+ '&sso=true&ssoAction=' + action + '&code=INJECTION_POINT' + logonIdParam + userTypeParam + '&uoa=' + uoa 
			+ '&dodaac=' + document.getElementById('dodaac').value + '&json=' + document.getElementById('json').value;
	} else {
		window.location.href = 'ProcessUserSSO?catalogId=10051&langId=-1&sso=true&ssoAction=' + action + '&code=INJECTION_POINT';
	}
}

function getCode() {
	var clientId = "fedmall";
	

	window.location.href = 'https://█████████/portal/oauth2/authorize?response_type=code&client_id=' + clientId + '&redirect_uri=https://www.████████.mil/webapp/wcs/stores/servlet/en/fedmall?sso=true';	
}
</script>
<br/>

<div class="rowContainer" id="container_SSO_UserInfo">
	<div class="row margin-true">
		<div class="col8 acol12 ccol9">
			<div id="UserInfoPageHeading" tabindex="0">
				<h2 class="userInfo_header" style="margin-bottom: 10px !important;">Processing User Sign In...</h2>
			</div>
		</div>
	</div>
</div>

<script type="text/javascript">
dojo.addOnLoad(function() {
	ra2 = "false";
	if ((document.referrer.indexOf('-ra2.') !== -1)) {
		ra2 = "true";	
	}
	
	var clientId = "fedmall";
	
	
	window.location.href = 'ProcessUserSSO?catalogId=10051&langId=-1&app='+clientId+'&ra2='+ra2+'&ssoAction=logon&code=INJECTION_POINT&uoa=' + getUnitOfAssignment();
});
</script>
```



## Attachments
No attachments
