# Throttling Bypass - ws1.dashlane.com

## Report Details
- **Report ID**: 225897
- **URL**: https://hackerone.com/reports/225897
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-03T18:09:34.753Z
- **Disclosed**: 2017-07-30T03:27:44.525Z

## Reporter
- **Username**: corb3nik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dashlane

## Vulnerability Information
# Description
The host at ws1.dashlane.com throttles requests based on the IP address of the user after a certain amount of repeated requests.
By adding the `X-Forwarded-For` header, an attacker can bypass the throttling completely, rendering the security measure ineffective against DOS attacks. 

# Proof of concept
1. Send a large amount of requests like the following until a `{"error":{"code":-32600,"message":"Throttled."}}` message is received.
2. Send another request with an added `X-Forwarded-For` header : 
3. The web server will respond with a successful message instead of a throttled response.

I have attached two screenshots demonstrating the proof of concept.

Thank you,

Ian

## Attachments
- throttled.png
- bypassed.png
