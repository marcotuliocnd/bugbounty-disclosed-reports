# libevent (stack) buffer overflow in evutil_parse_sockaddr_port

## Report Details
- **Report ID**: 112784
- **URL**: https://hackerone.com/reports/112784
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-25T22:43:17.005Z
- **Disclosed**: 2017-10-19T10:16:39.032Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
in ```evutil.c```:
```c
1798     char buf[128];
...
...
1809     cp = strchr(ip_as_string, ':');
1810     if (*ip_as_string == '[') {
1811         int len;
1812         if (!(cp = strchr(ip_as_string, ']'))) {
1813             return -1;
1814         }
1815         len = (int) ( cp-(ip_as_string + 1) );
1816         if (len > (int)sizeof(buf)-1) {
1817             return -1;
1818         }
1819         memcpy(buf, ip_as_string+1, len);
```

Length between '[' and ']' is cast to signed 32 bit integer on line 1815. Is the length is more than 2<<31 (INT_MAX), ```len``` will hold a negative value. Consequently, it will pass the check at line 1816. Segfault happens at line 1819.

Generate a resolv.conf with ```generate-resolv.conf```, then compile and run ```poc.c```. See ```entry-functions.txt``` for functions in tor that *might* be vulnerable.

Guido

## Attachments
- entry-functions.txt
- libev-to_evutil_parse_sockaddr_port.txt
- poc.c
- generate-resolv.conf.py
