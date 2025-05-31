# internal dev tokens disclosure

## Report Details
- **Report ID**: 1940443
- **URL**: https://hackerone.com/reports/1940443
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-04-10T08:51:08.284Z
- **Disclosed**: 2023-06-14T10:27:08.739Z

## Reporter
- **Username**: happytohelp22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
snapchat has made Keydb as opensource but its development repo on github is leaking too much internal sensitive data in commits history which should not be a good idea to be revealed in open source project.
such as https://github.com/Snapchat/KeyDB/commit/157b32109854f947843366f66215ccf90809e766
```
[Dockerfile](https://github.sc-corp.net/Snapchat/keydb-internal/github-action-runner-docker/Dockerfile). 
3. Take the token from that script. Should be in "Configure" section: 
    ``` 
    ./config.sh --url https://github.com/EQ-Alpha/KeyDB --token ████
```
██████

## Impact

internal dev sensitive information disclosed publicaly
for example PAT token i pasted above

## Attachments
No attachments
