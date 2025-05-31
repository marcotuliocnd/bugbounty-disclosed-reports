# Code Injection Bug Report

## Report Details
- **Report ID**: 745921
- **URL**: https://hackerone.com/reports/745921
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-11-25T13:32:06.662Z
- **Disclosed**: 2021-05-07T11:50:39.776Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Good morning, I hope this message finds you well. On 22 November 2019, I emailed security@ruby-lang.org about a Code Injection bug on cache.ruby-lang.org, as the ruby-lang.org website is considered out-of-scope on H1. on 24 November 2019 the bug was acknowledged and [a patch](https://github.com/ruby/cache.r-l.o/commit/8739ca125f412a0cf2583b4b49a10ea52c75ff5f) released. This morning, 27 November 2019, I was asked to open this ticket.

## Impact

A lack of filtering on the cache.ruby-lang.org website enabled persons to inject code into the page, spoofing messages to the user, or redirecting them to malicious websites.

## Attachments
No attachments
