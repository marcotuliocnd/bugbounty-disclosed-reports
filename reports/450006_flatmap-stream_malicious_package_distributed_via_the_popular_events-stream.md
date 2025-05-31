# flatmap-stream malicious package (distributed via the popular events-stream)

## Report Details
- **Report ID**: 450006
- **URL**: https://hackerone.com/reports/450006
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-11-26T18:28:49.050Z
- **Disclosed**: 2018-11-26T22:26:43.896Z

## Reporter
- **Username**: danny_grander
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a case of malicious package (flat-stream) that made it's way into many other npm packages. One such popular package is `event-stream` (user dominictarr transferred the ownership of an npm module to another user because he wasn't actively maintaining it. That user then added malicious dependency to the package)

See discussion here: 
https://github.com/dominictarr/event-stream/issues/116

# Module

**module name:**  flatmap-stream
**version:** [MODULE VERSION]
**npm page:** `https://www.npmjs.com/package/flatmap-stream` (removed from npm by now)

## Module Description

It is not yet clear what the malicious code was doing. 
See discussion here: https://github.com/dominictarr/event-stream/issues/116#issuecomment-441737695

## Module Stats

> Replace stats below with numbers from npm’s module page:

flatmap-stream is not popular, but event-stream is very popular (1,996,440 downloads per week)

## Impact

RCE

## Attachments
No attachments
