# DOM based CSS Injection on grammarly.com

## Report Details
- **Report ID**: 500436
- **URL**: https://hackerone.com/reports/500436
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-24T11:42:51.113Z
- **Disclosed**: 2019-05-06T09:11:54.696Z

## Reporter
- **Username**: gamer7112
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
**Summary:** An attacker can inject an external css file which can lead to phishing attacks and xss in older browsers.

**Description:** Within the main.js file the following code exists:
```javascript
t.prototype.componentWillMount = function () {
        var e = this.getCtx().nav.waypoint.query,
        t = e.extcss,
        n = e.affParams,
        a = e.minWords;
        this.affParams = n ? JSON.parse(decodeURIComponent(n))  : {
        },
        this.minWords = parseInt(a, 10),
        t && this.addExternalCss(t)
      },
      t.prototype.addExternalCss = function (e) {
        var t = document.createElement('link');
        t.setAttribute('href', e),
        t.setAttribute('rel', 'stylesheet'),
        t.setAttribute('type', 'text/css'),
        document.head.appendChild(t)
      },
```
Which allows an external css file to be loaded via the extcss parameter without any kind of origin checking or filtering.

## Browsers Verified In:

Chrome Version 72.0.3626.109
Firefox 65.0.1

## Steps To Reproduce:
1. Visit ```https://www.grammarly.com/embedded?height=300&extcss=https://www.dl.dropboxusercontent.com/s/e0g51ibqswh0v7d/xss.css?dl=0```

## Supporting Material/References:

  * CSS Injection can be used to create a phishing page like so:
{F429327}

## Impact

An attacker can use an external css file to spoof the page to their liking allowing for phishing attacks and if the victim is on an older browser an attacker can execute javascript as well.

## Attachments
- css_injection.png
