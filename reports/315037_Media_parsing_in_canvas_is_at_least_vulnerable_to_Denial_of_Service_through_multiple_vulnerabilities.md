# Media parsing in canvas is at least vulnerable to Denial of Service through multiple vulnerabilities

## Report Details
- **Report ID**: 315037
- **URL**: https://hackerone.com/reports/315037
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-11T21:24:24.145Z
- **Disclosed**: 2019-04-03T20:07:37.401Z

## Reporter
- **Username**: webtonull
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
There is at least a DoS vulnerability in canvas.
It segfaults node.js which leads to a Denial of Service, but according to !exploitable it could possibly be worse

## Module

**canvas**

node-canvas is a Cairo backed Canvas implementation for NodeJS.

https://www.npmjs.com/package/canvas

version: 1.6.9

Stats
2,207 downloads in the last day
42,354 downloads in the last week
194,214 downloads in the last month

~1,587,298 estimated downloads per year (2017) 

## Description

The vulnerabilities were found with fuzzing with afl. PNG, JPG and GIF parsing are all vulnerable.
The vulnerabilities can be exploited if user provided images are passed through the libraries. One example of a package using canvas, is ascci-art which generates ascii from an image. 

One of the bugs appear to be a classic buffer overflow (PNG), while for some of the other bugs it appears to try to read memory it should not have access to.

## Steps To Reproduce:

Provided with this report is a set of images triggering the vulnerabilities. These can be tested with ascii-art which uses canvas:
`ascii-art image /full/path/to/test/image`

## Supporting Material/References:

- Ubuntu 16.04 64-bit
- nodejs v9.5.0
- npm v5.6.0

## Impact

Denial of service - take down a service running on node.js, if that service can be tricked into parsing a user-supplied image
Possibly worse if !exploitable is right, and these vulnerabilities can be used to inject shell code.

## Attachments
- canvas_crashes.zip
