# Real Time Error Logs Through Debug Information

## Report Details
- **Report ID**: 503283
- **URL**: https://hackerone.com/reports/503283
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-28T11:01:26.220Z
- **Disclosed**: 2019-04-11T09:15:29.815Z

## Reporter
- **Username**: rubaljain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
**Summary**: During the assessment, I have found the debug URL on slackb.com which is disclosing the World Wide real time error logs of Slack users.

The information leaked includes the following:
1. User Device Information
2. Redacted Token
3. Client IP Address
4. Description
5. Session ID
6. Team ID
7. User ID
8. User Agent
9. Server Response
10. Timestamp
11. api_call
12. x-amz-cf-id
13. x-amz-id-2

And other user sensitive information.

**Steps to Reproduce**

Open below URL in browser and refresh it to see real time logs.

https://slackb.com/debug

The vulnerable domain here is slackb.com. I have confirmed this with Slack to report this on Hackerone and mention the vulnerable domain.

## Impact

By exploiting this vulnerabiliti​y, an attacker can dump the real-time logs and information gained through this is critical which includes the team ID, user ID and redacted token which allows attackers to gather information which can be used later in the attack lifecycle, in order to achieve more than they could if they didn’t get access to such information.

## Attachments
No attachments
