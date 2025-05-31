# Instant open redirect on Live preview WEB Ide opening

## Report Details
- **Report ID**: 437142
- **URL**: https://hackerone.com/reports/437142
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-08T14:39:28.541Z
- **Disclosed**: 2020-11-04T11:16:59.809Z

## Reporter
- **Username**: chaosbolt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello Gitlab team! Asset is my own gitlab installation for Ubuntu.

The issue I want to report is lack of sandbox attribute in iframe pointing to codesandbox. This results content inside iframe redirect top level window on load.

How to reproduce:

1. create index.js with following content:
```
window.open("https://evil.com","_top");
```
2.  create package.json with following content:
```
{
  "main": "index.js",
  "dependencies": {
    "vue": "latest"
  }
}
```
3. open file in Web IDE and load preview

How to fix:

1. add sandbox attribute with needed permissions (for example, you need allow-scripts for sure) on codesandbox iframe.

## Impact

Open redirect on web ide preview load.

## Attachments
- openredirectwebide.gif
