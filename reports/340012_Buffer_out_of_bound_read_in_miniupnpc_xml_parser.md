# Buffer out of bound read in miniupnpc xml parser 

## Report Details
- **Report ID**: 340012
- **URL**: https://hackerone.com/reports/340012
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-04-18T09:32:51.100Z
- **Disclosed**: 2018-04-25T05:49:15.662Z

## Reporter
- **Username**: yukichen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:**

This is a buffer oob read vulnerability in miniupnpc when parsing xml response. This vulnerability could result in denial of service attack in monero client to in local area Network.

**Description:** 

In miniupnpc, file "Minixml.c":

The funnction parseelt:

static void parseelt(struct xmlparser * p)
{
...
				if(memcmp(p->xml, "<![CDATA[", 9) == 0)		// (1)  Failed to do bound check prior to "memcmp" here
				{
					/* CDATA handling */
					p->xml += 9;
					data = p->xml;
					i = 0;
					while(memcmp(p->xml, "]]>", 3) != 0)
...
}

Here it tries to match the CDATA section in the xml file using memcmp. However, it does not check whether it has already reached the end of the xml buffer. By sending a specially crafted xml response, we can make it read out of bounds of the xml buffer, which may crash the client.


## Releases Affected:

It affects all monero clients which use miniupnpc.

I have tested with the Windows, 64-bit (Command-Line Tools Only), version 0.12.0.0 Lithium Luna, downloaded from:   https://getmonero.org/downloads/

The environment I used to test was Windows 10 64-bits.


## Steps To Reproduce:

Step  1. Enable page heap for monerod.exe:

The page heap on windows helps to crash the program at the first place when memory corruption issue (buffer overrun, uaf...) happens, similar to tools like valgrind, ASAN. 

See:
https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/gflags-and-pageheap


1.1 Install WinDbg to get gflags
Install the Debugging tools for windows, which contains the gflags.exe tool.

1.2 Enable page heap for monerod.exe
Execute the following command:
"c:\Program Files\Debugging Tools for Windows (x64)\gflags.exe" /i monerod.exe +hpa


Step 2. Start the malicious upnp server:

python poc.py --listen 127.0.0.1:65000 --target havoc


Step3. Start monerod:

monerod.exe --test-drop-download


Step 4. Wait for monerod crash

The crash stack trace:


(5c10.56c0): Access violation - code c0000005 (!!! second chance !!!)
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for C:\Users\test\Desktop\monero\monero-win-x64-v0.12.0.0\monero-v0.12.0.0\monerod.exe - 
monerod+0x448737:
00000000`01768737 4c3908          cmp     qword ptr [rax],r9 ds:00000000`200b0fff=????????????????
0:000> k
Child-SP          RetAddr           Call Site
00000000`0294d5f0 00000000`01767edb monerod+0x448737
00000000`0294d660 00000000`01970b5b monerod+0x447edb
00000000`0294d7a0 00000000`019792ff monerod!ZN5boost7archive6detail11oserializerINS0_24portable_binary_oarchiveEN8nodetool26anchor_peerlist_entry_baseIN4epee9net_utils15network_addressEEEEC2Ev+0x1addb
00000000`0294e6b0 00000000`01987503 monerod!ZN5boost7archive6detail11oserializerINS0_24portable_binary_oarchiveEN8nodetool26anchor_peerlist_entry_baseIN4epee9net_utils15network_addressEEEEC2Ev+0x2357f
00000000`0294e960 00000000`01986aa2 monerod!ZN5boost7archive6detail11oserializerINS0_24portable_binary_oarchiveEN8nodetool26anchor_peerlist_entry_baseIN4epee9net_utils15network_addressEEEEC2Ev+0x31783
00000000`0294ead0 00000000`01331c96 monerod!ZN5boost7archive6detail11oserializerINS0_24portable_binary_oarchiveEN8nodetool26anchor_peerlist_entry_baseIN4epee9net_utils15network_addressEEEEC2Ev+0x30d22
00000000`0294eca0 00000000`01336735 monerod+0x11c96
00000000`0294ede0 00000000`017fdb73 monerod+0x16735
00000000`0294ee70 00000000`01ab0f0b monerod+0x4ddb73
00000000`0294f000 00000000`013213c7 monerod!ZNK5boost7archive6detail11oserializerINS0_24portable_binary_oarchiveEN8nodetool26anchor_peerlist_entry_baseIN4epee9net_utils15network_addressEEEE16save_object_dataERNS1_14basic_oarchiveEPKv+0x112c1b
00000000`0294f860 00000000`013214fb monerod+0x13c7
00000000`0294f930 00007ffa`6b921fe4 monerod+0x14fb
00000000`0294f960 00007ffa`6d7bf061 KERNEL32!BaseThreadInitThunk+0x14
00000000`0294f990 00000000`00000000 ntdll!RtlUserThreadStart+0x21



## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

A malicious attacker may crash the monero clients within the same local network area.

## Attachments
- monerod_crash.png
- poc.py
