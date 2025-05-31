# Cross-site Scripting (XSS) - Stored | forum.acronis.com

## Report Details
- **Report ID**: 1161241
- **URL**: https://hackerone.com/reports/1161241
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-12T10:11:01.837Z
- **Disclosed**: 2022-02-08T13:52:00.761Z

## Reporter
- **Username**: quadrant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary

There is an XSS vulnerability in the search function of the forum (forum.acronis.com).

## Steps To Reproduce

  1. Modify your own forum Nickname, add the following payload after the original nickname:

```
<script>alert(0)</script>
```

  2. Fill in your nickname in the Author form of the search function and wait for the search, it will automatically trigger a pop-up.

{F1262581}

## Recommendations

Add special character filtering to the nickname modification function of the forum.

## Impact

You can add any keywords that users may use when searching for authors to your nickname to attack the corresponding users. It is possible to execute any Javascript.

## Attachments
- forum.acronis.com_XSS.png
