# Vulnerable moment-timezone version shipped

## Report Details
- **Report ID**: 1708873
- **URL**: https://hackerone.com/reports/1708873
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-09-22T14:19:37.967Z
- **Disclosed**: 2023-02-08T05:44:57.412Z

## Reporter
- **Username**: mik-patient
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
After this vulnerability refferences #1604606, I searching again about the vulnerabilities in other repositories and today we found a Information exposure in https://github.com/nextcloud/server Many communication channels can be "sniffed" by attackers during data transmission. For example, network traffic can often be sniffed by any attacker who has access to a network interface. This significantly lowers the difficulty of exploitation by attackers.



**Fix:**
Problem has been patched in version `0.5.35`, patch should be applicable with minor modifications to all affected versions. The patch includes changing the FTP endpoint with an HTTPS endpoint.
```json
        "moment-timezone": "^0.5.35",
        "version": "0.5.35",
        "resolved": "https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.5.35.tgz",
        "integrity": "sha512-cY/pBOEXepQvlgli06ttCTKcIf8cD1nmNwOKQQAdHBqYApQSpAqotBMX0RJZNgMp6i0PlZuf1mFtnlyEkwyvFw==",
```

## Impact

* if Alice uses `grunt data` (or `grunt release`) to prepare a custom-build, moment-timezone with the latest tzdata from IANA's website
  * and Mallory intercepts the request to IANA's unencrypted ftp server, Mallory can serve data which might exploit further stages of the moment-timezone tzdata pipeline, or potentially produce a tainted version of moment-timezone (practicality of such attacks is not proved)

[GHSA-v78c-4p63-2j6c](https://github.com/moment/moment-timezone/security/advisories/GHSA-v78c-4p63-2j6c)

## Attachments
No attachments
