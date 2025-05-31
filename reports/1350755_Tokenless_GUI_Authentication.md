# Tokenless GUI Authentication

## Report Details
- **Report ID**: 1350755
- **URL**: https://hackerone.com/reports/1350755
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-24T21:19:56.251Z
- **Disclosed**: 2021-11-04T20:09:05.966Z

## Reporter
- **Username**: seanland
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
A person has the ability to bypass the login screen using the 401 error code produced from a failed token login.  The user is given the privileges of an system:anonymous user. 

## Kubernetes Version:
kubectl, kubeadm, kubelet 1.22.2
Ubuntu 20.04.3 - 64bit

## Component Version:
Dashboard v2.3.1+0.g8d9f8e76c

## Steps To Reproduce:

  1. Attempt to log in with a token (just put in gibberish)
  2. Cut and paste the entire 401 authentication error starting from the back, forwards.
  3. Paste the 401 error into the token password field 
  4. Hit enter to Submit

## Supporting Material/References:
Please refer to the demonstration.

## Impact

The user is given the privileges of an system:anonymous user and access to the GUI.

## Attachments
- recording-1632518357039.webm
