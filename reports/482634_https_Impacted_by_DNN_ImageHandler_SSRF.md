# https://████████ Impacted by DNN ImageHandler SSRF

## Report Details
- **Report ID**: 482634
- **URL**: https://hackerone.com/reports/482634
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-19T18:00:45.913Z
- **Disclosed**: 2019-10-08T18:43:17.892Z

## Reporter
- **Username**: warsong
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Summary:
https://███████ runs DNN 8.0.0 to 9.1.1 and is impacted by CVE 2017-0929 allowing for a SSRF through the DNN ImageHandler. Origin servers will request any image file supplied by the attacker. This allows for internal NIPR sites to be mapped and accessed through a vulnerable host. The attack is limited by file extension.

Impact
Vulnerable site allows interaction with internal NIPR sites. Pulling default image files from internal NIPR sites verifies the site is online and responsive. Discloses origin IP addresses, and could be manipulated further.  This could also be used as a defacement technique making the sight display images of radical ideologies or pornography.  

Step-by-step Reproduction Instructions
Access the DNN image handler on the vulnerable site.
Supply Burp collaborator payload (working on free burp right now and cannot provide a collab payload) or external attacker controlled image for SSRF trigger.
Payload Example:
https://█████/DnnImageHandler.ashx?mode=file&url=http://1.bp.blogspot.com/-q19YK-T_wAU/UdpDm76jIgI/AAAAAAAAAWo/yjeRx4Vet80/s400/meme11.jpg

https://████████/DnnImageHandler.ashx?mode=file&url=http://www.███/data/uploads/images/DC3_seal.png

Product, Version, and Configuration
DNN 8.0.0 to 9.1.1 with ImageHandler exposed.

Suggested Mitigation/Remediation Actions
Upgrade to DNN 9.2.0 or later. If upgrading isn't possible, consider blocking requests to ImageHandler if it is unused.

## Impact

Recommend High Severity: Vulnerable site allows interaction with internal NIPR-Only sites. Pulling default image files from internal NIPR sites verifies the site is online and responsive. Discloses origin IP addresses, and could be manipulated further to cause harm on internal NIPR sites. This could also be used as a defacement technique making the sight display images of radical ideologies or pornography.

## Attachments
No attachments
