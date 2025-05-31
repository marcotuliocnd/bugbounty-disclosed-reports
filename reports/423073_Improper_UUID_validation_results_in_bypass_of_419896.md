# Improper UUID validation results in bypass of #419896

## Report Details
- **Report ID**: 423073
- **URL**: https://hackerone.com/reports/423073
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-12T19:18:06.645Z
- **Disclosed**: 2018-10-25T22:38:41.919Z

## Reporter
- **Username**: popeax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
This was found while evaluating the vulnerability and patch identified in #419896.  I determined the deployed patch to be effective.  However, I noticed tracer values could be sent which didn't conform to the UUID specification as characters outside of the a-f and 0-9 ranges could be used.  For example, a value such as "zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzzzz" was accepted by the server as valid.  Likely this indicates a problem with a regex filter that needs to be slightly changed.  

Steps
1. Navigate to a program which allows anonymous submissions.
2. Open the report submission form and add an attachment.
3. Observe the request sent to /attachments includes a client side generated UUID in the tracer field.
4. Replay the request from step 3.  Use an invalid UUID (e.g. "zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzzzz") for the tracer and observe the server accepts the value.

## Impact

The impact is unknown, but it is believed to have a cascading side effect.  I was asked to submit this by @jobert.

## Attachments
No attachments
