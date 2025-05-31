# Race Condition in Definition Votes

## Report Details
- **Report ID**: 152717
- **URL**: https://hackerone.com/reports/152717
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-21T01:01:36.034Z
- **Disclosed**: 2017-10-29T08:05:34.461Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: urbandictionary

## Vulnerability Information
There exists a race condition vulnerability in definition votes, allowing any user to artificially manipulate the number of up/down votes for a definition by making asynchronous requests to vote. A malicious user can use this method to reach any number of up or down votes for a definition.

See the attached screenshot for an example.

POC:

1. Visit any definition.
2. Intercept a vote of the definition, such as with Chrome Developer tools or BurpSuite.
3. Make the opposite vote, so you are able to vote again.
4. Copy the vote request as a curl command, and in the command line execute the command in the format (command) & (command).
4. Revisit the vote. There will now be 2 votes cast, and a negative number of the opposite votes. This can be repeated by removing your vote and executing the request again.

Please let me know if you have any questions,

Jack

## Attachments
- ub.png
