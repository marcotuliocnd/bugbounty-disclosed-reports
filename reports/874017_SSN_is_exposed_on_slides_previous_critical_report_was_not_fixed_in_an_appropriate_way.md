# SSN is exposed on slides, previous critical report was not fixed in an appropriate way

## Report Details
- **Report ID**: 874017
- **URL**: https://hackerone.com/reports/874017
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-14T09:20:06.307Z
- **Disclosed**: 2020-06-11T18:19:46.012Z

## Reporter
- **Username**: pvm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
SSN is exposed on slides, previous critical report was not fixed in an appropriate way

**Description:**
1. SSN is exposed on a screenshot. Slide 13th. SSN is covered by an olive/green rectangle which is moveable. The image itself was not updated. 
██████wp-content/uploads/2018/12/████████

2. The issue was previously submitted and was not fixed in an appropriate way.
https://hackerone.com/reports/█████████

3. The file is easy to find by the file name.
https://duckduckgo.com/?q=%22███%22&t=hj&ia=web

## Impact
Critical
███████ is a real person (officer) according to  ██████████

## Step-by-step Reproduction Instructions
1. Download the file ████████wp-content/uploads/2018/12/█████
2. Navigate to slide 13
3. Move the olive rectangle which covers SSN

## Product, Version, and Configuration (If applicable)
N/A

## Suggested Mitigation/Remediation Actions
Blur/remove/cover the SSN on the image and replace the image on the slides.

## Impact

PII leakage. Name and SSN.

## Attachments
No attachments
