# Information disclosure - Feedback is accessible on Public profile even after 'disallowed' at https://hackerone.com/settings/feedback

## Report Details
- **Report ID**: 1264725
- **URL**: https://hackerone.com/reports/1264725
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-15T21:09:24.371Z
- **Disclosed**: 2021-08-03T18:43:56.405Z

## Reporter
- **Username**: brdoors3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi team,

I noticed one possible information disclosure scenario related to My Feedback managed at https://hackerone.com/settings/feedback

**Description:**

In current scenario even after uncheck the option "Show this blurb on my profile" I can access the feedback using one one  request``POST /graphql HTTP/1.1`` 

### Steps To Reproduce

1 I go to https://hackerone.com/settings/feedback 

I see one Feedback of program Legal Robot with option "Show this blurb on my profile" > I make sure that this option is not checked 

 ██████████

2 I access my account in incognito mode **not logged in any Hackerone account**

Using inspect element of browser search for ``feedback`` 

I find this request:
```
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 2218
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
accept: */*
X-Auth-Token: ----
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
content-type: application/json
Origin: https://hackerone.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://hackerone.com/brdoors3?type=user
Accept-Language: en-US,en;q=0.9
Cookie: _cfuid=8e7b0719-b897-43ac-a3c4-a1da6de0de25; _ga=GA1.2.1354168190.1626382636; _gid=GA1.2.169172629.1626382636; __Host-session=Z3ZEcTkvM2YvSFYrV0dsSUFXdnpDb0gwdXdobytBUFFDbU5WM05oWkZOTVk2U2JmZGlsUStBeGcrRWVGak5Ybm9acWI2ZU1oNGU0OTZIMlpPOGdzZTN1T1pMZzZlMjlGZ2lSV3BaRGFsNHJ2ak96Uk5PekpMRnFMVVZYL2VFYlBiVmV4TEdXdzdDQWFyV2dKWDVqZ29YdmdLZUxSczhLaDdFZFVzL1A0ZzVxL1RGOHBVUlRldVFlZ0cvUVgvV25SNjNlb1lJU2p2Z2UzeDdSRi84Y2lRK2ZlZm91aGlpSW5aUVlMSVlNeVBEOUIrNmJOZU96VFFPT1lNM1VlKzNFNHJGZG4xTlFueFdHZURjMXZheVcxYzh6ZldxcGxJN1BXb29Ba3FKd2FHK0E9LS12RzlNUnV6NUNOQ0FhcHdMaU1SS1dRPT0%3D--b9e3da4a42bb5566ca041114dd6113434d3779bf

{"operationName":"UserProfilePage","variables":{"resourceIdentifier":"brdoors3"},"query":"query UserProfilePage($resourceIdentifier: String!) {\n  me {\n    id\n    username\n    ...UserProfileSubheaderMe\n    ...UserProfileCardMe\n    ...UserStatsMe\n    __typename\n  }\n  user(username: $resourceIdentifier) {\n    id\n    username\n    name\n    intro\n    profileActivated: profile_activated\n    pentester_profile {\n      id\n      ...PentestsPentesterProfile\n      __typename\n    }\n    ...UserProfileSubheaderUser\n    ...UserProfileCardUser\n    ...CreditsUser\n    ...BadgesUser\n    ...ReviewUser\n    ...UserStatsUser\n    __typename\n  }\n}\n\nfragment UserProfileSubheaderMe on User {\n  id\n  username\n  __typename\n}\n\nfragment UserProfileSubheaderUser on User {\n  id\n  username\n  __typename\n}\n\nfragment UserProfileCardUser on User {\n  id\n  created_at\n  location\n  website\n  bio\n  name\n  username\n  profile_picture(size: large)\n  bugcrowd_handle\n  github_handle\n  gitlab_handle\n  linkedin_handle\n  twitter_handle\n  cleared\n  ...FollowUser\n  __typename\n}\n\nfragment FollowUser on User {\n  id\n  followed\n  __typename\n}\n\nfragment UserProfileCardMe on User {\n  id\n  __typename\n}\n\nfragment PentestsPentesterProfile on PentesterProfile {\n  id\n  completed_pentests_number\n  __typename\n}\n\nfragment CreditsUser on User {\n  id\n  username\n  resolved_report_count\n  thanks_item_count: thanks_items {\n    total_count\n    __typename\n  }\n  __typename\n}\n\nfragment BadgesUser on User {\n  id\n  username\n  badges(first: 3) {\n    edges {\n      awarded_at\n      node {\n        id\n        name\n        image_path\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ReviewUser on User {\n  id\n  public_reviews(first: 5) {\n    edges {\n      node {\n        id\n        public_feedback\n        team {\n          id\n          name\n          handle\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment UserStatsUser on User {\n  id\n  username\n  __typename\n}\n\nfragment UserStatsMe on User {\n  id\n  __typename\n}\n"}
```

3 send the request

