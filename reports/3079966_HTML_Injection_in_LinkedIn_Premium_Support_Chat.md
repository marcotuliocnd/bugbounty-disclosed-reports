# HTML Injection in LinkedIn Premium Support Chat

## Report Details
- **Report ID**: 3079966
- **URL**: https://hackerone.com/reports/3079966
- **State**: Closed
- **Severity**: low
- **Submitted**: 2025-04-06T17:28:07.539Z
- **Disclosed**: 2025-05-07T07:53:59.481Z

## Reporter
- **Username**: nagu123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
**Summary:**  
A vulnerability exists in the LinkedIn Premium support chat interface where unsanitized HTML input is rendered directly in the chat window. An attacker can exploit this by injecting malicious HTML such as clickable links, potentially leading to phishing or redirection attacks on LinkedIn support staff.

**Steps to Reproduce:**

1. Go to [https://www.linkedin.com/feed](https://www.linkedin.com/feed) and log in to your LinkedIn account.

2. On the left sidebar, under **"Job search smarter with Premium"**, click **"Try for ₹0"**.

3. You will be redirected to this URL:  
   `https://www.linkedin.com/premium/survey/?destRedirectURL=https%3A%2F%2Fwww.linkedin.com%2Fsearch%2Fresults%2Fall%2F%3Fkeywords%3Dtest%2520card%2520bugbounty%26origin%3DGLOBAL_SEARCH_HEADER%26sid%3Dn%253Bl`

4. Once the page loads, wait for the support chat widget to appear in the **bottom-right corner**.

5. Open the chat window and send the following input:  
   ```html
   <a href="https://evil.com">CLICK</a>
   ```

6. The input is rendered as an **actual clickable link** in the chat interface.

7. If a LinkedIn support employee views the message and clicks the link, they are redirected to an external site, which could be used for phishing or other malicious purposes.

{F4223329}

**Impact:**  
- HTML injection in a support chat poses risks of phishing, social engineering, or redirection attacks.
- It breaks the assumption of trust in support systems.
- If used cleverly, attackers could mimic internal LinkedIn UI elements to trick employees into further interaction.

**Security Risk:**  
- **HTML Injection**
- **Phishing/Social Engineering Risk**
- **Potential for Clickjacking or Further Exploits**

**Expected Behavior:**  
User input in chat should be sanitized and rendered as plain text. No HTML or tags should be interpreted.

**Observed Behavior:**  
HTML, such as `<a>` tags, is rendered in the chat and appears clickable to support agents.

**Severity:**  
**Medium** (may be increased based on internal LinkedIn threat models)

**Recommendation:**  
- Sanitize user input using libraries like DOMPurify.
- Encode all user-generated content before rendering.
- Review all chat-related components for similar injection points.

## Impact

### 🔸 1. **Phishing Attacks Against LinkedIn Employees**  
By injecting a crafted HTML link (e.g., `<a href="https://malicious-site.com">CLICK HERE</a>`), the attacker can:
- Trick LinkedIn support staff into visiting malicious websites
- Lead them to phishing pages mimicking LinkedIn internal portals
- Attempt to harvest credentials or trigger malware downloads

---

### 🔸 2. **Social Engineering and Internal Trust Exploitation**  
Since the injected content appears in the official LinkedIn chat interface:
- It can be used to impersonate UI elements or instructions (e.g., "Click here to fix the issue")
- Employees may trust and act on malicious instructions

---

### 🔸 3. **Reputation and Legal Risk for LinkedIn**  
If an employee clicks on a malicious link and gets compromised, this could:
- Lead to unauthorized access to internal tools or user data
- Trigger compliance or data protection issues

---

### 🔸 4. **Potential Pathway to Escalation**  
Although currently limited to HTML injection:
- If any future misconfiguration allows JavaScript execution, it could escalate to stored/reflected XSS
- This could lead to full session hijacking or internal system compromise

---

## Attachments
- Screencast_From_2025-04-06_22-30-15.mp4
