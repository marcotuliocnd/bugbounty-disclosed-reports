# Reading redacted data via hackbot's answers

## Report Details
- **Report ID**: 247628
- **URL**: https://hackerone.com/reports/247628
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-10T06:40:27.817Z
- **Disclosed**: 2017-07-27T17:27:52.565Z

## Reporter
- **Username**: inhibitor181
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello, I have found a way to use hackbot's automated duplication answers to reveal redacted data via brute force. This is restricted by the length of the report and number of radacted items. For short report with little content and just 1-2 redacted texts this is rather easy to accomplish, but for very long report this is nearly impossible without luck and a lot of time.


**Impact**
Because hackbot posts comments in order to help customers identify duplicated reports, I wanted to try and see if I can somehow manage to make it disclose other information. I have then seen that the bot identifies duplicated reports from other public reports unrelated to the program. To my surprise, I have then observed that the bot does not identify duplicated reports while using the same redacted text (the black squares), but it has identified the real text that it has already been redacted.

IMO, this is a medium  issue because:
- Someone actually wanted to hide information form public eyes and this information can be identified AND it does not require any other user's action.
- This method is not usable in EVERY case and only affects public reports OR reports from the same program.


### Steps To Reproduce

1. Create a test program
2. With a hacker create a submission (example for my test was with subject "testredact" and the content "testredact password is 123456789".
3. Login with an admin and redact a certain part of the text (in my test I redacted 123456789)
4. Login with another hacker and submit a new report while trying to mimic the redacted report

So, using the data from my tests this has been accomplished :
- By making a new submission with the same subject, but the content "testredact password is 123456xxx", the hackbot told me that the report is 78% the same
- By making a new submission with the same subject, but the content "testredact password is 123456781", the hackbot told me that the report is 88% the same
- By making a new submission with the same subject, and the same content "testredact password is 123456789", the hackbot told me that the report is 100% the same

This method should also works against public reports that have redacted content and a user can simply create his own test program in order to try and identify redacted text.

__IMO, the hackbot should not try and identify redacted texts__

### Optional: Supporting Material/References (Screenshots)

I have uploaded a screenshot where you can see the 100% and the 88% identified text (last 2 tests from my replication steps)

## Attachments
No attachments
