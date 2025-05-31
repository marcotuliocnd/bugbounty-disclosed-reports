# Stored XSS from Display Settings triggered on Save and viewing realtime search demo

## Report Details
- **Report ID**: 156387
- **URL**: https://hackerone.com/reports/156387
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-03T23:24:17.569Z
- **Disclosed**: 2016-09-07T08:34:23.049Z

## Reporter
- **Username**: ctee
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Here are the steps to trigger the XSS:

1. Create a JSON record that will contain the following attribute:
     **{"<img src=1 onerror=alert(document.domain)>": "XSS attribute"}**

2. Go to  **Indices -> Display** and select the attribute **<img src=1 onerror=alert(document.domain)>** under **Attributes for Faceting** and click save. 

3. Note that XSS is triggered multiple times on that page.

4. XSS  is now triggered on **https://www.algolia.com/explorer#?index=index_name** as it also shows the attribute.

5. Create a public UI Demo and to the public url, xss is triggered. I've created a demo url:  https://www.algolia.com/realtime-search-demo/xsstest


## Attachments
- facetattribute.png
- public_page_xss.png
