# Unprotected Api EndPoints

## Report Details
- **Report ID**: 511536
- **URL**: https://hackerone.com/reports/511536
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-18T12:22:37.952Z
- **Disclosed**: 2019-03-21T17:38:02.468Z

## Reporter
- **Username**: kaushalag29
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
## Summary:
I am able to automate the get/post requests of the following api end-points with a python script which can lead to heavy load to server resulting in dos attack or buffer overflow.
/internal_api/v0.2/getSuggestedProjects
/internal_api/v0.2/getLanguages
/internal_api/v0.2/getLoggedInUser
/internal_api/v0.2/getSecuritySettings
/internal_api/v0.2/getActiveOAuthGrants
/internal_api/v0.2/getAccountEmails
/internal_api/v0.2/getExternalAccounts
/internal_api/v0.2/getAuthenticationProviders
/internal_api/v0.2/getActivePRIntegrations
/internal_api/v0.2/getProjectLatestStateStats
/internal_api/v0.2/getBlogPosts
/internal_api/v0.2/setUsername
/internal_api/v0.2/savePublicInformation

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Create an account  lgtm-com.pentesting.semmle.net.
  2. Get The cookie and nonce value of your logged in session by intercepting post/get requests with burpsuite.
  3. Use the cookie and nonce value in dos.py script(attached) inorder to execute endless api calls.
  4.Watch Video Attached as POC. 

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
Video and Script is attached.

  * [attachment / reference]

## Impact

Leading to heavy load on server that can lead to dos attack or buffer overflow using post requests with no rate limit restriction.

## Attachments
- dos.py
- Kazam_screencast_00001.mp4
- Kazam_screencast_00000.mp4
