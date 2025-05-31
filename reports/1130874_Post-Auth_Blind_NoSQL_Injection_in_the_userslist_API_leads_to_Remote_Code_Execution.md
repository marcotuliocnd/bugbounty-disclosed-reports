# Post-Auth Blind NoSQL Injection in the users.list API leads to Remote Code Execution

## Report Details
- **Report ID**: 1130874
- **URL**: https://hackerone.com/reports/1130874
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-03-19T17:31:20.862Z
- **Disclosed**: 2021-07-31T08:31:05.616Z

## Reporter
- **Username**: sonarsource
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:**
The `users.list` API endpoint is vulnerable to NoSQL injection attacks. It can be used to take over accounts by leaking password reset tokens and 2FA secrets. Taking over an admin account leads to Remote Code Execution.

**Description:**
The `users.list` API endpoint takes a custom query via the `query` URL query parameter. Although the returned fields are restricted, the query is not validated or sanitized properly and can thus be used to perform a blind NoSQL injection that can leak any field's value of any document in the `users` collection.

By using [MongoDB's `$where` operator](https://docs.mongodb.com/manual/reference/operator/query/where/), an attacker can build arbitrary oracles that can leak the value of any field of any user document. The query can be tailored to leak only the values of a specific account which makes it easy to target an admin account. Most notably an attacker can leak password reset tokens and 2FA secrets.

Example: in order to check if the password reset token of an admin user begins with a specific letter, e.g. `A`, the attacker would send the JSON object `{"$where":"this.roles.includes('admin') && /^A/.test(this.services.password.reset.token)"}` as the `query` parameter. The response contains the matching admin user when the guess was correct, or no users otherwise. This can be repeated for all possible characters and for each position in the token, until the whole token is known. See the `users_nosqli_blind_leak` function in the attached exploit for an implementation of this.

In order to take over another account, an attacker would perform the following high-level steps:
1. Leak the user's email address
1. Request a password reset for the target user's account
1. Leak the password reset token
1. Leak the TOTP 2FA secret or email 2FA token hash if necessary
1. Reset the target user's password to an attacker known one using the password reset token and any leaked 2FA tokens/secrets if necessary

To gain Remote Code Execution capabilities on the server, an attacker can follow these steps to take over an admin account. The attacker can then use the newly gained admin privileges to create an incoming web hook that has a script. This allows them  to execute commands or get a shell on the server, because the script is executed on the server without a security boundary in place (which seems to be intended).

The vulnerable code can be found here: [users.js:230](https://github.com/RocketChat/Rocket.Chat/blob/eba1e9b3146e5102baed000953c2cb51930c345c/app/api/server/v1/users.js#L230-L237)

See `post_auth_nosqli.py` for a reference exploit and the attached video for a demonstration of it.

## Releases Affected:
- Tested on 3.12.1
- Seems to be affected since 0.49.0 as the vulnerability was introduced in [commit 3112d22](https://github.com/RocketChat/Rocket.Chat/commit/3112d225fe1533dd77cfad7fff085d53d78c19f2#diff-84949efc4b8041a5ac51e7bcd0f2cd38b8fd3690f059235769ab437b453feab8R120)

## Steps To Reproduce (from initial installation to vulnerability):
1. Install Python3 (required by the exploit)
1. Install the Python dependencies required by the exploit: `pip3 install requests bcrypt`
1. Set up an instance of RocketChat 3.12.1, e.g. by cloning the repo and using Docker Compose:
  1. `git clone git@github.com:RocketChat/Rocket.Chat.git`
  1. `cd Rocket.Chat`
  1. `git checkout tags/3.12.1`
  1. `docker-compose up -d`
1. Configure the instance with default settings
1. Create a normal (non-admin) user with username `attacker` and password `attacker`
1. Run the reference exploit against the instance: `python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'`
1. The exploit should provide an interactive shell on the the server, use it to verify that you can execute commands as the rocketchat user: `whoami`

## Supporting Material/References:
The attached proof-of-concept video shows the setup and exploitation of a fresh Rocket.Chat instance.
**Please note:** The unsuccessful login at the end of the video does not mean that the exploit did not work, it just shows that the original admin password was restored (as stated in the exploits output). The exploit was successful, which can be seen by the output of the shell commands at the end of the exploit.

This is the exploit's output:
```
 ___  ___  _ __   __ _ _ __ ___  ___  _   _ _ __ ___ ___ 
/ __|/ _ \| '_ \ / _` | '__/ __|/ _ \| | | | '__/ __/ _ \
\__ \ (_) | | | | (_| | |  \__ \ (_) | |_| | | | (_|  __/
|___/\___/|_| |_|\__,_|_|  |___/\___/ \__,_|_|  \___\___|

[+] Found admin: username=admin id=56gyPQKt8Ff3Weowk
[*] Leaking email...
[+] Leaked email: admin@rocketchat.local
[*] Leaking password hash...
[+] Leaked password hash: $2b$10$ubhEIM/j6qLFNINHVbP.B.CJFCXagK7V5zD0Q8BYzs6UBlbBpiECa
[+] Requesting password reset...
[*] Leaking password reset token...
[+] Leaked password reset token: ET4sx905cF9pTZOsHFu6eRad7MwpYmqs-iTMWQIXAhv
[+] Resetting password to "DEbCf2b0A2BE79bBcDf1"...
[+] Admin account takeover successful!
[+] Creating hook "backdoor-9Fbd6E5A" with secret "AbE217B9d9e7Dd0CB2EB8dd30d26edfe"...
[*] Hook: 7bgxdkGHQYdBwtHWA/2S3EGB2ywWHM3aeYKu2q7akGF6TEjXEKMGK2Smggw7LpSLHc
[+] Restoring admin password...
[+] Dropping into shell:
$ whoami
rocketchat
$ id
uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)
$ 
```

## Suggested mitigation
- Properly validate the `query` parameter:
  - Restrict the usage of MongoDB operators using an allowlist, especially top level operators like `$where`
  - Restrict the set of query-able fields using an allowlist (like the restriction on the returned fields)
- Check every API endpoint that uses the `parseJsonQuery()` function for similar vulnerabilities

## Disclosure Policy
All reported issues are subject to a 90 day disclosure deadline. 
After 90 days elapse, parts of the bug report will become visible to the public.

Don't hesitate to ask if you have any questions or need further help with this issue.

## Impact

An attacker can use this vulnerability to target an admin user and take over their account, which is already a high impact. The attacker can then use certain features that are available to admins in order to gain Remote Code Execution capabilities. This is demonstrated in the reference exploit by creating an incoming web hook that executes the attacker's payload in the context of the server process.

This gives them complete control over the Rocket.Chat instance and exposes all attached components, e.g. the database or any external system whose credentials are stored within Rocket.Chat settings. An attacker can read, change, or delete all items in the database, impacting confidentiality, integrity, and availability.

## Attachments
No attachments
