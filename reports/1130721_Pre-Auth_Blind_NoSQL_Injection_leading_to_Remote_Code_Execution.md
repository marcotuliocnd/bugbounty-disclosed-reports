# Pre-Auth Blind NoSQL Injection leading to Remote Code Execution

## Report Details
- **Report ID**: 1130721
- **URL**: https://hackerone.com/reports/1130721
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-03-19T14:59:53.943Z
- **Disclosed**: 2021-05-18T20:36:02.110Z

## Reporter
- **Username**: sonarsource
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:**
The `getPasswordPolicy` method is vulnerable to NoSQL injection attacks and does not require authentication/authorization. It can be used to take over accounts by leaking password reset tokens. Taking over an admin account leads to Remote Code Execution.

**Description:**
The `getPasswordPolicy` method does not properly validate or sanitize the `token` parameter and can thus be used to perform a blind NoSQL injection. It can be called without authentication (which seems intended), e.g. by using the `/api/v1/method.callAnon` API endpoint

By using [MongoDB's `$regex` operator](https://docs.mongodb.com/manual/reference/operator/query/regex/), a password reset token can be leaked character by character. Example: in order to check if the password reset token begins with a specific letter, e.g. `A`, the attacker would send the JSON object `{"$regex":"^A"}` as the `token` parameter. The response contains the server's password policy when the guess was correct, or an error otherwise. This can be repeated for all possible characters and for each position in the token, until the whole token is known. See the `pwpolicy_leak_token` function in the attached exploit for an implementation of this.

In order to take over an account, an attacker would perform the following high-level steps:
1. Request a password reset for the target user's account. This requires the attacker to know the target user's email address.
1. Leak the password reset token as explained above
1. Reset the target user's password to an attacker known one using the password reset token. The target user cannot have email or TOTP 2FA enabled in order for this step to work.

To gain Remote Code Execution capabilities on the server, an attacker can follow these steps to take over an admin account. The attacker can then use the newly gained admin privileges to create an incoming web hook that has a script. This allows them  to get execute commands or get a shell on the server, because the script is executed on the server without a security boundary in place (which seems to be intended).

See `pre_auth_nosqli.py` for a reference exploit and the attached video for a demonstration of it.

The vulnerable code can be found here: [getPasswordPolicy.js:8](https://github.com/RocketChat/Rocket.Chat/blob/eba1e9b3146e5102baed000953c2cb51930c345c/server/methods/getPasswordPolicy.js#L8)

## Releases Affected:
- Tested on 3.12.1
- Seems to be affected since 3.8.0 as the vulnerability was introduced in [commit b950f17](https://github.com/RocketChat/Rocket.Chat/commit/b950f17e4225efb99b7b80022877f9b2cdf14b64?branch=b950f17e4225efb99b7b80022877f9b2cdf14b64#diff-2fc491cc6f1ca015c2e3f7c36ee12f8d7c7e40907257fd5256d3f39e85c12b88R8)

## Steps To Reproduce (from initial installation to vulnerability):
1. Install Python3 (required by the exploit)
1. Install the Python dependencies required by the exploit: `pip3 install requests`
1. Set up an instance of RocketChat 3.12.1, e.g. by cloning the repo and using Docker Compose:
  1. `git clone git@github.com:RocketChat/Rocket.Chat.git`
  1. `cd Rocket.Chat`
  1. `git checkout tags/3.12.1`
  1. `docker-compose up -d`
1. Configure the instance with default settings, remember the admin's email address (e.g. `admin@rocketchat.local`)
1. Disable all 2FA methods on the admin account
1. Run the reference exploit against the instance, provide the admin's email address: `python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@rocketchat.local'`
1. The exploit should provide an interactive shell on the the server, use it to verify that you can execute commands as the rocketchat user: `whoami`

## Supporting Material/References:
The attached proof-of-concept video shows the setup and exploitation of a fresh Rocket.Chat instance.
This is the exploit's output:
```
 ___  ___  _ __   __ _ _ __ ___  ___  _   _ _ __ ___ ___ 
/ __|/ _ \| '_ \ / _` | '__/ __|/ _ \| | | | '__/ __/ _ \
\__ \ (_) | | | | (_| | |  \__ \ (_) | |_| | | | (_|  __/
|___/\___/|_| |_|\__,_|_|  |___/\___/ \__,_|_|  \___\___|

[+] Requesting password reset for "admin@rocketchat.local"...
[*] Leaking password reset token...
[+] Leaked password reset token: 0q9oakr3Lc94p3AnUjtQGlBm4bqJF3AndFYOjIg94ld
[+] Resetting password to "f7c87ed1559f2fe101ee"...
[+] Admin account takeover successful!
[+] Creating hook "backdoor-8624225d" with secret "8e2b809f6d1e9c561f9625d362726672"...
[*] Hook: T4nRot8nRvgEDp6rn/6sfs8GYcZCmH7SjKeazsexGmCJjFdLwWMdsqyz9hTcPFYxKF
[+] Dropping into shell:
$ whoami
rocketchat
$ id
uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)
$ 
```

## Suggested mitigation
Ensure that the user-provided `token` parameter is a string.

## Disclosure Policy
All reported issues are subject to a 90 day disclosure deadline. 
After 90 days elapse, parts of the bug report will become visible to the public.

Don't hesitate to ask if you have any questions or need further help with this issue.

## Impact

An attacker can use this vulnerability to target an admin user and take over their account, which is already a high impact. The attacker can then use certain features that are available to admins in order to gain Remote Code Execution capabilities. This is demonstrated in the reference exploit by creating an incoming web hook that executes the attacker's payload in the context of the server process.

This gives them complete control over the Rocket.Chat instance and exposes all attached components, e.g. the database or any external system whose credentials are stored within Rocket.Chat settings. An attacker can read, change, or delete all items in the database, impacting confidentiality, integrity and availability.

## Attachments
No attachments
