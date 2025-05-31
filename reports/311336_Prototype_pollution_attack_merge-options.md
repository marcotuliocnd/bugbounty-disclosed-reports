# Prototype pollution attack (merge-options)

## Report Details
- **Report ID**: 311336
- **URL**: https://hackerone.com/reports/311336
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-02-01T14:17:41.994Z
- **Disclosed**: 2018-04-15T18:32:41.072Z

## Reporter
- **Username**: holyvier
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
As discussed in #309391, here's the separate report for each of the library. This one is the information for the merge-options library.

**Module:**
[merge-options](https://www.npmjs.com/package/merge-options)

**Summary:**

Utilities function in all the listed modules can be tricked into modifying the prototype of "Object" when the attacker control part of the structure passed to these function. This can let an attacker add or modify existing property that will exist on all object.

**Description:**

## Steps To Reproduce:

The simplest test case to reproduce the issue is the following code snippet. In the code snippet, "malicious_payload" would come from an endpoint which accepts JSON data.

> var merge = require('merge-options');
> var malicious_payload = '{"\_\_proto\_\_":{"oops":"It works !"}}';
>
> var a = {};
> console.log("Before : " + a.oops);
> merge({}, JSON.parse(malicious_payload));
> console.log("After : " + a.oops);

This shows that an attacker can add attributes to all existing object on the server. Additional attribute can be used to change the execution code flow or cause error on every subsequent request by replacing "toString" or "valueOf".

## Impact:

This vulnerability is guaranteed to at least obtain denial of service as all the library allow the property "toString" and "valueOf" to be replaced by a "String". This breaks the express module and forces the server to either crash or return a 500 to every subsequent request.

More complex payload can be crafted to gain remote code execution (see PoC in #309391).

## Supporting Material/References:

If extra information is needed don't hesitate to ask.

## Impact

Variable. Server crash or the server becoming unable to respond to all request is guaranteed, but more significant impact like remote code execution can be achieved in some cases.

## Attachments
No attachments
