# TAMS registration details API for admins open at https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/

## Report Details
- **Report ID**: 1061292
- **URL**: https://hackerone.com/reports/1061292
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-18T02:32:53.271Z
- **Disclosed**: 2021-05-07T04:45:11.155Z

## Reporter
- **Username**: skarsom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
## Summary:
TAMS administrators are supposed to approve or deny all registration requests. The dashboard that shows these administrators details of a registration request calls the endpoint `https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/(REGISTRATION_ID)`, where `(REGISTRATION_ID)` is numeric.

This endpoint will, without authentication, return the email, address, phone, attachment IDs, address, corporate info, and user roles. It will also return their request status and denial reason if applicable.

Attachments can then be viewed unauthenticated through `https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/(ATTACHMENT_ID)`.

## Steps To Reproduce:

  1. Navigate to the following URL: https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/2634
  2. For attachments, navigate to the following URL: https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/600

## Recommended Mitigation:
Only allow users with valid JWT tokens for the admin role view these two endpoints.

## Impact

An unauthorized attacker can view personal information about contractors and employees gaining access to TAMS.

## Attachments
No attachments
