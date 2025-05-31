# Prototype pollution via console.table properties

## Report Details
- **Report ID**: 1431042
- **URL**: https://hackerone.com/reports/1431042
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-12-20T00:35:48.498Z
- **Disclosed**: 2022-01-11T17:23:04.445Z

## Reporter
- **Username**: rugvip
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

Attacker control of the second `properties` parameter of `console.table` may lead to prototype pollution.

**Description:**

Due to the formatting logic of the `console.table` function it is not safe to allow user controlled input to be passed to the `properties` parameter while simultaneously passing a plain object with at least one property as the first parameter.

The prototype pollution has very limited control, in that it only allows an empty string to be assigned numerical keys of the object prototype.

## Steps To Reproduce:

The vulnerability can be reproduced in the Node.js REPL, tested with version `v16.7.0`:

  1. Run the following: `console.table({foo: 'bar'}, ['__proto__'])`
  2. Verify that the object prototype has been polluted: `Object.prototype[0] === ''`

The pollution will vary depending on the number of properties on the object passed as the first parameter, with each additional property assigning another incrementing index of the object prototype. This means that if the first parameter is also controlled by the attacker, it is possible to assign empty strings from `0..n` to the object prototype, for any `n`:

```
> console.table({a: 1, b: 1, c: 1}, ['__proto__'])
Uncaught TypeError: Cannot create property '0' on string ''

> Object.prototype
[Object: null prototype] { '0': '', '1': '', '2': '' }
```

The vulnerable assignment can be found [here](https://github.com/nodejs/node/blob/3f7dabdfdc9e2a3cd3f92e377755c0dd43f6751b/lib/internal/console/constructor.js#L576) in the Node.js `console.table` implementation.

A suggested remediation is to ignore `properties` named `'__proto__'`, or to use a different data structure to store the computed table fields. For example:

```diff
 const keys = properties || ObjectKeys(item);
 for (const key of keys) {
+  if (key === '__proto__') {
+    continue
+  }
   if (map[key] === undefined)
     map[key] = [];
```

## Impact:

Users of `console.table` have no reason to expect the danger of passing on user input to the second `properties` array, and may therefore do so without sanitation. In the even that for example a web server is exposed to this vulnerability, it is likely to be a very effective denial of service attack. In extremely rare cases the prototype pollution can lead to more severe attack vectors such as bypassing authorization mechanisms, although due to limited control of the pollution this is unlikely.

## Supporting Material/References:

  * [CWE-1321: Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution')](https://cwe.mitre.org/data/definitions/1321.html)
  * [The vulnerable assignment](https://github.com/nodejs/node/blob/3f7dabdfdc9e2a3cd3f92e377755c0dd43f6751b/lib/internal/console/constructor.js#L576)

## Impact

Users of `console.table` have no reason to expect the danger of passing on user input to the second `properties` array, and may therefore do so without sanitation. In the even that for example a web server is exposed to this vulnerability, it is likely to be a very effective denial of service attack. In extremely rare cases the prototype pollution can lead to more severe attack vectors such as bypassing authorization mechanisms, although due to limited control of the pollution this is unlikely.

## Attachments
No attachments
