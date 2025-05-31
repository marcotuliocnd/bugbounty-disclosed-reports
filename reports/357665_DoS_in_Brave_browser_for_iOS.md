# DoS in Brave browser for iOS

## Report Details
- **Report ID**: 357665
- **URL**: https://hackerone.com/reports/357665
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-26T00:32:25.545Z
- **Disclosed**: 2018-09-24T23:36:19.672Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Attacker could initiate DoS during page loading.

## Products affected: 

1.6 (18.05.17.13)
Device iPhone 6s (iOS 11.3.1)

## Steps To Reproduce:

PoC:
```html
<body>
    <script>
        let o = document.body.appendChild(document.createElement('object'));
        // application/json or application/pdf are valid values too
        o.type = 'text/html' // <-- triggers DoS
    </script>
</body>
```

The problem is the way Brave handles `<object>` tag with specific `type` attribute's values. 
Looks like unsupported mimeTypes or non-string values don't trigger crash, so I assume, that only valid mimeTypes could be used. Image mimeTypes don't trigger DoS.

## Supporting Material/References:

As I understood, Brave browser for iOS is a fork of Mozilla Firefox for iOS. 
Firefox isn't vulnerable, what makes this bug eligible. 

Crash log attached.
Screencast attached.

## Impact

The first page loaded after the browser crash is the crashed page. The PoC is immediate and doesn't require any additional interaction, so it could make browser broken, until the tab will be closed in offline.

> I suggest remembering the crashed page and ignoring it during browser opening. Probably, it could make all DoS attacks less dangerous.

> I'm not sure that the trick with tab closing in offline is obvious for most users.

## Attachments
- Client-2018-05-25-102537.ips
- video_(2).mp4
