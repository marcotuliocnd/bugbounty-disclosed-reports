# Authenticated but unauthorized users may enumerate Application names via the API

## Report Details
- **Report ID**: 1916583
- **URL**: https://hackerone.com/reports/1916583
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-03-24T08:50:46.704Z
- **Disclosed**: 2023-05-25T19:49:06.641Z

## Reporter
- **Username**: bean-zhang
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
All versions of Argo CD starting with v0.5.0 are vulnerable to an information disclosure bug allowing unauthorized users to enumerate application names by inspecting API error messages. 

STEPS:
1. Login argocd with a user who has not application module's priviledge.
2. The user request 'api/v1/application/**/logs' restful api to download a log file.
3. The log file's content lead a information disclosure bug, which allowing unauthorized users to enumerate application names by inspecting API error messages. The error messages like 'error gettingg applicaiton by name: ** not found'.

## Impact

An attacker could use the discovered application names as the starting point of another attack. For example, the attacker might use their knowledge of an application name to convince an administrator to grant higher privileges (social engineering).

## Attachments
- argocd-application_enum_issue.mp4
