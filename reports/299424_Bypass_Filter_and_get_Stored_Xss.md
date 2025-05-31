# Bypass Filter and get Stored Xss 

## Report Details
- **Report ID**: 299424
- **URL**: https://hackerone.com/reports/299424
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-12-19T18:18:30.760Z
- **Disclosed**: 2018-12-12T17:50:32.678Z

## Reporter
- **Username**: dr_dragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Description

Shopify allows developers to create a special type of application called a "Sales Channel". Developers are allowed to upload a 16x16 SVG "Navigation Icon" for their app provided the SVG follows the design guidelines which limits the allowed elements and attributes. For some reason when the SVG contains an XML entity this whitelist is no longer enforced allowing the developer to include malicious attributes such as onload. By uploading a malicious SVG a developer can obtain XSS on both partners.shopify.com, as well as any the admin panel of any shop which has authorized the sales channel.

# Proof of Concept

This is relatively easy to reproduce, first create a new application within the Partners dashboard then navigate to "Extensions" -> "Sales channel" to convert the application. After saving those changes a new field within the "App info" section titled "Navigation icon". Upload the following SVG:

```
<svg><!--?php "--><script>confirm(20)</script>?&gt;</svg>
```

## Impact

An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page. For more details on the different types of XSS flaws

## Attachments
- xss.JPG
