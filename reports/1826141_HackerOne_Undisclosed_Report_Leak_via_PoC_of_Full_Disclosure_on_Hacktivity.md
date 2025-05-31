# HackerOne Undisclosed Report Leak via PoC of Full Disclosure on Hacktivity

## Report Details
- **Report ID**: 1826141
- **URL**: https://hackerone.com/reports/1826141
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-01-08T16:22:50.789Z
- **Disclosed**: 2023-02-10T13:37:05.894Z

## Reporter
- **Username**: syjane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi Team,

HackerOne is very sensitive when it comes to HackerOne report data such as `report title`,`severity`,`program` etc. H1 will not share those private data base on the HackerOne privacy policy.

Recently, HackerOne disclosed this report #1540969 [Race condition in joining CTF group](https://hackerone.com/reports/1540969) submitted by @zeyu2001 but the video PoC by the researcher was not redacted, the video contains undisclosed report reported by @zeyu2001 to other program like __██████__ and __███__ , this is both mistak by the researcher and HackerOne.

Researcher leak his own undisclosed report to PoC which is not related the #1540969 , and HackerOne did not redacted it before disclosure, resulting in disclosing sensitive information like `report title`.

### Steps To Reproduce

1. Go to this fully disclosed report: https://hackerone.com/reports/1540969
2. Check this comment when report participant named @osman1337 completed the retest: https://hackerone.com/reports/1540969#activity-16794287
3. Observed that there is video PoC named `poc-h1.mp4`
4. Watch the video PoC carefully and 3 undisclosed reports unrelated to the submission was leaked on the video poc.
5. See screenshot below for my proof

█████████

__The screenshot was taken from the video PoC, I can directly comment that the below undisclosed report was leaked__

Report ID: #1570556 
Report Title: ████
Severity: Medium
Reported to: ████ (I believe this program is private because I can't see that in public directory)

Report ID: #1576582 
Report Title: ██████████
Severity: Medium
Reported to: ███████

Report ID: #1576582 
Report Title: ██████
Severity: High
Reported to: ████

## Impact

Sensitive report data leak such as report title, severity. program, report id.

This is a clear violation of HackerOne data privacy for customers.

## Mitigation:

Always review sensitive information before full disclosure to not disclosed other report data that was unrelated to the submission.

Let me know if you need more information.

Regards
@syjane

## Attachments
No attachments
