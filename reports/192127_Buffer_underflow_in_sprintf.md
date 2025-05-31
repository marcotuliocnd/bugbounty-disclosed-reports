# Buffer underflow in sprintf

## Report Details
- **Report ID**: 192127
- **URL**: https://hackerone.com/reports/192127
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-18T05:30:43.743Z
- **Disclosed**: 2017-03-05T04:12:40.333Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hi,

So I found this in mruby as part of the shopify-scripts program, and I notice that my patch also landed upstream in ruby as well. Shame on me for not checking ruby as well!

Wondered if it counted for a bounty here as well?

https://github.com/mruby/mruby/issues/3347 <- issue that shopify guys opened on my behalf.
https://github.com/ruby/ruby/commit/0854193a684acc2b3a13ab28091a4397000c8822 <- commit landed upstream.

https://hackerone.com/reports/191328 (still open so not public) is the original report of mine.

Let me know if you need anything more.

Cheers,

Hugh

## Attachments
No attachments
