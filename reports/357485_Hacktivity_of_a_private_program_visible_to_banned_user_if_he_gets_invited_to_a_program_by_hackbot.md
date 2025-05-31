# Hacktivity of a private program visible to banned user if he gets invited to a program by hackbot

## Report Details
- **Report ID**: 357485
- **URL**: https://hackerone.com/reports/357485
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-25T15:02:57.212Z
- **Disclosed**: 2018-06-27T05:38:36.959Z

## Reporter
- **Username**: parth
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
The hacktivity of a private program is visible to banned user if he gets invited to a program by hackbot.
**Description:**
Back in 2016 i was banned by █████'s private program ( ███ ) due to some conflict between me and their security team, i think they manually put me in banned users list, but few months back i was invited to █████████'s Program by Hackbot in the occasional invites HackerOne sends and i accepted it. But still i am not able to access their program which obviously i shouldn't as i am banned by their security team, but today i noticed in Hacktivity that i am still able to view the reports they have closed.
████
While going to ██████████ still shows me `Page not found` : 

██████

Also in my profile's `whitelisted_team_ids` i can see the team id of ██████████ `████`
#Also i am able to make the following requests : 

## 1) Get Complete Hacktivity of program : 
###Request : 
```
GET /hacktivity?sort_type=latest_disclosable_activity_at&page=1&filter=type%3Aall%20to%3A██████████&range=forever HTTP/1.1
Host: hackerone.com
Connection: close
Accept: application/json, text/javascript, */*; q=0.01
X-CSRF-Token: REDACTED
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
Content-Type: application/json
DNT: 1
Referer: https://hackerone.com/REDACTED/hacktivity
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: REDACTED
```
###Response :
```
HTTP/1.1 200 OK
Date: Fri, 25 May 2018 14:30:37 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Disposition: inline; filename="response.json"
X-Request-Id: 17dafd21-a2e3-42c5-b046-e061da2a283c
Set-Cookie: REDACTED
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Expect-CT: enforce, max-age=86400
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self' hackerone-attachments.s3.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare
CF-RAY: 4208b363780d8a7f-BOM
Content-Length: 17633

████████
```

##2) In Scope Items / Assets
###Request :
```
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 1250
Accept: */*
X-Auth-Token: REDACTED
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
Origin: https://hackerone.com
Content-Type: application/json
DNT: 1
Referer: https://hackerone.com/REDACTED
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: REDACTED

{"query":"query Team_assets($first_0:Int!,$first_1:Int!) {\n  query {\n    id,\n    ...F0\n  }\n}\nfragment F0 on Query {\n  me {\n    _membership3abeOl:membership(team_handle:\"██████\") {\n      permissions,\n      id\n    },\n    id\n  },\n  _team3p4BfA:team(handle:\"███\") {\n    handle,\n    _structured_scopes2tadtg:structured_scopes(first:$first_0,archived:false) {\n      max_updated_at\n    },\n    _structured_scopes2tzyk4:structured_scopes(first:$first_1,archived:false,eligible_for_submission:true) {\n      edges {\n        node {\n          id,\n          asset_type,\n          asset_identifier,\n          rendered_instruction,\n          max_severity,\n          eligible_for_bounty\n        },\n        cursor\n      },\n      pageInfo {\n        hasNextPage,\n        hasPreviousPage\n      }\n    },\n    _structured_scopes1j7lgN:structured_scopes(first:$first_1,archived:false,eligible_for_submission:false) {\n      edges {\n        node {\n          id,\n          asset_type,\n          asset_identifier,\n          rendered_instruction\n        },\n        cursor\n      },\n      pageInfo {\n        hasNextPage,\n        hasPreviousPage\n      }\n    },\n    id\n  },\n  id\n}","variables":{"first_0":100,"first_1":50}}
```
###Response :
```
HTTP/1.1 200 OK
Date: Fri, 25 May 2018 14:44:40 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Disposition: inline; filename="response."
X-Request-Id: 9c159688-f22b-4f74-89ef-73df5e85a2f3
Set-Cookie: REDACTED
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Expect-CT: enforce, max-age=86400
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com b5s.hackerone-ext-content.com; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self' hackerone-attachments.s3.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare
CF-RAY: 4208c802e9c88aa3-BOM
Content-Length: 5292

████████
```

##3) Program Updates
###Request : 
```
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 496
Accept: */*
X-Auth-Token: REDACTED
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
Origin: https://hackerone.com
Content-Type: application/json
DNT: 1
Referer: https://hackerone.com/REDACTED/updates
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: REDACTED

{"query":"query Team_posts($first_0:Int!) {\n  query {\n    id,\n    ...F0\n  }\n}\nfragment F0 on Query {\n  _teamhn8Kp:team(handle:\"█████████\") {\n    _posts3y3M77:posts(first:$first_0) {\n      total_count,\n      edges {\n        node {\n          id,\n          created_at,\n          markdown_message,\n          title\n        },\n        cursor\n      },\n      pageInfo {\n        hasNextPage,\n        hasPreviousPage\n      }\n    },\n    id\n  },\n  id\n}","variables":{"first_0":100}}
```
###Response :
```
HTTP/1.1 200 OK
Date: Fri, 25 May 2018 14:33:25 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Disposition: inline; filename="response."
X-Request-Id: 19e8ac92-8663-49b9-a614-a80e01b8d2df
Set-Cookie: REEDACTED
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Expect-CT: enforce, max-age=86400
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com b5s.hackerone-ext-content.com; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self' hackerone-attachments.s3.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare
CF-RAY: 4208b7850b348aa9-BOM
Content-Length: 240

████████
```

## Impact

As hackerone is sending lot of invites these days so it is possible that the users a program banned get invites by hackbot, hackbot shouldn't send invites to users who are in the banned list of program whose invite is being sent to the hacker and/or the above endpoints should check if the user is in program ban list.

___Regards,
Parth :)___

## Attachments
No attachments
