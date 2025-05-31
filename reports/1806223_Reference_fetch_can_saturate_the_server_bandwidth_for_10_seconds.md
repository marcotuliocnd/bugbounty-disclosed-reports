# Reference fetch can saturate the server bandwidth for 10 seconds

## Report Details
- **Report ID**: 1806223
- **URL**: https://hackerone.com/reports/1806223
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-15T09:47:06.964Z
- **Disclosed**: 2023-04-29T08:12:58.786Z

## Reporter
- **Username**: brthnc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
When posting a message on talk, a reference is fetched for any link in the message
There is a hardcoded mandatory 10sec timeout. But the ressource is still fetched for those entire 10 seconds.

For high-bandwidth servers, this can result in disk space being temporarily filled and saturate the server bandwidth.
Tested on my 2.5gbps network, I was easily able to find 10GB ressources online that have higher network speed and fully saturate the netwrok for a few seconds and a few messages.

## Steps To Reproduce:

  1. Open a talk room
  1. Post multiple messages containing a link to a high availability ressource like https://speed.hetzner.de/10GB.bin

## Impact

Can severly impact server performances and/or lead to a denial of service

## Attachments
No attachments
