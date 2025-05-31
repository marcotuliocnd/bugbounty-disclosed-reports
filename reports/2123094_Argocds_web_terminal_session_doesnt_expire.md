# Argocd's web terminal session doesn't expire

## Report Details
- **Report ID**: 2123094
- **URL**: https://hackerone.com/reports/2123094
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-25T05:24:05.809Z
- **Disclosed**: 2023-09-09T13:15:30.125Z

## Reporter
- **Username**: bean-zhang
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The vulnerability is that  web terminal sessions do not expire, even if the argocd's web session has expired.

Step 1: Log in to ArgoCD.

Step 2: Open a web terminal session in ArgoCD, which is used to operate a machine.

Step 3: Wait until the web session expires, but the web terminal session does not expire.

## Impact

All versions of Argo CD starting from v2.6.0 have a bug where open web terminal sessions do not expire. This bug allows users to send any websocket messages even if the token has already expired. The most straightforward scenario is when a user opens the terminal view and leaves it open for an extended period. This allows the user to view sensitive information even when they should have been logged out already.

## Attachments
- argocd-web-based-terminal-JWT.mp4
