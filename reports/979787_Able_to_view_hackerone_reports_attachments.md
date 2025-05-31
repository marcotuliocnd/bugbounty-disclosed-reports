# Able to view hackerone reports attachments

## Report Details
- **Report ID**: 979787
- **URL**: https://hackerone.com/reports/979787
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-09-11T13:48:44.894Z
- **Disclosed**: 2022-07-11T16:00:07.348Z

## Reporter
- **Username**: sateeshn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

(Hi team,

I accidentally found this bug. While reading one of hackerone public report (https://hackerone.com/reports/446238) about gitlab, I found a link posted by gitlab member which is related to internal tracking of the report. I clicked that link (https://gitlab.com/gitlab-org/gitlab-foss/-/issues/54220) and found one of the attachment. I am able to view all the attachments by directly visiting the attachment domain.)

### Steps to reproduce

1. Open https://h1.sec.gitlab.net/a/ (you will able to view all the attachments) and copy any content key 
2. Paste key infront of  https://h1.sec.gitlab.net/a/  (ex: https://h1.sec.gitlab.net/a/copied_key.jpg) (you will able to view attachment)

To view nonpublic hackerone report attachment, find the hackerone report key from the above link > copy and paste infront of https://h1.sec.gitlab.net/a/

Try to view this hackerone report you will see access denied https://hackerone.com/reports/446237 

but still you can able to view the report attachment by visiting https://h1.sec.gitlab.net/a/█████

## Impact

As attachments consist of researcher attached POC images and videos. So attacker can directly exploit by using these information.

## Attachments
- gitlab-h1-attachments-poc.PNG
