# Snowflake server: Leak of TLS packets from other clients

## Report Details
- **Report ID**: 1880610
- **URL**: https://hackerone.com/reports/1880610
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-02-21T11:13:54.342Z
- **Disclosed**: 2023-03-15T07:29:09.416Z

## Reporter
- **Username**: hazae41
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
## Summary:
This issue is related to the Snowflake pluggable transport server. 
It seems Snowflake clients receive "ghost" packets at the KCP layer, that encapsulate TLS packets unrelated to the current session.
Those TLS packets are from other clients, and contain handshake record, application data, or other TLS stuff.

## Steps To Reproduce:
Just run a Snowflake client and it will start receiving ghost packets.

## Setting up KCP logging:

1. Git clone the Snowflake client
2. Open VSCode or similar editor
3. In the `torrc` file,  setup logging with `ClientTransportPlugin snowflake exec ./client -log snowflake.log`
4. Open `./lib/snowflake.go`, search `kcp.NewConn2`, right click then `Go to definition`
5. Search `readLoop`, right click then `Go to definition`
6. Right click on `defaultReadLoop` then `Go to definition`
7. Now just under the line where it says `s.conn.ReadFrom(buf)`, add the line `log.Println("kcp <-", buf)`
8. Now start Tor with Snowflake using `tor -f ./torrc`
9. Open `./snowflake.log`

## Inspecting

Notice that the KCP layer receive bytes not starting with the regular KCP header:

{F2187164}

`X X X X 81 0 255 255 ...`

4 little-endian bytes for the conversation ID, then 81/82 for the command, then 0, then 255 255 (little-endian) for the window size.

This is an issue because KCP packets, just like TCP packets, are segments, and are never segmented themselves.

So, KCP doesn't recognize those ghost packets and discard them.

In `Input`

{F2187165}

In `kcpInput`, which calls `Input`

{F2187166}

They are completely discarded and never reach the upper layer, that's why this has never been noticed.

So, what are those packets? 

Some look like SMUX packets: 

{F2187167}
 
`2 2 L L S 0 0 0`

2 for the SMUX version, 2 for the psh command, 2 little-endian bytes for the length, and 4 little-endian bytes for the stream.

By the way, the stream ID is always set to 3, which is a proof that those packets are from other clients, as if you change the default SMUX stream ID to something else (in the SMUX code), you will still receive those packets from stream 3.

 Some other look like KCP packets, but the conversation ID is not the same as other KCP packets:

{F2187168}

If you Cmd+F these bytes, you will not find any other occurence, so you never had this conversation ID, which is another proof that those packets are from other clients, and not from a previous connection.

Those KCP packets also contains a SMUX packet:

{F2187169}

Now, the creepy part is that both those packets contain TLS packets:

{F2187171}

{F2187172}

{F2187173}

20/21/22/23 for the record type (handshake, application data, ...), then 3 3 (big-endian) for the TLS version (which is 1.2), then the TLS fragment (encrypted if type 23)

{F2187174}

Notice that in the following screenshot, we have a ghost packet containing TLS application data (23) before our normal packets containing TLS handshake data (22)

{F2187175}

This is another proof that the ghost packets are from another TLS connection, as it would be impossible to get TLS application data before handshake data (except if renegociation, which is not the case here as it's a fresh new connection)

## Conclusion

All this leads to the conclusion that the Snowflake server is leaking TLS packets to clients from other clients.

This would still need further investigation: 
- Why is this occuring?
- Is the Snowflake client leaking too?
- Can we exploit this? To deanonymize people?

While we don't know those answers, this issue must be considered with high severity.

## Impact

Even if it seems we can't modify those packets or exploit the TLS protocol, this issue still needs further investigation in order to show its real impact, as it could possibly deanonymize users.

## Attachments
- Capture_d_e_cran_2023-02-21_a__10.51.11.png
- Capture_d_e_cran_2023-02-21_a__10.53.28.png
- Capture_d_e_cran_2023-02-21_a__10.54.45.png
- Capture_d_e_cran_2023-02-21_a__11.06.20.png
- Capture_d_e_cran_2023-02-21_a__11.22.31.png
- Capture_d_e_cran_2023-02-21_a__11.24.55.png
- Capture_d_e_cran_2023-02-21_a__11.27.49.png
- Capture_d_e_cran_2023-02-21_a__11.28.58.png
- Capture_d_e_cran_2023-02-21_a__11.30.11.png
- Capture_d_e_cran_2023-02-21_a__11.31.19.png
- Capture_d_e_cran_2023-02-21_a__11.44.29.png
