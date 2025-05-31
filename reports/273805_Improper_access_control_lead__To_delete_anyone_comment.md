# Improper access control lead  To delete anyone comment

## Report Details
- **Report ID**: 273805
- **URL**: https://hackerone.com/reports/273805
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-02T16:38:32.956Z
- **Disclosed**: 2017-10-16T05:48:54.911Z

## Reporter
- **Username**: ranjit_p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
SUMMURY
========================
Here server dont check the owner of any comment.
During Comment deletion it does not check whether the comment is  created by user or not.
so i can delete a comment of others user.

STEP TO REPRODUCE
=======================
1. goto https://localhost:8080/blog/comments .

2. select any commnet which is already aproved.

3.Unaprove it by clicking "Hide Comment".

4. Now delete that commnet and see comment is deleted which is not created by himself.

FIX
========
implement proper access control mechanism so that when user try to delete a comment first check the comment is belongs to that user or not.

## Attachments
No attachments
