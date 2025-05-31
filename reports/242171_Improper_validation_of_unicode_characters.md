# Improper validation of unicode characters

## Report Details
- **Report ID**: 242171
- **URL**: https://hackerone.com/reports/242171
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-21T19:43:02.301Z
- **Disclosed**: 2017-08-19T05:47:06.499Z

## Reporter
- **Username**: asaxena2190
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,
I just saw a report of #229483

This issue still persist. When i tried some Unicode characters like smilies etc. It is working perfectly by displaying the Error message on the same page that **Username may only contain letters, numbers or the following characters: @ . + - _**

See 1.jpg for smilies handling (Expected)
See 2.jpg for other Unicode characters (Not handled correctly)

But when i put some other unicode charachters like  👨‍👩‍👧‍👦

1. Copy this  👨‍👩‍👧‍👦
2. Put in the username field and save.
3. Following Error will be displayed. 
It still showing the same error as in previous report. 

```

Server Error
The server had serious problems while serving your request. We've just sent our trained monkeys to fix the issue.

```
Please check.

Thanks,
Akash Saxena

## Attachments
- 1.jpg
- 2.jpg
