# Open redirect on "Unsupported browser" warning

## Report Details
- **Report ID**: 1977222
- **URL**: https://hackerone.com/reports/1977222
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-08T15:24:16.321Z
- **Disclosed**: 2023-06-22T06:54:21.862Z

## Reporter
- **Username**: akshayravic09yc47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello team,
The below mentioned source code is using a unsanitized URL redirection mechanism which will cause open redirection vulnerability

```
			const urlParams = new URLSearchParams(window.location.search)
			if (urlParams.has('redirect_url')) {
				const redirectPath = Buffer.from(urlParams.get('redirect_url'), 'base64').toString() || '/'
				window.location = redirectPath
				return
			}
```
The `UnsupportedBrowser.vue` component used to display a message to users of unsupported browsers. If the user's browser is unsupported, it will display a message with an icon and a button to continue browsing with the unsupported browser.The script checks if there is a query parameter called `redirect_url` in the query string. If the parameter is present, it decodes the value of the parameter from base64 and then redirects the user to the decoded URL and it does not validate the decoded URL or check whether it is a trusted URL before redirecting the user. This makes it possible for an attacker to construct a malicious URL that includes the `redirect_url` parameter and a URL of their choice. When a user clicks on the link, the script will decode the value of the `redirect_url` parameter and redirect the user to the attacker's URL

#Vulnerable Source Permalink:
https://github.com/nextcloud/server/blob/master/core/src/views/UnsupportedBrowser.vue#L140-#L146

#Mitigation:
- Use any functions that check if the input of the `redirect_url` parameter and ensure that it is a trusted URL before redirecting the user.
- Add a Link warning popup like hackerone do, proceed redirection only when user accept the conditions, example like this:

{F2340720}

## Impact

If the app does not validate untrusted user input, an attacker could supply a URL that redirects an unsuspecting victim from a legitimate domain to an attacker's site.

## Attachments
- Screenshot_2023-05-08_at_8.48.54_PM.png
