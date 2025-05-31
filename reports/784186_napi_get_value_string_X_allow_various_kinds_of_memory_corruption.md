# napi_get_value_string_X allow various kinds of memory corruption

## Report Details
- **Report ID**: 784186
- **URL**: https://hackerone.com/reports/784186
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-27T16:49:36.768Z
- **Disclosed**: 2020-07-02T19:53:41.174Z

## Reporter
- **Username**: tniessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

`napi_get_value_string_latin1`, `napi_get_value_string_utf8`, `napi_get_value_string_utf16` are vulnerable to buffer overflows, partially due to an integer underflow.

**Description:**

`napi_get_value_string_latin1`, `napi_get_value_string_utf8`, and `napi_get_value_string_utf16` behave like this:

1. If the output pointer is `NULL`, return.
2. Write `min(string_length, bufsize - 1)` bytes to the output buffer. Note that `bufsize` is an unsigned type, so this leads to an integer underflow for `bufsize == 0`. Since this is a `size_t`, the underflow will cause the entire string to be written to memory, no matter how long the string is.
3. Finally, write to `buf[copied]`, where `copied` is the number of bytes previously written. Even if step 2 hadn't written out of bounds, this would (for `bufsize == 0`).

## Steps To Reproduce:

```cpp
Napi::Value Test(const Napi::CallbackInfo& info) {
  char buf[1];
  // This should be a valid call, e.g., due to a malloc(0).
  napi_get_value_string_latin1(info.Env(), info[0], buf, 0, nullptr);
  return info.Env().Undefined();
}
```

```js
const binding = require('bindings')('validation');
console.log(binding.test('this could be code that might later be executed'));
```

Running the above script corrupts the call stack:

```bash
tniessen@local-vm:~/validation-fails$ node .
*** stack smashing detected ***: <unknown> terminated
Aborted (core dumped)
```

The best outcome is a crash, but a very likely outcome is data corruption. If the attacker can control the string's contents, they can even insert code into the process heap, or modify the call stack. Depending on the architecture and application, this can lead to various issues, up to remote code execution.

It is perfectly valid to pass in a non-NULL pointer for `buf` while specifying `bufsize == 0`. For example, `malloc(0)` is not guaranteed to return `NULL`.  A npm package might correctly work on one machine based on the assumption that `malloc(0) == NULL`, but might create severe security issues on a different host. Passing a non-NULL pointer is also not ruled out by the documentation of N-API, so it is not valid to assume that `buf` will always be `NULL` if `bufsize == 0`.

## Impact

npm packages and other applications that use N-API may involuntarily open up severe security issues, that might even be exploitable remotely. Even if `buf` is a valid pointer, passing `bufsize == 0` allows to write outside of the boundaries of that buffer.

Step 2 of the description allows an attacker to precisely define what is written to memory by passing in a custom string. Depending on whether the pointer points to heap or stack, possible results include data corruption, crashes (and thus DoS), and possibly even remote code execution, either by writing instructions to heap memory or by corrupting the stack.

Many attacks are likely caught by kernel and hardware protection mechanisms, but that depends on the specific hardware, kernel, and application, and memory layout. Even if they are caught, the entire process will crash (which is still good compared to other outcomes).

## Attachments
No attachments
