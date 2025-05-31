# Google API key leaked to Public

## Report Details
- **Report ID**: 1065041
- **URL**: https://hackerone.com/reports/1065041
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-12-23T09:47:26.779Z
- **Disclosed**: 2021-01-23T00:38:30.188Z

## Reporter
- **Username**: bb89e4af088379499c73f7d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fetlife

## Vulnerability Information
Hi team,

I found a bunch of endpoints that is leaking you Google Api key.
I tested the key and found it is vulnerable to Geocode Api.

List of vulnerable endpoints
https://ass0.fetlife.com 
https://ass2.fetlife.com
https://app.fetlife.com
https://ass1.fetlife.com 
https://ass3.fetlife.com 
https://fetlife.com
https://ws.fetlife.com 


**POC key:**
`AI████████DM`



**Exploit POC:**
API key is  vulnerable  for Geocode API! Here is the PoC link which can be used directly via browser:
https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AI████████DM

## Impact

costing companies extra money and in some cases DOS.

Identifies cost: $5 per 1000 request

## Attachments
No attachments
