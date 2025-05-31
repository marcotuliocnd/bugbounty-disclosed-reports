# Open redirect

## Report Details
- **Report ID**: 2957962
- **URL**: https://hackerone.com/reports/2957962
- **State**: Closed
- **Severity**: none
- **Submitted**: 2025-01-25T10:56:58.239Z
- **Disclosed**: 2025-02-06T13:12:47.114Z

## Reporter
- **Username**: p_anand1234
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
## Summary:
An open redirect vulnerability was discovered on the website https://www.xnxx.com/todays-selection/1. This issue allows attackers to modify URLs to redirect users to arbitrary external websites, including malicious or phishing sites. The vulnerability can be exploited by manipulating specific URL parameters, leading to potential phishing attacks, credential theft, or malware distribution.

## Steps To Reproduce:
1. Navigate to the following URL:https://www.xnxx.com/todays-selection/1
2. inspect the page
3. Go to this attribut:-"href="/todays-selection/2""
3. instead of the "href="/todays-selection/2"" put the "https://google.com"
4. Then browser are the redirect the page on the google.com 


## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

The open redirect vulnerability allows attackers to perform malicious redirections, leading to potential phishing attacks or malicious website access. By using this vulnerability, attackers could deceive users into clicking on harmful links that might steal credentials or compromise security.

## Recommendation:
The website should implement input validation for URLs provided in the redirection parameters, allowing only trusted domains or URLs. A whitelist of allowed domains should be enforced for redirection links to mitigate the risk of abuse.

## Attachments
- xnnx.mp4
