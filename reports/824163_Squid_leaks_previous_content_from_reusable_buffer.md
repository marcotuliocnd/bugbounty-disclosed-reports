# Squid leaks previous content from reusable buffer

## Report Details
- **Report ID**: 824163
- **URL**: https://hackerone.com/reports/824163
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-18T22:01:47.240Z
- **Disclosed**: 2021-08-26T23:37:23.822Z

## Reporter
- **Username**: jeriko_one
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary:
A malicious response to a FTP request can cause Squid to miscalculate the length of a string copying data past the terminating NULL. Due to Squid's memory pool the contents that is exposed could range from internal data, to other user's private Request/Response to Squid. 

This exist in Squid-4.9 and Below and was fixed in Squid-4.10
This vulnerability was assigned CVE-2019-12528.

## Steps To Reproduce:
A custom config is should not be needed. 
I've attached a python script that returns the needed response to trigger this.

1) Start Squid 
```
./sbin/squid
```

2) Start your malicious FTP Server
```
./squid_leak.py 8080
```

3) Make a request to the FTP server via Squid.
```
printf "GET ftp://<ftp ip>:8080/ HTTP/1.1\r\n\r\n" | nc <squid hostname> 3128
```

4) The FTP server should have sent the listing. A message from it saying
```
<- 226 Listing sent
```
Should be visible

The leaked data is now in the HTML that Squid has returned. The data will be under the line 

```<th nowrap="nowrap"><a href="../">Parent Directory</a> (<a href="/">Root Directory</a>)</th>```

Within the following <tr>

For reference a normal response would look like 

```
<tr class="entry"><td colspan="5">hi</td></tr>
```

## Analysis
The issue begins in Ftp::Gateway::parsingListing the relevant snippet being

```
    line = (char *)memAllocate(MEM_4K_BUF);
    ++end;
    s = sbuf;
    s += strspn(s, crlf);

    for (; s < end; s += strcspn(s, crlf), s += strspn(s, crlf)) {
        debugs(9, 7, HERE << "s = {" << s << "}");
        linelen = strcspn(s, crlf) + 1;
		<snip>
        xstrncpy(line, s, linelen);
		<snip>
		if (htmlifyListEntry(line, html)) 
```

A crucial thing to notice here is the following: 
- line is allocated with memAllocate(MEM_4K_BUF) this is what will lead us to reading previous content. Buffers allocated via this method aren't ever free'd, but are put back into their respective pools. Zeroing of the buffer is possible, but is not enabled for this type of memory.

Within ftpListParseParts (FtpGateway.cc) is where the root of the vulnerability exist. 
This function can handle various formats for listings. 

A common procedure is done on all of them before that then. They are converted
into tokens by strtok.
```
    for (t = strtok(xbuf, w_space); t && n_tokens < MAX_TOKENS; t = strtok(NULL, w_space)) {
        tokens[n_tokens] = xstrdup(t);
        ++n_tokens;
    }
```
Please note that strok uses w_space as delimiters 
```
	#define w_space     " \t\n\r"
```
The listing format that we'll focus on is DOS format (FtpGateway.cc:648)

For listings that aren't directories the following code is executed:
```
        } else {
            /* A file. Name begins after size, with a space in between */
            snprintf(tbuf, 128, " %s %s", tokens[2], tokens[3]);
            ct = strstr(buf, tbuf);

            if (ct) {
                ct += strlen(tokens[2]) + 2;
            }
        }

        p->name = xstrdup(ct ? ct : tokens[3]);
```

Squid will put tokens[2] and tokens[3] in a temporary buffer with 2 spaces. It
then searches for this string in the original line setting ct to the start of
this string. It then increments ct by the length of tokens[2] + 2. What is
pointed to now is used as the name. 

The false assumption here is that tokens will be separated by spaces in the
original line.

Consider the following example where \t denotes a tab, and * is for repetition:

```
04-05-70 09:33PM\tA*126 A*126
```

Going through the referenced code path when snprintf is called tbuf will be
filled as: " A*126". Then when strstr is called, it'll find the token, but it
won't be token[2] it'll be token[3] as token[2] started with a tab. When it
increments by the length strlen(tokens[2]) + 2 it'll put ct past the
terminating NULL byte of this line.

The contents is then copied into another buffer which will be displayed to the attacker

 p->name = xstrdup(ct ? ct : tokens[3]);

Setting a breakpoint in we can confirm that it's leaking data

Confirming that the tokens are 126:
```
(gdb) call (size_t)strlen(tokens[2])
$2 = 126
(gdb) call (size_t)strlen(tokens[3])
$3 = 126
```
Here ct is set to the wrong token since it's looking for " A"
```
snprintf(tbuf, 128, " %s %s", tokens[2], tokens[3]);
(gdb) n
675	            ct = strstr(buf, tbuf);
(gdb) call (size_t)strlen(tbuf)
$4 = 127

(gdb) p tbuf
$5 = " ", 'A' <repeats 126 times>

(gdb) p ct
$6 = 0x62100006918f " ", 'A' <repeats 126 times>

678	                ct += strlen(tokens[2]) + 2;
(gdb) call (size_t) strlen(tokens[2]) + 2
$8 = 128
```
Here we see ct is now past the terminating NULL
```
(gdb) x/2xb ct - 1
0x62100006920e:	0x00	0x66
```

## Impact

An attacker can leak sensitive information from the Squid process. This could include other user's Request and Response which could have headers, cookies, full bodies, and post data.

## Attachments
- squid_leak.py
