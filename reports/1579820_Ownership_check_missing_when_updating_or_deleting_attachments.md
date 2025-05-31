# Ownership check missing when updating or deleting attachments

## Report Details
- **Report ID**: 1579820
- **URL**: https://hackerone.com/reports/1579820
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-24T12:53:28.714Z
- **Disclosed**: 2022-07-06T17:50:56.771Z

## Reporter
- **Username**: kesselb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:

Ownership check is missing for attachments.

## Steps To Reproduce:

1. Open mail app
2. Compose a new message
3. Attach some file
4. Send message
5. Copy the xhr request and modify the attachment ids 
6. See that local_message_id is changed for a different user

When you compose a message and put them into the outbox to send them later we keep a reference for the attachments in oc_mail_attachments. An attacker is able to overwrite the local_message_id for an existing attachment  or delete the given row. Impact is that for the given message in the outbox the attachment is unavailable. 

- It's not possible to delete the actual attachment on file. Only the database reference. 
- It's not possible to send another person's attachment to you or someone else. 

## Supporting Material/References:

https://github.com/nextcloud/mail/blob/1752cbbba12285a4e93ec257d6e06ac1f790b171/lib/Db/LocalAttachmentMapper.php#L89-L118

## Impact

For the given message in the outbox the attachment is unavailable.

## Attachments
No attachments
