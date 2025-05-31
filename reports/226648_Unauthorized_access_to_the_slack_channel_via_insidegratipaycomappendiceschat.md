# Unauthorized access to the slack channel via inside.gratipay.com/appendices/chat

## Report Details
- **Report ID**: 226648
- **URL**: https://hackerone.com/reports/226648
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-06T22:47:32.498Z
- **Disclosed**: 2017-05-09T13:41:58.518Z

## Reporter
- **Username**: 7h0r4pp4n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Summary
It is possible to force send invites for gratipay slack channel to arbitary email ids with no bruteforce limit. This is done by modifying the `coc` parameter to `1` in the POST data sent from https://inside.gratipay.com/appendices/chat

# Description
Sending a post request with `coc` parameter set to `1` appears to be bypassing some validation that is being done in the server. Without the same, the server responds with `Woot. Check your email` to the requests. 

**Request**
```
POST /invite HTTP/1.1
Host: gratipay-slackin.herokuapp.com
Content-Type: application/json
Content-Length: 36

{"coc":1,"email":"dobum@alienware13.com"}
```

**Response**
```
HTTP/1.1 400 Bad Request
Server: Cowboy
Connection: keep-alive
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 93
Date: Sat, 06 May 2017 22:33:39 GMT
Via: 1.1 vegur

{"msg":"You have already been invited to Slack. Check for an email from feedback@slack.com."}
```

Even though the response is a `400 Bad Request`, an invite email is received from `"Slack" <feedback@slack.com>` with the subject `Paul Kuruvilla has invited you to join a Slack team`.
Whatever the validation may be, this allows invites to be forced sent to arbitary email ids with no brute force limit.

# Steps To Reproduce
 * Send the post data with an arbitary email id
 * An invite to the gratipay slack channel `gratipay.slack.com` will be received at that email account 

# Supporting References:
  * https://gratipay.slack.com/team/dobum

## Attachments
No attachments
