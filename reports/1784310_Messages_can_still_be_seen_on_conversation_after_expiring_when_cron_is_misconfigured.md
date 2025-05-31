# Messages can still be seen on conversation after expiring when cron is misconfigured

## Report Details
- **Report ID**: 1784310
- **URL**: https://hackerone.com/reports/1784310
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-25T16:25:36.306Z
- **Disclosed**: 2023-02-27T15:48:58.336Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Nextcloud talk has a feature called ```Message Expiration```, Chat messages can be expired after a certain time. However the message  does not really expire and can still be seen by anyone.

## Steps To Reproduce:

1. Create a conversation
1. Set the message expiration Go to Settings > Moderation 
1. Pick anything and using burp intercept the request and set it to 60 or 120 seconds.
1. send a message
1. wait for the message to expire
1. Copy the conversation link and open it to a new tab


## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

 ██████████

## Impact

Messages that should expired is divulged to anyone that can access the conversation, This includes personal and group.

## Attachments
No attachments
