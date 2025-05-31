# CSRF when unlocking lenses leads to lenses being forcefully installed without user interaction

## Report Details
- **Report ID**: 1085336
- **URL**: https://hackerone.com/reports/1085336
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-23T14:19:13.410Z
- **Disclosed**: 2021-07-29T22:33:23.649Z

## Reporter
- **Username**: sdushantha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hi,

The url below allows a user to unlock a particular lens. Once they have opened the URL on their phone, Snapchat opens up and prompts the user to unlock this lens.
```
https://www.snapchat.com/unlock/?type=SNAPCODE&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```

By changing the value of  `type` in the URL above, from `SNAPCODE` to `SNAPCODE_NO_PROMPT`, we can bypass the prompt mentioned earlier, and instead forcefully unlock the lens and make them use it, hence why this is a CSRF:
```
https://www.snapchat.com/unlock/?type=SNAPCODE_NO_PROMPT&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```

This issue also happens to Snapchat's deeplink on Android:
```
snapchat://unlock/?type=SNAPCODE_NO_PROMPT&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```


I do not have an iOS device but I am certain that this issue also occurs on the iOS version of Snapchat.

## Impact

A Snapchat lens developer can abuse this bug and increase the number of people who use their lens by making people opening the URL to the lens and replacing `SNAPCODE` with `SNAPCODE_NO_PROMPT`.  This can cause false popularity for that lens as it is being unlocked without the user wanting to do so. This would then lead to the user having to manually delete the lense that was automatically added.

## Attachments
No attachments
