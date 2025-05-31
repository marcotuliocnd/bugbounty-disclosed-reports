# DoS via large console messages

## Report Details
- **Report ID**: 1243724
- **URL**: https://hackerone.com/reports/1243724
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-06-25T01:28:09.376Z
- **Disclosed**: 2022-04-29T07:11:43.046Z

## Reporter
- **Username**: thesecuritydev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
When server console logging is enabled, it's possible to cause a complete denial of service to the server by submitting large text (>64KB) that gets output in the console log. This causes the server to become unavailable for all users.

## Steps To Reproduce:
_I set up my environment following the steps at https://developers.mattermost.com/contribute/server/developer-setup/windows-wsl/_

  1. Create a test server and team.
2. Make sure console logging is enabled in the server settings, with debug level.
  3. Visit the server via Burp Suite for the next step.
 4. Go to a channel, and type some non-existing slash command like`/command` that doesn't exist, and execute it while intercepting the request in Burp Suite.
5. You should get a POST request to `/api/v4/commands/execute` with a JSON body with a `command` value.
6. Send the request to the Repeater in Burp Suite.
7. _The vulnerability comes from the fact that if you type a non-existent command, it will log an error that includes the command you gave. There is no size limit on the command value in the API directly (only in the text box)._
8. Replace the command value with `/000000000000000000000000000000000000000000000000000000000000000...`, where you use more than ~64KB of text (66,000+ characters will do nicely). _You can copy and paste, select all, and copy-paste repeatedly to generate a large text size._
9. If you send the request with this super large payload, the server will see the command is invalid, and try to log the error message to the console. The error message contains the large payload, and **will cause the server to become unresponsive if the log message is over ~64KB** (65,535 bytes) (The size includes the rest of the error message, so the exact payload size required will be a bit less, but 66,000 bytes ensures it will always work without adding too many unnecessary characters).
10. The server will not connect now until you restart with the `make run-server` command, and will be unavailable for all users and all teams.

This only works when CONSOLE logging is enabled (file logging doesn't seem to be affected). And for this attack vector, it is required to have DEBUG logging enabled, but it might be possible to find a vector that works via a different log type.

I will say I also found another vector abusing this same issue via SQL query logging, which I will submit later depending on the status of this report. But obviously, since it requires SQL query logging to be enabled it's not as big of an issue as this one, and it has the same root cause.

## Impact

Complete Denial of Service to all users of a server. It would be trivial to execute a script that automatically sends the payload whenever the server is available, to make sure it continually crashes.

## Attachments
No attachments
