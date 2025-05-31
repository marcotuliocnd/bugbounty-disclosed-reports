# Ability to Add and Verify Uncontrolled Mobile Numbers Leading to Account Takeover (ATO)

## Report Details
- **Report ID**: 2762462
- **URL**: https://hackerone.com/reports/2762462
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-10-07T02:52:17.165Z
- **Disclosed**: 2025-03-04T13:30:06.992Z

## Reporter
- **Username**: trev0ck
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary
A critical vulnerability was identified in the OTP verification process on the shop.mtn.ng platform, which allows attackers to add and verify mobile numbers that they do not control. By tampering with the OTP verification request, an attacker can link a victim's mobile number to their account. This leads to an Account Takeover (ATO) scenario where the attacker gains full access to the victim's account without owning or controlling the victim's phone number.

## Steps to Reproduce

###  Initiate OTP Request
- Begin the login or registration process on the platform.
- Enter a valid mobile number (MSISDN) and request an OTP.

### Capture OTP Verification Request
- Use a proxy tool like **Burp Suite** or **Caido** to intercept the OTP verification request when submitting the OTP.
- The intercepted request will look like this

```http
POST /mtn_otp/index/verification/ HTTP/2
Host: shop.mtn.ng
Content-Type: application/x-www-form-urlencoded
Content-Length: 53

ajax=1&action=verifyotp&msisdn=█████████&otp=█████████
```
### Manipulate Server Response

- Upon capturing the request, submit an incorrect OTP to receive the server's response

```json
{
  "status": 400,
  "message": "Invalid OTP",
  "msisdn": "2347037855490",
  "success": false
}
```

Modify the response in the intercepted traffic to indicate a successful verification

```json
{
  "status": 200,
  "message": "success",
  "msisdn": "2347037855490",
  "success": true
}
```
This will trick the client into thinking that the OTP was successfully verified, even though the OTP is incorrect.

- The manipulated server response now grants full access to the victim's phone number account. Even though the OTP was incorrect, the altered response bypasses the verification, which could allow the attacker to log in as the target user.

## NOTE I do not own this phone number at all and as you can see it is now linked to my account
{F3659097}

# Root Cause

- The application fails to protect against the manipulation of the OTP verification response. The server does not perform integrity checks on the response sent back to the client, allowing attackers to alter it and bypass OTP verification entirely.

## Impact

An attacker can exploit this flaw to hijack user accounts by manipulating the OTP verification response. This allows the attacker to

1. Access personal user information such as names, phone numbers, and email addresses.
2. Modify sensitive account settings like passwords, linked emails, and phone numbers.
3. Perform unauthorized actions such as transactions or purchases.
4. Further escalate the attack to other services connected to the victim's account.

## Attachments
- image.png
