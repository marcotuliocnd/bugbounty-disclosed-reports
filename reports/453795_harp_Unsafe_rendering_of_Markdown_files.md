# [harp] Unsafe rendering of Markdown files

## Report Details
- **Report ID**: 453795
- **URL**: https://hackerone.com/reports/453795
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-12-02T10:32:57.942Z
- **Disclosed**: 2019-04-06T17:54:27.270Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Cross Site Scripting vulnerablity in harp module
It allows to execute arbitrary JavaScript due to unsafe rendering of markdown files.
Similar to [#404126](https://hackerone.com/reports/404126)

# Module

**module name:** harp
**version:** 0.29.0
**npm page:** `https://www.npmjs.com/package/harp`

## Module Description

zero-configuration web server with built in pre-processing


## Module Stats

3,576 downloads in the last week

# Vulnerability

## Vulnerability Description

Harp uses `marked` in their preprocessor `terraform` for parsing and rendering markdown. By default `marked` does not sanitize html. An uninformed user may assume the output of markdown to be sanitized and thus become vulnerable to XSS by rendering malicious markdown files.

See https://github.com/sintaxi/terraform/blob/master/lib/template/processors/md.js

```js
var TerraformError = require("../../error").TerraformError
var marked = require("marked").setOptions({
  langPrefix: 'language-',
  headerPrefix: '',
  gfm: true,
  tables: true,
})
var renderer = new marked.Renderer()
...
```

## Steps To Reproduce:

* Install harpjs
```
yarn global add harp
```
* Run harp server
```
harp server 
```
* Add malicious markdown file in the server directory (`test.md` attached) and open it in browser.
Eg:. `http://localhost:9000/test` will open `test.md` if it exists in the project directory

Refer http://harpjs.com/docs/development/markdown

## Patch

`marked` provides an option `sanitize` which is set to `false` by default. You can also pass a custom `sanitizer` function through options.
Either set the `santize` option to `true` in `terraform` while importing `marked`  or inform the user to safely handle markdown files by displaying an appropriate warning.

## Supporting Material/References:

- Ubuntu 16.04
- node v11.3.0
- npm 6.4.1

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

User is exposed to unsafely rendered markdown files which may lead to execution of arbitrary JS

## Attachments
- test.md
