# Stored-XSS in merge requests

## Report Details
- **Report ID**: 1261148
- **URL**: https://hackerone.com/reports/1261148
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-07-14T08:06:42.416Z
- **Disclosed**: 2021-07-19T19:03:53.004Z

## Reporter
- **Username**: ba5d2d132de8622c890dd60
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Summary
As an attacker I could do XSS on Web.com because it is vulnerable Stored XSS, also known as persistent XSS, is more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application.


### Steps to reproduce
1. Go to https://gitlab.com/
2. Create a new branch with name  any of these

<form><button formaction=javascript&colon;alert(1)>CLICKME

"><img src=x onerror=alert(document.domain)>

<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=></iframe>

<iframe srcdoc="<img src=x onerror=alert(document.domain)>"></iframe>

3. Create a new merge request from the new branch to master
4. XSS is saved and if you will open the readme file and add these payloads to it it will also save these payloads




### Output of checks

This bug happens on GitLab.com

## Impact

This stored-XSS allows attacker to execute arbitrary actions on behalf of victim notably via gitlab API. The attacker can steal data from whoever checks the report.

## Attachments
- bandicam_2021-07-14_13-33-47-160.mp4
- bandicam_2021-07-14_13-26-29-234.mp4
- bandicam_2021-07-14_13-22-17-346.mp4
