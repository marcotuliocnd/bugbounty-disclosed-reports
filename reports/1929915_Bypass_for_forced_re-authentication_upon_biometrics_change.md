# Bypass for forced re-authentication upon biometrics change

## Report Details
- **Report ID**: 1929915
- **URL**: https://hackerone.com/reports/1929915
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-02T15:33:28.575Z
- **Disclosed**: 2023-07-19T10:47:50.062Z

## Reporter
- **Username**: rink_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bitwarden

## Vulnerability Information
Verified in Android, might also apply for iOS
This description requires 2 accounts, here called the primary and the secondary vault. 

1. Sign in to the Bitwarden app with the primary account and enable biometric unlock
2. Make sure the app is locked (e.g. by force killing the app)
3. Enroll a new fingerprint
4. As per [GH-1026](https://github.com/bitwarden/mobile/pull/1026), `BiometricIntegrityValid` will now be false and hence the app will display "Biometric unlock disabled pending verification of master password"
5. Add the secondary account following the regular procedure (and enable biometric unlock)
6. Attempt to switch to the primary vault; note that it still does not allow biometric unlock
7. Force kill the app making sure both vaults are locked
8. Switch back to the secondary vault and unlock it
9. From the secondary vault, switch to the primary vault and note how it is possible to unlock it using biometrics

## Impact

Changing biometric options, for example enrolling extra fingerprints should prompt for re-authentication according to the integrity checks implemented in [GH-1026](https://github.com/bitwarden/mobile/pull/1026) and [GH-1093](https://github.com/bitwarden/mobile/pull/1093).

This vulnerability allows bypassing those integrity checks if the following three conditions are met:
1. The attacker has physical access to the phone and is able to unlock the phone
2. The user has enabled biometrics unlock
3. The attacker has any valid Bitwarden account (including selfhosted)

Upon gaining access to the vault, export is not possible because the master password is required, but it is possible to view and delete all passwords the user has access to. It is also possible to enable device login if that was not enabled yet and gain access to the vault on a desktop computer.

## Attachments
No attachments
