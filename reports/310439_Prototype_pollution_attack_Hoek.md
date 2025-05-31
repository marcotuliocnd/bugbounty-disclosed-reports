# Prototype pollution attack (Hoek)

## Report Details
- **Report ID**: 310439
- **URL**: https://hackerone.com/reports/310439
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-30T06:24:55.040Z
- **Disclosed**: 2018-02-13T19:23:40.361Z

## Reporter
- **Username**: holyvier
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
As discussed in #309391, here's the separate report for each of the library. This one is the information for the Hoek library.

**Module:**

[hoek](https://www.npmjs.com/package/hoek)

**Summary:**

Utilities function in all the listed modules can be tricked into modify the prototype of "Object" when the attacker control part of the structure passed to these function. This can let an attacker add or modify existing property that will exist on all object.

**Description:** 

## Steps To Reproduce:

The simplest test case to reproduce the issue is the following code snippet. In the code snippet, "malicious_payload" would come from an endpoint which accepts JSON data. The test case also works with the "Hoek.applyToDefaults" function.

> var Hoek = require('hoek');
> var malicious_payload = '{"__proto__":{"oops":"It works !"}}';
> 
> var a = {};
> console.log("Before : " + a.oops);
> Hoek.merge({}, JSON.parse(malicious_payload));
> console.log("After : " + a.oops);

This shows that an attacker can add attributes to all existing object on the server. Additional attribute can be used to change the execution code flow or cause error on every subsequent request by replacing "toString" or "valueOf".

## Impact:

This vulnerability is garanteed to at least obtain denial of service as all the library allow the property "toString" and "valueOf" to be replaced by a "String". This breaks the express module and forces the server to either crash or return a 500 to every subsequent request.

More complex payload can be crafted to gain remote code execution (see PoC in #309391).

## Supporting Material/References:

If extra information is needed don't hesitate to ask.

## Impact

Variable. Server crash or the server becoming unable to respond to all request is garanteed, but more significant impact like remote code execution can be achieved in some cases.

## Attachments
No attachments
