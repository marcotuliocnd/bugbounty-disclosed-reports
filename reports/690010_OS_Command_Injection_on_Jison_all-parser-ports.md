# OS Command Injection on Jison [all-parser-ports]

## Report Details
- **Report ID**: 690010
- **URL**: https://hackerone.com/reports/690010
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-07T05:36:16.351Z
- **Disclosed**: 2020-05-28T10:39:50.786Z

## Reporter
- **Username**: 0x48piraj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report **OS Command Injection** vulnerability on [Jison](https://www.npmjs.com/package/jison) in parser ports. *(CSharp, PHP)*

It allows arbitrary OS shell command execution through a crafted command-line argument.

# Basic Information

**Module:** ***jison***
**Version:** `0.4.18`
**NPM Project Page:** `https://www.npmjs.com/package/jison`

## Module Description

##### An API for creating parsers in JavaScript

> Jison generates bottom-up parsers in JavaScript. Its API is similar to Bison's, hence the name. It supports many of Bison's major features, plus some of its own. If you are new to parser generators such as Bison, and Context-free Grammars in general, a good introduction is found in the Bison manual. If you already know Bison, Jison should be easy to pickup.
> Briefly, Jison takes a JSON encoded grammar or Bison style grammar and outputs a JavaScript file capable of parsing the language described by that grammar. You can then use the generated script to parse inputs and accept, reject, or perform actions based on the input.

## Module Stats

##### Downloads in the last week: (https://api.npmjs.org/downloads/point/last-week/jison)

```
downloads : 138857
start : 2019-08-31
end : 2019-09-06
package : jison
```

##### Downloads in the last month: (https://api.npmjs.org/downloads/point/last-month/jison)

```
downloads : 678197
start : 2019-08-08
end : 2019-09-06
package : jison
```
> Stats by npm-stat: https://npm-stat.com/charts.html?package=jison

# Vulnerability

**Jison** has parsing/lexing template to php, C# which don't sanitize `process.argv` (command line arguments), before passing it to `child_process.exec()`, hence allowing arbitrary shell command injection.

The vulnerable code is in `/ports/csharp/Jison/Jison/csharp.js` at [csharp.js#L19](https://github.com/zaach/jison/blob/bcf986e180359aa2404b1b73ecbfef1df4c6b011/ports/csharp/Jison/Jison/csharp.js#L19)

```
console.log("Executing: " + "jison " + process.argv[2]);

exec("jison " + process.argv[2], function (error) {
    if (error) {
        console.log(error);
        return;
    }
```

## Steps To Reproduce:
1. Installing Jison command-line tool via `npm install jison -g`
2. Obtaining *Jison* parsing templates : `git clone https://github.com/zaach/jison`
3. `cd jison/ports/csharp/Jison/Jison/`
4. Payload : `node csharp.js "echo''>pwned"`
5. Check if the attack was successful or not (dummy payload was executed or not): `ls -la`

Similarly, `/ports/php/php.js` is vulnerable too as it contains the same blob ([php.js#L19](https://github.com/zaach/jison/blob/bcf986e180359aa2404b1b73ecbfef1df4c6b011/ports/php/php.js#L19)). `""` was added just to isolate the payload.

## Patch

Sanitizing the input. Using `execFile` (this method signatures force developers to separate the command and its arguments)

## Supporting Material/References:

- Windows 10 1803 (OS Build 17134.950)
- **NodeJS Version:** v10.16.3
- **NPM Version:** 6.9.0 

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

Arbitrary OS command execution.

## Attachments
- jison-osi.png
