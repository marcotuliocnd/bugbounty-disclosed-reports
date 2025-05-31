# Improper Access Control in Buddypress core allows reply,delete any user's activity

## Report Details
- **Report ID**: 837256
- **URL**: https://hackerone.com/reports/837256
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-02T15:09:51.209Z
- **Disclosed**: 2020-05-22T00:33:25.125Z

## Reporter
- **Username**: hoangkien1020
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:

Improper Access Control in Buddypress core allows reply,delete any user's activity in other public group,which they don't join.

## Steps To Reproduce:
Step 1: Create two account A, B with two public groups
Step 2: In group A-account A, create a new activity [id_A]
Step 3: In group B-account B, create a new activity [id_B]
Step 4: In group A-account A select reply/delete action, use proxy to capture this request
Step 5: Change id_A by id_B
Step 6: Done, you deleted or reply user's activity without joining group
## Recommendations
Valid access control with their roles 

PoC with video

## Impact

Attacker without joining to group performs to reply,delete any activities without permission.

## Attachments
No attachments
