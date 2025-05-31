# [bl] Uninitialized memory exposure via negative .consume()

## Report Details
- **Report ID**: 966347
- **URL**: https://hackerone.com/reports/966347
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-08-24T22:04:17.543Z
- **Disclosed**: 2020-08-27T15:16:42.547Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
# Module

**module name:** bl
**version:** 4.0.2
**npm page:** `https://www.npmjs.com/package/bl`

## Module Description

> A Node.js Buffer list collector, reader and streamer thingy.

## Module Stats

8 660 595 weekly downloads

# Vulnerability

## Vulnerability Description

If user input (even typed) ends up in `consume()` argument and can become negative,
BufferList state can be corrupted, tricking it into exposing uninitialized memory via
regular `.slice()` calls.

## Steps To Reproduce:

```
const { BufferList } = require('bl')
const secret = require('crypto').randomBytes(256)
for (let i = 0; i < 1e6; i++) {
  const clone = Buffer.from(secret)
  const bl = new BufferList()
  bl.append(Buffer.from('a'))
  bl.consume(-1024)
  const buf = bl.slice(1)
  if (buf.indexOf(clone) !== -1) {
    console.error(`Match (at ${i})`, buf)
  }
}
```

## Patch

### First component (more important):

In `BufferList.prototype.copy`, before the last `return dst`:
```js
  if (dst.length !== bufoff) return dst.slice(0, bufoff)
```

### Second component:

Check `.consume()` argument to be a non-negative integer.

## Supporting Material/References:

- Node.js v14.8.0

# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: N

## Impact

In case if the argument of `consume()` is attacker controlled:
1. Expose uninitialized memory, containing source code, passwords, network traffic, etc.
2. Cause invalid data in slices (low control)
3. Cause DoS by allocating a large buffer this way (with a large negative number before a slice/toString call is performed).

## Attachments
No attachments
