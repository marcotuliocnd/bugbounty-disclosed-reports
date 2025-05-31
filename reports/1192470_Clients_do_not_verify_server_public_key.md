# Clients do not verify server public key

## Report Details
- **Report ID**: 1192470
- **URL**: https://hackerone.com/reports/1192470
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-11T19:53:21.365Z
- **Disclosed**: 2021-09-23T12:25:24.232Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So this is related to https://hackerone.com/reports/1189162 but also to your RFC

Bear with me because there is going to be some hand waving here and there. Since not everything is implemented yet from your RFC.

Right now what happens is: https://github.com/nextcloud/end_to_end_encryption_rfc/blob/master/RFC.md#initial-device
The missing step there is that the returned certificate in step 4 is verified by the client to be signed by the actual server.

This serves multiple purposes.

1. It will allow clients to detect (more easily) if the server has been compromised. For example if public key changed
2. The sharing described there does require the client to check the certificate of another user against the servers certificate. However without making sure that is the same certificate as your key this check is not that useful

(This is for now ignoring the fact that a compromised server can issue any cert they want, HSM and CT would really help a lot here!)

To summarize. Clients should:

1. on initial setup verify that their certificate is signed by the public key of the server
2. on adding a new device they should also verify their obtained public key is signed by the server

## Impact

Currently there is nothing stopping a compromised server from sending each client a different public key for the server. And upon sharing (once implemented) people would not even notice that both their keys are signed by a different server CA.

I believe this check is somewhat implied in the RFC but not made explicit. And hence non of the clients do this.
Currently I do not see a big impact. But this should be fixed to make your end to end encryption more robust and less prone to be broken in the future.

## Attachments
No attachments
