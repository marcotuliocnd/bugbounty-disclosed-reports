# [Partial] SSN & [PII] exposed through iPERMs Presentation Slide.

## Report Details
- **Report ID**: 719631
- **URL**: https://hackerone.com/reports/719631
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-10-22T03:15:50.117Z
- **Disclosed**: 2019-12-02T20:03:29.777Z

## Reporter
- **Username**: try__harder
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello @deptofdefense, when performing reconnaissance, I came across a presentation slide that displayed live data since the data is blocked out & is formatted with `XXX-XX` with the last 4 digits.

The exposed data contains the following: `UPC, Division/Brigade, Rank, Soldier Name, Last 4 digits of SSN, FRR (Financial Record Reviews), PRR (Personal Record Reviews).`

Here are a few exposed users:
████████, XXX-XX-█████████
████████, XXX-XX-█████

The link that is hosting the Presentation Slide: `https://████████/wp-content/uploads/2017/12/Introduction-to-iPERMS-Slides.pptx` & on Slide 25, there is the exposed data.

The remediation/mitigation for this security flaw is the removal of the data/file & I have set the severity to `Critical` as it is exposing sensitive [PII] which could lead to a data breach.

## Impact

The sensitive information can be used to authenticate through various web-portals especially with the last 4 digits & full name with rank.

## Attachments
No attachments
