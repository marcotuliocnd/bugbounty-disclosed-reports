# Status Bar Obfuscation

## Report Details
- **Report ID**: 175701
- **URL**: https://hackerone.com/reports/175701
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-14T01:47:24.657Z
- **Disclosed**: 2016-10-15T02:42:41.841Z

## Reporter
- **Username**: ajdumanhug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

In this issue, Brave's Status Bar will show the link where the user will be redirected but after he clicks the link, he redirected to other website.

## Products affected: 

Latest Version of Brave

## Steps To Reproduce:

1. Open the HTML file
2. You will see a hyperlink of google.com, So hover your mouse.
3. See the Status Bar(located at the lower left of the browser) and you will see the link where it should be redirected
4. Now, click the hyperlink and you will be redirected to another website which is not the expected website.


## Supporting Material/References:

{F127785}


## Attachments
- test.html
- poc.png
