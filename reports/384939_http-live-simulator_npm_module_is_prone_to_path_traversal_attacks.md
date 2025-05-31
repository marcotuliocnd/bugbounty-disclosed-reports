# http-live-simulator npm module is prone to path traversal attacks

## Report Details
- **Report ID**: 384939
- **URL**: https://hackerone.com/reports/384939
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-21T12:34:12.401Z
- **Disclosed**: 2018-09-18T13:07:19.601Z

## Reporter
- **Username**: lirantal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report Path Traversal vulnerability in http-live-simulator
It allows to read arbitrary files from any location on disk

# Module

**module name:** http-live-simulator
**version:** 1.0.5
**npm page:** `https://www.npmjs.com/package/http-live-simulator`

## Module Description

> Copy description from npm page

## Module Stats

> Replace stats below with numbers from npm’s module page:

[9] weekly downloads

# Vulnerability

## Vulnerability Description

> Description about how the vulnerability was found and how it can be exploited, how it harms package users (data modification/lost, system access, other.

The http-live-simulator module doesn't set a root directory and allows any arbitrary paths to be accessed on the file system and returned to requesting clients

## Steps To Reproduce:

> Detailed steps to reproduce with all required references/steps/commands. If there is any exploit code or reference to the package source code this is the place where it should be put.

1. Install the module locally in an npm project: `npm install http-live-simulator`
2. Run the live server on a specified port: `node_modules/.bin/http-live --port 8181`
3. Attempt to access a file from outside that project's directory, such as `curl --path-as-is http://localhost:8181/../../file.txt`
4. Files output should be returned 

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- MacOS
- Node.js 8.11.3
- npm 5.6.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

path traversal vulnerability leading to read access in arbitrary files on disk

## Attachments
No attachments
