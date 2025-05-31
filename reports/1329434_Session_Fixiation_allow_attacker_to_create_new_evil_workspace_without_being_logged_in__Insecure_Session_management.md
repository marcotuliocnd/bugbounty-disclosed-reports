# Session Fixiation allow attacker to create new evil workspace without being logged in [ Insecure Session management  ]

## Report Details
- **Report ID**: 1329434
- **URL**: https://hackerone.com/reports/1329434
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-03T07:17:25.801Z
- **Disclosed**: 2021-09-16T17:32:06.627Z

## Reporter
- **Username**: basant0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trycourier

## Vulnerability Information
Hello,
How are you, hope you are doing great in this pandemic.  While testing again for the session management related bugs in your application, i found some session related issue where evil person can easily create new workspace from victims account without being logged in, that mean the session of the account is not properly managed and not expiring properly. Once the attacker capture while creating new workspace account , it can be used even after workspace admin completely logged out from his account. 

I looked other place for similar issues but i'm getting 500 Server error which is great patch. 

```java script
HTTP/2 500 Internal Server Error
Content-Type: text/plain; charset=utf-8
Content-Length: 21
Date: Fri, 03 Sep 2021 06:33:49 GMT
X-Amzn-Requestid: ece1b8ef-c45a-4ea8-955d-26e98e8a4308
X-Amzn-Remapped-Content-Length: 21
X-Amz-Apigw-Id: FEs4MGmEoAMF0ng=
X-Amzn-Trace-Id: Root=1-6131c1cd-33c2fcec7004102e0f866113
X-Cache: Error from cloudfront
Via: 1.1 f796d609ac1c79ad0a05543b9f9cb557.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: MAA51-C2
X-Amz-Cf-Id: g8M22dhNs2AUTGjA2Dx8yhgTt9x-SF3DXlcGK17Ac7I384cVyQtgkA==

Internal Server Error
```
but i think you missed something here to fix, We can easily create new workspace even after logged out from account, session still active and won't expiring properly and instantly. Which is definitely an issue and appeal you to fix :)

#STEP TO REPRODUCE:
[1]. First logged in to your account 
[2]. Fire up your burp-suite proxy and intercept the request while creating new workspace account
[3]. Now send the intercepted request to the repeater and drop the intercepted request
[4]. Click to the log out, and logged out from your account.
[5]. go to the burp repeater and send previous intercepted request. Instead of getting 500 Server error you will get something like 
```java script
HTTP/2 200 OK
Content-Type: application/json
Content-Length: 104
Date: Fri, 03 Sep 2021 06:43:36 GMT
X-Amzn-Requestid: 5111dd10-3f7a-461e-9b6b-8100ed580193
Access-Control-Allow-Origin: *
Strict-Transport-Security: max-age=31536000;includeSubDomains;preload
X-Amz-Apigw-Id: FEuTkFb_IAMF_Tw=
X-Content-Type-Options: nosniff
X-Amzn-Trace-Id: Root=1-6131c416-06e41869071723af5a7b685c
Access-Control-Allow-Credentials: true
X-Cache: Miss from cloudfront
Via: 1.1 4a092e2e376215eb2d400d6cdb1cd2e2.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: MAA51-C2
X-Amz-Cf-Id: HmbTR1RX4OY8-CH-A2V_qJie5f2rv9NLu3E8iEUSDO6od1IN8O-g_Q==

{"id":"1860152f-3ce6-4dda-9ae6-77455cc498e6","name":"EvilCorp","welcomeTemplateId":"courier-quickstart"}
```

#I have added a video poc for you so that you can replicate the steps properly and clearly without any difficulties. 
{F1435257}


#Please let me know if you need any extra information in this  :) Thank you

## Impact

Sessions are not expiring properly which creates session management issue and allow attacker to create new evil workplace without logged in.

## Attachments
- __Session_Fixiation_Issue___Without_logged_in_there_is_possible_to_create_new_workplace.mp4
