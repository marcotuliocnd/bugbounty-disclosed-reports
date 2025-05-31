# Expose relay IP in the debug (The source is different from the rendering)

## Report Details
- **Report ID**: 330721
- **URL**: https://hackerone.com/reports/330721
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-03-28T10:22:07.534Z
- **Disclosed**: 2018-07-21T17:57:04.911Z

## Reporter
- **Username**: rbcafe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Greetings,
--

I observed that it was possible to expose the ip of  a relay by doing this :

Poc :
--

- Go to https://sorry.google.com/sorry/misc/
- You must observe this visual.

{F279451}

- Open Tor Browser debug
- You must observe this visual 

{F279452}

Note :
--

You observe that between the debug and the main window there is no relation between the rendered text and the source code. The text discloses the IP of the client while the source discloses the IP of the relay.

Best regards 

@Rbcafe

## Impact

- Get the IP of the relay by changing the ip of the client.

## Attachments
- 1.png
- 2.png
