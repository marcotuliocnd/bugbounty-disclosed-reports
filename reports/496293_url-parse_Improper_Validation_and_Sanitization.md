# [url-parse] Improper Validation and Sanitization

## Report Details
- **Report ID**: 496293
- **URL**: https://hackerone.com/reports/496293
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-14T22:41:05.962Z
- **Disclosed**: 2020-01-27T09:10:53.941Z

## Reporter
- **Username**: ronperris
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report Improper Validation and Sanitization in url-parse.

It allows attacker-controlled URL values to bypass validation and sanitization.

# Module

**module name:** url-parse
**version:** 1.4.4
**npm page:** `https://www.npmjs.com/package/url-parse`

## Module Description

The url-parse method exposes two different API interfaces. The url interface that you know from Node.js and the new URL interface that is available in the latest browsers.

## Module Stats

> Replace stats below with numbers from npm’s module page:

5,544,078 downloads in the last week

# Vulnerability

## Vulnerability Description

When using url-parse in the browser the protocol of the URL returned by the parser is not validated correctly. In the Node.js environment strings like, ` javascript:` return and empty string on the resulting URL object, but in the browser the current `document.location.protocol` is used when the provided URL doesn't match the validation expression `/^([a-z][a-z0-9.+-]*:)?(\/\/)?([\S\s]*)/i`.

## Steps To Reproduce:

Add the following `test to test/test.js` and run `npm run test-browser`.

 assume(parse.extractProtocol(' javscript:')).eql({
        slashes: false,
        protocol: '',
        rest: ''
      })

# Wrap up
Line 199 in index.js is setting the protocol to location.protocol, this is probably not the right move.

url protocol = extracted.protocol || location.protocol || '';

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y] 
- I opened an issue in the related repository: [N]

## Impact

Bypass input sanitization and validation.

## Attachments
No attachments
