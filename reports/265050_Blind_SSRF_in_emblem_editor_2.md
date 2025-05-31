# Blind SSRF in emblem editor (2)

## Report Details
- **Report ID**: 265050
- **URL**: https://hackerone.com/reports/265050
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-31T19:38:53.911Z
- **Disclosed**: 2017-10-28T23:44:08.493Z

## Reporter
- **Username**: alexbirsan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockstargames

## Vulnerability Information
Hello,

As per your recommendation in #233301, I'm submitting a PoC for another blind SSRF in the emblem editor.

To oversight here is allowing absolute `url()` values for the `fill` attribute:

`<path fill="url(https://requestb.in/15rxmgv1#test)" stroke="#a1a1a1"  ... `

Upon publishing an emblem containing such an element, a HTTP request to the given URL is sent from a Rockstar server. (`███`). The destination port can be easily modified. This doesn't seem to work without including a fragment in the URL (`#test` in the example above).

Further testing showed that, if a valid SVG is found at the given URL, the `fill` data is actually used in the final image. Fortunately, ████████ doesn't seem to support scripts, although the possibility of finding another way to exfiltrate data doesn't seem that out of reach.

I've attached the full body of the emblem I've used to confirm this bug for ease of reproduction.

## Attachments
No attachments
