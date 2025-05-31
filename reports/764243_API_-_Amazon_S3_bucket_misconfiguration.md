# API - Amazon S3 bucket misconfiguration

## Report Details
- **Report ID**: 764243
- **URL**: https://hackerone.com/reports/764243
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-25T02:31:24.148Z
- **Disclosed**: 2020-04-14T23:54:07.670Z

## Reporter
- **Username**: c37m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bcm

## Vulnerability Information
Dear, BCM Messenger 
##Description
My discovering was starting from com.bcm.messenger,
First, i trace what application send and receive from the network so i use [Frida tool](https://www.frida.re) to [bypass SSL pinning](https://medium.com/@buff3r/root-detection-ssl-pinning-bypass-with-frida-framework-31769d31723a),
Then i was able to trace application  http traffic, and since API data is not encrypted and there's nothing protect API such as token... 
that's make the `API Opened to public` .

So in this point : 
http://47.52.75.65:8080//v1/attachments/s3/upload_certification application send demand to upload image (profile image )
 Api respond with : 
```json
{"downloadUrl":"https://d3v5qmgpw891au.cloudfront.net/profile/1CDfyqYQfPRs2m1a1VSMaD89GZ63Mwu78N/7a6998d3f4ab421e9619627b33f1ce6b","fields":[{"key":"key","value":"profile/1CDfyqYQfPRs2m1a1VSMaD89GZ63Mwu78N/7a6998d3f4ab421e9619627b33f1ce6b"},{"key":"X-Amz-Credential","value":"AKIA3NG2JXZC3SY2WNXE/20191225/ap-east-1/s3/aws4_request"},{"key":"X-Amz-Date","value":"20191225T002608Z"},{"key":"X-Amz-Algorithm","value":"AWS4-HMAC-SHA256"},{"key":"Policy","value":"eyAiZXhwaXJhdGlvbiI6ICIyMDE5LTEyLTI1VDAwOjU2OjA4LjAwMFoiLAogICJjb25kaXRpb25zIjogWwogICAgeyJidWNrZXQiOiAiYmNtLWhrIn0sCiAgICBbImVxIiwgIiRrZXkiLCAicHJvZmlsZS8xQ0RmeXFZUWZQUnMybTFhMVZTTWFEODlHWjYzTXd1NzhOLzdhNjk5OGQzZjRhYjQyMWU5NjE5NjI3YjMzZjFjZTZiIl0sCiAgICBbImNvbnRlbnQtbGVuZ3RoLXJhbmdlIiwgMSwgNjcxMDg4NjRdLAogICAgeyJ4LWFtei1jcmVkZW50aWFsIjogIkFLSUEzTkcySlhaQzNTWTJXTlhFLzIwMTkxMjI1L2FwLWVhc3QtMS9zMy9hd3M0X3JlcXVlc3QifSwKICAgIHsieC1hbXotYWxnb3JpdGhtIjogIkFXUzQtSE1BQy1TSEEyNTYifSwKICAgIHsieC1hbXotZGF0ZSI6ICIyMDE5MTIyNVQwMDI2MDhaIiB9CiAgXQp9"},{"key":"X-Amz-Signature","value":"dc4f9003a5613f72ee7b13154deaa503dcc23eb233d6fb651e12b907926f86ce"}],"postUrl":"https://bcm-hk.s3.ap-east-1.amazonaws.com/"}
```
So as you can see, the bucket name is bcm-hk with <access-key-id> = `AKIA3NG2JXZC3SY2WNXE` 

By this json data  we can upload any file with any size to this bucket for (current user) .
 
##PoC :
I Write a Python3 script ( {F668054} ) make the upload file fast and easy :
USAGE : `python aws.py filename`


Chose any file with any size , the file will uploaded and encoded with base65 
Requirement : requests,json,base64,mimetypes,sys 
{F668052}

File saved in : 
https://bcm-hk.s3.ap-east-1.amazonaws.com/profile%2F14HXhz8Aef9NnH1Ubvwb5gEXUebzZjtEem%2F23a3ca622f9d4e52bc69387451580ae8

## Impact

## Risk : 
Since the registration is free, and no limit of how much account can be opened from one user (no email check , no phone check ...)  attacker or ATTACKERS  find this bucket as free cloud service they will upload what they want and share they files using your resources (in groups,in their communities  ... ) so you will get fake users or hackers.



Best regards ,
Mohamed Slamat
m.slamat@outlook.com

## Attachments
- poc_IC_bcm.png
- aws.py
