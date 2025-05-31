# Open Redirect in m.uber.com

## Report Details
- **Report ID**: 125000
- **URL**: https://hackerone.com/reports/125000
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-22T16:42:22.959Z
- **Disclosed**: 2016-09-27T18:28:28.141Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Reproduction Steps:
`https://m.uber.com//youtube.com/%2F..`

HTTP Response:
```
HTTP/1.1 303 See Other
...
Location: //youtube.com/%2F../
```

## Attachments
No attachments
