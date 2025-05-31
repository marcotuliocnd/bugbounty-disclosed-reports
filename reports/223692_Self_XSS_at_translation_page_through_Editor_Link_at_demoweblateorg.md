# Self XSS at translation page through Editor Link at demo.weblate.org

## Report Details
- **Report ID**: 223692
- **URL**: https://hackerone.com/reports/223692
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-25T08:07:25.328Z
- **Disclosed**: 2017-05-17T16:48:51.756Z

## Reporter
- **Username**: csanuragjain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
User input is not sanitized properly at Editor link causing self xss.

**Steps to reproduce**
1) Navigate to https://demo.weblate.org/accounts/profile/#preferences
2) Provide Editor link as javaScript:alert(document.cookie);//confirm(1); and click on Save
3) Navigate to English Translation page of the project at https://demo.weblate.org/translate/hello/master/en_GB/?type=all
4) Click on the main.c under Source Information
5) Self XSS executes showing user cookie

Mitigation:
Proper server side filtering of user input

## Attachments
- weblate.PNG
