# Biometric key is stored in Windows Credential Manager, accessible to other local unprivileged processes

## Report Details
- **Report ID**: 1874155
- **URL**: https://hackerone.com/reports/1874155
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-14T17:34:40.525Z
- **Disclosed**: 2023-06-07T12:33:12.491Z

## Reporter
- **Username**: mebeim
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bitwarden

## Vulnerability Information
Bitwarden Desktop on Windows allows the user to enable vault unlock through Windows Hello (under File > Settings > Unlock with Windows Hello). When this is done, a "Biometric master key" is generated and stored locally inside the Windows' user credential set. This is done through the "wincred" API, in particular through the functions [CredWrite](https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credwritew) and [CredRead](https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credreadw) that are called from the native module written in Rust ([here: `apps/desktop/desktop_native/src/password/windows.rs`](https://github.com/bitwarden/clients/blob/desktop-v2023.1.1/apps/desktop/desktop_native/src/password/windows.rs)). The item created in the user credential set has a name of the form `Bitwarden_biometric/<account_uuid>_masterkey_biometric`.

When unlocking the vault through Windows Hello, the unlock operation prompts the user for authentication through Windows Hello ([here: `apps/desktop/src/main/biometric/biometric.windows.main.ts` line 45](https://github.com/bitwarden/clients/blob/desktop-v2023.1.1/apps/desktop/src/main/biometric/biometric.windows.main.ts#L45)). If the authentication succeeds, the vault is unlocked and the items are decrypted after decrypting the master keys through the keys derived from the biometric master key.

However, the authentication through Windows Hello is unneeded. Commenting the line linked above, the vault still unlocks with no problem. The biometric master key can in fact be retrieved with a simple call to the `CredRead` windows API function, and then used to decrypt the locally saved data present in `%appdata%\Bitwarden\data.json`. The Windows Hello authentication prompt therefore gives a false sense of security to the user, making it seem as if authentication is *needed* to decrypt vault data, when in reality it is not.

The local data in `%appdata%\Bitwarden\data.json`, as well as the master biometric key, persist after the vault is locked and the Bitwarden desktop allication is closed. Both of them are easily readable by any program running in the current user session, without the need to elevate privileges. Furthermore, both are accessible to any administrator account on the same machine.

Given the above, a potentially malicious program running locally on the machine can decrypt the entirety of the user vault, i.e. all ciphers (logins, cards, notes, identities). Furthermore, since the Desktop application stores locally (still in `%appdata%\Bitwarden\data.json`) a refresh token and a bearer token used for authentication with the Bitwarden server, user data can easily be modified, encrypted and updated on the server on behalf of the user.

The attached proof of concept (of which a recorded video demo is also attached) consists of a Python 3 script that uses the `ctypes` module to extract the biometric master key (if any) from the current user's credential set, decrypts all cipher names stored locally, and also modifies and updates the content of a secret note with a specific (if present), sending the new data to the server through standard bitwarden API.

The setup needed before running the proof of concept script is as follows:

1. Create a test account on https://vault.bitwarden.com/#/register (or use an existing one at your own risk).
2. Login to the test account and create some items in the vault for testing purposes. In particular, among them create a *secure note* with name `Super Secret Note` and arbitrary content.
3. Download and install the latest Bitwarden Desktop client **for Windows** from https://bitwarden.com/download/ (make sure to install on a PC that supports Windows Hello biometric authentication in order to enable it).
3. Use the installed desktop client to log in to the test account using the master password.
5. Enable Windows Hello authentication through File > Settings > "Unlock with Windows Hello". Optionally also disable "Ask for Windows Hello on launch".
6. Lock the vault and close the Bitwarden desktop application.

Now to run the proof of concept, follow these steps:

1. Install Python 3 (recommended Python) on the machine if not already present.
2. Install the following libraries through Pip: `pycryptodome` `Cryptography` and `requests`.

   ```
   python -m pip install pycryptodome Cryptography requests
   ```

3. Launch the Python 3 script from a CMD or Powershell prompt (running as administrator is *not* needed):

   ```
   python poc.py
   ```

The proof of concept script output should be similar to the following:

```none
Account: <uuid-of-the-account>
-> Biometric master key: <bio-master-key-in-hex>
-> Encryption key: <master-encryption-key-in-hex>
-> HMAC key: <master-hmac-key-in-hex>
-> Decrypted entry: Super Secret Login
-> Decrypted entry: Super Secret Card
-> Decrypted entry: Super Secret Note
-> Modifying item: Super Secret Note
-> Old content: b'This is a super secret note!'
-> New content: b'Pwned!'
-> Sending API request...
-> Response: 200
```

NOTE: Python 3 was my choice for its simplicity and ease of use. The same operations could be performed by other means as well (for example through a native application).

## Impact

An attacker that is able to briefly obtain local access to a machine with Bitwarden desktop installed, is able to decrypt the contents of *all* vaults that have unlock through Windows Hello enabled. On top of that, an attacker would also be able to alter their content through simple API requests to the bitwarden server, since they have the symmetric encryption and HMAC keys used to encrypt the fields of any item in the vault.

Furthermore, on a multi-user Windows machine, any administrator account has the ability to perform the same operations for any other users on the same machine that is using Bitwarden desktop with Windows Hello unlock enabled. Although not implemented in the attached proof of concept, this would be possible by simply enumerating local users and accessing each user's credential set, enumerating the entries and retrieving any Bitwarden biometric master key that is present.

In conclusion, Bitwarden Desktop's biometric authentication through Windows Hello gives the user a false sense of security. While normally the vault data is locally stored encrypted *without* the master key, in case of Windows Hello authentication the biometric master key *is locally stored in plaintext as well*. This contradicts the [Bitwarden Security Whitepaper](https://bitwarden.com/help/bitwarden-security-white-paper/), which states:

> We do not keep the Master Password stored locally or in memory on the Bitwarden Client. Your encryption key (Symmetric Key) is kept in memory while the app is unlocked. This is needed to decrypt data in your Vault. When the Vault is locked, this data is purged from memory. After a certain time frame of inactivity on lock screen, we reload the application processes to make sure that any leftover managed memory addresses are also purged. We do our best to ensure that any data that may be in memory for the application to function is only held in memory for as long as you need it and that memory is cleaned up whenever the application is locked. We consider the application to be completely safe while in a locked state.

## Attachments
- poc.py
- demo.mkv