Response:
```
HTTP/1.1 200 OK
Date: Thu, 15 Jul 2021 21:07:03 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: no-cache, no-store
Content-Disposition: inline; filename="response."
X-Request-Id: 2d322339-9159-4b49-88b3-0216758ad759
ETag: W/"35e4f1f253173287718c90dfc1fcd49d"
Set-Cookie: __Host-session=VFlXKzJTak9Zb2ZtUXpNdmhISDl1NFlydStpM3oxaWxmK1piU2lmeHprbHVxbUdpUk9nUWpITmtyMXg0SlhqVWF0TitTd0lWRVYxUXdEWjZoWmloVVozOHhYUDVaN3hhV09JZTAvcXhjV0VYT2kzNE1BQStkYnJBNnZXZFNxVDVmb3Nwdm1HWWpncEN6SHR0dDVEVS91QTZpVDlvb2F2QTZILytMb0xvZVpUcTR1WFlQWVdFenBxUDJjWFJWYzVGTXBSRjVudUpJeFU2bms1bklZRlVSS1JXSlBTNDBDUmFPeU9YOWVpSHVGYWdiR0c0SVoyUnlzaURZSW0rTTZONDgrL2lzSlc1VFl4VkhneU1yWUhkdFdFaDh4aGtVbXJoUkUrNStwVE9kUlU9LS1PQlRxVkpjTUZEWTFweEE5cUxVRTlnPT0%3D--640967a2e3cbce33415ccaf47fc90bbbaa94a86f; path=/; expires=Thu, 29 Jul 2021 21:07:03 GMT; secure; HttpOnly; SameSite=None
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Expect-CT: enforce, max-age=86400
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com a5s.hackerone-ext-content.com b5s.hackerone-ext-content.com; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com; media-src 'self' hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=374aea95847f4040a69f9c8d49a3a59d
CF-Cache-Status: DYNAMIC
Server: cloudflare
CF-RAY: 66f5f54a2be2f754-GRU
Content-Length: 2060

{"data":{"me":null,"user":{"id":"Z2lkOi8vaGFja2Vyb25lL1VzZXIvMTMwNDY3","username":"brdoors3","name":"Leandro Chaves","intro":"","profileActivated":true,"pentester_profile":null,"__typename":"User","created_at":"2016-12-13T17:12:06.352Z","location":"","website":null,"bio":"hi team, any update?","profile_picture":"https://profile-photos.hackerone-user-content.com/variants/000/130/467/14c08e02f02a6d8a8ae224012965f50954389546_original.jpg/3a92d35ded291cb6603c042e6805cce06895beaa6e173fbe2dd001db123414cf","bugcrowd_handle":"lccunha","github_handle":"","gitlab_handle":"","linkedin_handle":"","twitter_handle":"cecleandro","cleared":true,"followed":false,"resolved_report_count":232,"thanks_item_count":{"total_count":54,"__typename":"ThanksItemConnection"},"badges":{"edges":[{"awarded_at":"2020-05-28T08:29:44.319Z","node":{"id":"Z2lkOi8vaGFja2Vyb25lL0JhZGdlLzQ4OA==","name":"$100 Million Dollars in Bounties","image_path":"https://hackathon-photos.hackerone-user-content.com/KEPkZQmZZFyPBYAen6JTsDPR","__typename":"Badge"},"__typename":"BadgesUsersEdge"},{"awarded_at":"2020-03-31T20:09:59.153Z","node":{"id":"Z2lkOi8vaGFja2Vyb25lL0JhZGdlLzIy","name":"Diversity","image_path":"/assets/users/badges/diversity_gold-3f081a79ff0749d00cc329ce2ed66fe71e3bfe8fb0bfd24740a5d719ff13f58a.png","__typename":"Badge"},"__typename":"BadgesUsersEdge"},{"awarded_at":"2019-08-22T07:37:17.951Z","node":{"id":"Z2lkOi8vaGFja2Vyb25lL0JhZGdlLzMw","name":"Belle of the Ball","image_path":"/assets/users/badges/popular-eee04dcea8d47d18996bfa4438a6c7d365146aa0c1417350608c903fb00ec28d.png","__typename":"Badge"},"__typename":"BadgesUsersEdge"}],"__typename":"BadgesUsersConnection"},"public_reviews":{"edges":[{"node":{"id":"Z2lkOi8vaGFja2Vyb25lL0hhY2tlclJldmlldy83","public_feedback":"Clear language \u0026 video proof - excellent report.","team":{"id":"Z2lkOi8vaGFja2Vyb25lL0VuZ2FnZW1lbnRzOjpMZWdhY3kvMTYwMQ==","name":"Legal Robot","handle":"legalrobot","__typename":"Team"},"__typename":"HackerReview"},"__typename":"HackerReviewEdge"}],"__typename":"HackerReviewsConnection"}}}}
```

Note:

``"public_feedback":"Clear language \u0026 video proof - excellent report."```

{F1378277}

## Impact

My Feedback is disclosed in one endpoint at user profile even after uncheck the option 'Show this blurb on my profile' at https://hackerone.com/settings/feedback

## Attachments
- h2.JPG
