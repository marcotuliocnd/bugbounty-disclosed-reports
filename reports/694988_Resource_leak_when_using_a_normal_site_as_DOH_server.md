# Resource leak when using a normal site as DOH server

## Report Details
- **Report ID**: 694988
- **URL**: https://hackerone.com/reports/694988
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-09-14T20:45:50.296Z
- **Disclosed**: 2021-02-08T07:54:50.365Z

## Reporter
- **Username**: pauldreik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
If a DOH server is used, which is not really a DOH server but just a normal web server, the DNS request is sent but the reply will not be the expected DNS payload. In that case, curl correctly thinks DNS resolution failed, but it does not clean up allocated memory properly.

## Steps To Reproduce:
See the attached demonstration program. It can use either no DOH, a valid DOH, a garbage DOH address, or a valid web server not serving DOH.
Valgrind sees that it leaks memory only in the last case, the others are cleaned up properly.

### Leaking case
This will use https://example.com/ both as the URL to reach and as a DOH.
```
valgrind ./a.out notadoh
 (snip)
==3096== HEAP SUMMARY:
==3096==     in use at exit: 98,252 bytes in 1,043 blocks
==3096==   total heap usage: 101,296 allocs, 100,253 frees, 9,473,596 bytes allocated
==3096== 
==3096== LEAK SUMMARY:
==3096==    definitely lost: 8,564 bytes in 3 blocks
==3096==    indirectly lost: 88,144 bytes in 995 blocks
==3096==      possibly lost: 0 bytes in 0 blocks
==3096==    still reachable: 1,544 bytes in 45 blocks
==3096==         suppressed: 0 bytes in 0 blocks
==3096== Rerun with --leak-check=full to see details of leaked memory
```
### Normal case - no DOH
This will use https://example.com/ without DOH.
```
valgrind ./a.out none
(snip)
==3217== HEAP SUMMARY:
==3217==     in use at exit: 1,544 bytes in 45 blocks
==3217==   total heap usage: 37,396 allocs, 37,351 frees, 3,332,013 bytes allocated
==3217== 
==3217== LEAK SUMMARY:
==3217==    definitely lost: 0 bytes in 0 blocks
==3217==    indirectly lost: 0 bytes in 0 blocks
==3217==      possibly lost: 0 bytes in 0 blocks
==3217==    still reachable: 1,544 bytes in 45 blocks
==3217==         suppressed: 0 bytes in 0 blocks
```
### Normal case - working DOH
This will use https://example.com/ with cloudflare DOH.
```
valgrind ./a.out cloudflare
(snip)
==3376== HEAP SUMMARY:
==3376==     in use at exit: 1,656 bytes in 49 blocks
==3376==   total heap usage: 101,564 allocs, 101,515 frees, 9,062,588 bytes allocated
==3376== 
==3376== LEAK SUMMARY:
==3376==    definitely lost: 0 bytes in 0 blocks
==3376==    indirectly lost: 0 bytes in 0 blocks
==3376==      possibly lost: 0 bytes in 0 blocks
==3376==    still reachable: 1,656 bytes in 49 blocks
==3376==         suppressed: 0 bytes in 0 blocks
```

## Supporting Material/References:

See the attached program.

## Impact

The failed DOH is invisible to the end user, it seems to fallback to normal DNS.
So if the user has the wrong DOH adress (perhaps confused, or the DOH url changed slightly and now points to some generic hello page), I guess the memory leaks will add up, eventually leading to denial of service because of resource depletion.

It does not feel like a serious issue but I wanted to go through hackerone instead of filing a public report right away.

## Attachments
- dohleak.c
