# Phabricator is vulnerable to padding oracle attacks and chosen-ciphertext attacks.

## Report Details
- **Report ID**: 216746
- **URL**: https://hackerone.com/reports/216746
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-28T17:31:13.989Z
- **Disclosed**: 2017-04-05T20:16:10.747Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
Dear Phabricator bug bounty team,

# Summary
---

Phabricator encrypts data with AES in CBC mode, but does not ensure integrity of the encrypted data. You must authenticate the data, by either using an HMAC or by using an authenticated block cipher mode like GCM.

# Why does this vulnerability exist?
---

`src/applications/files/format/PhabricatorFileAES256StorageFormat.php` encrypts the data as follows without checking the integrity of the message:

~~~
private function encryptData(
    $data,
    PhutilOpaqueEnvelope $key,
    PhutilOpaqueEnvelope $iv) {
    $method = 'aes-256-cbc';
    $key = $key->openEnvelope();
    $iv = $iv->openEnvelope();
    $result = openssl_encrypt($data, $method, $key, OPENSSL_RAW_DATA, $iv);
    if ($result === false) {
      throw new Exception(
        pht(
          'Failed to openssl_encrypt() data: %s',
          openssl_error_string()));
    }
    return $result;
}
~~~

Link to source code: https://github.com/phacility/phabricator/blob/master/src/applications/files/format/PhabricatorFileAES256StorageFormat.php

# How can this be exploited?
---

By not ensuring integrity Phabricator is vulnerable to padding oracle attacks and chosen-ciphertext attacks.

# How can this be fixed?
---

As stated previously, you must check the integrity of the data, by either using an HMAC or by using an authenticated block cipher mode like GCM.

Best regards,
Ed

## Attachments
No attachments
