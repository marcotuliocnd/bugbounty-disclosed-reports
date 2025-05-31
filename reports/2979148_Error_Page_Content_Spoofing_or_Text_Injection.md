# Error Page Content Spoofing or Text Injection

## Report Details
- **Report ID**: 2979148
- **URL**: https://hackerone.com/reports/2979148
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2025-02-06T18:43:36.247Z
- **Disclosed**: 2025-02-07T15:44:41.498Z

## Reporter
- **Username**: mcblockchamp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
{F4027663}

**Title: Error Page Content Spoofing or Text Injection**

**URL:**  
[https://www.xvcams.com/assets/!!!ATENTION!%20This%20server%20is%20on%20Maintenance%20please%20go%20to%20WWW.EVIL.COM](https://www.xvcams.com/assets/!!!ATENTION!%20This%20server%20is%20on%20Maintenance%20please%20go%20to%20WWW.EVIL.COM)

---

https://www.xvcams.com/assets/%0A%0A%0A----------------------------------------------------%0A!!!CONGRATULATIONS!!!%0A--------------------------------------------------------------------------------------------------%0AYour%20Bug%20Bounty%20Report%20Has%20Been%20Approved!%0A%0AYou%20Have%20Been%20Rewarded%20$1500%20for%20Your%20Vulnerability%20Report.%0A%0ATo%20Claim%20Your%20Reward,%20Please%20Login%20to%20Your%20HackerOne%20Account%20or%20Go%20Here:%20WWW.FAKE-CLAIM.COM

---

### **Description:**

Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

---

### **Steps to Reproduce:**

1. Open a web browser and navigate to the target.
2. Target: [https://www.xvcams.com/assets/](https://www.xvcams.com/assets/)
3. Add any text or content after the `/` in the URL.
4. Example:
   ```
   !!!ATENTION!%20This%20server%20is%20on%20Maintenance%20please%20go%20to%20WWW.EVIL.COM
   ```

And

   ```
%0A%0A%0A----------------------------------------------------%0A!!!CONGRATULATIONS!!!%0A--------------------------------------------------------------------------------------------------%0AYour%20Bug%20Bounty%20Report%20Has%20Been%20Approved!%0A%0AYou%20Have%20Been%20Rewarded%20$1500%20for%20Your%20Vulnerability%20Report.%0A%0ATo%20Claim%20Your%20Reward,%20Please%20Login%20to%20Your%20HackerOne%20Account%20or%20Go%20Here:%20WWW.FAKE-CLAIM.COM
   ```

5. The browser reflects the content or text injected in the URL.

---

### **References:**

1. [https://hackerone.com/reports/327671](https://hackerone.com/reports/327671)
2. [https://hackerone.com/reports/498562](https://hackerone.com/reports/498562)
3. [https://hackerone.com/reports/106350](https://hackerone.com/reports/106350) ($250 bug bounty)

## Impact

This attack is typically used as, or in conjunction with, social engineering because it exploits a code-based vulnerability and a user's trust. As a side note, this attack is widely misunderstood as a kind of bug that brings no impact.

## Attachments
- image.png
