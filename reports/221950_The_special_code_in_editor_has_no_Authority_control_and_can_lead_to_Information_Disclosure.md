# The special code in editor has no Authority control and can lead to Information Disclosure

## Report Details
- **Report ID**: 221950
- **URL**: https://hackerone.com/reports/221950
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-18T16:42:12.630Z
- **Disclosed**: 2017-04-22T02:55:54.034Z

## Reporter
- **Username**: xifengweiyu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
Here is your keyword:mongoose

Details:
- Summary:

Uploaded file will be showed as a special code `{Fxxx}` in Phabricator editor,but it has no Authority control.

- Reproduce steps:

1.Open two different browsers (to simulate two different users)
2.browser A:login as user "toma"
3.browser B:login a user "test4"
4.user "toma" create a Maniphest task with visibility "toma" only,and upload a file "toma.html" to description,its code is`{F18}`
5.user "test4" open anyone editor and write:
```
{F1}{F2}{F3}{F4}{F4}{F5}{F6}{F7}{F8}{F9}{F10}{F11}{F12}{F13}{F14}{F15}{F16}{F17}{F18}{F19}{F20}
```
then post it,then you will find user "test4" has got the file of user "toma" with visibility "toma".



## Attachments
- toma's_task.png
- test4_got_it.png
