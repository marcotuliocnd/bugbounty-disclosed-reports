# CSRF on Periscope Web OAuth authorization endpoint 

## Report Details
- **Report ID**: 215381
- **URL**: https://hackerone.com/reports/215381
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-22T16:01:27.460Z
- **Disclosed**: 2017-07-26T23:02:48.018Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an issue in the OAuth authorization endpoint on Periscope Web. This allows a malicious 3rd party application to gain full API access to a victim's Periscope account.

#Details
Periscope has developer APIs that allow a 3rd party application to access resources on behalf of a user. The authorizion page is like this https://www.periscope.tv/oauth?client_id=█████████&redirect_uri=https://getmevo.com/oauth/periscope

It was found that the authorize endpoint does not have any protection against CSRF. The request to authorize a 3rd party application to access one's Periscope account is as follows:
```http
POST https://www.periscope.tv/oauthAuthorize HTTP/1.1
Host: www.periscope.tv
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Cookie: sid=[...]

client_id=████&redirect_uri=https%3A%2F%2Fgetmevo.com%2Foauth%2Fperiscope?abc
```
As one can see, there is no CSRF token or Origin validation.

After a 3rd party application gets the *authorization code* from *redirect_uri*, it can then exchange it for an access token.

#Impact
Since the Developer APIs are not public, I have no information what the APIs can perform. Based on the the description on the authorization page however, it looks intimidating that it has **full access** to an account.
{F170579}
At minimum, I found endpoints that allow creating a broadcast (https://public-api.periscope.tv/v1/broadcast/create), tweeting it (https://public-api.periscope.tv/v1/broadcast/publish) and deleting a broadcast (https://public-api.periscope.tv/v1/broadcast/delete).

#PoC
1. Make sure you are logged into Periscope Web (https://periscope.tv)
2. Go to http://innerht.ml/pocs/periscope-oauth-csrf/
3. You will be redirected to something like https://getmevo.com/oauth/periscope?code=abcde&state=, copy the *code* value in the parameter
4. Go to http://innerht.ml/pocs/periscope-oauth-csrf/code.php?code=abcde and replace the above code in the parameter
5. A tweet will be posted in your timeline with a broadcast

The behind the scene is:
1. Exchange *code* for *access_token* (https://public-api.periscope.tv/v1/oauth/token)
2. Create a broadcast (https://public-api.periscope.tv/v1/broadcast/create)
3. Publish it (https://public-api.periscope.tv/v1/broadcast/publish)

Note that a real attack does not require user interaction. In this PoC the manual copying of *code* is because I don't have a 3rd party Periscope application. 

#Fix
Add CSRF protection

## Attachments
- periscope-fullaccess.PNG
