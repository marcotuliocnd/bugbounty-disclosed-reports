# Public instance of Jenkins on https://██████████/ with /script enabled

## Report Details
- **Report ID**: 768266
- **URL**: https://hackerone.com/reports/768266
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-04T21:46:01.280Z
- **Disclosed**: 2020-01-31T13:58:19.278Z

## Reporter
- **Username**: niteshsurana
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An Amazon instance was found on https://█████/ running Jenkins. On analysing the SSL certificate, I reported here to the DoD.

**Description:**
On checking the SSL certificate, the details show:

```
Issued to and Issued By records:

CN: █████
Organization(O): █████████
Organizational Unit (OU): ███
```
Here, this instance is already authenticated and this does not require a password to login. The major impact of this vulnerability is, an attacker can exploit and gain access to critical internals of the server as `/script` is enabled.

Through `/script`, an attacker can run remote commands on the server through the Java programming language.

## Impact

Unauthenticated instances of Jenkins with `/script` enabled can lead to an attacker running remote command on the instance.

## Step-by-step Reproduction Instructions

1. Go to https://███/script/
  1.1 Check the SSL certificate for proof.

2. In the textbox that comes up, enter the following code:

```bash
"ls /".execute().text
```

3. The Response is

```
Result: bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```

After verifying this issue, I looked up `██████████` and `█████`. That's how I confirmed that this instance was of critical importance.

## Product, Version, and Configuration (If applicable)

Jenkins

## Suggested Mitigation/Remediation Actions:

Mitigation for this, as per my understanding would be to add a 2FA authentication if this instance is in use. If this instance is not in use, please shut down the instance.

P.S: I've also attached a PoC video of the same for clarity and reference. I am reporting this issue to the US DOD as ██████████ would be more logical to be associated with the DOD. If this bug is not acknowledged here, please forward this report to the authority that handles the US ███████.

## Impact

On a Jenkins instance with `/script` enabled, an attacker can remote commands on the server and this can later lead to critical information leakage, lateral movement and other catastrophic events as the instance can be manipulated by the skills of the attacker.

Such instances should be closed when not in use and authentication mechanisms should be properly enforced.

## Attachments
No attachments
