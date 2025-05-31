# authenticity token not verfied leads to change business name

## Report Details
- **Report ID**: 994504
- **URL**: https://hackerone.com/reports/994504
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-29T21:20:42.947Z
- **Disclosed**: 2020-10-23T14:54:08.123Z

## Reporter
- **Username**: cforu12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello security team , 
while sign up I have noticed that authenticity token is not verified leads to change info like business name
#Steps to reproduce
1- visit this url https://www.shopify.com/partners and add you mail then click on join now
2- Then fill out your data and click on create new partner account fill out the data then intercept the request with burp proxy
I have notice is that the request looks like this 
```
POST /signup HTTP/1.1
Host: partners.shopify.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://partners.shopify.com/signup
Content-Type: application/x-www-form-urlencoded
Content-Length: 690
Connection: close
Cookie: █████
Upgrade-Insecure-Requests: 1

authenticity_token=2vAI2NSYAWswz76VP5oZOX9qsoS%2BriQxAkUstj53i1xLI59byffVldnssNEjtHqZKcM%2BQ1VRq5kheL5Vibf%2FTw%3D%3D&organization%5Bbusiness_name%5D=df&organization%5Bbusiness_email%5D=cforu%2B6%40wearehackerone.com&organization%5Bwebsite%5D=&address%5Baddress1%5D=fake&address%5Baddress2%5D=&address%5Bcity%5D=cairo&address%5Bcountry_code%5D=EG&address%5Bprovince_code%5D=C&address%5Bpostal_code%5D=123&signup_profile_form%5Bprimary_revenue_intent%5D=other&signup_profile_form%5Bcustom_primary_revenue_intent%5D=bug+bounty&signup_profile_form%5Bcustom_other_platforms%5D=&signup_profile_form%5Bother_platforms%5D%5B%5D=no_platform&partner_agreement_accepted=0&partner_agreement_accepted=1
```
now generate csrf poc with burp suite and try to change the value of the ```authenticity_token``` paramter notice that here the request will go through
I have attached a video to make it easy for you

As a summary
The problem is that the ```authenticity_token``` is not properly validated and leads to change info being submitted what i was doing in the video is that i tried to change two or more chars to prove that it may be validating the length of the token I don't know actually but it works

## Impact

forcing user to change settings like business name

## Attachments
No attachments
