# Buffer overrun in Steam SILK voice decoder

## Report Details
- **Report ID**: 1180252
- **URL**: https://hackerone.com/reports/1180252
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-29T18:33:33.502Z
- **Disclosed**: 2021-09-13T17:56:19.395Z

## Reporter
- **Username**: slidybat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
#Vulnerability
The SteamWorks SDK has a function available named [DecompressVoice()](https://partner.steamgames.com/doc/api/ISteamUser#DecompressVoice), which takes as input some compressed voice data, and returns the raw audio data.

The format for the input voice data is as follows:
```
8 bytes - steamid
1 byte - payload type
2 bytes - payload size
<payload data>
4 bytes - CRC checksum
```

There are numerous payload types available, including Opus PLC, Opus, SILK, Raw and Silence. The bug being considered here is specific to the SILK decoder.

The pseudo-code for the SILK decoder is:
```cpp
unsigned int VoiceEncoder_SILK::Decode( const char* pPayloadData, size_t nPayloadSize, char* pDestBuffer, size_t nDestBufferSize )
{
	m_decControl.API_sampleRate = m_nSampleRate;
	int nSamplesInFrame = 20 * m_nSampleRate / 1000;
	int nBytesInFrame = 2 * nSamplesInFrame;
	
	const char* pPayloadCurr = pPayloadData;
	const char* pPayloadEnd = pPayloadData + pPayloadSize;
	
	char* pDestCurr = pDestBuffer;
	char* pDestEnd = pDestBuffer + nDestBufferSize;
	
	while ( pPayloadCurr < pPayloadEnd )
	{
		unsigned short nSize = *(short*)pPayloadCurr;
		pPayloadCurr += 2;
		if ( nSize == 0xFFFF )
		{
			return ( pDestCurr - pDestBuffer ) / 2;
		}
		
		if ( nSize )
		{
			//  [1] Make sure we're not reading past end of our input
			if ( pPayloadCurr + nSize > pPayloadEnd )
				break;
			
			//  [2] Make sure we have enough room in output for a full frame
			if ( pDestCurr + 2 * nBytesInFrame > pDestEnd )
				break;
			
			// Zero out the frame
			memset( pDestCurr, 0, nBytesInFrame );
			
			do
			{
				unsigned short nDecodedSamples = ( pDestCurr - pDestBuffer ) / 2;
				SKP_Silk_SDK_Decode( m_pDecoder, &m_decControl, 0, pPayloadCurr, nSize, pDestCurr, &nDecodedSamples );
				
				pPayloadCurr += nSize;
				pDestCurr += 2 * nDecodedSamples;
				
				Assert( m_decControl.moreInternalDecoderFrames == 0 ); // [3] We shouldn't get this condition in normal contexts
			}
			while ( m_decControl.moreInternalDecoderFrames );
		}
		else
		{
			pDestCurr += nBytesInFrame;
		}
	}
	
	return ( pDestCurr - pDestBuffer ) / 2;
}
```

Some important things to note:
 - At `[1]`, a bounds check is performed to ensure we don't read outside the bounds of the input buffer
 - At `[2]`, a bounds check is performed to ensure we don't write outside the bounds of the output buffer
 - At `[3]`, an assert is performed that `m_decControl.moreInternalDecoderFrames == 0`, however, without running with a debugger attached, this assertion is ignored.

The bug has to do with the do/while loop with `m_decControl.moreInternalDecoderFrames`. Inside the loop, `pPayloadCurr` and `pDestCurr` are both incremented, but the bounds checks at `[1]` and `[2]` aren't repeated.

This means that if `m_decControl.moreInternalDecoderFrames` is true, then we can increment `pDestCurr` past the end of the destination buffer, and overwrite stack data.

#Exploiting the vulnerability
For the PoC, I chose to show this bug working in CS:GO, but any service that also uses the DecompressVoice function is also vulnerable. We can use this bug to crash Steam/CS:GO for any players on the server that our voices are transmitted to.

Note that the PoC simply overwrites the stack with garbage data which leads to a crash, however it is entirely possible for an attacker to overwrite the return pointer on the stack with meaningful data that results in RCE. Doing so requires quite a lot of setup work with the payload to get SILK to decode it to a valid ROP chain, so I simply went with the crash for an easier PoC.

One of the challenges to getting this working is to keep the payload size small. CS:GO has a rate-limit on voice data, so the entire voice packet must be kept under 512 bytes.

To accomplish this, we can build a voice payload that does this:
 -  First, set `nSize` in the payload to 0 multiple times to get `pDestCurr` closer to `pDestEnd` (just over 1 frame away).
 - Next, trigger a call to `SKP_Silk_SDK_Decode` that also sets `m_decControl.moreInternalDecoderFrames` to true. At this point, `pDestCurr` will be incremented by 1 frame, and there will now be less than 1 frame of room in the dest buffer.
 - Trigger another call to `SKP_Silk_SDK_Decode`. Since `m_decControl.moreInternalDecoderFrames` is true, no bounds check is performed. This time there isn't enough room for a frame in the dest buffer and the decode function will overwrite the stack past `pDestBuffer`.

Attached is a compiled version of a public cheat ([CSGOSimple](https://github.com/spirthack/CSGOSimple)) that adds a console command (`send_voice_packet`) to send the voice payloads from a file to the server.

A file that implements this payload is attached as `voice_payload`, which can be fed to the `send_voice_packet` command to replicate the PoC.
*NOTE*: Unrelated for replicating the PoC, but this payload is missing the SteamID/CRC data mentioned above. It is expected to be passed into `CP2PVoiceSingleton::DecompressVoice()` directly, or have the SteamID/CRC added before calling it.

#Replication steps
1) Start CS:GO on device A with `-insecure` launch param and join a server (any empty vanilla server will do, I have one at `s1.slidyb.at` if needed).
2) Extract CSGOSimple.zip from the attachments onto device A and run `injector.exe`. Ensure that it has injected into the CS:GO process successfully by checking if the `send_voice_packet` command exists.
3) Start CS:GO on device B and join the same server.
4) Run `send_voice_packet path\to\voice_payload` in the CS:GO console on device A, where `path\to\voice_payload` is the absolute path to the `voice_payload` file without the `C:`. For example, if the file as at `C:\Users\me\Desktop\voice_payload`, then you would use the command `send_voice_packet Users\me\Desktop\voice_payload`.
5) Steam and CS:GO should both crash on device B.

## Impact

This bug affects any service using the SteamWorks DecompressVoice function, which includes Steam itself and most Source engine titles. It can be used on any other client that can hear voice data from the attacker, including on official Valve matchmaking servers in Source games.

In the best case, it is possible for an attacker to utilize the bug as a DoS to crash other clients, and in the worst case it can lead to RCE by using ROP.

## Attachments
- voice_payload
- CSGOSimple.zip
