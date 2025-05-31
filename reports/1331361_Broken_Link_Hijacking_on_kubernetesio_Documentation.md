# Broken Link Hijacking on kubernetes.io Documentation

## Report Details
- **Report ID**: 1331361
- **URL**: https://hackerone.com/reports/1331361
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-09-06T17:19:27.800Z
- **Disclosed**: 2021-11-06T18:04:26.463Z

## Reporter
- **Username**: codermak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Kubernetes docs has Spanish translation available. One of the page of spanish doc has an external reference to a confluence page.
The confluence account was not registered on Atlassian.
So I was able to takeover the page and host the PoC

## Kubernetes Version:
NA

## Component Version:
NA

## Steps To Reproduce:

  1. Go to https://kubernetes.io/es/docs/concepts/workloads/controllers/daemonset/
  2. Search for `Sysdig Agent`
  3. Click on the atlassian link next to that text
  4. You will be redirected to `https://sysdigdocs.atlassian.net/wiki/spaces/Platform),/overview`
  5. Now try opening the confluence account with this url https://sysdigdocs.atlassian.net/wiki/spaces/TAKEOVER/overview
  6. You will see the takeover message

## Supporting Material/References:

- https://sysdigdocs.atlassian.net/wiki/spaces/TAKEOVER/overview

{F1438785}

## Impact

As an attacker, I can host malicious content on the confluence page to misguide the user.
I can also, host details about installing malicious sdk or softwares, which user will think is part of the deployment docs as its referreded in kubernetes.io, this can lead to RCE for users who are referring to this doc

## Attachments
- Screenshot_from_2021-09-06_22-47-49.png
