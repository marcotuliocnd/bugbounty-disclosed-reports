# Team object exposes amount of participants in a private program to non-invited users

## Report Details
- **Report ID**: 380317
- **URL**: https://hackerone.com/reports/380317
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-10T22:13:56.389Z
- **Disclosed**: 2018-07-20T17:44:07.836Z

## Reporter
- **Username**: kapytein
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello.

Similar to other reports, suddenly after the update with ordering users, the GraphQL API is exposing the amount of participants in a private program to non-invited users. This allows an attacker to retrieve the amount of participants in a private program, as well as their details.

**Description:**
Steps To Reproduce

Query, for example, ██████ via the GraphQL API. ██████ is known to have a private program running on HackerOne, and they do exist in the external directory.
```
query {
    team(handle: "█████") {
     participants { total_count  }
     about

}
}
```
You'll get the amount of participants, as well as their details if you query them. 
```
...
{ "data": { "team": {participants": { "total_count": 268 }, "about": "████" } } }
...
```

**Impact**

This leads to information disclosure. An attacker can expose the existence of a private program under the external program directory.

## Impact

This will eventually lead to information disclosure.

## Attachments
No attachments
