# Examples directory is PUBLIC on https://████████mil, leading to multiple vulns

## Report Details
- **Report ID**: 674741
- **URL**: https://hackerone.com/reports/674741
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-15T22:24:37.289Z
- **Disclosed**: 2019-10-10T19:11:41.367Z

## Reporter
- **Username**: masonhck357
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Hello, 

In an effort to consolidate reporting. I have located 4 issues with having the Examples Directory open(my require just 1 solution to mitigate) The following URLs that show concern are the following:

1. https://█████mil/examples/servlets/servlet/SessionExample <--Will lead to Session Manipulation and potential Account Takeover

2. https://██████mil/examples/servlets/servlet/RequestHeaderExample <---Internal IP disclosure

3. https://██████████mil/examples/servlets/ <---Source Code Disclosure and an "Execute" option(did not press Execute button so I am not sure the impact of it.

4. https://████mil/examples/servlets/servlet/CookieExample <----Insecure Cookie Handling



## Step-by-step Reproduction Instructions

1. Please visit the above links
2.
3.


## Suggested Mitigation/Remediation Actions

Disable public access to the examples directory as soon as possible!

## Impact

Ordered by Highest Impact:

1. https://██████mil/examples/servlets/servlet/SessionExample <--Will lead to Session Manipulation and potential Account Takeover. Because the session is global this servlet poses a big security risk as an attacker can potentially become an administrator by manipulating its session.

2. https://██████████mil/examples/servlets/servlet/CookieExample <----Insecure Cookie Handling

3. https://███████mil/examples/servlets/ <---Source Code Disclosure and an "Execute" option

4. https://██████mil/examples/servlets/servlet/RequestHeaderExample <---Internal IP disclosure

## Attachments
No attachments
