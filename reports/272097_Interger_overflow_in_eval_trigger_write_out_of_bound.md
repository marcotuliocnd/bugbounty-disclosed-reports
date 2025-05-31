# Interger overflow in eval trigger write out of bound

## Report Details
- **Report ID**: 272097
- **URL**: https://hackerone.com/reports/272097
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-26T16:44:35.846Z
- **Disclosed**: 2017-12-11T07:53:16.489Z

## Reporter
- **Username**: mipu94
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hi security team,
i [reported](https://rt.perl.org/Public/Bug/Display.html?id=131562)  some samples triggered crash in eval funtion in perl. 
The bug come because variable `start` and `items` used type `I32` which takes half the range of line_t and folds it into negative numbers, leading to trying to store the lines at negative indexes.

## Attachments
No attachments
