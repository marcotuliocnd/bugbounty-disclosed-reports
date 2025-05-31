# TLS client authentication can be bypassed due to ticket resumption

## Report Details
- **Report ID**: 2978267
- **URL**: https://hackerone.com/reports/2978267
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-02-06T13:18:17.741Z
- **Disclosed**: 2025-05-27T13:18:05.989Z

## Reporter
- **Username**: snhebrok
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
*If you require the PoC, we can also attach it. As this issue is resolved and fixed, we assume this not to be required.*

TLS session tickets are not properly isolated for multiple virtual hosts in one server.
That is, a ticket issued for one virtual host, may be resumed at a different virtual host.
Using this, we were able to circumvent client authentication in the following scenario:
Two hosts need to enable client authentication. The attacker should only be able to access one but not the other.
The attacker was still able to access the second site nonetheless.

We found that tickets are always resumed. If the HTTP host header and TLS SNI value diverge, the server correctly returns a 421 (if client authentication is used). However, if the SNI is chosen appropriately (changed to resumption host, or omitted), nginx allows the Host header to specify the second site.

## Impact

We were able to circumvent client authentication. More specifically, if two sites (A and B) both use client authentication (but with different configurations), we could resume a TLS session from A at B. This achieves privilege escalation:
Consider a user who is allowed to access A, but not B. They can connect to A, receive a ticket, and using that ticket access B.

Further, nginx uses the wrong key material on the second virtual host to encrypt the tickets. We do not see a direct impact for this, other than the privilege escalation.

## Attachments
No attachments
