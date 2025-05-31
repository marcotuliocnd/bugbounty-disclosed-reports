# Header modification results in disclosure of Slack infra metadata to unauthorized parties

## Report Details
- **Report ID**: 727330
- **URL**: https://hackerone.com/reports/727330
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-01T08:49:07.107Z
- **Disclosed**: 2021-06-09T02:21:07.522Z

## Reporter
- **Username**: showuon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
I found *files.slack.com* domain will honor the **X-Forwarded-Host** header, instead of host header. Although file.slack.com has host validation to return 500 Internal server error when host is not files.slack.com, I can bypass the validation by appending @ at the end of host name. Also, the server will send request to the host in X-Forwarded-Host. And, we can see the server sent request is not the front end server (not from cloudfront.net), it is from the back end server(from amazonaws.com). So, with the blind SSRF vulnerability, the attackers can send arbitrary requests to the intranet, ex: port scanning by identifying the response delay time, to know 169.265.169.254:443 is closed, 169.265.169.254:80 is opened...and so on.

**Reproduce steps:**

1. upload a file onto the slack, find the original image path via Open original. Intercept this original path (i.e. https://files.slack.com/files-pri/TNXC4JD70-FPSL307RB/test.png) on burp suite
2. Send to repeater, make sure it works fine by clicking send directly
3. Add a header X-Forwarded-Host: xxx.com, make sure server returned 500 error
{F623016}

4. Update header to X-Forwarded-Host: files.slack.com@YOUR_DOMAIN, make sure server response with 302, and the location is YOUR_DOMAIN/files-pri/....
{F623017}

5. Make sure the request did sent to your domain, and the server is from xxx.amazonaws.com
6. change *YOUR_DOMAIN* into intranet ip, ex: 169.254.169.254:PORT, change the port to check the response delay time.

Here's the demo video: https://youtu.be/j5_WicLwwC4

## Impact

With the blind SSRF vulnerability, the attackers can send arbitrary requests to the intranet, ex: port scanning by identifying the response delay time. To mitigate it, the server should always honor the **Host** header, not others. Thank you.

## Attachments
- web_cache_500_error.png
- web_cache_poisionable_result.png
