# HTTPS is not validating TLS mac codes

## Report Details
- **Report ID**: 402671
- **URL**: https://hackerone.com/reports/402671
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-08-30T02:29:52.957Z
- **Disclosed**: 2019-05-25T14:26:47.393Z

## Reporter
- **Username**: cy1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
https://twitterflightschool.com is prone to POODLE and also a stronger variant of POODLE which allows a MITM attacker to actively decrypt bytes from an HTTPS request.
This attack is possible because the device terminating this TLS connection responds differently to a bad record mac when the last byte (e.g. padding) is 0x00.

My test tool recognized this by sending a series of connections with malformed mac/padding on a GET request.
This differs from POODLE scanning in that my tool tests how stacks respond to padding errors on application data rather than handshake messages.
The tool establishes a connection and sends a GET request with length such that it will need 16 bytes of padding.

https://twitterflightschool.com responds with an HTTPS response and no TLS error when it receives a request ending 0x00.
This is a unique behavior from how it responds when the padding is correct but the mac is wrong or when the padding is malformed (e.g. random).

To exploit this, a MITM attacker can replace the last block (padding block) with a targeted ciphertext block as is done in POODLE.
The difference here is that the attacker can also select specific bytes for the last byte of the previous ciphertext.
The attacker can calculate the output from the block cipher decryption by guessing a plaintext byte.
This byte is then placed at the end of the second to last ciphertext block.
If the guess is correct, the decryption of the target block xor'd with that byte yields 0x00 for the plaintext.
This is observed by the attacker based on the lack of error and/or presence of an encrypted application data response.

The attack requires a MITM attacker to be able to inject JavaScript into the connection of some victim who has an authenticated session to an affected domain. This JavaScript will trigger a series of controlled HTTPS requests which are then rearranged by the attacker while monitoring for the bad record mac alert. After an average of 256 connections, the attacker learns the value of a targeted secret byte (i.e. from an auth cookie) and then changes the request length to repeat this process for the next byte until the full secret is recovered.

Supporting Material/References
---------------------------------

I am attaching a packet capture and premaster secret list so that the packet capture can be decrypted in Wireshark.

To decrypt this, enter Wireshark preferences, then select protocols -> SSL and specify the path to the .pms file as '(Pre)-Master-Secret log filename' and set "SSL debug file" to point to a new file.

After opening the supplied pcap with the provided logged Premaster-Secret data, you can see that there are 10 TCP streams:
- tcp.stream eq 0 : Proper HTTPS GET request/response
- tcp.stream eq 1 : ***Response Received (non-deterministic padding bytes ending 0x00)***
- tcp.stream eq 2 : EOF (All padding bytes 0xff)
- tcp.stream eq 3 : EOF (Non-deterministic values with proper length)
- tcp.stream eq 4 : EOF (All padding bytes 0x80)
- tcp.stream eq 5 : ***Response received (corrupted last byte of mac)***
- tcp.stream eq 6 : ***Response received (padding ends with 0x00 and mac is broken)***
- Streams 7-9 all receive EOF for various other padding errors

As you can see, an attacker can select a value to insert as the last byte of the second to last ciphertext and have an oracle to know whether the last byte of the last ciphertext block (e.g. padding byte) corresponding to a plaintext 0x00.

Explaining GOLDENDOODLE (POODLE's fiercer cousin)
--------------------

The mitm attacker would inject some JavaScript into an HTTP session of the victim or otherwise get them to load JavaScript from any domain. (e.g. there is no XSS needed) This JavaScript triggers HTTPS requests to the targeted server with precise alignment so that the attacker can roughly know how the request will be broken into blocks. As the request is received, the handshake is allowed to complete but when application data from the client is received, the attacker will copy a ciphertext block containing some secret value (e.g. a cookie) and use it to replace the last block. 

The attacker then starts with some initial guess value and XORs this with the last byte of the block prior to the targeted ciphertext block. This reveals what the intermediate value from the block cipher decryption would be if the guess is correct. The last byte of the second to last ciphertext block is now set to this calculated byte and the packet is passed along to the server. If the server disconnects, the attacker waits for the next request and tries again with the next possible value. If the server sends back data, it has confirmed the attacker's guess.

The bottom line is that a GOLDENDOODLE oracle can be exploited to decrypt HTTPS requests considerably faster than POODLE if the secret value is in a known character set. (POODLE requires an average of 256 requests per byte.)

## Impact

An attacker with mitm of a victim authenticated to this domain could use a practical attack to break the confidentiality of HTTPS and recover cookie values or other data sent to the server.

## Attachments
- twitterflightschool.pcap
- twitterflightschool.pms
