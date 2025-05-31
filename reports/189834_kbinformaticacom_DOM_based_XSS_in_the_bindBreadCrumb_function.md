# [kb.informatica.com] DOM based XSS in the bindBreadCrumb function

## Report Details
- **Report ID**: 189834
- **URL**: https://hackerone.com/reports/189834
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-09T13:44:42.532Z
- **Disclosed**: 2017-06-24T13:54:59.729Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
The ***bindBreadCrumb*** function, which is called after the document is loaded:

```javascript
$(document).ready(function () {
    bindBreadCrumb();
});
```

has the following insecure link assignments, that use non-encoded URL values:

```javascript
strChild = "<a href='" + document.URL + "' style='color:#fff !important;font-size:10px'>Search Results</a>";

strChild = "<a href='" + varCoveoSearchResultPageURL + "' style='color:#999 !important;' >Search Results</a>";

strChild = "<a href='" + varDocumentReferrer + "' style='color:#999 !important;' >Search Results</a>";

strChild = "<a href='" + varStaticCoveoSearchResultPageURL + "' style='color:#999 !important;' >Search Results</a>";
```
etc.

This gives an attacker the opportunity to inject code with Javascript there.

 
As a proof of concept let's consider the case of the referrer value injection at the https://kb.informatica.com/solution/4/Pages/7377.aspx page:

```javascript
if (qString('myk') != '') {

	var previousUrl = document.referrer.toLowerCase();

	var varCoveoSearchResultPageName = fnGetSearchPageName();

	if (previousUrl.indexOf("/home.aspx") > -1) {
	
		<...>
		
	} else {
	
	if (varCoveoSearchResultPageName != "") {
	
		<...>
		
	} else {
		
		var varDocumentReferrer = document.referrer;

		if (varDocumentReferrer != "") {
		
			if (varDocumentReferrer.toLowerCase().indexOf(fnGetKBSFDCHostName()) != -1) {
			
				var li = document.createElement("li");
				strChild = "<a href='" + varDocumentReferrer + "' style='color:#999 !important;' >Search Results</a>";
				li.innerHTML = strChild;
				document.getElementById('DynamicBreadcrumb').appendChild(li);
				
			} else {
				
				<...>
				
			}
			
		}
		else {
			
			<...>
			
		}

	}
	
	<...>

	}
}
```

As we can see, for the attack to succeed, the query string parameter **myk** must be non-empty:

```javascript
if (qString('myk') != '') {
```

the **referrer** value most not contain **/home.aspx**:

```javascript
var previousUrl = document.referrer.toLowerCase();

if (previousUrl.indexOf("/home.aspx") > -1) {

	<...>
	
} else {
```

the **CoveoSearchUrl** cookie value must be mepty:

```javascript
function fnGetSearchPageName() {
	
	var searchPageName = GetKBCookieValue("CoveoSearchUrl");
	
	if (searchPageName != "") {
		searchPageName = searchPageName.split("/").slice(-1)[0].split("?")[0];
	}
	
	return searchPageName;
}

<...>

var varCoveoSearchResultPageName = fnGetSearchPageName();

if (varCoveoSearchResultPageName != "") {

	<...>
	
} else {
```

and the **referrer** value must contain **//search.informatica.com**:

```javascript
function fnGetKBSFDCHostName() {
	
	<...>
	
	if (document.location.href.indexOf("kb.informatica.com") > -1) {
		return "//search.informatica.com"; 
	}
	
	<...>
	
}

<...>

var varDocumentReferrer = document.referrer;

if (varDocumentReferrer != "") {
		
	if (varDocumentReferrer.toLowerCase().indexOf(fnGetKBSFDCHostName()) != -1) {
```

**PoC:**

1. Open the http://spqr.zz.mu/loc.php?//search.informatica.com&'/onmouseover='alert(document.domain)'&url=https://kb.informatica.com/solution/4/Pages/17377.aspx?myk=xxx link in IE
2. Wait for the page to load and put the mouse cursor over the "Search results" link on top

The script will be executed:

{F142063}

Tested with Internet Explorer 11.447 and Microsoft Edge 38.14393.

Same for the other link assignment cases.

## Attachments
- inf_xss.png
