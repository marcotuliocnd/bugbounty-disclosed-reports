# Lack of Rate Limiting on Account Creation Endpoint  

## Report Details
- **Report ID**: 2915502
- **URL**: https://hackerone.com/reports/2915502
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-12-27T17:20:11.221Z
- **Disclosed**: 2025-01-16T11:23:16.436Z

## Reporter
- **Username**: nagu123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
---

**Title:** Lack of Rate Limiting on Account Creation Endpoint  

**Description:**  
The **`/account/signinform/premium_tour_login`** endpoint on **██████████** lacks rate limiting, allowing attackers to automate the account creation process. This vulnerability can be exploited to generate a large number of fake accounts by automating requests using tools like Burp Suite's Intruder.

**Endpoint Affected:**  
`POST /account/signinform/premium_tour_login`  
Host: `█████`

**Steps to Reproduce:**  
1. Navigate to the account creation page on **███**.  
2. Fill in the required details such as email, username, and password.  
3. Intercept the HTTP POST request using Burp Suite.  
4. Send the captured request to Burp Suite's Intruder.  
5. Configure the ████████ position in the email field. For example, replace `████████` with `████`.  
6. Set the ██████████ type to numbers and range it from `0` to `1000`.  
7. Start the attack.  
8. Observe that the server processes all requests successfully, creating accounts without rate limiting or CAPTCHA validation.

█████████

**Impact:**  
This vulnerability can lead to:  
- Creation of numerous fake accounts, overwhelming legitimate user registrations.  
- Exploitation by malicious actors for bot-related activities, such as spamming or abusing the platform.  
- Increased server resource usage and potential degradation of service.  

**Suggested Fixes:**  
- Implement a rate-limiting mechanism for the affected endpoint. For example:  
  - Limit requests to a maximum of 5 per minute per IP address.  
- Introduce CAPTCHA verification during the account creation process to prevent automated requests.  
- Enforce email verification to finalize the account registration process.  

**Proof of Concept (PoC):**  
1. Intercepted request (example):  
   ```
   POST /account/signinform/premium_tour_login HTTP/1.1  
   Host: ████  
   Content-Type: application/x-www-form-urlencoded  
   Content-Length: 120  

   email=██████████&password=████████&username=█████
   ```
████████

2. Screenshot or logs from Burp Suite Intruder showing multiple successful account creation responses for email variations (e.g., `███`, `████`, etc.).
  
█████

## Impact

### ** Impact**:  
- **Account Flooding**: Automated creation of fake accounts overwhelms the system.  
- **Abuse & Spamming**: Fake accounts can be used for malicious activities.  
- **Degraded Performance**: Slower system performance for legitimate users.  
- **Data Exposure**: Sensitive user data may be leaked.  
- **Reduced Integrity**: Compromised user data and increased security risks.  
- **Availability Issues**: Server overload impacting system availability.

## Attachments
No attachments
