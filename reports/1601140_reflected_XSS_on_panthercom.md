# reflected XSS on panther.com

## Report Details
- **Report ID**: 1601140
- **URL**: https://hackerone.com/reports/1601140
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-15T00:40:21.436Z
- **Disclosed**: 2022-07-23T05:19:50.943Z

## Reporter
- **Username**: ibrahimatix0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: panther_labs

## Vulnerability Information
## Summary:
When visiting  runpanther.io I got redirected to panther.com and the application failed to sanitise user's input resulting into HTML injection and possible XSS.

## Steps To Reproduce:

{F1774502}
  1. Go to https://panther.com/search/Users%3Ch1%3EHello,%20I%20am%3C/h1%3E%3Cfont%20color=red%3E%20Ibrahimatix0x01%3C/font%3E
  1. You will notice that HTML codes in the search form are executed by the browser.
  

## Supporting Material/References:
{F1774497}

## Impact

The vulnerability allow a malicious user to inject html tags and could possibly execute Javascript (if WAF is successfully bypassed)which could lead to steal user's session

## Attachments
- 1.png
- vokoscreenNG-2022-06-15_02-34-23.mp4
