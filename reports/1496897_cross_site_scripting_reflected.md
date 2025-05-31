# cross site scripting reflected 

## Report Details
- **Report ID**: 1496897
- **URL**: https://hackerone.com/reports/1496897
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-01T22:15:56.676Z
- **Disclosed**: 2024-09-09T14:38:09.649Z

## Reporter
- **Username**: alitoni224
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
[cross site scripting reflected]

## Steps To Reproduce:
[at first hello
[Found that via the script site payload is reflected  '-alert(1)-' It was tested on Chrome and Firefox browsers as shown in the pictures below   ]

  1. [Simply open the link https://mtn-investor.com/mtn-cmd/index.php ]
  1. [In the search button, enter the payload  '-alert(1)-'  ]
  1. [You will notice the reflection]

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [https://owasp.org/www-community/attacks/xss/]

## Impact

As in any vulnerability via scripted sites. The top line is that an attacker might steal cookies to abuse users' session.
- phishing scam
- Some important input data stolen

## Attachments
- PoC_Chroom.png
- PoC_Firfox.png
