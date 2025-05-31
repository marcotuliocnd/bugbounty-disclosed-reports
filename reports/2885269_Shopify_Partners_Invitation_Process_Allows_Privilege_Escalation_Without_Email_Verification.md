# Shopify Partners Invitation Process Allows Privilege Escalation Without Email Verification

## Report Details
- **Report ID**: 2885269
- **URL**: https://hackerone.com/reports/2885269
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-12-06T00:39:03.705Z
- **Disclosed**: 2025-05-15T18:25:56.285Z

## Reporter
- **Username**: mr_asg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## **Summary**
A recent change in Shopify’s invitation process for joining **Shopify Partners** has introduced a vulnerability that allows unauthorized users to gain access to accounts and escalate their privileges without email verification. This report provides a detailed walkthrough of the vulnerability, exploitation method, and potential impact.

## **Vulnerability Details**

### **Issue:**  
- **Invitations to join Shopify Partners no longer require Invitation email link verification.**

{F3818639}

- An attacker can exploit this by creating an account using email addresses of employees at a target organization. Once an invitation is sent to one of these email addresses, the attacker can accept the invitation and gain unauthorized access to the **Shopify Partners** account.

---

## **Steps to Reproduce**

### **Note:**
==The following steps simulate a scenario where a **low-privilege member** discovers an **invited owner** and uses that email address to escalate privileges. This approach simplifies the reproduction steps instead of demonstrating the creation of multiple accounts with different employee emails and waiting for invitations.==

---

### **Reproduction Steps:**

1. **Have a Shopify Partners Account:**
   - Make sure to have a **Shopify Partners account**.

2. **Invite Members and Owners:**
   - Add a new member (attacker-controlled account) to the **Shopify Partners account**.
   - Add a new **owner** (victim's email) to the account.

3. **Harvest the Invited Owner’s Email:**
   - As a **member**, view the email list of invited owners.

4. **Create a New Account Using the Victim’s Email:**
   - Create a new **Shopify** account using the victim’s email address (no email verification required).

5. **Accept the Invitation Using the New Account:**
   - Log into the new attacker-controlled account using the victim’s email.
   - Accept the invitation to join the **Shopify Partners account**, thereby escalating privileges to **Owner**.

---



## **Suggested Mitigation**

To resolve this issue, the following measures are recommended:
- Reintroduce **email verification** for the invitation process to ensure that only the legitimate user can accept invitations.
- Implement **multi-factor authentication (MFA)** on invitations to enhance security and prevent unauthorized access.
- Ensure that invitations and access rights are validated with more robust security protocols.

---


**Additional Information:**
A Proof of Concept (PoC) video is attached to demonstrate the exploit and the steps taken to successfully escalate privileges using the method described above.

████
---

## **Conclusion**
The vulnerability allows unauthorized users to gain access to sensitive **Shopify Partners accounts** and escalate their privileges without proper verification. Immediate attention is recommended to patch this issue and enhance the security of the platform.

---

Please refer to the attached video for a visual demonstration of the exploit.

## Impact

## **Impact Analysis**

### **Internal Escalation by Low-Privilege Member:**
- A **low-privilege member** can escalate their role by exploiting this vulnerability to accept an invitation sent to a victim's email, gaining unauthorized access to **Owner** privileges.

### **External Attack by Unaffiliated Attacker:**
- An **external attacker** can gather email addresses of employees and create accounts using those emails. The attacker can then monitor for invitations and exploit them to gain unauthorized access to the **Shopify Partners account**.

---

## **Security Impact**

This vulnerability enables unauthorized access to **Shopify Partners accounts** and facilitates privilege escalation without proper verification. This is especially concerning as attackers can leverage publicly available email addresses to target potential victims, leading to unauthorized access and modification of sensitive data.

## Attachments
No attachments
