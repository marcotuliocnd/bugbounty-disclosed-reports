# Searching from Hacktivity returns hits for words in limited disclosure reports that are not visible

## Report Details
- **Report ID**: 685909
- **URL**: https://hackerone.com/reports/685909
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-01T11:28:31.585Z
- **Disclosed**: 2019-11-08T21:27:56.007Z

## Reporter
- **Username**: nathand
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

It appears I'm able to discover words used in limited disclosed reports, that are not publicly visible, by using the search function available from the Hactivity page.

**Description:**

Recently I was investigating a finding for another program which involved exploiting XSS ████. I wondered how relevant exploiting ████ was to programs these days, so I set about searching Hackerone for relevant reports. Normally I'd just use Google for this, but this time I decided to use the Hackerone search in the Hacktivity stream page. To find relevant reports, I first searched for:

```
xss ███████
```

Or in URL form: ██████

This returned a lot of clearly relevant reports. However, when I came across the report #413412 in the search results, entitled "Reflected XSS on secure.chaturbate.com", I noticed something a bit odd - it doesn't mention ███████ anywhere in the report that is publicly visible (and in fact that string is nowhere to be found in its markup such as keyword meta data):

https://hackerone.com/reports/413412

However, in the results, Chaturbate does have a report ██████████ involving XSS ████, so it seems probable this limited report is referencing ██████████, even though what's publicly available does not mention this.

This had me wondering if I stumbled across a bug in Hackerone report searching, where by I am able to reveal words contained within the hacker's description and/or comments of limited disclosed reports. To test this theory, I wrote a script to perform this search, but while also adding other words, and seeing if this report still gets returned in the results, and try and reveal more content that is not available in the limited public report. For which words to add I used a list of the 'top 3000 English words' and ignored words that are 3 characters or shorter in length, or are very common (than, that, your etc).

The results proved successful, in the sense I was able to build a lengthy search query that only returns this report, of words that are not found in the limited report (but still seem fairly likely to be matches, given the context). This search string was:

```
xss ████████ against application attack dangerous detect convince deliver direct mail mechanism occur publicly reference remove request responsible scheme script security supply themselves under victim vulnerable
```

Or in URL form: ███████

While this particular example did not reveal any sensitive information for this specific report, I thought this worth reporting due to the obvious potential here to find details in reports that the program may not want to be public.

### Steps To Reproduce

1. Go to the Hacktivity page.
2. Search for `xss ███ against application attack dangerous detect convince deliver direct mail mechanism occur publicly reference remove request responsible scheme script security supply themselves under victim vulnerable`
3. Note the single result as report #413412, and other than "XSS", none of these words appear in the limited disclosed public report.

## Impact

By abusing this, an attacker could reveal content hidden in a limited disclosed report.

## Attachments
No attachments
