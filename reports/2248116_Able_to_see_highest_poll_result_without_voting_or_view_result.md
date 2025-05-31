# Able to see highest poll result without voting or view result

## Report Details
- **Report ID**: 2248116
- **URL**: https://hackerone.com/reports/2248116
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-11-10T18:31:39.484Z
- **Disclosed**: 2023-11-15T21:27:16.240Z

## Reporter
- **Username**: deepblue29
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fetlife

## Vulnerability Information
Hi Fetlife, in your last blog post https://fetlife.com/releases/2023-11-10-view-poll-results-without-voting

But it seem there is a way to see the highest vote count without even without `view result` and I was able to vote later as well. And my appology, I do have a working example, but the exact mechanism I'm not go through the end - which line of code or which request does this (I'll update in comment if I find one - pressure for the first report).

This vote: https://fetlife.com/users/17704987/s/6168250076, currently have 1 vote, you could find out which vote by doing this:

1. Open Burp and proxy all http request.
2. Click `view result` and accept.

{F2848145}

Because I already intercept all request, no request actually go to fetlife server. However, I notice that, the vote number 2 light up.

{F2848148}

It is infact the vote have highest count (this is the third time I test - so it is not a fluke). I will update my investigate further if I find the root core in comment (it might be in the html).

## Impact

I was able to see which vote have the highest vote without `view result` or even `voting`. Now I know which vote is the highest - and I have not `vote` or even `view result` yet.

## Attachments
- image.png
- image.png
