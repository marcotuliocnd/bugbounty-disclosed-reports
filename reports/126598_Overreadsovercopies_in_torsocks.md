# Overreads/overcopies in torsocks

## Report Details
- **Report ID**: 126598
- **URL**: https://hackerone.com/reports/126598
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-28T22:31:30.976Z
- **Disclosed**: 2017-10-19T10:14:57.678Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
First off, I know torsocks isn't in scope, so I don't expect anything in return for this. I happened to stumble upon this so why not report it. However if you feel generous you're welcome to give me bounty/swag ofcourse :P.

Here 16 bytes instead of 4 are copied, thereby copying 12 bytes of non-relevant stack memory.

```c
 62 LIBC_GETHOSTBYNAME_RET_TYPE tsocks_gethostbyname(LIBC_GETHOSTBYNAME_SIG)
 63 {
 64     int ret;
 65     uint32_t ip;
 ...
 86     memcpy(tsocks_he_addr, &ip, sizeof(tsocks_he_addr));
```

Here 255 bytes (```sizeof(tsocks_he_name)```) are copied even if the resolved hostname is much smaller (say 20 bytes). Thus a overread/overcopy of hundreds of bytes occurs.

```c
151 LIBC_GETHOSTBYADDR_RET_TYPE tsocks_gethostbyaddr(LIBC_GETHOSTBYADDR_SIG)
152 {
153     int ret;
154     char *hostname;
...
173     ret = tsocks_tor_resolve_ptr(addr, &hostname, type);
...
184         memcpy(tsocks_he_name, hostname, sizeof(tsocks_he_name));
```

```hostname``` is set via this path:

```tsocks_gethostbyaddr``` calls ```tsocks_tor_resolve_ptr```
```tsocks_tor_resolve_ptr``` calls ```socks5_recv_resolve_ptr_reply```

in (```lib/torsocks.c```)
```c
641     /* Force IPv4 resolution for now. */
642     ret = socks5_recv_resolve_ptr_reply(&conn, ip);
643     if (ret < 0) {
644         goto end_close;
645     }
```

(```socks5_recv_resolve_ptr_reply```, in ```common/socks5.c```)
```c
784 ATTR_HIDDEN                                                          
785 int socks5_recv_resolve_ptr_reply(struct connection *conn, char **_hostname)                                                                   
786 {
787     int ret;
788     ssize_t ret_recv;
789     char *hostname = NULL;
...
799     ret_recv = recv_data(conn->fd, &buffer, sizeof(buffer));
...
817     if (buffer.msg.atyp == SOCKS5_ATYP_DOMAIN) {
818         /* Allocate hostname len plus an extra for the null byte. */
819         hostname = zmalloc(buffer.len + 1);
820         if (!hostname) {
821             ret = -ENOMEM;
822             goto error;
823         }
824         ret_recv = recv_data(conn->fd, hostname, buffer.len);
825         if (ret_recv < 0) {
826             ret = ret_recv;
827             goto error;
828         }
829         hostname[buffer.len] = '\0';
830     } else {
```

Also, if recv_data() puts over 255 bytes in 'buffer', say 300 bytes, then line 829 becomes:

```c
829         hostname[300] = '\0';
```

and consequently ```tsocks_gethostbyaddr``` puts a string of 300 bytes in h_addr_list:

```c
184         memcpy(tsocks_he_name, hostname, sizeof(tsocks_he_name));
185         free(hostname);
186         tsocks_he_addr_list[0] = (char *) addr;
187     }
188 
189     tsocks_he.h_name = tsocks_he_name;
190     tsocks_he.h_aliases = NULL;                                                                                                                
191     tsocks_he.h_length = strlen(tsocks_he_name);
192     tsocks_he.h_addrtype = type;
193     tsocks_he.h_addr_list = tsocks_he_addr_list;
```

If the application using this library things that it is guaranteed that the strings in h_addr_list are never more than 255 bytes, an overflow in the "parent" application might occur. But honestly I haven't tested whether any of this could actually occur.

Although I think there isn't a *direct* security risk in the overreads/overcopies, it could lead to crashes, and moreover, their existence makes it easier to secretly implement backdoors in applications that use torsocks as a wrapper (they could introduce code that looks like a regular programming error but in fact exploit the fact that torsocks writes non-relevant heap/stack memory in order to aid an attacker with ASLR circumvention, for example), if you get my drift.

Guido


## Attachments
No attachments
