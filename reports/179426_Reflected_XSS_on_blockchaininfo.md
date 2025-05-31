# Reflected XSS on blockchain.info

## Report Details
- **Report ID**: 179426
- **URL**: https://hackerone.com/reports/179426
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-11-01T16:53:12.047Z
- **Disclosed**: 2017-03-06T16:08:43.220Z

## Reporter
- **Username**: kasperkarlsson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: blockchain

## Vulnerability Information
The application at https://blockchain.info is vulnerable to reflected XSS/HTML injection through the URL at the block-index page.

Proof of concept
===
The following PoC contains the payload `"><h1>XSS here` which displays the text in heading size.
https://blockchain.info/en/block-index/1160457/%22%3E%3Ch1%3EXSS%20here
Another example with some scrolling text `"><marquee>XSS here`:
https://blockchain.info/en/block-index/1160457/%22%3E%3Cmarquee%3EXSS%20here

Print screens from the two PoCs above are attached to this report. This was tested using Mozilla Firefox 49.0.2 and Google Chrome 54.0.2840.71.

Due to the strict Content Security Policy which even blocks 'self', arbitrary javascript cannot be executed through this vulnerability without some CSP bypass. Great! :)

Recommended solution
===
Make sure to properly encode the last part of the URL before printing it to the page. Another possible solution is to make sure the URL matches a strict whitelist regexp, so that this part of the URL is not put on the page at all if it looks fishy.

## Attachments
- blockchain_info_block-index_XSS_h1_Firefox.png
- blockchain_info_block-index_XSS_marquee_Chrome.png
