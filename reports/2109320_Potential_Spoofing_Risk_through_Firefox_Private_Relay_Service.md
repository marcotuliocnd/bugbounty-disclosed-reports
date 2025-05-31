# Potential Spoofing Risk through Firefox Private Relay Service

## Report Details
- **Report ID**: 2109320
- **URL**: https://hackerone.com/reports/2109320
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-14T16:13:15.045Z
- **Disclosed**: 2023-10-13T10:16:47.576Z

## Reporter
- **Username**: nicholas_cw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
** Note: This is a duplicate of Bugzilla Report Bug ID: 1755749.**


The problem: adversaries can leverage Firefox’s Relay service to send spoofing emails to users. The current Relay design increases the chance for the spoofing emails to reach the target inbox that would be otherwise blocked.

Root causes:
(1) The forwarding system re-composes the entire email with a new HTML template and also re-writes the “From:” header as “@relay.firefox.com”. This removes/invalidates the signatures of DKIM and ARC headers.

(2) “@relay.firefox.com” and the IP of Firefox Relay have a high reputation, which bumps the trust of the forwarded spoofing emails. For these two reasons, a spoofing email that would otherwise be blocked (or placed into the spam folder) can enter the user's inbox.

Proof-of-concept:

Step 1: Pick a spoofing target domain. We tried domains with different DMARC policies: “none”, “quarantine”, and “reject”. All three cases worked. Specifically, we tested spoofing targets as “illinois.edu”, “usenix.org”, and “nicehash.com”

Step 2: Craft a spoofing email with the forged “From:” in the header

Step 3: Send the email to the “Firefox Relay” victim address

The email enters the target user's inbox, without any warnings as long as the email is successfully delivered to @relay.firefox.com SMTP server.

We noticed that even when the spoofed domain has DMARC=reject (i.e., nicehash.com), Firefox Relay will forward the emails. The modified emails can then enter the user's inbox. See the screenshot attached (our forged login notification from nicehash.com).

Our Recommendations:
(1). Relay should perform authentication and drop emails with failed DMARC (especially for sender policy=“reject”).
(2). Relay should perform ARC validation and sealing to maintain the integrity of the ARC chain.
(3). By default, Relay should not modify the original email, nor re-composing a new one with Firefox's template && forwarded content.

Explanations: if the incoming email has DKIM, because of (3), the DKIM signature will still be valid when the email reaches the receiver, which makes DMARC pass (i.e., no harm on deliverability). If the incoming email does not have DKIM but has SPF, the above recommendations might hurt deliverability when (a) the sender’s DMARC policy is “reject”/“quarantine” and (b) SPF=“pass” at the relay. Under this condition, the relay may consider modifying “From” to ensure deliverability. In this case, because SPF is “pass” at the relay (i.e., email authenticity is verified), modifying “From” does not introduce additional risks to the receiver. If the incoming email does not have DKIM or SPF, the above recommendations also do not hurt deliverability.

Best regards,

## Impact

Adversaries can leverage Firefox’s Relay service to send spoofing emails to users. The current Relay design increases the chance for the spoofing emails to reach the target inbox that would be otherwise blocked.

## Attachments
No attachments
