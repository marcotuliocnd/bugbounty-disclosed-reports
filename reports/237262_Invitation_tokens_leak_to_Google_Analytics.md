# Invitation tokens leak to Google Analytics

## Report Details
- **Report ID**: 237262
- **URL**: https://hackerone.com/reports/237262
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-06T14:44:07.247Z
- **Disclosed**: 2017-07-16T16:41:58.418Z

## Reporter
- **Username**: h33tjev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,

While testing i have noticed that , the hackerone invitation token gets exposed to google-anaytics.com

How?

Here look at the photo-
████████

We can see that the request payload is exposing the invitation token and its not filtered like this one-

███████

And this is what google does with their request payload-

███████

So that means h1 is giving away invitation tokens to third party apps and letting them store it.

If i missed something ask me before closing the report

And requesting you to check this report- #237201

That report is about exposing private programs with valid POC

## Attachments
No attachments
