# Open redirect found on account.brave.com

## Report Details
- **Report ID**: 1338437
- **URL**: https://hackerone.com/reports/1338437
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-13T11:49:20.448Z
- **Disclosed**: 2022-06-30T17:47:12.485Z

## Reporter
- **Username**: tabaahi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## What is open redirect
A web application accepts a user-controlled input that specifies a link to an external site, and uses that link in a Redirect. This simplifies phishing attacks.
An http parameter may contain a URL value and could cause the web application to redirect the request to the specified URL. By modifying the URL value to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials. Because the server name in the modified link is identical to the original site, phishing attempts have a more trustworthy appearance.

## Step to reproduce
visit https://account.brave.com//example.com/%2F.. you will redirect to example.com

## POC
{F1446362}

## Fix / prevention
You can prevent redirects to other domains by checking the URL being passed to the redirect function. Make sure all redirect URLs are relative paths – i.e. they start with a single / character. (Note that URLs starting with // will be interpreted by the browser as a protocol agnostic, absolute URL – so they should be rejected too.)

If you do need to perform external redirects, consider whitelisting the individual sites that you permit redirects to.

## Impact

One of the main uses for this vulnerability is to make phishing attacks more credible and effective. When an Open Redirect is used in a phishing attack, the victim receives an email that looks legitimate with a link that points to a correct and expected domain.

Let me know if you have any questions.

thanks & best regards

## Attachments
- bandicam_2021-09-13_17-18-26-482.mp4
