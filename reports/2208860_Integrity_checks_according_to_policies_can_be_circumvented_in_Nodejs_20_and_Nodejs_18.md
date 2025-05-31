# Integrity checks according to policies can be circumvented in Node.js 20 and Node.js 18

## Report Details
- **Report ID**: 2208860
- **URL**: https://hackerone.com/reports/2208860
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-14T00:08:48.104Z
- **Disclosed**: 2023-11-30T15:52:02.663Z

## Reporter
- **Username**: tniessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
**Summary:** When Node.js is checking the integrity of a resource against a trusted manifest, the application can intercept the operation and return a forged checksum to node's policy implementation, thus effectively disabling the integrity check.

**Description:** Node.js uses the `Hash` class of the built-in `crypto` module to compute a cryptographic hash of each resource. The implementation protects itself against modifications of the `Hash` class prototype by the application, however, the `Hash` class internally relies on several C++ bindings that the application can replace at runtime.

Consider the following `policy.json` file:

```json
{
  "resources": {
    "./main.js": {
      "integrity": true,
      "dependencies": {
        "./protected.js": true,
        "crypto": true
      }
    },
    "./protected.js": {
      "integrity": "sha384-OLBgp1GsljhM2TJ+sbHjaiH9txEUvgdDTAzHv2P24donTt6/529l+9Ua0vFImLlb",
      "dependencies": true
    }
  }
}
```

The file `main.js` may contain arbitrary code, but it cannot access, for example, the built-in `fs` module. The file `protected.js`, on the other hand, has a strict integrity requirement but can access arbitrary modules. The `main.js` file may require `protected.js`, provided that the integrity of `protected.js` is verified by Node.js.

The file `main.js` can thus contain arbitrary code. Let the contents be:

```js
const h = require('crypto').createHash('sha384');
const fakeDigest = h.digest();

const kHandle = Object.getOwnPropertySymbols(h)
                      .find((s) => s.description === 'kHandle');
h[kHandle].constructor.prototype.digest = () => fakeDigest;

require('./protected.js');
```

The file `protected.js` does _not_ match the integrity value specified in `policy.json`:

```js
console.log(require('fs').readFileSync('/etc/passwd').length);
```

Running `main.js` with the policy enabled succeeds despite  the integrity mismatch, and the application reads `/etc/passwd`:

```js
$ node --experimental-policy=policy.json main.js 
3224
```

---

This vulnerability is exploitable in the default build configuration of Node.js, and only requires the user to enable the policy feature when starting Node.js.

I provided a patch, which has been merged into the main branch as [commit e673c0362979f9cb2c74fc6876c45ae9be1fe853](https://github.com/nodejs/node/commit/e673c0362979f9cb2c74fc6876c45ae9be1fe853), into the v20.x release line as [commit a4cb7fc7c04869f051e270ed192a679d2d108328](https://github.com/nodejs/node/commit/a4cb7fc7c04869f051e270ed192a679d2d108328), and into the v18.x release line as [commit 1c538938ccadfd35fbc699d8e85102736cd5945c](https://github.com/nodejs/node/commit/1c538938ccadfd35fbc699d8e85102736cd5945c), all of which have been released on October 13th, 2023.

## Impact

As per the Node.js documentation at the time the issue was reported, "Policies are a security feature intended to allow guarantees about what code Node.js is able to load" and "The policy manifest will be used to enforce constraints on code loaded by Node.js." The current revision of the documentation adds that "policies guarantee the file integrity when a module is loaded using `require()`, `import()` or `new Module()`."

The presented vulnerability invalidates these statements. Code may be executed through `require()` even if the code has been modified. The modified code inherits all permissions of the supposedly trusted code, which potentially allows the attacker to escalate their permissions as demonstrated above.

## Attachments
No attachments
