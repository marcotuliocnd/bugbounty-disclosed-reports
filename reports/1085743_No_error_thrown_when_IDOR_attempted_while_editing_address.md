# No error thrown when IDOR attempted while editing address

## Report Details
- **Report ID**: 1085743
- **URL**: https://hackerone.com/reports/1085743
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-24T05:06:42.298Z
- **Disclosed**: 2021-04-26T05:45:45.249Z

## Reporter
- **Username**: merbin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: openmage

## Vulnerability Information
## Summary:
demo.openmage.org application having features to add, edit and delete addresses. When a user tries to edit the address of another user, the server adds a new address with a new id on the attacker's account. By sending it to an intruder, an attacker may cause Dos.

## Steps To Reproduce:

  1. Create two user accounts demo.openmage.org with different emails
  2. Add addresses on both accounts
  3. Edit the address on account 1 and capture the request on burp and send it to the repeater
  4. Replace the ID of the address on both GET request and referee header with the ID of the address of the account 2
  5. Submit the request, Now you can see a new address is added on account 1 with a new ID.
(here, when an attacker try to edit the address of another user, the server should not create new address)
  6. Now Send the same request to intruder with the id of the address of the victim, and set payload as null byte
  7. Start attack with min 60 threads
  8. Now you can see many addresses is added on user account 1. and soon you will see 503 Error code

## Supporting Material/References:


  * {F1169693}

## Impact

* It may cause  Dos

## Attachments
- Kazam_screencast_00000.mp4
