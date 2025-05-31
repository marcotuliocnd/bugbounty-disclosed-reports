# Mismatch between frontend and backend validation via `ban_researcher` leads to H1 support and hackers email spam

## Report Details
- **Report ID**: 808755
- **URL**: https://hackerone.com/reports/808755
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-02T14:41:30.367Z
- **Disclosed**: 2020-05-15T17:10:04.821Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
We found a mismatch between the frontend and backend validation when using the ban researcher feature, available for program customer.

**Description:**
When a program customer issues a ban, an automatic email will be send both to the banned user and H1 support. The problem is that fronted will not allow us to make the request again as the button will be inactive. However the backend allows us to repeat the request many times. Thus, we can send a lot of messages to the banned user and to the H1 platform (moderators), although this should only be allowed once . This report is similar #156948 and #159512 where @andrewone says : `it does demonstrate a disconnect between our frontend and backend validation, which should not happen in the first place.`

## Steps To Reproduce:

1) As the user we want to ban, submit a test report
2) As a manager of the program, go to the report and click `report abuse` => click `ban reporter`
3) Intercept the request

https://hackerone.com/reports/808343/ban_researcher

POST:
X-CSRF-Token: you_token_:)`

message_to_hackerone=test"><h1>asd&message_to_researcher=test"><h1>asd

3.1) After `ban report` , We will see an inactive button
{F734385}

4) Re-issue the request multiple times
5) As the banned user, check your inbox - you should have received multiple emails, as the support did.

Thanks, @haxta4ok00

## Impact

Spam banned users and H1

## Attachments
- disabled_button.png
