# Reflected Xss  https://██████/

## Report Details
- **Report ID**: 759418
- **URL**: https://hackerone.com/reports/759418
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-16T14:02:42.015Z
- **Disclosed**: 2021-10-18T19:28:55.426Z

## Reporter
- **Username**: 0xelkomy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello security all teams
**Relevant Products/Components:**
last version

**Detailed Description:**
Reflected XSS so have high impact.

**Steps To Reproduce:**

1-go in subdomain
2-and check url if tableau uses
3-Uses you can add this redirect dir in url with Authentication redirect:-
/en/embeddedAuthRedirect.html?auth=javascript:alert(%22xElkomy%22)

**Such as**

 https://████████/en/embeddedAuthRedirect.html?auth=javascript:alert(%22xElkomy%22)

**Browsers Verified In:**
all browsers supporting javascript

**Supporting Material/References:**
███

**Access Vector Required for Exploitation:**

no required any access but need only web access :)

**Vulnerability Exists in Default Configuration?:**
yes

**Exploitation Requires Authentication?:**
no need anything



#xElkomy

## Impact

The need for an external delivery mechanism for the attack means that the impact of reflected XSS is generally less severe than stored XSS, where a self-contained attack can be delivered within the vulnerable application itself.

## Attachments
No attachments
