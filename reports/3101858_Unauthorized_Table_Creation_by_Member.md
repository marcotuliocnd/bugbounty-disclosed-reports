# Unauthorized Table Creation by Member

## Report Details
- **Report ID**: 3101858
- **URL**: https://hackerone.com/reports/3101858
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-04-20T18:56:08.039Z
- **Disclosed**: 2025-04-23T19:06:06.262Z

## Reporter
- **Username**: mous_haxk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
## Summary:
A member user is able to create tables inside restricted company data spaces, despite the UI indicating that only workspace builders (admins) should be allowed. The “Add Data” button appears disabled in the UI, but it is still interactable and functional. Upon clicking it, the member can proceed to create and save a new table successfully.

## Steps To Reproduce:

1. Log in as a member user.
2. Navigate to the restricted data space where only builders should have write access.
3. Click the (visually disabled) “Add Data” button.
4. Select “Create Table.”
5. Fill in the required inputs and click “Save.”
6. Observe that the table is successfully created, despite the user lacking the proper permissions.

## Supporting Material/References:

█████████

## Impact

Unauthorized data manipulation by lower-privileged users. This could lead to data tampering, workspace clutter, or information leakage, depending on how the data is later handled and exposed.

**Recommendation:**  
Enforce access control server-side by validating user roles before allowing data creation. Never rely solely on front-end/UI restrictions to protect sensitive functionality.

## Attachments
No attachments
