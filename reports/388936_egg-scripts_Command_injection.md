# [egg-scripts] Command injection

## Report Details
- **Report ID**: 388936
- **URL**: https://hackerone.com/reports/388936
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-31T13:54:26.547Z
- **Disclosed**: 2018-08-19T07:27:08.095Z

## Reporter
- **Username**: pontus_johnson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a command injection vulnerability in egg-scripts.
It allows arbitrary shell command execution through a maliciously crafted command line argument.

# Module

**module name:** [egg-scripts]
**version:** [2.6.0]
**npm page:** `https://www.npmjs.com/package/egg-scripts`

## Module Description

"deploy tool for egg project."

## Module Stats

Replace stats below with numbers from npm’s module page:

209 downloads in the last day
1,958 downloads in the last week
8,333 downloads in the last month

# Vulnerability

## Vulnerability Description

egg-script does not sanitize the --stderr command line argument, and subsequently passes it to child_process.exec(), thus allowing arbitrary shell command injection.

## Steps To Reproduce:

1. Install egg: `npm i egg --save`
2. Install egg-scripts: `sudo npm i egg-scripts -g --save`
3. Run eggctl with malicious argument: `eggctl start --daemon --stderr=/tmp/eggctl_stderr.log; touch /tmp/malicious`
4. Check that the injected command was executed: `ls /tmp/`
5. Stop eggctl: `eggctl stop`

## Patch

Command execution happens [here](https://github.com/eggjs/egg-scripts/blob/22faa4cfbb84cc5bc819d981dce962d8f95f8357/lib/cmd/start.js#L214):
```
const [ stdout ] = yield exec('tail -n 100 ' + stderr);
```
`exec` could be replaced by `execFile`, which would force developers to separate the command and its arguments.

## Supporting Material/References:
- Operating system: Debian GNU/Linux 9.5 (stretch)
- Node.js v8.11.3
- npm v5.6.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Arbitrary shell command execution.

## Attachments
No attachments
