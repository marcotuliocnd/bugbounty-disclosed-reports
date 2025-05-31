# Denial of Service  [Chrome]

## Report Details
- **Report ID**: 921286
- **URL**: https://hackerone.com/reports/921286
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-11T21:51:46.289Z
- **Disclosed**: 2020-07-24T20:00:58.923Z

## Reporter
- **Username**: asdasdasdasdasda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi Team,

**Summary:**
I encountered such an error while creating a new account:
{F903872}
But I don't remember where I found this last point. I remember only when I was a new member.
I created a url using the load **%xx** as in #500686 reports as follows.
`https://twitter.com/i/flow/%00`

I got a result like the #903740 report I just sent you:
{F903873}

But this time only Chrome works. I haven't figured out why this DoS was triggered yet.
 I will keep you updated when I find new findings.

Thanks!
@cyanpiny

## Impact

An attacker could apply this DoS to any Twitter account or popular tag. It prevents a large audience or target user from accessing Twitter from the browser.

## Attachments
- 1.jpg
- 2.jpg
