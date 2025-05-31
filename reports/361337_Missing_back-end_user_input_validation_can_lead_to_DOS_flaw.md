# Missing back-end user input validation can lead to DOS flaw

## Report Details
- **Report ID**: 361337
- **URL**: https://hackerone.com/reports/361337
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-06-03T13:28:49.737Z
- **Disclosed**: 2018-06-05T12:13:33.373Z

## Reporter
- **Username**: zuh4n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hello Team,

Usually such kind of reports are out of scope, however I still would like to report you the business logic weakness that should be eliminated, at least from my point of view. Due to missing user input validation it is can lead to application unavailability.

**_Details:_**
During brief review of Liberapay application I have noticed that under 'Profile' page it's allowed to change username + name data. The first thing that caught my eye - "Name (optional) Maximum length is 64 `<input name="public_name" class="form-control" value="zzzzz" maxlength="64" placeholder="Name">`". It means that application has front-end user input validation, but what about back-end?

In case when the user exceeds the specified limit, the application server will return a response with the following status: 400 Bad Request + entire string that was inserted by user. Having this information in mind it was decided to check how the application server will handle the POST request that contains 100, 500, 10000, ... public_name value length.

In my case I simply changed the `maxlength` value directly at the DOM.

**_PoC:_**
The usual response time for valid request is about ~150-200ms (65 public_name value length)
{F304705}

This one for 500 public_name value length
{F304706}

This one for 10000 public_name value length
{F304707}

This one for 15000 public_name value length
{F304708}

**_Remediation:_**
- The recommendation here is simple, before sending an actual processing request - the application need to double check the content-length at back end. _All_ user input input should be validated at back-end.

## Impact

This surface is a good base for a planning a DDoS attack Liberapay with a small bot-net asset, i.e. small number of machines may cause a consuming of server's RAM.

## Attachments
- 65_chars.jpg
- 500_chars.jpg
- 10000_chars.jpg
- 15000_chars.jpg
