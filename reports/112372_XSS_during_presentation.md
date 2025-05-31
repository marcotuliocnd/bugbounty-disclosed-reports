# XSS during presentation

## Report Details
- **Report ID**: 112372
- **URL**: https://hackerone.com/reports/112372
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-23T00:26:03.038Z
- **Disclosed**: 2017-10-28T17:34:20.471Z

## Reporter
- **Username**: hogarth45
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zaption

## Vulnerability Information
It is possible for a presenter to xss a viewer
Video attached:

## Recreation steps
Create publish lesson and start a presentation (join presentation in another browser)
Select "Quick question"
Open response
Insert the question 
asdf"><img src=x onerror=prompt(1)>

The Javascript will fire on the presenter's side and the viewers side.

## Attachments
- zaption.avi
