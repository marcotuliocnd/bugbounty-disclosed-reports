# Host Header Injection/Redirection Attack

## Report Details
- **Report ID**: 157465
- **URL**: https://hackerone.com/reports/157465
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-08-07T19:03:20.003Z
- **Disclosed**: 2016-08-07T23:06:12.949Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,

__I'm sorry for adding this, please allow me to close if you do not accept the risk involved.__

Gratipay is vulnerable to host header injection because the host header can be changed to something outside the target domain (ie. gratipay.com and grtp.co) and cause it to redirect to to that domain instead.

Attack vectors are somewhat limited but depends on how the host header is used by the back-end application code. If code references the hostname used in the URL such as password reset pages, an attacker could spoof the host header of the request in order to trick the application to forwarding the password reset email to the attackers domain instead, etc. Other attack vectors may also be possible through manipulation of hyperlinks or other misc. code that relies on the host/domain of the request.

__PoC:__
{F110430}

Regards,
Shuaib Oladigbolu

## Attachments
- gratipay_HHI.png
- Grtp.png
