# Disclosure of the name of a program that has a private part with an external link

## Report Details
- **Report ID**: 871142
- **URL**: https://hackerone.com/reports/871142
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-11T22:12:09.285Z
- **Disclosed**: 2020-05-22T17:10:18.073Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team , @jobert , @bencode . Not so long ago, you made an output to the program panel of information about whether the program has the function- `retest`. Also, this is reflected in the report by the attribute `active_retest_subscription`. It seems that it is reflected in publish reports that are created in programs that have external links. The function itself cannot be enabled in the sandbox, which means that it can only be found in real programs. It turns out that if we see this attribute in the report, it means that the program is real, which means it is private

### Steps To Reproduce

1. Go to https://hackerone.com/hacktivity/publish
2. Input program , create reports
3. Check .json report - https://hackerone.com/reports/ID.json

If we see this attribute, it means that the program is private. And it has the `retest` function enabled

Thanks!
@haxta4ok00

## Impact

Disclosure of the name of a program that has a private part with an external link

## Attachments
No attachments
