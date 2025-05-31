# Password authentication at newsletter.nextcloud.com discloses username list

## Report Details
- **Report ID**: 476439
- **URL**: https://hackerone.com/reports/476439
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-08T09:59:42.261Z
- **Disclosed**: 2020-03-01T11:00:36.833Z

## Reporter
- **Username**: br3ach
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**summary:**
A vulnerability classified as problematic has been found in OpenSSH 7.2p2. check (INFO.png)Affected is an unknown function of the component Authentication. The manipulation of the argument Password with an unknown input leads to a information disclosure vulnerability (Username). CWE is classifying the issue as CWE-200. This is going to have an impact on confidentiality.
The weakness was disclosed 07/14/2016 by Eddie Harari as opensshd - user enumeration as confirmed mailinglist post (Full-Disclosure). The advisory is available at seclists.org. The vendor was not involved in the coordination of the public release. This vulnerability is traded as CVE-2016-6210 since 07/13/2016. It is possible to launch the attack remotely. The exploitation doesn't require any form of authentication. Technical details and a public exploit are known.

**POC**
download POC.py and write the next command. (you can try with any word-list or just use some random names like I did)
- LINK: https://www.exploit-db.com/exploits/40136
- CODE: python
Command:
python POC.py newsletter.nextcloud.com -U usernames.txt

OUTPUT:
check (POC.png)

in this case user whose time < 0.04717744470807732 is non existing user
I tried with a small usernames list for POC, attacker will use a big list like rockyou.txt that on Kali Linux by default.

## Impact

Allows remote attackers to enumerate users by leveraging the timing difference between responses when a large password is provided.

## Attachments
- POC.png
- INFO.png
