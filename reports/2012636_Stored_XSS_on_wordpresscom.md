# Stored XSS on wordpress.com

## Report Details
- **Report ID**: 2012636
- **URL**: https://hackerone.com/reports/2012636
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-05T00:56:43.440Z
- **Disclosed**: 2023-06-26T15:49:29.173Z

## Reporter
- **Username**: riadalrashed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hello team,
I found a Stored XSS vulnerability in WordPress.com via app.crowdsignal.com. It is similar to report #1987172.

## Platform(s) Affected:
wordpress.com

1 .Go to https://app.crowdsignal.com/dashboard and create a poll.
2. Enter the following payload as an answer: "style="position:fixed;top:0;left:0;border:999em solid green;" onmouseover="alert(document.cookie)"
3. Go to "Share Your Poll" and copy the link.
4. Navigate to https://wordpress.com/posts and add a new post.
5. Include the copied link in the post.
6. Save the post.
7. Open the page and click on "View Results."
8. The XSS vulnerability will be triggered.

████

## Impact

The attacker can use this issue to execute malicious script code in the victim user browser also redirect the victim user to malicious sites

## Attachments
No attachments
