# Robots.txt file with potentially sensitive content.

## Report Details
- **Report ID**: 1724771
- **URL**: https://hackerone.com/reports/1724771
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-10-06T17:29:19.433Z
- **Disclosed**: 2023-01-13T22:29:07.960Z

## Reporter
- **Username**: ethack1886
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Summary:


Invicti detected a Robots.txt file with potentially sensitive content.
 ##Description:
It must be in the topmost directory of your site; if you place it in a subdirectory, search engines will simply ignore it.

Despite its great power, robots.txt is often a relatively simple document, and a basic robots.txt file can be created in a matter of seconds using an editor like Notepad.

There are other ways to achieve some of the same goals that robots.txt is usually used for.

Individual pages can include a robots meta tag within the page code itself.

You can also use the X-Robots-Tag HTTP header to influence how (and whether) content is shown in search results.


## Platform(s) Affected:
website

## Steps To Reproduce:
If a mistake in robots.txt is having unwanted effects on your website’s search appearance, the most important first step is to correct robots.txt and verify that the new rules have the desired effect.

  1. Submit an updated sitemap and request a re-crawl of any pages that have been inappropriately delisted.
  2. Unfortunately, you are at the whim of Googlebot – there’s no guarantee as to how long it might take for any missing pages to reappear in the Google search index.
    3.All you can do is take the correct action to minimize that time as much as possible and keep checking until the fixed robots.txt is implemented by Googlebot.

## Supporting Material/References:


  *https://www.searchenginejournal.com/common-robots-txt-issues/437484/#close

## Impact

Attackers can use your website’s robots.txt file to gain a foothold in your environment and lead to further compromise. Learn how to mitigate your risks.

## Attachments
- Screenshot_2022-10-06_16_18_45.png
- Screenshot_2022-10-06_16_18_41.png
