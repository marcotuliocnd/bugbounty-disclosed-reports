# Admin Login Credential Leak for DoD Gitlab EE instance

## Report Details
- **Report ID**: 799898
- **URL**: https://hackerone.com/reports/799898
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-19T16:44:42.418Z
- **Disclosed**: 2020-05-14T17:44:38.871Z

## Reporter
- **Username**: daehee
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary

A DoD employee/contractor exposed the ███ password in a GitHub repository ([█████████](https://█████)) leading to full ███ access in a DoD DISA-associated private Gitlab EE instance (`███`).

## Description

The IP address `████` recently hosted the subdomain `█████████` (as of 2019-09-23). 

██████

Now `port 80` points to a private Gitlab Enterprise Edition instance. The current hostname is `██████` and the TLS certificate points to `████`.

```
HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Tue, 18 Feb 2020 12:30:01 GMT
Content-Type: text/html
Content-Length: 162
Connection: keep-alive
Location: https://████:443/
```

Going to `https://██████████/explore` shows no projects, groups, or snippets exposed publicly.

However, a Github search for `█████████` as displayed in the TLS certificate leads to a few interesting code commits. This commit  ([████████](https://██████████)) for a project titled "██████ (█████)" contains █████ credentials for a particular Jenkins instance.

```
- name: JENKINS_OC_USER
value: ███████
- name: JENKINS_OC_PASSWD
value: ████████
```

The default Gitlab EE username `████████`  with the password `██████`, as shown in GitHub commit, gains full █████████istrative access.

After confirming valid login, I made no further attempts to escalate privileges on the machine, nor attempted deeper access into the private contents of this Gitlab EE instance. 

## Suggested Mitigation/Remediation Actions

In addition to updating security credentials to this Github commit, you might want to review any other DoD applications that are possibly using the same password.

### Other

In addition to updating ██████ credentials for this Gitlab EE application, you might want to review any other DoD applications that are possibly using the same password.

## Impact

Exploited by a malicious actor, the security impact of this leak could include:

* Leverage valid credential to gain access to other DoD applications
* View sensitive source code in private repositories
* Access potential secret tokens, API keys, passwords contained in source code
* Change user information
* Access other user accounts
* Create new unauthorized repositories
* Host malicious content

## Attachments
No attachments
